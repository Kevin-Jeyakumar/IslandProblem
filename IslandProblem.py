def islandCount(mat):
    for row in mat:
        print(row)
    count = 0
    left_border, right_border , top_border, bottom_border = -1, len(mat[0]), -1, len(mat)
    landSeen = set()
    def traverseLand(y,x):
        # print(f"Islands: {count}, Traversing {y}, {x}, seen: {landSeen}")
        if y > top_border and y < bottom_border and x > left_border and x < right_border and mat[y][x] == 1 and (y,x) not in landSeen:
            landSeen.add((y, x))
            traverseLand(y, x - 1)
            traverseLand(y, x + 1)
            traverseLand(y + 1, x)
            traverseLand(y - 1, x)

    for i in range(0, len(mat)):
        for j in range(0, len(mat[0])):
            if mat[i][j] == 1 and (i, j) not in landSeen:
                count += 1
                traverseLand(i, j)
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
    print(islandCount([
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0]]))