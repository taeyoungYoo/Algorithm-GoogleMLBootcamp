import collections
import math

def solution(fee, records):
    answer = []
    time_lim = "23:59"
    car_info = collections.defaultdict(list)

    for rec in records:
        tmp = rec.split(" ")
        car_info[tmp[1]].append(tmp[0])
    car_info = sorted(car_info.items())

    for car in car_info:
        time = collections.deque(car[1])
        ret = 0
        if len(time) % 2 == 1:
            time.append(time_lim)
        while time:
            str_time_late = time.pop().split(":")
            str_time_early = time.pop().split(":")
            ret += int(str_time_late[0]) * 60 + int(str_time_late[1]) - int(str_time_early[0]) * 60 - int(str_time_early[1])
        if ret > fee[0]:
            answer.append(fee[1] + math.ceil((ret-fee[0])/fee[2]) * fee[3])
        else:
            answer.append(fee[1])
    return