import random
choices = ["камень", "ножницы", "бумага"]
player_score = 0
computer_score = 0
print("Играем до 3 побед!\n")
while player_score < 3 and computer_score < 3:
    player = input("Ваш ход: ").lower().strip()
computer = random.choice(choices)
print(f"Компьютер выбрал: {computer}")
if player == computer:
    print("Ничья!")
elif (player == "камень" and computer == "ножницы") or \
     (player == "ножницы" and computer == "бумага") or \
     (player == "бумага" and computer == "камень"):
     print("Вы выиграли раунд!")
        player_score += 1
else:
        print("Компьютер выиграл раунд!")
        computer_score += 1
    print(f"Счёт: Вы {player_score} — {computer_score} Компьютер\n")
if player_score == 3:
        print("Вы победили!")
else:
    print("Компьютер победил хаха!")
