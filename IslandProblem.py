def islandCount(mat):
    count = 0
    land = set()
    for i in range(0, len(mat)):
        for j in range(0, len(mat[0])):
            if mat[i][j] == 1:
                land.add((i,j))
                if (i-1,j) not in land and (i,j-1) not in land:    
                    if i < len(mat)-1 and j < len(mat[0])-1 and mat[i+1][j] == 0 and mat[i][j+1] == 0:
                            count += 1
                    elif i < len(mat)-1 and mat[i+1][j] == 0:
                            count += 1
                    elif j < len(mat[0])-1 and mat[i][j+1] == 0:
                            count += 1
                    else:
                            count += 1
    return count

if __name__ == "__main__":
    print(islandCount([
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,1,0,0,0],
    [0,1,1,1,0],
    [0,0,0,0,0]]))
    # expected 1
    print(islandCount([
    [0,0,0,0,0],
    [0,0,1,0,0],
    [0,1,0,1,0],
    [0,0,1,0,0],
    [0,0,0,0,0]]))
    # expected 4
    print(islandCount([
    [1,0],
    [1,1],
    [1,0],
    [1,1],
    [1,0]]))
    # expected 1
