import random

def pc_move(N):
    if ((N - 1) - 1) % 4 == 0:
        p = 1
    elif ((N - 1) - 2) % 4 == 0:
        p = 2
    elif ((N - 1) - 3) % 4 == 0:
        p = 3
    else:
        p = random.randint(1, 3)
    print("Ход компьютера:", p)
    return p

def ney_nya_en(N):
    if (N < 10) or (N > 20):
        if N % 10==1:
            return "ень"
        elif N % 10 == 2 or N % 10 == 3:
            return "ня"
        else:
            return "ней"
    else:
        return "ней"

N = random.randint(4,30)
is_pc_turn = False

while N > 1:
    print("В куче", N, "кам"+ney_nya_en(N))
    if is_pc_turn:
        N = N - pc_move(N)
        is_pc_turn = False
    else:
        try:
            a = int(input("Ход игрока: "))
            if (a != 1) and (a != 2) and (a != 3) or ((N - a) < 1):
                print("Ввод некорректен, попробуйте снова.")
            else:
                N = N - a
                is_pc_turn = True
        except:
            print("Ввод некорректен, попробуйте снова.")
print("В куче", N, "кам"+ney_nya_en(N))
if is_pc_turn:
    print("Победил игрок!")
else:
    print("Победил компьютер!!!")
#qwerty
#computer

