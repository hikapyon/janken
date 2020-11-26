import random
h_list = ["グー","チョキ","パー"]
your_n = int(input("グーは0,チョキは1,パーは2を入力してください"))
your_hand = h_list[your_n]
cp_n = random.randint(0,2)
cp_hand = h_list[cp_n]
print(your_hand)
print(cp_hand)


        

if your_n == cp_n:
    print("あなた コンピューター")
    print("{} {}".format(your_hand,cp_hand))
    print("あいこです")
elif((your_n == 0)and(cp_n ==1))or((your_n == 1)and(cp_n ==2))or((your_n == 2)and(cp_n ==0)):
    print("あなた コンピューター")
    print("{} {}".format(your_hand,cp_hand))
    print("あなたの勝ちです")
else:
    print("あなた コンピューター")
    print("{} {}".format(your_hand,cp_hand))
    print("あなたの負けです")


    
