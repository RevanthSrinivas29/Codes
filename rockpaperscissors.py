from random import choice
game={"rock":"scissors","scissors":"paper","paper":"rock"}
while True:
    player=input('Enter your choice:').lower()
    if player not in game.keys():
        break
    computer=choice(list(game.keys()))
    if player==computer:
        print('Draw')
    else:
        print('You win' if game[player]==computer else 'Computer win')
    print(f'Player:{player}  Computer:{computer}')

print('|')