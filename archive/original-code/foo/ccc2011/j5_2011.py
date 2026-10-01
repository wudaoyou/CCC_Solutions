data = []
data2 = []
counter = 0


def all_subsets(given_array):
    subset = [None] * len(given_array)
    helper(given_array, subset, 0)


def helper(given_array, subset, i):
    if i == len(given_array):
        # print(subset)
        data.append(subset[:])
    else:
        subset[i] = None
        helper(given_array, subset, i + 1)
        subset[i] = given_array[i]
        helper(given_array, subset, i + 1)


def remove_relation(invs):
    lst = []
    for per, inv in invs:
        if len(inv) > 0:
            # if you remove per, you need remove inv too.
            # in the data, we need to remove item only have per
            p = invs[per - 1]
            lst = [invs[i - 1] for i in inv]
            # print(lst)
            for item in data[::-1]:
                if p in item:
                    if all(elem in item for elem in lst):
                        continue
                    else:
                        #print(item)
                        data.remove(item)


if __name__ == "__main__":
    total = int(input())
    friends = {}
    for i in range(total + 1):
        friends[i] = []
    # print(friends)

    for i in range(total - 1):
        invite = int(input())
        friends[invite].append(i + 1)

    friends.pop(len(friends) - 1)
    friends.pop(0)
    invites = [(k, v) for k, v in friends.items()]
    #print(invites)
    all_subsets(invites)
    # print(data)
    remove_relation(invites)
    # print(data)
    print(len(data2) if len(data2) > 0 else len(data))