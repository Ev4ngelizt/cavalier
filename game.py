l = ["a", "b", "c", "d", "e", "f", "g", "h"]
def get_moves(x, y):
        moves = []
        if x < 6:
            if y < 7:
                moves.append((x+2, y+1))
            if y > 0:
                moves.append((x+2, y-1))
        if x > 1:
            if y < 7:
                moves.append((x-2, y+1))
            if y > 0:
                moves.append((x-2, y-1))
        if y < 6:
            if x < 7:
                moves.append((x+1, y+2))
            if x > 1:
                moves.append((x-1, y+2))
        if y > 1:
            if x < 7:
                moves.append((x+1, y-2))
            if x > 1:
                moves.append((x-1, y-2))
        return moves

def convert_coord(coord):
    x, y = coord[0], coord[1]
    print(x,y)
    return l[x]+str(y+1)

moves = get_moves(2,3)
new_moves = [convert_coord(move) for move in moves]
print(new_moves)