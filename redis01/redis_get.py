from redis import Redis

if __name__ == '__main__':
    try:
        redis_client = Redis(host="192.168.84.128", port=6379, decode_responses=True)
        result = redis_client.get("name5")
        print(result, type(result))
        # str1 = result.decode("utf-8")
        # print(str1, type(str1))
    except Exception as e:
        print(e)
