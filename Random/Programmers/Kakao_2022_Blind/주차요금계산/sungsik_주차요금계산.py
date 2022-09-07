import math


def solution(fees, records):
  answer = []

  # 차량 번호 별 주차시간 산출
  parking_time_by_car = sorted(set([x.split()[1] for x in records]))
  parking_time_by_car = dict.fromkeys(parking_time_by_car, 0)
  car_in = []
  car_out = []

  for record in records:
    time, no, io = record.split()
    if io == 'IN':
      car_in.append([no, time])
    elif io == 'OUT':
      car_out.append([no, time])

  for car in car_in:
    no, in_time = car
    if no in [x[0] for x in car_out]:
      out_car = [x for x in car_out if x[0] == no][0]
      out_time = out_car[1]
      car_out.remove(out_car)
    else:
      out_time = '23:59'

    ih, im = list(map(int, in_time.split(':')))
    in_time_by_m = ih * 60 + im

    oh, om = list(map(int, out_time.split(':')))
    out_time_by_m = oh * 60 + om

    parking = out_time_by_m - in_time_by_m
    parking_time_by_car[no] += parking

  # 요금 산정
  # 기본시간: fees[0] / 기본요금 : fees[1] / 단위시간 : fees[2] / 단위시간당요금 : fees[3]

  for car, parking_time in parking_time_by_car.items():
    if parking_time <= fees[0]:
      answer.append(fees[1])  # 기본요금
    else:
      answer.append(fees[1] + (math.ceil((parking_time - fees[0]) / fees[2]) * fees[3]))  # 기본요금 + 초과 시간에 대한 요금

  return answer

fees = [120, 0, 60, 591]
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]

print(solution(fees, records))
