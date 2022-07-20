def solution(s):
    answer = s
    dict_num_str = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
                    "six": "6", "seven": "7", "eight": '8', "nine": '9', "zero": "0"}
    for key in dict_num_str.keys():
        while (key in answer):
            answer = answer.replace(key, dict_num_str[key])

    return int(answer)