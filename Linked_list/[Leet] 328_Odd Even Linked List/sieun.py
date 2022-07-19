# 시은 풀이 - 70ms
class Solution(object):
    # 리스트 크기 반환 함수
    def get_size(self, head):
        size = 0

        while head:
            size += 1
            head = head.next

        return size

    # 홀수(또는 짝수) 리스트 반환 함수
    def get_list(self, head, mod, count):
        list = ListNode()
        node = ListNode()
        list.next = node
        i = 1

        while head:
            if i % 2 == mod:
                node.val = head.val
                if count > 1:
                    node.next = ListNode()
                    node = node.next
                    count -= 1
            i += 1
            head = head.next

        return list.next, node

    def oddEvenList(self, head):
        # 리스트 크기
        n = self.get_size(head)

        # 0개 또는 1개 => 그대로 반환
        if n <= 1:
            return head

        # 홀수 리스트 head, node
        odd_head, odd_node = self.get_list(head, 1, (n + 1) // 2)
        # 짝수 리스트 head, node
        even_head, even_node = self.get_list(head, 0, n // 2)
        # 연결
        odd_node.next = even_head

        return odd_head