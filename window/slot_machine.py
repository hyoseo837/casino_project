import random
import os

slots = ["🍋", "🥝", "🍓", "🍇", "🍏", "🍒", "👑"]

def slot_machine(money):
    coin = money
    playing = True
    while playing:
        os.system("cls")
        result = [None,None,None]

        print(coin)
        print("돌리기 (10 G)")
        if coin < 10:
            print("돈이 부족합니다")
            playing = False
            break
        coin -= 10

        for k in range(3):
            input()
            os.system("cls")
            result[k] = random.choice(slots)
            for i in result:
                if i != None:
                    print(i,end=" ")

        print()

        if result[0] == result[1] and result[1] == result[2]:
            if result[0] == slots[0]:
                print("200 G")
                coin += 200
            elif result[0] == slots[1]:
                print("300 G")
                coin += 300
            elif result[0] == slots[2]:
                print("500 G")
                coin += 500
            elif result[0] == slots[3]:
                print("1000 G")
                coin += 1000
            elif result[0] == slots[4]:
                print("2000 G")
                coin += 2000
            elif result[0] == slots[5]:
                print("3000 G")
                coin += 3000
            elif result[0] == slots[6]:
                print("5000 G")
                coin += 5000
        
        if slots[5] in result:
            if result.count(slots[5]) == 1:
                print("10 G")
                coin += 10
            elif result.count(slots[5]) == 2:
                print("20 G")
                coin += 20
        print()
        if input("q 를 눌러 나가기 : ") == "q":
            break
    return coin