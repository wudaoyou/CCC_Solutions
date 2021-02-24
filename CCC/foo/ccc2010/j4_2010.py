# To check if the sequence has a period of n
# will come here at position 7, position 0 is -1 and position 7 is -1
def verify(seq, n):
    for i in range(n, len(seq)):
        # n is 7 and we get the length of the sequence.
        # [-1,-11,9,-7-89,44,0,-1,-11]
        #  i%n                  i
        if seq[i] != seq[i % n]:
            return False
    return True


while True:
    # Input data, only stores "changes" in a list named "seq"
    # example 10 100 99 88 97 90 1 45 45 44 33
    seq = input().split()
    if seq[0] == "0":
        break
    seq = seq[1:]
    for i in range(len(seq) - 1):
        seq[i] = int(seq[i + 1]) - int(seq[i])
    seq.pop()
    # seq = [-1,-11,9,-7,-89,44,0,-1,-11]
    # t is the max number.
    t = len(seq)
    for i in range(1, len(seq)):
        # first check if seq[0] is same as seq[i],
        # if they are the same, we need go to verify if the i is a new start.
        if seq[0] == seq[i] and verify(seq, i):
            t = min(t, i)
            break
    print(t)
