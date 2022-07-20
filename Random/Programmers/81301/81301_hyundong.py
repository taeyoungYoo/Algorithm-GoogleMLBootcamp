# # def solution(s):
# #     min_point = 0
# #     answer = []
# #     board = {'zero' : 0, 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 
# #              'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9, 'ten' : 10}
# #     for index, str_num in enumerate(s):
# #         if str_num.isdigit() or index == len(s):
# #             answer.append(board[s[min_point:index]])
# #             answer.append(str_num)
# #             min_point = index+1
# #             pass

# #     return answer

# # print(solution("one4seveneight"))



# def solution(s):
#     min_point = 0
#     answer = ''
#     board = {'zero' : 0, 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 
#              'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9, 'ten' : 10}
#     while min_point < len(s):
#         if s[min_point].isdigit():
#             answer.append(int(s[min_point]))
#             min_point += 1
#         else:
#             for i in range(3, 6):
#                 current = s[min_point:min_point + i]
#                 if current in board:
#                     answer.append(board[current])
#                     min_point = min_point+i
#     return answer

# print(solution("one4seveneight"))

# def solution(s):
#     min_point = 0
#     answer = []
#     board = {'zero' : 0, 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 
#              'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9, 'ten' : 10}
#     for index, str_num in enumerate(s):
#         if str_num.isdigit() or index == len(s):
#             answer.append(board[s[min_point:index]])
#             answer.append(str_num)
#             min_point = index+1
#             pass

#     return answer

# print(solution("one4seveneight"))



def solution(s):
    min_point = 0
    answer = ''
    board = {'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 
             'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9', 'ten' : '10'}
    while min_point < len(s):
        if s[min_point].isdigit():
            answer = answer + s[min_point]
            min_point += 1
        else:
            for i in range(3, 6):
                current = s[min_point:min_point + i]
                if current in board:
                    answer = answer + board[current]
                    min_point = min_point+i
    return int(answer)

print(solution("one4seveneight"))