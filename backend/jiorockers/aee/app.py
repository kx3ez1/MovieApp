import html

import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, redirect, url_for, request

from redis_ import RedisClass

fast = True
app = Flask(__name__)

redis = RedisClass()
r = requests.session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    "Connection": 'keep-alive'
}
url_conv = lambda id1: f'http://www.jiorockerss.vin/movies/{id1}/t.html'
down_url = lambda id1: f'http://servjraws1.jiorockerss.vin/file/view/{id1}?download'


def get_root_links(url):
    urls = {}
    a = r.get(url, headers=headers)
    soup = BeautifulSoup(a.text, 'html.parser')
    for i in soup.find_all('a'):  # all a tags in root page
        # print(i['href'], '==@@', i.text)
        if 'http://www.jiorockerss.vin' in i['href']:
            i['href'] = i['href'].replace('http://www.jiorockerss.vin', '')
        urls[i['href'].strip()] = i.text.strip()

    return urls


def get_id(id1):
    b = r.get(url_conv(id1), headers=headers)
    soup = BeautifulSoup(b.text, 'html.parser')
    url_id = None
    for i in soup.find_all('a'):  # all a tags in root page
        if 'file/view' in i['href']:
            ee = i['href']
            ww = ee.split('/')
            url_id = ww[-1]
            break
    return url_id


def get_downsub_id(id1):
    down_url1 = id1 + '-download'
    if RedisClass().check(down_url1) == 0:
        b = r.get(f'http://www.jiorockerss.vin/movies/{id1}/p.html', headers=headers)
        soup = BeautifulSoup(b.text, 'html.parser')
        url_id = None
        for i in soup.find_all('a'):  # all a tags in root page
            if 'movies/' in i['href']:
                ee = i['href']
                ww = ee.split('/')
                url_id = ww[-2]
        RedisClass().set(down_url1, url_id)
        return url_id
    else:
        return RedisClass().get(down_url1)


@app.route('/movies/<id1>/<htmlname1>/')
def index1(id1, htmlname1):
    page = request.args.get('page')
    dir1 = request.args.get('dir')
    if 'movies' not in htmlname1:
        id2 = get_downsub_id(id1)
        down_id = get_id(id2)
        if down_id:
            link = down_url(down_id)
            return render_template('video2.html', link=link)
        else:
            return redirect(url_for('index3', htmlname=f'movies/c/{id1}/{htmlname1}', page=page, dir=dir1))
    else:
        return redirect(url_for('index3', htmlname=f'movies/c/{id1}/{htmlname1}', page=page, dir=dir1))


@app.route('/movies/c/<id1>/<htmlname>/')
def get_custom_a(id1, htmlname):
    page = request.args.get('page')
    dir1 = request.args.get('dir')
    url = ''
    print(page, dir1)
    if page and dir1:
        url = "http://www.jiorockerss.vin/movies/" + id1 + '/' + htmlname + f'?page={page}&dir={dir1}'
    else:
        url = "http://www.jiorockerss.vin/movies/" + id1 + '/' + htmlname
    print('get_custom_a', url)
    links = get_root_links(url)
    return render_template('index_links.html', links=links)


@app.route('/<htmlname>')
def index3(htmlname):
    url = 'https://www.jiorockerss.vin/' + htmlname
    links = get_root_links(url)
    return render_template('index_links.html', links=links)


@app.route('/movies/<htmlname>')
def index_m_htm(htmlname):
    url = 'https://www.jiorockerss.vin/' + 'movies/' + htmlname
    links = get_root_links(url)
    return render_template('index_links.html', links=links)


@app.route('/file/view/<id1>')
def fileviewq(id1):
    # id2 = get_downsub_id(id1)
    url_name = id1 + '-view'
    if redis.check(url_name) == 0:
        link = down_url(id1)
        redis.set(url_name, link)
        return render_template('video2.html', link=link)
    else:
        link = redis.get(url_name)
        return render_template('video2.html', link=link.decode('utf-8'))


@app.route('/')
def index2():
    url = "http://www.jiorockerss.vin/"
    links = get_root_links(url)
    return render_template('index_links.html', links=links)


def span(data):
    return f'<span class="text-danger" border border-5>  <i class="material-icons text-dark">folder_open</i>{data}<span>'


@app.template_filter('m')
def movie_filter(title):
    if 'Movies' in title:
        return span(title)
    elif 'Shows' in title:
        return span(title)
    elif 'Actors' in title:
        return span(title)
    else:
        return title


@app.template_filter('x-redis')
def xtract(data):
    url1 = lambda num: f'http://www.jiorockerss.vin/details/Screenshots/{num}/{num}a.jpg'
    if 'movies' in data:
        try:
            data_parts = data.split('/')
            img1 = data_parts[1].isdigit()
            img2 = data_parts[2].isdigit()
            if img1:
                img_url = str(data_parts[1]) + 'a'
                if RedisClass().check(img_url) == 0:
                    img = r.get(url1(data_parts[1]), headers=headers)
                    RedisClass().set(img_url, img.content)
                    return '/get/' + img_url
                else:
                    return '/get/' + img_url
                    # return url1(data_parts[1])
            elif img2:
                img_url = str(data_parts[2]) + 'a'
                if RedisClass().check(img_url) == 0:
                    img = r.get(url1(data_parts[2]), headers=headers)
                    RedisClass().set(img_url, img.content)
                    return '/get/' + img_url
                else:
                    return '/get/' + img_url
                    # return url1(data_parts[1])
            else:
                return None
        except:
            return None
    else:
        return None


