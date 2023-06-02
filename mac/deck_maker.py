# deck making
def single():
    deck = []
    for i in ["♠","♢","♡","☘"]:
        for j in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]:
            deck.append(f"{i}{j}")
    deck.append("jocker")
    deck.append("JOCKER")
    return deck

def no_jocker():
    deck = []
    for i in ["♠","♢","♡","☘"]:
        for j in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]:
            deck.append(f"{i}{j}")
    return deck


def double():
    deck = single() + single()
    return deck

def whole_H():
    deck = []
    for i in ["1","2","3","4","5","6","7","8","9","10","11"]:
        for j in range(2):
            deck.append(f"{i}피 ")
    for i in ["1","3","8","11","12"]:
        deck.append(f"{i}광 ")
    for i in ["9","11","12"]:
        deck.append(f"{i}쌍피")
    for i in ["1","2","3"]:
        deck.append(f"{i}홍단")
    for i in ["6","9","10"]:
        deck.append(f"{i}청단")
    for i in ["4","5","7"]:
        deck.append(f"{i}초단")
    for i in ["2","4","5","6","7","8","9","10","12"]:
        deck.append(f"{i}열끗")
    return deck

def half_H():
    deck = []
    for i in ["1","3","8"]:
        deck.append(f"{i}특")
    for i in ["9"]:
        deck.append(f"{i}특")
    for i in ["1","2","3"]:
        deck.append(f"{i}일")
    for i in ["6","9","0"]:
        deck.append(f"{i}일")
    for i in ["4","5","7"]:
        deck.append(f"{i}일")
    for i in ["2","4","5","6","7","0"]:
        deck.append(f"{i}특")
    deck.append("8일")
    return deck
