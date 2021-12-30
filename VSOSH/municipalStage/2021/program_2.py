def get_cells(game_grid):
    a = []
    for x in range(3):
        for y in range(3):
            if game_grid[x][y] == '':
                a.append([x, y])

    return a


def result_move(game_grid):
    if (game_grid[0][0] == game_grid[0][1] == game_grid[0][2] == 'PETYA' or
            game_grid[1][0] == game_grid[1][1] == game_grid[1][2] == 'PETYA' or
            game_grid[2][0] == game_grid[2][1] == game_grid[2][2] == 'PETYA' or
            game_grid[0][0] == game_grid[1][0] == game_grid[2][0] == 'PETYA' or
            game_grid[0][1] == game_grid[1][1] == game_grid[2][1] == 'PETYA' or
            game_grid[0][2] == game_grid[1][2] == game_grid[2][2] == 'PETYA' or
            game_grid[0][0] == game_grid[1][1] == game_grid[2][2] == 'PETYA' or
            game_grid[0][2] == game_grid[1][1] == game_grid[2][0] == 'PETYA'):
        return 'PETYA'

    elif (game_grid[0][0] == game_grid[0][1] == game_grid[0][2] == 'VANYA' or
          game_grid[1][0] == game_grid[1][1] == game_grid[1][2] == 'VANYA' or
          game_grid[2][0] == game_grid[2][1] == game_grid[2][2] == 'VANYA' or
          game_grid[0][0] == game_grid[1][0] == game_grid[2][0] == 'VANYA' or
          game_grid[0][1] == game_grid[1][1] == game_grid[2][1] == 'VANYA' or
          game_grid[0][2] == game_grid[1][2] == game_grid[2][2] == 'VANYA' or
          game_grid[0][0] == game_grid[1][1] == game_grid[2][2] == 'VANYA' or
          game_grid[0][2] == game_grid[1][1] == game_grid[2][0] == 'VANYA'):
        return 'VANYA'

    elif not len(game_grid):
        return 'UNKNOWN'

    else:
        return 'game'


def game_cycle(game_grid, player, coords_move):
    game_grid[coords_move[0]][coords_move[1]] = player
    result_game = (result_move(game_grid), coords_move)
    if result_game[0] == 'game':
        for cell in get_cells(game_grid):
            tmp = game_cycle(game_grid, 'VANYA' if player == 'PETYA' else 'PETYA', cell)
            if tmp[0] == 'PETYA':
                result_game = tmp
            elif result_game[0] != 'PETYA' and tmp[0] == 'UNKNOWN':
                result_game = tmp

    # print(game_grid, result_game)

    return result_game


n = int(input())
game_grid = [['' for i in range(3)] for j in range(3)]
for i in range(n):
    x, y = map(int, input().split())
    player = 'VANYA' if (n % 2 + i) % 2 else 'PETYA'
    game_grid[x - 1][y - 1] = player

print(game_grid)
print(game_cycle(game_grid, player, [x-1, y-1]))
