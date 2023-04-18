grid=[]

def get_adj_col(r,c):
    if grid[r][c] == 1:
        return c+1
    return c-1
    
def get_next_pos(current_row,current_col):
    adj_col= get_adj_col(current_row,current_col)
    if adj_col < n and adj_col >= 0:
        if grid[current_row][current_col] == grid[current_row][adj_col]:
            return current_row+1,adj_col
    return current_row,current_col

def get_exit_pos(col):
    current_row = 0
    current_col = col
    while current_row < m:
        next_row,next_col = get_next_pos(current_row,current_col)
        if next_row == current_row:
            return -1
        current_row,current_col=next_row,next_col
    return next_col

def read_grid(m,n):
    for i in range(m):
        row = list(map(int,input().split()))
        grid.append(row)


def main():
    global grid, m, n
    m,n = map(int,input().split())
    read_grid(m,n)
    exit_pos_list=[]
    for col in range(n):
        exit_pos = get_exit_pos(col)
        exit_pos_list.append(exit_pos)
    print(exit_pos_list)
    
main()
