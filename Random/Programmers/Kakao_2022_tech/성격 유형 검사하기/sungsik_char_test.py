def solution(survey, choices):
  answer = ''

  dic = {'R': 0, 'T': 0,
         'C': 0, 'F': 0,
         'J': 0, 'M': 0,
         'A': 0, 'N': 0}

  for i in range(len(choices)):
    if choices[i] < 4:
      dic[survey[i][0]] += 4 - choices[i]
    elif choices[i] > 4:
      dic[survey[i][1]] += choices[i] - 4

  if dic['R'] < dic['T']:
    answer += 'T'
  else:
    answer += 'R'

  if dic['C'] < dic['F']:
    answer += 'F'
  else:
    answer += 'C'

  if dic['J'] < dic['M']:
    answer += 'M'
  else:
    answer += 'J'

  if dic['A'] < dic['N']:
    answer += 'N'
  else:
    answer += 'A'

  return answer
