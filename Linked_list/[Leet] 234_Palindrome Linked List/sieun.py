# 시은 풀이 - 1091ms
class Solution(object):
    def isPalindrome(self, head):
        # 노드의 값만 저장
        nodes = []

        while head:
            nodes.append(head.val)
            head = head.next

        # 팰린드롬 여부 확인
        return nodes == nodes[::-1]

# 교재 풀이 - 1355ms
class Solution2(object):
    def isPalindrome(self, head):
        # 데크 자료형 선언 (이중 연결 리스트 구조)
        q = collections.deque()

        while head:
            q.append(head.val)
            head = head.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True

# 리스트는 pop(index)를 통해 index 위치의 요소를 꺼낼 수 있다.
# 이때 pop(0)은 O(n)의 시간이 걸린다.
# 데크는 popleft()를 통해 pop(0)과 같은 역할을 수행하는데,
# O(1)의 시간이 걸린다. => 최적화 가능