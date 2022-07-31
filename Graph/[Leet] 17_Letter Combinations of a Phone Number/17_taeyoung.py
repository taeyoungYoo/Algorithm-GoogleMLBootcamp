# Queue를 사용한 풀이
# runtime: 38ms, memory: 13.9MB
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        match_digit = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
               '6':"mno", '7':'pqrs', '8':'tuv', '9':'wxyz'}
        ret = []
        q = collections.deque()
        for char_ in digits:
            q.append(char_)
        if not q:
            return []
        init_ = q.popleft()
        for char_ in match_digit[init_]:
            ret.append(char_)
        while q:
            cur = q.popleft()
            rem_after = len(ret)
            for i in range(len(ret)):
                tmp = ret[i]
                for sub in match_digit[cur]:
                    ret.append(tmp + sub)
            ret = ret[rem_after:]
        return ret