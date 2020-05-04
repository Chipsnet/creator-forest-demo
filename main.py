import random

print('やぁ！じゃんけんへようこそ！\n1, 2, 3の中から好きな手を選んでね！')
num = input('(1=グー, 2=チョキ, 3=パー) >> ')

print('あなたが選んだ手は: {}'.format(num))

try:
    num = int(num)
except:
    print("入力が間違っているよ！")
    exit()

com_num = random.randint(1, 3)

print('コンピュータが選んだ手は: {}'.format(com_num))

if num == 1:
    if com_num == 1:
        print("あいこ！")
    if com_num == 2:
        print("あなたの勝ち！")
    if com_num == 3:
        print("あなたの負け！")
elif num == 2:
    if com_num == 1:
        print("あなたの負け！")
    if com_num == 2:
        print("あいこ！")
    if com_num == 3:
        print("あなたの勝ち！")
elif num == 3:
    if com_num == 1:
        print("あなたの勝ち！")
    if com_num == 2:
        print("あなたの負け！")
    if com_num == 3:
        print("あいこ！")
else:
    print("入力が間違っているよ！")