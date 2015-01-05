def checkio(matrix):
    matrix_copy = matrix[ : ]
    connect_points = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    result = []
    for i in xrange(0, len(matrix)):
        for j in xrange(0, len(matrix[i])):
            if matrix_copy[i][j] == -1:
                continue
            stack = [(i, j)]
            count = 1
            connect_value = matrix_copy[i][j]
            matrix_copy[i][j] = -1
            #print i, j
            while len(stack) != 0:
                index_i, index_j = stack.pop()
                #connect_value = matrix_copy[index_i][index_j]
                for c_i, c_j in [(connect[0] + index_i, connect[1] + index_j) for connect in connect_points if (connect[0] + index_i) >= 0 and (connect[0] + index_i) < len(matrix) and (connect[1] + index_j) >= 0 and (connect[1] + index_j) < len(matrix[0])]:
                    #print c_i, c_j
                    if connect_value == matrix_copy[c_i][c_j]:
                        #if connect_value == 1:
                        #    print c_i, c_j
                        stack.append((c_i, c_j))
                        count += 1
                        matrix_copy[c_i][c_j] = -1
            result.append([count, connect_value])
    #print result
    #replace this for solution
    return max(result, key = lambda x:x[0])

#web page:http://www.checkio.org/mission/radiation-search/
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [1, 2, 3, 4, 5],
        [1, 1, 1, 2, 3],
        [1, 1, 1, 2, 2],
        [1, 2, 2, 2, 1],
        [1, 1, 1, 1, 1]
    ]) == [14, 1], "14 of 1"

    assert checkio([
        [2, 1, 2, 2, 2, 4],
        [2, 5, 2, 2, 2, 2],
        [2, 5, 4, 2, 2, 2],
        [2, 5, 2, 2, 4, 2],
        [2, 4, 2, 2, 2, 2],
        [2, 2, 4, 4, 2, 2]
    ]) == [19, 2], '19 of 2'
