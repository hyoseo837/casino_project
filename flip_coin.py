import os,random

def coin_side(money):

    coin = money

    sides = ["앞", "뒤"]

    while True:
        if coin <= 0:
            os.system('clear')
            print("꺼져")
            input()
            break

        os.system('clear')
        print("현재 잔고", coin)
        while True:
            try:
                input_coin = float(input("코인투입: "))
                break
            except:
                pass
        if input_coin <= coin:
        
            print("\n1. 앞면")
            print("2. 뒷면")

            while True:
                choice = input("\n당신의 선택: ")
                if choice in ["1","2"]:
                    choice = int(choice)
                    break
            
            result = random.choice(sides)

            print(" ")
            print(result)
            if choice < 3 and choice > 0:
                if result == "앞" and choice == 1:
                    print("당신의 승리!")
                    coin += input_coin
                elif result== "뒤" and choice == 2:
                    print("당신의 승리!")
                    coin += input_coin
                # if choice not int:
                #     print("다시 시도하세요")
                #     continue

                else:
                    print("당신의 패배")
                    coin -= input_coin
            
            print("\n1. 계속", "2. 그만")
            while True:
                exit_choice = input()
                if exit_choice in ["1","2"]:
                    exit_choice = int(exit_choice)
                    break

            if exit_choice == 2:
                break

        else:
            continue
    return coin