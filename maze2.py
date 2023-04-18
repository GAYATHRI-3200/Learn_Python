
def exit_points_list(m, n, x, y, matrix) :
    exit_points = []
    time = []
    for i in range (n) :
        exit_points.append(0)
        time.append(0)
    for column in range (n) :
        prevColumn = column
        currentColumn = column
        for row in range (m) :
            nextColumn = currentColumn + matrix[row][currentColumn]
            if ( nextColumn < 0 or nextColumn > n - 1 or matrix[row][currentColumn] != matrix[row][nextColumn] ) :
                exit_points[column] = -1 
                break
            exit_points[column] = nextColumn
            time[column] += x
            if row < m - 1 :
                if matrix[row][currentColumn] != matrix[row + 1][nextColumn] :
                    time[column] += y
            if row == m  - 1 :
                if matrix[row - 1][prevColumn] != matrix[row][currentColumn] :
                    time[column] += y
            prevColumn = currentColumn
            currentColumn = nextColumn
    result = []
    for i in range (n) :
        if exit_points[i] != -1 :
            result.append([exit_points[i], time[i]])
        else :
            result.append([-1, -1])
    return result
def main() :
    m, n, x, y = map(int, input().split())
    matrix = []
    for i in range (m) :
        row = list(map(int, input().split()))
        matrix.append(row)
    print(exit_points_list(m, n, x, y, matrix))
main()
