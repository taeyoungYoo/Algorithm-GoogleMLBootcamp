# 시은 풀이 - 64ms
class Solution(object):
    # 정렬 비교 함수
    def comparator(self, x, y):
        x, y = x.split(' '), y.split(' ')
        x_id, x_log = x[0], x[1:]
        y_id, y_log = y[0], y[1:]

        if x_log == y_log:
            return 1 if x_id > y_id else -1
        else:
            return 1 if x_log > y_log else -1

    def reorderLogFiles(self, logs):
        # 분류
        letter_logs = filter(lambda x: re.match(r'[a-z]', x.split(' ')[1]), logs)
        digit_logs = filter(lambda x: re.match(r'[0-9]', x.split(' ')[1]), logs)

        # letter_logs 정렬
        letter_logs.sort(key=cmp_to_key(self.comparator))

        return letter_logs + digit_logs


# 교재 풀이 - 42ms
class Solution2(object):
    def reorderLogFiles(self, logs):
        # 분류
        letter_logs, digit_logs = [], []

        for log in logs:
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        # 정렬
        letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letter_logs + digit_logs