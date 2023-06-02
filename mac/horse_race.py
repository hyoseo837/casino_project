import os, random, time

def horse(money):
    if money > 1000:
        os.system('clear')
        print("우승  | 배팅금액x3\n준우승| 배팅금액x1.5\n\033[1;30m(동시에 들어온다면, 번호순으로 승리합니다)\033[0m")
        input()
    while True:
        if money < 1000:
            os.system('clear')
            print("꺼져")
            input()
            break

        horse_distance = [0,0,0,0,0,0,0]
        os.system('clear')
        print(f"현재자금 {money}G")
        while True:
            try:
                bet = int(input(f"베팅금액 "))
                if bet >= 1000 and bet <= money:
                    money -= bet
                    break
                else:
                    print("베팅 최소한도는 1000G 입니다.")
                    input("")
            except:
                pass
        while True:
            try:
                choice = int(input("\n베팅할 마번 (1-7): "))
                if choice >= 1 and choice <= 7:
                    break
            except:
                pass
        countdown = 3
        for i in range(3):
            os.system('clear')
            for i in range(len(horse_distance)):
                print(f"{i+1} |" + " "*horse_distance[i] + "🐴")
            print(f"\033[0;33;40m\n{countdown}\033[0m")
            time.sleep(1)
            countdown -= 1

        for i in range(800):
            os.system('clear')
            b = random.randrange(7)
            horse_distance[b] += 1

            for i in range(len(horse_distance)):
                print(f"{i+1} |" + " "*horse_distance[i] + "🐴")

            
        #순위
        print("")
        prise = []
        j = horse_distance.copy()
        for i in range(7):
            a = j.index(max(j))
            j.remove(max(j))
            j.insert(a, 0)
            prise.append(a)

        print(f"\033[1;37;40m베팅| {choice} 번마\033[0m\n")
        for i in range(7):
            winner = horse_distance.index(max(horse_distance))
            if i > 1:
                time.sleep(0.5)
                print(f"\033[1;30;40m{i+1}위|", prise[i]+1,"번마\033[0m")
            else:
                time.sleep(0.5)
                print(f"\033[1;33;40m{i+1}위|", prise[i]+1,"번마\033[0m")

        if choice == prise[0]+1:
            print("\n우승!!\n베팅금액 x3\n\033[1;30mq를 눌러 나가기\033[0m")
            money += bet*3
        elif choice == prise[1]+1:
            print("\n준우승!!\n베팅금액 x1.5\n\033[1;30mq를 눌러 나가기\033[0m")
            money += bet*1.5
        else:
            print("\n\033[1;30mq를 눌러 나가기\033[0m")
        end = input()
        if end == "q":
            break

    return money

