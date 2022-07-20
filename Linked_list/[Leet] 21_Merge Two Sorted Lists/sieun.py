# 시은 풀이-44ms
class Solution(object):
    # 한 리스트 merge 함수
    def merge_one(self, list1):
        while list1:
            self.node.val = list1.val
            list1 = list1.next

            if list1:
                self.node.next = ListNode()
                self.node = self.node.next

    # 두 리스트 merge 함수
    def merge_two(self):
        while self.list1 and self.list2:
            if self.list1.val < self.list2.val:
                self.node.val = self.list1.val
                self.list1 = self.list1.next
            else:
                self.node.val = self.list2.val
                self.list2 = self.list2.next

            if self.list1 or self.list2:
                self.node.next = ListNode()
                self.node = self.node.next

    def mergeTwoLists(self, list1, list2):
        if not list1 and not list2:
            return list1

        self.list1 = list1
        self.list2 = list2
        self.head = ListNode()
        self.node = ListNode()
        self.head.next = self.node

        self.merge_two()
        self.merge_one(self.list1)
        self.merge_one(self.list2)

        return self.head.next

# 교재 풀이 - 40ms
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # 비교 및 스왑
        if not list1 or list2 and list1.val > list2.val:
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1