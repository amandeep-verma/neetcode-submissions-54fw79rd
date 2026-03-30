class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            tmp = self.cache.pop(key)
            self.cache[key] = tmp
            return tmp

        # for i in range(len(self.cache)):
        #     if self.cache[i][0] == key:
        #         tmp = self.cache.pop(i)
        #         self.cache.append(tmp)
        #         return tmp[1]
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            tmp = self.cache.pop(key)
            self.cache[key] = value
            return

        if self.capacity == len(self.cache):
            self.cache.pop(list(self.cache.keys())[0])


        self.cache[key] = value

        # for i in range(len(self.cache)):
        #     if self.cache[i][0] == key:
        #         tmp = self.cache.pop(i)
        #         tmp[1] = value
        #         self.cache.append(tmp)
        #         return

        # if self.capacity == len(self.cache):
        #     self.cache.pop(0)

        # self.cache.append([key, value])