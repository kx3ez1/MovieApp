import json
import logging as lg
from itertools import count
import time
import random

import requests
from bs4 import BeautifulSoup
import pymongo
from dateutil.parser import parse


class LatestMovieCrawler:
    def __init__(self):
        self.final_file_url = ''  # movie url
        self.f_name = ''  # movie name
        self.fid = ''  # movie id
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        }

    def getMovieRootUrls(self, url, namelist):
        a = requests.get(url, headers=self.headers)
        smovie_links = namelist
        soup = BeautifulSoup(a.text, 'html.parser')
        cards = soup.find_all('div', {'class': 'card'})
        for i in cards:
            img_tags = i.find_all('img')
            h5_tags = i.find_all('h5')
            anchor_tags = i.find_all('a')
            if img_tags:
                if anchor_tags:
                    if anchor_tags:
                        if 'su1.tech' not in anchor_tags[0]['href']:
                            smovie_links.append(
                                {'url': 'https://su1.tech' + anchor_tags[0]['href'], 'name': h5_tags[0].text})
                            print(h5_tags[0].text, ' ==> ', 'https://su1.tech' + anchor_tags[0]['href'])
                        else:
                            smovie_links.append({'url': anchor_tags[0]['href'], 'name': h5_tags[0].text})
                            print(h5_tags[0].text, ' -- ', anchor_tags[0]['href'])

    def getMovieUrl(self, url1):
        result_url = {}
        # print('==> ',url1)
        sub_mov = requests.get(url1, headers=self.headers)
        soup2 = BeautifulSoup(sub_mov.content, 'html.parser')
        anc1 = soup2.find_all('a')
        cardBody = soup2.find_all('div', {'class': 'card'})
        for i in cardBody:
            img_tags = i.find_all('img')
            card_body = i.find_all('div', {'class': 'card-body'})
            h5_tags = i.find_all('h5')
            anchor_tags = i.find_all('a')
            if img_tags:
                if anchor_tags:
                    if 'su1.tech' not in anchor_tags[0]['href']:
                        result_url = 'https://su1.tech' + anchor_tags[0]['href']
                    else:
                        result_url = anchor_tags[0]['href']
            else:
                for i in anchor_tags:
                    if 'file/view' in i['href']:
                        if 'su1.tech' not in i['href']:
                            result_url = 'https://su1.tech' + anchor_tags[0]['href']
                        else:
                            result_url = i['href']
        return result_url

    def outFile(self, url):
        a = self.getMovieUrl(url)
        if 'file/view' in a:
            # print(a)
            self.final_file_url = self.finalOut(a)
        else:
            self.outFile(a)

    def extractNum(self, url):
        numbers = []
        for word in url.split('/'):
            if word.isdigit():
                numbers.append(int(word))
        return numbers[0]

    def finalOut(self, url):
        dd = requests.get(url, headers=self.headers)
        tt = BeautifulSoup(dd.text, 'html.parser')
        return tt.find_all('h5')[0].find_all('a')[0]['href']

    """#**Run Program Here**"""

    def getYYY(self, url):
        smovie_links = []
        # https://su1.tech/movies/7997/balamitra-2021-telugu-original-hdrip.html
        self.getMovieRootUrls(url, smovie_links)
        for i in smovie_links:
            self.f_name = i['name']
            self.fid = self.extractNum(i['url'])
            # print('{"name":"' + i['name'] + '",')
            url100 = i['url']
            # print(f'"id": {self.extractNum(url100)},')
            try:
                self.outFile(url100)
            except Exception as e:
                print('Err : ', e, ' ==> ', url100)

    # need to run first - all functions take care by this running
    # outputs from this class --> f_name,fid,final_file_url
    def get_output(self, all_links=[]):
        all_links = [x.replace('www.jiorockerss.vin', 'su1.tech') for x in all_links]
        for i in all_links:
            self.getYYY(i)


