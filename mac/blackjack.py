import random
import os
from deck_maker import *

mystary = "🂠  "
bet = 0
player_hand = []
dealer_hand = []


def prt_hand(hand):
    message = ""
    for i in hand:
        message += i+"  "
    return message
    

def total(hand):
    total_score = 0
    have_A = False
    for i in hand:
        if i[1] in ["J","Q","K"]:
            total_score += 10
        elif i[1] == "A":
            total_score += 11
            have_A = True
        else:
            total_score += int(i[1:])
    if have_A and total_score > 21:
        total_score -= 10
        have_A = False
    return total_score

def table(d_hand,p_hand,coin,bet):
    os.system("clear")
    mys = mystary * (len(dealer_hand)-1)
    print(f"""
    {d_hand[0]}  {mys}
    _________________________

    {bet:^25}
    _________________________

    {prt_hand(p_hand)}
    {total(p_hand):>25}
    
    money : {coin}

    """)


def blackjack(money):

    coin = money
    bet = 0
    nomore = True
    winner = ""

    while True:
        nomore = False
        winner = ""
        first = True

        deck = no_jocker()
        random.shuffle(deck)

        player_hand = []
        dealer_hand = []

        os.system("clear")
        print(round(coin))

        while True:
            try:
                morebet = int(input("배팅 해주십시오 : "))
            except:
                morebet = -1
            if morebet >= 0 and morebet <= coin:
                bet += morebet
                coin -= morebet
                break
            print("error: 잘못된 값을 입력하셨습니다. ")

        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())

        while True:
            table(dealer_hand, player_hand, coin, bet)
            print()

            if first and total(player_hand)==21:
                print("\n블랙잭!!\n")
                coin += bet * 0.2
                winner = "you"
                break

            if nomore and done:
                break

            if total(player_hand) > 21:
                print("\n버스트 되셨습니다! \n")
                winner = "dealer"
                break
            if total(dealer_hand) > 21:
                print("\n딜러가 버스트 되었습니다!\n")
                winner = "you"
                break
            
            if total(dealer_hand) < 17:
                dealer_hand.append(deck.pop())
                done = False
            else:
                done = True

            if not nomore:

                if input("1.더 받기 2.멈추기 : ") == "1":
                    player_hand.append(deck.pop())
                else:
                    nomore = True
            first = False

        if winner == "":
            if 21-total(player_hand) < 21-total(dealer_hand):
                winner = "you"
            elif 21-total(player_hand) > 21-total(dealer_hand):
                winner = "dealer"
            else:
                coin += bet
                winner = "tie"

        if winner == "you":
            coin += bet*1.5
        bet = 0

        print(f"당신 : {total(player_hand)}")
        print(f"딜러 : {total(dealer_hand)}")

        if winner != "tie":
            print(f"{winner} 승리!!")
        else:
            print("비겼습니다. ")
        if input("q 를 눌러 나가기\n") == "q":
            break
        if coin <= 0:
            print("돈이 부족합니다 다음에 다시 찾아주세요^^ ")
            input()
            break
    return coin
