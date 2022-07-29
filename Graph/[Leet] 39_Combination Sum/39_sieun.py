class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 알고리즘 수행 함수(조건에 맞는 중복 조합을 찾는 함수)
        def get_answer(i=0, combs=[]):
            combs_sum = sum(combs)

            # 종료 조건1 (정답 조건 만족)
            if combs_sum == target:
                answer.append(combs)
                return 
            # 종료 조건2 (정답 조건 위배)
            if combs_sum > target:
                return 
            # 종료 조건3 (모든 요소 순회)
            if i == len(candidates):
                return 
            
            # 재귀 수행 
            get_answer(i, combs + [candidates[i]]) # 삽입 후 현재 인덱스에 대해 수행
            get_answer(i+1, combs + [candidates[i]]) # 삽입 후 다음 인덱스에 대해 수행
            get_answer(i+1, combs) # 삽입하지 않고 다음 인덱스에 대해 수행 
            
        answer = []
        get_answer()
        return set(map(tuple, answer))