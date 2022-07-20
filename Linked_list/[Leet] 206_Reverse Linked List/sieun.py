# 시은 풀이 - 60ms
class Solution(object):
    def reverseList(self, head):
        if not head:
            return head

        # val만 추출
        q = collections.deque()

        while head:
            q.append(head.val)
            head = head.next

        # 연결 리스트 생성
        head = ListNode()
        node = ListNode()
        head.next = node

        while q:
            node.val = q.pop()
            if q:
                node.next = ListNode()
                node = node.next

        return head.next

# 시은 풀이(교재 참고) - 27ms
class Solution2(object):
    def reverseList(self, head):
        prev = None

        while head:
            # prev = {val: head.val, next: prev}
            prev = ListNode(head.val, prev)
            head = head.next

        return prev

# 교재 풀이 - 30ms
class Solution3(object):
    def reverseList(self, head):
        node, prev = head, None

        while node:
            # next가 node의 다음 노드를 가리키게 함
            next = node.next  # next = {val: node.next.val, next: node.next.next}

            # node의 다음 노드를 prev로 변경
            node.next = prev  # node = {val: node.val, next: prev}

            # prev를 node로 변경
            prev = node  # prev = {val: node.val, next: prev}

            # node를 node의 다음 노드로 변경
            node = next  # node = {val:node.next.val, next: node.next.next}

        return prev

