# Runtime: 1742ms, memory: 47MB
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        item = head
        data = []
        while item is not None:
            data.append(item.val)
            item = item.next
        left = 0
        right = len(data) - 1

        while (left < right):
            if data[left] == data[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

# 책 풀이 using deque
# runtime: 1255ms, memory:46.9MB
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q = collections.deque()

        node = head

        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True