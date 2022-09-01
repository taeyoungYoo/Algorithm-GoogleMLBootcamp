import collections

def solution(id_list : list, report : list, k : int):
    name_to_id = collections.defaultdict(list)
    report_time = collections.Counter()
    report = list(set(report))

    for rep in report:
        name_to_id[rep.split()[0]].append(rep.split()[1])
        report_time[rep.split()[1]] += 1
    ret = []


    for id in id_list:
        cnt = 0
        for rep in name_to_id[id]:
            if report_time[rep] >= k:
                cnt += 1
        ret.append(cnt)

    return