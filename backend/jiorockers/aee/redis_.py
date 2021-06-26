import redis
import json


#redis://default:v0OItWQz9LZE3jRTxT1k1psvYNWFPwPj@redis-16418.c8.us-east-1-4.ec2.cloud.redislabs.com:16418

class RedisClass:
    def __init__(self):
        self.url = {'password': 'v0OItWQz9LZE3jRTxT1k1psvYNWFPwPj',
                    'hostname': 'redis-16418.c8.us-east-1-4.ec2.cloud.redislabs.com',
                    'port': '16418'
                    }
        self.r = redis.Redis(host=self.url['hostname'], port=self.url['port'], password=self.url['password'])

    def set(self, key, value):
        return self.r.set(key, value)

    def get(self, key):
        return self.r.get(key)

    def delete(self, key):
        return self.r.delete(key)

    def check(self, key):
        return self.r.exists(key)

    def save_dict(self, key, dict_name):
        return self.r.set(key, json.dumps(dict_name))

    def get_rdict(self, key):
        return json.loads(self.r.get(key).decode('utf-8'))

    def save_hm(self, key, dict_name):
        return self.r.hset(key, dict_name)

    def get_hm(self, key):
        return self.r.hget(key)


