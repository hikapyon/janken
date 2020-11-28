import random
h_list = ["グー","チョキ","パー"]
wins = False
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

def game():
    h1= Your_Hand()
    h2 = Cp_Hand()
    if h1.n == h2.n:
        print("ジャンケンポイ")
        print("あなた　コンピューター")
        print("{0} {1}".format(h1.hand,h2.hand))
        print("あいこです")
    elif((h1.n == 0)and(h2.n ==1))or((h1.n == 1)and(h2.n ==2))or((h1.n == 2)and(h2.n ==0)):
        print("ジャンケンポイ")
        print("あなた　コンピューター")
        print("{0} {1}".format(h1.hand,h2.hand))
        print("あなたの勝ちです")
        wins = True
    else:
        print("ジャンケンポイ")
        print("あなた　コンピューター")
        print("{0} {1}".format(h1.hand,h2.hand))
        print("あなたの負けです")
        wins = True

def game_tie():
    h1= Your_Hand()
    h2 = Cp_Hand()
    if h1.n == h2.n:
        print("あいこでしょ")
        print("あなた　コンピューター")
        print("{0} {1}".format(h1.hand,h2.hand))
        print("あいこです")
    elif((h1.n == 0)and(h2.n ==1))or((h1.n == 1)and(h2.n ==2))or((h1.n == 2)and(h2.n ==0)):
        print("あいこでしょ")
        print("あなた　コンピューター")
        print("{0} {1}".format(h1.hand,h2.hand))
        print("あなたの勝ちです")
        wins = True
    else:
        print("ジャンケンポイ")
        print("あなた　コンピューター")
        print("{0} {1}".format(h1.hand,h2.hand))
        print("あなたの負けです")
        wins = True
while True:
    m = "qで終了、それ以外のキーでplay"
    response = input(m)
    if response == 'q':
        break
    try:
        game()
        while wins == False:
            game_tie()
    except IndexError:
        print('0,1,2以外が入力されました、0,1,2のみを入力してください')
        pass
    except ValueError:
        print('0,1,2以外が入力されました、0,1,2のみを入力してください')
        pass

