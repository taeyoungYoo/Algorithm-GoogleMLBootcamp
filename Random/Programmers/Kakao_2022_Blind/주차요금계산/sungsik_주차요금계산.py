import math

def solution(fees, records):
  answer = []
  return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
           "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]


# 차량 번호 별 주차시간 산출
parking_time = {}
car_in = []
car_out = []

for record in records:
  time, no, io = record.split()
  if io == 'IN':
    car_in.append([no, time])
  elif io == 'OUT':
    car_out.append([no, time])

print(car_in, car_out)

for car in car_in:
  no, in_time = car
  if no in [x[0] for x in car_out]:
    out_time = [x for x in car_out if x[0] == no][0][1]
  else:
    out_time = '23:59'

# 요금 산정

# print(math.ceil((334 - 180) / 10))



# print(solution(fees, records))
