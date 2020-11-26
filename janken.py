import random
h_list = ["グー","チョキ","パー"]
class Your_Hand:
    def __init__(self):
        n = int(input("グーは0,チョキは1,パーは2を入力してください"))
        self.n = n
        self.hand = h_list[self.n]
class Cp_Hand:
    def __init__(self):
        n = random.randint(0,2)
        self.n = n
        self.hand = h_list[self.n]

your_hand = Your_Hand()
cp_hand = Cp_Hand()
def game(h1,h2):
    print("ジャンケンポイ")
    if h1.n == h2.n:
        print("あなた　コンピューター")
        print("{0} {1}".format(h1.hand,h2.hand))
        print("あいこです")
    elif((h1.n == 0)and(h2.n ==1))or((h1.n == 1)and(h2.n ==2))or((h1.n == 2)and(h2.n ==0)):
        print("あなた　コンピューター")
        print("{0} {1}".format(h1.hand,h2.hand))
        print("あなたの勝ちです")
    else:
        print("あなた　コンピューター")
        print("{0} {1}".format(h1.hand,h2.hand))
        print("あなたの負けです")

game(your_hand,cp_hand)

