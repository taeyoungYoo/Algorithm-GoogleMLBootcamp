# runtime: 61ms, memory: 14MB
# Linked list를 시작부터 끝까지 검사하며 O(N)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head = ListNode(0)
        while list1 is not None and list2 is not None:
            if list1.val > list2.val:
                tmp.next = list2
                list2 = list2.next
            else:
                tmp.next = list1
                list1 = list1.next
            tmp = tmp.next
        if list1 is None:
            tmp.next = list2
        else:
            tmp.next = list1

        return head.next