def latest_get_links_crawl_main():
    """#Direct JioROckers"""
    res = requests.get('http://www.jiorockerss.vin', headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    })
    soup = BeautifulSoup(res.text, 'html.parser')

    aa = soup.find_all('a')
    aa11 = [
        "/hindi-movies-download.html",
        "/kannada-movies-download.html",
        "/malayalam-movies-download.html",
        "/movies/1519/telugu-actors-collection.html",
        "/movies/1769/telugu-2020-dubbed-movies.html",
        "/movies/1769/telugu-2021-dubbed-movies.html",
        "/movies/1858/telugu-2010-movies.html",
        "/movies/1865/telugu-2011-movies.html",
        "/movies/1880/telugu-2012-movies.html",
        "/movies/1905/telugu-2013-movies.html",
        "/movies/1914/telugu-2014-movies.html",
        "/movies/1945/telugu-2015-movies.html",
        "/movies/1988/telugu-2016-movies.html",
        "/movies/2968/telugu-2019-movies.html",
        "/movies/3/telugu-2017-movies.html",
        "/movies/4757/telugu-2020-movies.html",
        "/movies/5219/telugu-tv-shows---general-videos.html",
        "/movies/5220/bigg-boss-telugu.html",
        "/movies/5340/telugu-2004-movies.html",
        "/movies/5344/telugu-2009-movies.html",
        "/movies/5363/telugu-2005-movies.html",
        "/movies/5439/telugu-2006-movies.html",
        "/movies/5440/telugu-old-movies-1950-2000.html",
        "/movies/5512/telugu-2002-movies.html",
        "/movies/5644/telugu-2003-movies.html",
        "/movies/5672/telugu-2000-movies.html",
        "/movies/5673/telugu-2001-movies.html",
        "/movies/5866/telugu-2007-movies.html",
        "/movies/63/telugu-2018-movies.html",
        "/movies/7361/telugu-2021-movies.html",
        "/movies/79/telugu-dubbed-movies.html",
        "/movies/tamil-2021-movies.html",
        "/tamil-movies-download.html",
        "/telugu-movies-download.html",
        "/movies/6576/bigg-boss-2020-telugu-season-4.html",
        "/telugu-movies-download.html",
        "/kannada-movies-download.html",
        "movies/1769/telugu-2020-dubbed-movies.html",
        "movies/tamil-2021-movies.html",
        "movies/tamil-2021-movies.html",
        "movies/tamil-2021-movies.html",
        "movies/tamil-2021-movies.html",
        "movies/1769/telugu-2021-dubbed-movies.html",
        "movies/1769/telugu-2021-dubbed-movies.html",
        "movies/1769/telugu-2021-dubbed-movies.html",
        "movies/1769/telugu-2020-dubbed-movies.html",
        "movies/tamil-2021-movies.html",
        "movies/tamil-2021-movies.html",
        "movies/1769/telugu-2021-dubbed-movies.html",
        "/tamil-movies-download.html",
        "/movies/4757/telugu-2020-movies.html",
        "/malayalam-movies-download.html",
        "/hindi-movies-download.html",
        "/movies/79/telugu-dubbed-movies.html",
        "/movies/4757/telugu-2020-movies.html",
        "/movies/63/telugu-2018-movies.html",
        "/movies/1988/telugu-2016-movies.html",
        "/movies/1914/telugu-2014-movies.html",
        "/movies/1880/telugu-2012-movies.html",
        "/movies/1858/telugu-2010-movies.html",
        "/movies/5866/telugu-2007-movies.html",
        "/movies/5363/telugu-2005-movies.html",
        "/movies/5644/telugu-2003-movies.html",
        "/movies/5673/telugu-2001-movies.html",
        "/movies/5440/telugu-old-movies-1950-2000.html",
        "javascript:history.go(-1)",
    ]

    dup = []
    for i in aa:
        if i['href'] in aa11:
            dup.append(i)
    for i in dup:
        aa.remove(i)

    latest_links = []
    for i in aa:
        title = i['href'].split('/')[-1].replace('-', ' ')
        id1 = [int(s) for s in i['href'].split('/') if s.isdigit()][0]
        if '/' in i['href'][0]:
            a_url = 'http://www.jiorockerss.vin' + i['href']
        else:
            a_url = 'http://www.jiorockerss.vin/' + i['href']
        latest_links.append(a_url)
    return latest_links


