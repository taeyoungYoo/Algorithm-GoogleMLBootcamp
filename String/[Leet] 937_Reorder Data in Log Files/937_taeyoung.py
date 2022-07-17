class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # Both letter logs and digit logs consist of only letters or digits
        # Check only first letter that comes after the identifier
        letters = []
        numbers = []
        # n num of logs -> O(n)
        for log in logs:
            if (log.split()[1].isdigit()):
                numbers.append(log)
            else:
                letters.append(log)
        # How to sort the identifier?
        # use sort() api with key
        letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        return letters + numbers