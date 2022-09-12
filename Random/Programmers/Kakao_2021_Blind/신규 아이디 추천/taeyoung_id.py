import re
def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9-_.]','', new_id)
    answer = ''
    for i in range(len(new_id)):
        if new_id[i] == '.' and i != len(new_id)-1 and new_id[i+1] == '.':
            continue
        answer += new_id[i]
    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]
    if not answer:
        answer += 'a'
    if len(answer) > 15:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    while(len(answer) < 3):
        answer += answer[-1]
    return answer