import os

def earn_money(money):
    os.system('clear')
    print("엔터를 눌러 돈벌기 시작! (q를 눌러 언제든 나가기)")
    while True:
        a= input("")
        os.system('clear')
        if a == "q":
            break
        else:
            money += 1
            print(money, "G")
            
    return money
