def next_distinct_year(year):
    year += 1
    while len(set(str(year))) != len(str(year)):
        year += 1
    return year


if __name__ == '__main__':
    print(next_distinct_year(int(input())))
