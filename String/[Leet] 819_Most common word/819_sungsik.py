import re


class Solution:
    def mostCommonWord(self, paragraph, banned):

        paragraph = re.sub('[^a-z ]', ' ', paragraph.lower())   # 입력받은 paragraph에서 알파벳(소문자)과 공백만 추출
        banned.append('')   # 아래에서 words 리스트 내 공백을 삭제하기 위해 banned에 공백 요소 추가

        words = paragraph.split(' ')    # 알파벳과 공백만 추출한 paragraph를 word 단위로 분할하여 리스트화
        words = [word for word in words if word not in banned]  # words 요소 중 banned 리스트에 없는 단어만 추출

        word_dic = {word: 0 for word in set(words)}     # words 리스트를 요소를 key로 하는 딕셔너리 생성

        for word in words:
            word_dic[word] += 1     # word_dic에 해당 word의 값을 1씩 더해 개수를 세줌

        return [k for k, v in word_dic.items() if max(word_dic.values()) == v][0]   # 딕셔너리에서 가장 큰 값의 key 반환


paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]

print(Solution().mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))
