file_name="cards.txt"

def load_cards():
    cards={}
    try:
        f=open(file_name, "r")
        data=f.readlines()
        f.close()
    except:
        return cards
    for line in data:
        if line.strip()=="":
            continue
        p = line.strip().split("|")
        cards[p[0]]={
            "name":p[1],
            "pin":p[2],
            "limit":float(p[3]),
            "balance":float(p[4]),
            "blocked":p[5]=="1",
            "rewards":float(p[6]),
            "score":int(p[7])
        }
    return cards

def save_cards(cards):
    f = open(file_name, "w")
    for num, c in cards.items():
        t = num + "|" + c["name"] + "|" + c["pin"] + "|" + str(c["limit"])
        t += "|" + str(c["balance"]) + "|" + ("1" if c["blocked"] else "0")
        t += "|" + str(c["rewards"]) + "|" + str(c["score"]) + "\n"
        f.write(t)
    f.close()

def create_card(cards):
    num = input("Card number: ")
    if num in cards:
        print("Card already exists")
        return
    name = input("Name: ")
    pin = input("PIN: ")
    try:
        limit = float(input("Limit: "))
    except:
        print("Invalid")
        return
    cards[num] = {
        "name": name,
        "pin": pin,
        "limit": limit,
        "balance": 0.0,
        "blocked": False,
        "rewards": 0.0,
        "score": 750
    }
    save_cards(cards)
    print("Card created")

def purchase(card):
    if card["blocked"]:
        print("Card blocked")
        return
    try:
        amt = float(input("Purchase amount: "))
    except:
        print("Invalid")
        return
    if card["balance"] + amt > card["limit"]:
        print("Limit exceeded")
        card["score"] -= 5
    else:
        card["balance"] += amt
        card["rewards"] += amt * 0.02
        print("Purchase successful")

def payment(card):
    try:
        amt = float(input("Payment amount: "))
    except:
        print("Invalid")
        return
    if amt <= 0:
        print("Invalid")
        return
    card["balance"] -= amt
    if card["balance"] < 0:
        card["balance"] = 0
    card["score"] += 2
    print("Payment done")

def show_details(num, card):
    print("Card Number:", num)
    print("Name:", card["name"])
    print("Limit:", card["limit"])
    print("Balance:", card["balance"])
    print("Rewards:", card["rewards"])
    print("Score:", card["score"])
    print("Blocked:", "Yes" if card["blocked"] else "No")

def interest(card):
    i = card["balance"] * 0.03
    card["balance"] += i
    print("Interest added:", i)

def card_menu(num, card, cards):
    while True:
        print("\n1.Purchase\n2.Payment\n3.Details\n4.Block\n5.Unblock\n6.Interest\n7.Logout")
        c = input("Choose: ")
        if c == "1":
            purchase(card)
        elif c == "2":
            payment(card)
        elif c == "3":
            show_details(num, card)
        elif c == "4":
            card["blocked"] = True
            print("Card blocked")
        elif c == "5":
            card["blocked"] = False
            print("Card unblocked")
        elif c == "6":
            interest(card)
        elif c == "7":
            break
        else:
            print("Invalid")
        save_cards(cards)

def login(cards):
    num = input("Card number: ")
    if num not in cards:
        print("Not found")
        return
    pin=input("PIN: ")
    if cards[num]["pin"] != pin:
        print("Wrong PIN")
        return
    print("Welcome", cards[num]["name"])
    card_menu(num, cards[num], cards)

def main():
    cards= load_cards()
    while True:
        print("\n1.Create Card\n2.Login\n3.Exit")
        x=input("Choose: ")
        if x=="1":
            create_card(cards)
        elif x=="2":
            login(cards)
        elif x=="3":
            break
        else:
            print("Invalid")

main()
