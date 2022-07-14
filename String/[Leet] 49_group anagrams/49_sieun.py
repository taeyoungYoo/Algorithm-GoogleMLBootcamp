# 시은 풀이 - 시간 초과
class Solution(object):
    # 애너그램 판별 함수
    def isAnagrams(self, x, y):
        x = collections.Counter(x[0])
        y = collections.Counter(y[0])
        return x == y

    def groupAnagrams(self, strs):
        n = len(strs)

        # 단어 -> [단어, 그룹 번호]
        strs = [[strs[i], i] for i in range(n)]

        # 그룹 번호 갱신
        for i in range(n):
            if strs[i][1] != i:
                continue
            for j in range(i + 1, n):
                if self.isAnagrams(strs[i], strs[j]):
                    if strs[j][1] == j:
                        strs[j][1] = strs[i][1]
                    else:
                        strs[i][1] = strs[j][1]

        # 그룹화
        groups = {value[1]: [] for value in strs}

        for word in strs:
            groups[word[1]].append(word[0])

        return groups.values()

# 시은 풀이 (교재 참고) - 139ms
class Solution2(object):
    def groupAnagrams(self, strs):
        # 단어 -> (알파벳 정렬 리스트, 단어)
        strs = sorted([(sorted(word), word) for word in strs])

        # 그룹 리스트
        groups = []
        # 기준 애너그램
        anagram = None

        for word in strs:
            if anagram == word[0]:
                groups[-1].append(word[1])
            else:
                groups.append([word[1]])
                anagram = word[0]

        return groups

# 교재 풀이 - 137ms
class Solution3(object):
    # 애너그램을 판단하는 가장 간단한 방법
    # - 정렬하여 비교
    # - 애너그램 관계인 단어들은 정렬하면 서로 같은 값을 갖게 됨
    def groupAnagrams(self, strs):
        # collections.defaultdict()
        # - key가 존재하지 않아도 keyError 발생 x
        anagrams = collections.defaultdict(list)

        for word in strs:
            # 정렬
            anagram = ''.join(sorted(word))
            # 추가
            anagrams[anagram].append(word)

        return list(anagrams.values())
