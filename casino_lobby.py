import os, random
from flip_coin import coin_side
from blackjack import blackjack
from slot_machine import slot_machine
from horse_race import horse
from sutda import sutda
from earn import earn_money
from bigwheel import bigwheel

loc = os.path.dirname(__file__)

def load():
    # f = open("money.txt", "w")
    # f.close()
    f = open(f"{loc}/money.txt","r")
    log = f.readlines()
    f.close()
    for i in log:
        log[log.index(i)] = i[:-1].split(":")
    return log

def save(log):
    ids = []
    datas = []
    for i in log:
        ids.append(i[0])
        datas.append(i[1])
    f = open(f"{loc}/money.txt","w")
    for i in range(len(log)):
        f.write(f"{ids[i]}:{datas[i]}\n")
    f.close()

if True: # 로그인 매커니즘
    money = None
    user_data = load()
    os.system('clear')
    id = input("아이디를 입력해주세요 : ")
    for i in user_data:
        if i[0] == id:
            money = int(i[1])
            break
    if money == None:
        money = 500
        print("새 회원 500원이 지급됩니다. ")
        input()
        user_data.append([id,money])


while True: # 실행
    os.system('clear')
    print("\033[0;33m="*50, "Welcome to Casino", "="*35,"\033[0m","\033[1;36m",str(money).rjust(10),str("G").rjust(1),"\033[0m")
    print("0. 동냥", "1. 블랙잭", "2. 슬롯머신", "3. 동전뒤집기", "4. 경마","5. 섯다(NEW!)","6.빅휠(NEW!)")
    print("\n\n\n\033[1;30m도박은 정신건강에 해롭습니다. 도박중독 상담센터 국번없이 '1336'                                         q를 눌러 나가기", "\033[0m", "\033[0;33m")
    print("="*119,"\033[0m")
    choice = input(f"{id}님, 선택하십시오: ")
    if choice == "0":
        money = earn_money(money)
    if choice == "1":
        money = blackjack(money)
    elif choice == "2":
        money = slot_machine(money)
    elif choice == "3":
        money = coin_side(money)
    elif choice == "4":
        money = horse(money)
    elif choice == "5":
        money = sutda(money)
    elif choice == "6":
        money = bigwheel(money)
    elif choice == "q":
        money = round(money)
        save(user_data)
        os.system('clear')
        if money == 0:
            print("뭐야 이 그지새끼는")
            break
        else:
            print(f"이용해주셔서 감사합니다 {id}님, 다음에 또 오십시오.")
            break

    money = round(money)
    for i in user_data:
        if i[0] == id:
            i[1] = money

    save(user_data)
    