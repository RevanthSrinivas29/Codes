import  random as r
def Player_game():
    p_score=0
    while True:
            c=r.randint(1,10)
            p=int(input())
            if p<=0 or p>10:
                print('please enter valid numbers')
                pass
            else:
                if c==p:
                    print(f'player:{p} Compter:{c}\nPlayer total Score:{p_score}')
                    break
                else:
                    print(f'Computer ball:{c}')
                    p_score+=p
                    print(f"Player Current Score:{p_score}")
    return p_score

def Computer_game():
    c_score=0
    while True:
        c=r.randint(1,10)
        p=int(input())
        if p<=0 or p>10:
            print('please enter valid numbers')
            pass
        else:
            if c==p:
                print(f'player:{p} Compter:{c}\nComputer total Score:{c_score}')
                break
            else:
                print(f'Computer ball:{c}')
                c_score+=c
                print(f"Computer Current Score:{c_score}")
 
    return c_score
def StartGame(ch):
    if ch=='batting':
        print(f'start {ch}\n')
        p_score=Player_game()
        print(f'start bowling\n')
        c_score=Computer_game()
    else:
        print(f'start {ch}\n')
        c_score=Computer_game()
        print(f'start batting\n')
        p_score=Player_game()
    return c_score,p_score

def Choose_BB(com_in,player_in,com_ch):
    print(f'Computer:{com_in} Player:{player_in}')
    if (com_in+player_in)%2==0:
        if com_ch=='even':
            comp_choose=r.choice(['bat','ball'])
            print(f" {(com_in+player_in)} ->even .Computer wins\nComputer choose to {comp_choose}")
            c_sc,pl_sc=StartGame('batting' if comp_choose=='ball' else 'bowling')
        else:
            print(f'{(com_in+player_in)} ->Even . Player wins')
            player_choose=input("Choose Batting or bowling\t").lower()
            c_sc,pl_sc=StartGame(player_choose)
    else:
        if com_ch=='odd':
            comp_choose=r.choice(['bat','ball'])
            print(f"{com_in+player_in} ->Odd .Computer wins\nComputer choose to {comp_choose}")
            c_sc,pl_sc=StartGame('batting' if comp_choose=='ball' else 'bowling')
        else:
            print(f'{com_in+player_in} ->Odd . Player wins')
            player_choose=input("Choose batting or bowling\t").lower()
            c_sc,pl_sc=StartGame(player_choose)
    return 'Computer wins' if c_sc>pl_sc else 'Player Wins'

if __name__=='__main__':
    while True:
        print('******HandCricket__Game*******Only numbers from 1 to 10')
        L=['odd','even']
        player_ch=input("odd or even: ").lower()
        L.remove(player_ch)
        com_ch=r.choice(L)
        print(f'Computer:{com_ch}       Player:{player_ch}')
        player_in=int(input("Enter number "))
        if player_in<0 or player_in>10:
            print("Only numbers from 1 to 10\n\n")
            pass
        com_in=r.randint(1,10)
        Winner=Choose_BB(com_in,player_in,com_ch)
        print(f'**********{Winner}***********')
        if input("Do you want to continue?(y/n):").lower()=='n':
            break