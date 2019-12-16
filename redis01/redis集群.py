from rediscluster import *

if __name__ == '__main__':
    try:
        # 构建所有的节点，Redis会使用CRC16算法，将键和值写到某个节点上
        # 一个3个主3个从，这3个是主
        startup_nodes = [
            {"host": "192.168.84.128", "port": "7000"},
            {"host": "192.168.84.128", "port": "7001"},
            {"host": "192.168.84.128", "port": "7002"},
        ]
        src = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
        # 设置为name
        result = src.set("name", "itheima")
        print(result)

        name = src.get("name")
        print(name)
    except Exception as e:
        print(e)
