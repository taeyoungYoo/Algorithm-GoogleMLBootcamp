class Solution:
    def groupAnagrams(self, strs):

        items = set([tuple(sorted(s)) for s in strs])   # strs의 각 요소를 알파벳 정렬한 후 튜플 값으로 변환하여 중복제거

        items = {item: [] for item in items}        # 고유한 값만 남은 items의 각 요소를 key, 빈 리스트를 값으로 갖는 딕셔너리 생성

        for s in strs:
            items[tuple(sorted(s))].append(s)       # strs의 각 요소를 해당하는 딕셔너리 key의 값인 빈 리스트에 추가

        return [x for x in items.values()]      # 딕셔너리의 value만 리스트로 반환


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))
