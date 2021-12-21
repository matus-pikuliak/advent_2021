from functools import cache


@cache
def win(player, pos1, pos2, score1, score2, turn):
    if score1 >= 21: return not player
    if score2 >= 21: return player
    if turn < 3:
        return sum(
            win(player, p := (pos1 + dice) % 10, pos2, score1 + (p + 1) * (turn % 3 == 2), score2, (turn + 1) % 6)
            for dice in range(1, 4)
        )
    else:
        return sum(
            win(player, pos1, p := (pos2 + dice) % 10, score1, score2 + (p + 1) * (turn % 3 == 2), (turn + 1) % 6)
            for dice in range(1, 4)
        )


print(max(
    win(0, 6, 9, 0, 0, 0),
    win(1, 6, 9, 0, 0, 0)
))
