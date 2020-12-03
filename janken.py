import random
h_list = ["グー","チョキ","パー"]
wins = False
w_com = "あなたの勝ちです"
l_com = "あなたの負けです"
t_com = "あいこです"
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
def result(a,b):
    print("ジャンケンポイ")
    print("あなた　コンピューター")
    print("{0} {1}".format(a.hand,b.hand))

def result_tie(a,b):
    print("あいこでしょ")
    print("あなた　コンピューター")
    print("{0} {1}".format(a.hand,b.hand))

def game():
    h1= Your_Hand()
    h2 = Cp_Hand()
    if h1.n == h2.n:
        result(h1,h2)
        print(t_com)
    elif((h1.n == 0)and(h2.n ==1))or((h1.n == 1)and(h2.n ==2))or((h1.n == 2)and(h2.n ==0)):
        result(h1,h2)
        print(w_com)
        wins = True
    else:
        result(h1,h2)
        print(l_com)
        wins = True

def game_tie():
    h1= Your_Hand()
    h2 = Cp_Hand()
    if h1.n == h2.n:
        result_tie(h1,h2)
        print(t_com)
    elif((h1.n == 0)and(h2.n ==1))or((h1.n == 1)and(h2.n ==2))or((h1.n == 2)and(h2.n ==0)):
        result_tie(h1,h2)
        wins = True
        print(w_com)
    else:
        result_tie(h1,h2)
        print(l_com)
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

