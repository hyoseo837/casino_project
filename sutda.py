import random, deck_maker, os

def jokbo(hand):
    card1 = hand[0]
    card2 = hand[1]
    if {card1,card2} == {"3특","8특"}:
        return 9999
    elif {card1,card2} == {"3특","1특"} or {card1,card2} == {"8특","1특"}:
        return 1999
    elif card1[0] == card2[0]:
        return 100 * int(card1[0]) + 100
    elif {card1[0],card2[0]} == {"1","2"}:
        return 90
    elif {card1[0],card2[0]} == {"1","4"}:
        return 80
    elif {card1[0],card2[0]} == {"1","9"}:
        return 70
    elif {card1[0],card2[0]} == {"1","0"}:
        return 60
    elif {card1[0],card2[0]} == {"4","0"}:
        return 50
    elif {card1[0],card2[0]} == {"4","6"}:
        return 40
    elif {card1[0],card2[0]} == {"3","7"}:
        return -1
    else:
        return (int(card1[0]) + int(card2[0]))%10 +1

def get_jb(hand):
    if jokbo(hand) == 9999:
        jb = "38광떙"
    elif jokbo(hand) == 1999:
        jb = "광땡"
    elif jokbo(hand)%100 == 0:
        jb = f"{hand[0][0]}땡"
    elif jokbo(hand) == 90:
        jb = "알리"
    elif jokbo(hand) == 80:
        jb = "독사"
    elif jokbo(hand) == 70:
        jb = "구삥"
    elif jokbo(hand) == 60:
        jb = "장삥"
    elif jokbo(hand) == 50:
        jb = "장사"
    elif jokbo(hand) == 40:
        jb = "세륙"
    elif jokbo(hand) == -1:
        jb = "땡잡이"
    else:
        jb = f"{jokbo(hand)-1}끝"
    return jb


def sutda(money):
    coin = money
    bet = 0
    while True:
        if input("플레이 하시겠습니까?\n") == "q":
            break
        os.system("clear")
        deck = deck_maker.half_H()
        random.shuffle(deck)
        player_hand = []
        dealer_hand = []
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())

        print()
        for i in player_hand:
            print(i,end="  ")
        print("  " + get_jb(player_hand))
        
        print(f"\n{coin}G\n")
        while True:
            morebet = input("배팅해주세요 : ")
            try:
                morebet = int(morebet)
            except:
                continue
            if morebet <= coin and morebet >= 0:
                coin -= morebet
                bet += morebet
                break

        player_point = jokbo(player_hand)
        dealer_point = jokbo(dealer_hand)

        os.system("clear")
        print()
        for i in dealer_hand:
            print(i,end="  ")
        print("   "+get_jb(dealer_hand))
        print()
        print(bet)
        print()
        for i in player_hand:
            print(i,end="  ")
        print("   "+get_jb(player_hand))
        print()

        if player_point%100 == 0 and dealer_point == -1:
            winner = "dealer"
        elif dealer_point%100 == 0 and player_point == -1:
            winner = "player"
        else:
            if player_point > dealer_point:
                winner = "player"
            elif player_point < dealer_point:
                winner = "dealer"
            else:
                winner = "tie"

        if winner == "tie":
            if input("1. 스톱!  2. 고! : ") == "1":
                coin += bet
                bet = 0
        elif winner == "player":
            coin += bet * 1.5
            bet = 0
            print("승리")
        else:
            bet = 0
            print("패배")
            
        if input() == "q":
            break
        os.system("clear")
    return coin

