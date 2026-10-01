data = []
actions = ['R', 'S']
senders = {}


class Message:
    def __init__(self, indicator, sender, time=0):
        self.indicator = indicator
        self.sender = sender if indicator in actions else 'NA'
        self.time = time if indicator in actions else int(sender)


def add_data(msg):
    if msg.indicator in actions:
        if not data:
            msg.time = 0
        elif data[-1].indicator == 'W':
            msg.time = data[-1].time
        else:
            msg.time = 1

        if msg.sender not in senders and msg.sender != 'NA':
            senders[num] = 1
        else:
            senders[num] += 1

    data.append(msg)


def get_time(sender, times):
    second = 0
    if times % 2 != 0:
        return -1
    else:
        for i in range(len(data)):
            if data[i].indicator == 'R' and data[i].sender == sender:
                second += calculate_time(data[i].sender, i)
        return second


def calculate_time(s, idx):
    seconds = 0
    local_data = data[idx + 1:]
    for msg in local_data:
        if msg.sender == s and msg.indicator == 'S':
            seconds += msg.time
            return seconds
        else:
            seconds += msg.time
    return 0


if __name__ == "__main__":
    i = int(input())
    for _ in range(i):
        pair = input().split(' ')
        ind, num = pair[0], pair[1]
        add_data(Message(ind, num))
    # print(senders)

    data = list(filter(lambda x: x.indicator in actions, data))

    for k,v in sorted(senders.items()):
        print(f'{k} {get_time(k, v)}')