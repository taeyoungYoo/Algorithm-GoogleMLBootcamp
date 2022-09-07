def solution(n, k):
  answer = 0
  converted = ""
  while n:  # 숫자를 k진법으로 변환
    converted = str(n % k) + converted
    n = n // k

  converted = converted.split("0")

  for num in converted:
    if num == '':
      continue
    if int(num) < 2:
      continue

    prime = True
    for i in range(2, int(int(num) ** 0.5) + 1):
      if int(num) % i == 0:
        prime = False
        break

    if prime:
      answer += 1

  return answer

n = 437674
k = 3
# expect : 3

print(solution(n, k))