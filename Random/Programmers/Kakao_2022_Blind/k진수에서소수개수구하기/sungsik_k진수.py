def convert_n_to_k(n, k):  # n을 k진수로 반환
  ret = ""
  while n > 0:
    ret += str(n % k)
    n = n // k
  return ''.join(reversed(ret))

def solution(n, k):
  answer = -1


  return answer



