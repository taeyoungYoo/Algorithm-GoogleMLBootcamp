# 시은 풀이 - 400ms 
class MyHashMap:

    def __init__(self):
        self.hashMap = {}

    def put(self, key: int, value: int) -> None:
        self.hashMap[key] = value

    def get(self, key: int) -> int:
        if key in self.hashMap.keys():
            return self.hashMap[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.hashMap.keys():
            self.hashMap.pop(key)
