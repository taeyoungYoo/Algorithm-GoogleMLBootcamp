# Runtime: 8786ms, memory: 18.3MB
# sort strs and group them with visited list
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_strs = [sorted(x) for x in strs]
        visited = [False] * len(strs)
        ret = []
        for i in range(len(strs)):
            tmp = []
            if visited[i] == True:
                continue
            else:
                for j in range(i, len(strs)):
                    if visited[j] == False and sort_strs[i] == sort_strs[j]:
                        visited[j] = True
                        tmp.append(strs[j])
                ret.append(tmp)
        return ret

# runtime: 140ms, memory: 17.2MB
# use hash of the sorted word
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())