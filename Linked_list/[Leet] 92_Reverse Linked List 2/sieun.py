# 시은 풀이 - 44ms
class Solution(object):
    def reverseBetween(self, head, left, right):
        node, i = head, 1

        # 범위 이전 리스트
        outer_head, outer_node = ListNode(None), ListNode(None)
        outer_head.next = outer_node

        while node and i < left:
            outer_node.val = node.val
            if i < left - 1:
                outer_node.next = ListNode()
                outer_node = outer_node.next
            node = node.next
            i += 1

        # 범위 내 뒤집힌 리스트
        inner_head = None

        while node and i <= right:
            inner_head = ListNode(node.val, inner_head)
            node = node.next
            i += 1

        inner_node = inner_head

        while inner_node and inner_node.next:
            inner_node = inner_node.next

        # 범위 내 뒤집힌 리스트 삽입
        if inner_head:
            if outer_node.val:
                outer_node.next = inner_head
            else:
                outer_head.next = inner_head
        if inner_node and node:
            inner_node.next = node

        return outer_head.next