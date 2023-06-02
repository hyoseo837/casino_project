import random, os, time

def bigwheel(money):
    os.system('clear')
    print("색,숫자| 배팅금액x10\n숫자   | 배팅금액x5\n색     | 배팅금액x1.5")
    input()
    while True:
        if money <= 0:
            os.system('clear')
            print("꺼져")
            input()
            break

        color = [1,2]
        num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

        os.system('clear')
        while True:
            try:
                bet = int(input(f"현재금액 {money}G\n베팅금액 "))
                if bet > 0 and bet <= money:
                    break
                else:
                    print("\n적당한 금액을 투입하여 주십시오")
                    input()
                    os.system('clear')
            except:
                os.system('clear')

        money -= bet
        while True:
            try:
                color_choice = int(input("\n어떤 색을 고르시겠습니까? \n1.레드 2.블루: "))
                if color_choice in color:
                    break
            except:
                continue

        while True:
            try:
                num_choice = int(input("어떤 숫자를 고르시겠습니까? \n1-20: "))
                if num_choice in num:
                    break
            except:
                continue

        x = 0
        for i in range(35):
            sel_color = random.choice(color)
            sel_num = random.choice(num)
            x += 0.005
            if sel_color == 1:
                time.sleep(x)
                os.system('clear')
                print(f"\033[0;37;41m {sel_num} \033[0m")
            elif sel_color == 2:
                time.sleep(x)
                os.system('clear')
                print(f"\033[0;37;44m {sel_num} \033[0m")

        if sel_color == 1:
            os.system('clear')
            print(f"\033[0;37;41m {sel_num} \033[0m")
        elif sel_color == 2:
            os.system('clear')
            print(f"\033[0;37;44m {sel_num} \033[0m")
        input()

        if color_choice == 1:
            print(f"\n내 패: \033[0;37;41m {num_choice} \033[0m")
        elif color_choice == 2:
            print(f"\n내 패: \033[0;37;44m {num_choice} \033[0m")

        if color_choice == sel_color and num_choice == sel_num:
            money += bet*10
            print("\n베팅금액X10")
        elif color_choice == sel_color:
            money += bet*1.5
            print("\n베팅금액X1.5")
        elif num_choice == sel_num:
            money += bet*5
            print("\n베팅금액X5")

        a = input("\033[1;30mq를 눌러 나가기\033[0m")
        if a == "q":
            break
            
    return money