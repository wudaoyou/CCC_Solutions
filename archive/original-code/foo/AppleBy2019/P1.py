def cal(A, B, C, N):
    if C >= N:
        return 0, 0, N
    else:
        N -= C
        if B >= N:
            return 0, N, C
        else:
            N -= B
            return N, B, C


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = int(input())
        B = int(input())
        C = int(input())
        if A + B + C < N:
            r = [-1]
        else:
            r = cal(A, B, C, N)
        print(' '.join(map(str, r)))
