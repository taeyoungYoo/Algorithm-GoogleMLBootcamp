def solution(id_list, report, k):
  result = [0] * len(id_list)

  id_dict = dict.fromkeys(id_list, 0)

  report = set(report)
  reported_user = [x.split(' ')[1] for x in report]

  # 신고 횟수
  for i in reported_user:
    id_dict[i] += 1

  # 차단 유저
  block = [key for key, value in id_dict.items() if value >= k]

  # 메일 처리
  for j in report:
    reporter, reported = j.split(' ')
    if reported in block:
      result[id_list.index(reporter)] += 1

  return result
