import json

import pymongo
from flask import Flask, jsonify, request
from bson import json_util, ObjectId
import requests

app = Flask(__name__)


class MongoAPi:
    def __init__(self):
        myclient = pymongo.MongoClient(
            "mongodb://db:12345678@iad2-c14-2.mongo.objectrocket.com:53931/?authSource=db&ssl=false&retryWrites=false")
        self.mydb = myclient['db']
        self.tbb = self.mydb['tb1']


@app.route('/teluguold')
@app.route('/teluguOld')
async def root_acc():
    m = MongoAPi()
    telugu2001 = m.mydb.get_collection('Telugu Old Movies (1950-2000)')
    d = [x for x in list(telugu2001.find())]
    d = jsonify(json.loads(json_util.dumps(d).replace('$oid', 'oid').replace('_id', 'root_id')))
    d.headers.add("Access-Control-Allow-Origin", "*")
    return d


@app.route('/menu')
async def menu_all():
    d = jsonify([
        "latest",
        "Telugu 2021 Movies",
        "Telugu 2020 Movies",
        "Telugu 2019 Movies",
        "Telugu 2018 Movies",
        "Telugu 2017 Movies",
        "Telugu 2016 Movies",
        "Telugu 2015 Movies",
        "Telugu 2014 Movies",
        "Telugu 2013 Movies",
        "Telugu 2012 Movies",
        "Telugu 2011 Movies",
        "Telugu 2010 Movies",
        "Telugu 2009 Movies",
        "Telugu 2008 Movies",
        "Telugu 2007 Movies",
        "Telugu 2006 Movies",
        "Telugu 2005 Movies",
        "Telugu 2004 Movies",
        "Telugu 2003 Movies",
        "Telugu 2002 Movies",
        "Telugu 2001 Movies",
        "Telugu Old Movies (1950-2000)"
    ])
    d.headers.add("Access-Control-Allow-Origin", "*")
    return d


@app.route('/<name>')
async def root_acc2(name):
    m = MongoAPi()
    telugu2001 = m.mydb.get_collection(name)
    d = [x for x in list(telugu2001.find())]
    d = jsonify(json.loads(json_util.dumps(d).replace('$oid', 'oid').replace('_id', 'root_id')))
    d.headers.add("Access-Control-Allow-Origin", "*")
    return d


@app.route('/search')
async def search_q():
    query = request.args['q']
    from elasticsearch import Elasticsearch, helpers
    import re
    # Parse the auth and host from env:
    bonsai = 'https://o6vjjygehi:31eyp8h63l@spruce-264288808.us-east-1.bonsaisearch.net:443'
    auth = re.search('https\:\/\/(.*)\@', bonsai).group(1).split(':')
    host = bonsai.replace('https://%s:%s@' % (auth[0], auth[1]), '')

    # optional port
    match = re.search('(:\d+)', host)
    if match:
        p = match.group(0)
        host = host.replace(p, '')
        port = int(p.split(':')[1])
    else:
        port = 443

    # Connect to cluster over SSL using auth for best security:
    es_header = [{
        'host': host,
        'port': port,
        'use_ssl': True,
        'http_auth': (auth[0], auth[1])
    }]
    # Instantiate the new Elasticsearch connection:
    es = Elasticsearch(es_header)
    result_data = es.search(index='autocomplete', body={
        "size": 10,
        "query": {
            "multi_match": {
                "query": query,
                "type": "bool_prefix",
                "fields": [
                    "name",
                    "name._2gram",
                    "name._3gram"
                ]
            }
        }
    })
    result_data = result_data['hits']
    result_data = result_data['hits']
    print(result_data)
    result_data = [x['_source'] for x in result_data]
    result_data = jsonify(result_data)
    result_data.headers.add("Access-Control-Allow-Origin", "*")
    return result_data


@app.route('/latest')
async def latest_movies():
    from elasticsearch import Elasticsearch, helpers
    import re
    # Parse the auth and host from env:
    bonsai = 'https://o6vjjygehi:31eyp8h63l@spruce-264288808.us-east-1.bonsaisearch.net:443'
    auth = re.search('https\:\/\/(.*)\@', bonsai).group(1).split(':')
    host = bonsai.replace('https://%s:%s@' % (auth[0], auth[1]), '')

    # optional port
    match = re.search('(:\d+)', host)
    if match:
        p = match.group(0)
        host = host.replace(p, '')
        port = int(p.split(':')[1])
    else:
        port = 443

    # Connect to cluster over SSL using auth for best security:
    es_header = [{
        'host': host,
        'port': port,
        'use_ssl': True,
        'http_auth': (auth[0], auth[1])
    }]
    # Instantiate the new Elasticsearch connection:
    es = Elasticsearch(es_header)
    result_data = es.search(index='movie',
                            body={
                                "size": 20,
                                "sort": {"_seq_no": "desc"},
                                "query": {
                                    "match_all": {}
                                }
                            })
    result_data = result_data['hits']
    result_data = result_data['hits']
    print(result_data)
    result_data = [x['_source'] for x in result_data]
    result_data = jsonify(result_data)
    result_data.headers.add("Access-Control-Allow-Origin", "*")
    return result_data


if __name__ == '__main__':
    app.run()
