# Runtime: 106ms, Memory: 14MB
# check every letter in paragraph and remove non alpha-number letter
# then remove space and get the max count val using counter dictionary
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        tmp = ""
        for letter in paragraph:
            if(letter.isalnum() or letter.isspace()):
                tmp += letter.lower()
            else:
                tmp += " "
        ret = [x for x in tmp.split(' ') if x.isalnum()]
        for ban in banned:
            while(True):
                try:
                    ret.remove(ban)
                except:
                    break
        count = collections.Counter(ret)
        return max(count, key=count.get)

# Runtime: 56ms, memory 13.8MB
# using regular expression to remove non alpha-number letter
# then remove banned word and get the max count val using counter dictionary
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ret = [x for x in re.sub(r'[^\w]', ' ', paragraph).lower().split() if x not in banned]
        count = collections.Counter(ret)
        return max(count, key=count.get)