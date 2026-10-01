def find_year(year):
    year_num = int(year) + 1
    year = str(year_num)
    while (True):
        lst = list(year)
        if len(lst) > len(set(lst)):
            year_num += 1
            year = str(year_num)
        else:
            return year_num


if __name__ == "__main__":
    print(find_year(input()))