@app.template_filter('x')
def xtract1(data):
    url1 = lambda num: f'http://www.jiorockerss.vin/details/Screenshots/{num}/{num}a.jpg'
    if 'movies' in data:
        try:
            data_parts = data.split('/')
            img1 = data_parts[1].isdigit()
            img2 = data_parts[2].isdigit()
            if img1:
                return url1(data_parts[1])
            elif img2:
                return url1(data_parts[2])
            else:
                return None
        except:
            return None
    else:
        return None


@app.template_filter('x2')
def xtract2(data):
    url1 = lambda num: f'http://www.jiorockerss.vin/details/Preview/{num}.jpg'
    if 'movies' in data:
        try:
            data_parts = data.split('/')
            img1 = data_parts[1].isdigit()
            img2 = data_parts[2].isdigit()
            if img1:
                return url1(data_parts[1])
            elif img2:
                return url1(data_parts[2])
            else:
                return None
        except:
            return None
    else:
        return None


@app.template_filter('image_id')
def imgae_id(data):
    if 'movies' in data:
        data_parts = data.split('/')
        try:
            img1 = data_parts[1].isdigit()
            img2 = data_parts[2].isdigit()
            if img1:
                return data_parts[1]
            elif img2:
                return data_parts[2]
            else:
                return None
        except:
            return None


@app.template_filter('get_info')
def get_movie_info(id1):
    info = {}
    url_name = str(id1) + '-test'
    if id1 is not None:
        if redis.check(url_name) == 0:
            try:
                import requests
                url = f"http://www.jiorockerss.vin/movies/{id1}/p.html"
                print(url)
                r = requests.Session()
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
                    'Connection': 'keep-alive'
                }
                resp = r.get(url, headers=headers)
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(resp.text, 'html.parser')

                def set_info(name, listname, info):
                    """
                    name = movie_name,
                    listname - elements array,
                    info is dictonary
                    """
                    if name in listname:
                        info[listname[0]] = listname[1]

                for kj in soup.find_all('tr'):
                    all_tds_sub = kj.find_all('td')
                    all_tds_sub = [i.text for i in all_tds_sub]
                    set_info('Movie Name', all_tds_sub, info)
                    set_info('Starring:', all_tds_sub, info)
                    set_info('Director', all_tds_sub, info)
                    set_info('Genres', all_tds_sub, info)
                    set_info('Release Date', all_tds_sub, info)
                    set_info('Duration', all_tds_sub, info)
                    set_info('Description', all_tds_sub, info)
                    set_info('Rating', all_tds_sub, info)
            except:
                info = {}
            redis.save_dict(url_name, info)
        else:
            redis.get_rdict(url_name)
    return info


@app.route('/get/<img>')
def nav(img):
    return RedisClass().get(img)


@app.route('/search')
def search():
    query = request.args.get('q')
    query = html.escape(query)
    print(query)
    query = None if query == '' else query
    if query:
        url = f'https://www.jiorockerss.vin/search-movies.html?search={query}'
        print(url)
        import requests
        resp = requests.get(url, headers=headers)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(resp.text, 'html.parser')
        atags = soup.find_all('a')
        atags = {i['href'].replace('https://www.jiorockerss.vin', ''): i.text for i in atags}
        return render_template('index_links.html', links=atags, message=query)
    else:
        url = 'https://www.jiorockerss.vin/search-movies.html?search=latest'
        import requests
        resp = requests.get(url, headers=headers)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(resp.text, 'html.parser')
        atags = soup.find_all('a')
        atags = {i['href'].replace('https://www.jiorockerss.vin', ''): i.text for i in atags}
        return render_template('index_links.html', links=atags)


@app.errorhandler(500)
def on_abort(e):
    return render_template('500.html'), 500


@app.template_filter('minfo')
def minfo(url):
    import requests
    r = requests.head(url)
    url = r.headers['Location']
    filename = url.split('/')[-1]
    r = requests.head(url).headers
    size = int(int(r['Content-Length']) / 1024 / 1024)
    htmlMessage = f"""<table class="table table-bordered"><tr class="table-light"><td>Name</td><td>{filename}</td></tr><tr class="table-light"><td>Size</td><td>{size}mb</td></tr></table>"""
    return htmlMessage
    return f'<div class=""><p><span class="text-primary">name</span> :<br> {filename}<br><span class="text-primary">size</span> :<br>{size}mb</p></div>'


@app.template_filter('playurl')
def playurl(url):
    import requests
    r = requests.head(url)
    url = r.headers['Location']
    return url


@app.route('/details/Screenshots/<id1>/')
def get_image(id1):
    import requests
    return requests.get(f'http://www.jiorockerss.vin/details/Screenshots/{id1}/{id1}a.jpg').content



if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5001', debug=False)
