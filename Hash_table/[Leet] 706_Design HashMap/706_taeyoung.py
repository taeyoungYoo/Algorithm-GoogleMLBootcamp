# runtime: 1802ms, memory: 40.3MB
# Open addressing 방식을 사용
# 기본적으로 존재하지 않는 key를 조회하는 경우 -1을 반환하니 기본 값을 -1로 설정
# remove하는 경우 삭제가 아닌 -1로 되돌림

class MyHashMap:

    def __init__(self):
        self.map = [-1 for i in range(1000005)]

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1