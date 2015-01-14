from itertools import product
from collections import defaultdict

def color_map(region):
    connection_dict = defaultdict(set)

    for i, j in product(range(len(region)), range(len(region[0]))):
        connection_dict[region[i][j]].update(region[i + ni][j + nj] for ni, nj in ((-1, 0), (1, 0), (0, 1), (0, -1)) if 0 <= (i + ni) < len(region) and 0 <= (j +nj) < len(region[0]) and region[i][j] != region[i +ni][j + nj])
    #print connection_dict
    def draw_map(current_index, result):
        #print result
        if current_index >= len(result):
            return result
        for i in (set((1,2,3,4)) - set(map(lambda x:result[x], connection_dict[current_index]))):
            copy_result = result[ : ]
            copy_result[current_index] = i
            r = draw_map(current_index + 1, copy_result)
            if r:return r

    return draw_map(0, [0 for i in connection_dict])


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #web page:http://www.checkio.org/mission/color-map/
    NEIGHS = ((-1, 0), (1, 0), (0, 1), (0, -1))
    COLORS = (1, 2, 3, 4)
    ERROR_NOT_FOUND = "Didn't find a color for the country {}"
    ERROR_WRONG_COLOR = "I don't know about the color {}"

    result = color_map(((0, 0, 0), (0, 1, 1), (0, 0, 2)))
    print result
    def checker(func, region):
        user_result = func(region)
        if not isinstance(user_result, (tuple, list)):
            print("The result must be a tuple or a list")
            return False
        country_set = set()
        for i, row in enumerate(region):
            for j, cell in enumerate(row):
                country_set.add(cell)
                neighbours = []
                if j < len(row) - 1:
                    neighbours.append(region[i][j + 1])
                if i < len(region) - 1:
                    neighbours.append(region[i + 1][j])
                try:
                    cell_color = user_result[cell]
                except IndexError:
                    print(ERROR_NOT_FOUND.format(cell))
                    return False
                if cell_color not in COLORS:
                    print(ERROR_WRONG_COLOR.format(cell_color))
                    return False
                for n in neighbours:
                    try:
                        n_color = user_result[n]
                    except IndexError:
                        print(ERROR_NOT_FOUND.format(n))
                        return False
                    if cell != n and cell_color == n_color:
                        print("Same color neighbours.")
                        return False
        if len(country_set) != len(user_result):
            print("Excess colors in the result")
            return False
        return True

