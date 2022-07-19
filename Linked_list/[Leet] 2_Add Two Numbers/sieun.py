# 시은 풀이 - 93ms
class Solution(object):
    # 연결 리스트 -> 숫자
    def list_to_num(self, list):
        num = ''

        while list:
            num += str(list.val)
            list = list.next

        return int(num[::-1])

    # 숫자 -> 연결 리스트
    def num_to_list(self, num):
        head, node = ListNode(), ListNode()
        head.next = node

        num = str(num)[::-1]
        n = len(num)

        for i in range(n):
            node.val = num[i]
            if i < n - 1:
                node.next = ListNode()
                node = node.next

        return head.next

    def addTwoNumbers(self, l1, l2):
        n1 = self.list_to_num(l1)
        n2 = self.list_to_num(l2)
        return self.num_to_list(n1 + n2)