class MongoDbLatest:
    def __init__(self):
        self.my_client = pymongo.MongoClient(
            "mongodb://db:12345678@iad2-c14-2.mongo.objectrocket.com:53931/?authSource=db&ssl=false&retryWrites=false")
        self.my_db = self.my_client['db']
        self.latest_col = self.my_db['latest']
        lg.info('--> mongodb connection ok')

    def insert_mongo(self, name1, url1, id1):
        self.latest_col.insert_one({'name': name1, 'url': url1, 'id': id1, 'type': 'movie'})
        lg.info('mongodb insertion ok')

    def insert_mongo_by_col(self, name, name1=None, url1=None, id1=None):
        try:
            print('mongo insert function called')
            col = self.my_db.get_collection(name=name)
            col.insert_one({'name': name1, 'url': url1, 'id': id1, 'type': 'movie'})
        except:
            try:
                col = self.my_db.get_collection('others')
                col.insert_one({'name': name1, 'url': url1, 'id': id1, 'type': 'movie'})
            except:
                pass


class ElasticUpdate:
    def __init__(self):
        self.headers = {
            'content-type': 'application/json',
            'Authorization': 'Basic bzZ2amp5Z2VoaTozMWV5cDhoNjNs'
        }
        self._reindex = lambda src, tar: {"source": {
            "index": src
        },
            "dest": {
                "index": tar
            }
        }
        self.r = requests.Session()
        self.r.get('https://spruce-264288808.us-east-1.bonsaisearch.net/',
                   headers={'Authorization': 'Basic bzZ2amp5Z2VoaTozMWV5cDhoNjNs'})
        lg.info('--> connection to es ok')

    def insert_data(self, name, url, id1):
        # for inserting data
        res = self.r.put(f'https://spruce-264288808.us-east-1.bonsaisearch.net/movie/_create/{id1}',
                         headers=self.headers,
                         data=json.dumps({'name': name, 'url': url, 'type': 'movie', 'id': id1}))
        print(res.text)
        lg.info('insertion to es ok')

    def delete_data(self, source_id):
        # for deleting data by id
        res = self.r.delete(f'https://spruce-264288808.us-east-1.bonsaisearch.net/movie/_doc/{source_id}',
                            headers=self.headers)
        print(res)

    def reindex(self, src, tar):
        res = self.r.post('https://spruce-264288808.us-east-1.bonsaisearch.net/_reindex', headers=self.headers,
                          data=self._reindex(src, tar))
        lg.info('reindex ok')


for i in count(start=1):
    for i in latest_get_links_crawl_main():
        try:
            ll = LatestMovieCrawler()
            ll.get_output(all_links=[i])
            print(ll.f_name)
            print(ll.fid)
            print(ll.final_file_url)
            if ll.final_file_url:
                ee = ElasticUpdate()
                ee.insert_data(name=ll.f_name, url=ll.final_file_url, id1=ll.fid)
                ee.reindex('movie', 'autocomplete')

                year = parse(ll.final_file_url, fuzzy=True)
                movie_year = f"Telugu {year.year} Movies"
                print(movie_year)

                mm = MongoDbLatest()
                mm.insert_mongo_by_col(movie_year, name1=ll.f_name, id1=ll.fid, url1=ll.final_file_url)
        except Exception as e:
            lg.error(e)
            print(e)
        print('#' * 40)
    # delay every check between (10min - 20min)
    time.sleep(random.randint(60, 120) * 10)
