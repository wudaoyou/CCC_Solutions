outcome = []
ori = []
import copy


def get_game_result(game_table, result, idx):
    if idx == len(game_table):
        # print(result)
        outcome.append(copy.deepcopy(result))

    else:
        first, second = game_table[idx]
        # first team won
        # print('%d game %d team won' % (idx + 1, first))
        result[(first, second)] = 3
        result[(second, first)] = 0
        get_game_result(game_table, result, idx + 1)

        # second team won
        # print('%d game %d team won' % (idx + 1, second))
        result[(first, second)] = 0
        result[(second, first)] = 3
        get_game_result(game_table, result, idx + 1)
        # tie
        # print('%d game %d team and %d team tie' % (idx + 1, first, second))
        result[(first, second)] = 1
        result[(second, first)] = 1
        get_game_result(game_table, result, idx + 1)


def get_highest(result, fav):
    rank = []
    total = 0
    for i in range(1, 5):
        for j in range(1, 5):
            total += item[i, j]
        rank.append(total)
        total = 0

    # print(rank)
    m = max(rank)
    if fav == rank.index(m) + 1 and rank.count(m) < 2:
        return 1
    else:
        return 0


if __name__ == "__main__":
    fav = int(input())
    game = int(input())
    game_table = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    game_result = {}
    for i in range(1, 5):
        for j in range(1, 5):
            game_result[(i, j)] = 0

    data = [-1, 0, 0, 0, 0]
    for i in range(game):
        result = input()
        lst = result.split()
        lst = [int(c) for c in result if c != ' ']
        if lst[2] > lst[3]:
            data[lst[0]] += 3
            game_result[(lst[0], lst[1])] = 3
            game_result[(lst[1], lst[0])] = 0
        elif lst[2] == lst[3]:
            data[lst[0]] += 1
            data[lst[1]] += 1
            game_result[(lst[0], lst[1])] = 1
            game_result[(lst[1], lst[0])] = 1
        else:
            data[lst[1]] += 3
            game_result[(lst[0], lst[1])] = 0
            game_result[(lst[1], lst[0])] = 3
        game_table.remove((lst[0], lst[1]))
    # print(data)
    # print(game_table)
    # print(game_result)

    # ori = copy.deepcopy(data)
    get_game_result(game_table, game_result, 0)
    # print(outcome)
    # print(len(outcome))
    final = []
    for item in outcome:
        final.append(get_highest(item, fav))

    # print(final)
    print(sum(final))