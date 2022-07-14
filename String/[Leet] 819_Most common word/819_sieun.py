# 시은 풀이 - 55ms
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        # 소문자로 변환 + !?',;." 제거 + 문자열 -> 리스트
        paragraph = re.sub(r'[!?\',;.\"]', ' ', paragraph.lower()).split(' ')
        # 단어 종류
        words = {word for word in paragraph if word not in banned + ['']}
        # 최다 빈출 단어, 최다 빈출 횟수
        max_word, max_count = '', -1

        for word in words:
            count = paragraph.count(word)

            if count > max_count:
                max_count = count
                max_word = word

        return max_word


# 교재 풀이 - 40ms
class Solution2(object):
    def mostCommonWord(self, paragraph, banned):
        # 소문자로 변환 + !?',;." 제거 + 문자열 -> 리스트
        paragraph = re.sub(r'[!?\',;.\"]', ' ', paragraph.lower()).split(' ')
        # 단어 종류
        words = [word for word in paragraph if word not in banned + ['']]

        # collections.Counter(iterable)
        # - 데이터의 개수를 파악할 때 유용한 클래스
        # - 데이터를 key로 갖고 데이터의 개수를 value로 갖는 딕셔너리를 반환
        counts = collections.Counter(words)

        # most_common(n)
        # - 반환 값
        # -> 상위 n개 데이터의 정보
        # -> 각 데이터에 대하여 (데이터, 개수) 형식을 갖는 리스트
        # -> [('a', 1), ('b', 2), ..., ('?', n)]
        return counts.most_common(1)[0][0]