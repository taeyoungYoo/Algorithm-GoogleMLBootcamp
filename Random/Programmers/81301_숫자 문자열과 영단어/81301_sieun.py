import re

def solution(s):
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(numbers)):
        s = re.sub(numbers[i], str(i), s)

    return int(s)