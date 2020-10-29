import redis


class Storage:
    def __init__(self):
        self.r = redis.Redis(host='redis_server')

    def send_message(self, message: str):
        self.r.rpush('all_messages', message)

    def get_all_messages(self) -> list:
        # return [msg.decode('UTF-8') for msg in self.r.lrange('all_messages', 0, 1000)]
        return list(map(lambda x: x.decode('UTF-8'), self.r.lrange('all_messages', 0, 1000)))

