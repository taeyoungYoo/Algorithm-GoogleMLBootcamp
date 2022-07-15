class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        ㅇ 애너그램? : 단어 철자 순서를 바꿔서 다른 뜻을 가지는 단어를 만들기        
        ㅇ 풀이법
          - sorted() 는 단어를 풀어서 오름차순 정렬한다. 
          - sorted 처리한 w를 key, 원래 단어(w)를 value로 딕셔너리(anagrmas)에 append 한다
            * 이때 defaultdict로 딕셔너리 생성 안해두면 에러 발생
          - 딕셔너리의 values()을 반환한다.
        '''
        # defaultdict 선언
        anagrams = collections.defaultdict(list)
        
        for w in strs:
            anagrams[''.join(sorted(w))].append(w)
            # anagrams[sorted(w)].append(w)  #에러발생
            # list 형태는 key값으로 설정할 수 없나보다, join 없으니까 TypeError 발생
        return anagrams.values()
