from redis import Redis, StrictRedis

if __name__ == '__main__':
    try:
        redis_client = Redis(host='192.168.84.128', port=6379)  # port 6379   主从模式中，从是只读的不能向里面写东西

        result = redis_client.set('name5', '王七')
        print(result)
        # redis_client.flushall() # 把数据全部都清除了

        # print(redis_client.get("name"))
    except Exception as e:
        print(e)
