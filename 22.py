import random

def double_coin(): 
    capital = int(input('Сколько монет на старте? '))
    current_bet = 1  
    steps = 0

    while capital > 0:
        if current_bet > capital:
            print(f"Крах на {steps + 1} ходу. Следующая ставка {current_bet} больше, чем оставшийся капитал {capital}.")
            break

        steps += 1
        win = random.choice([True, False])

        if win:
            capital += current_bet  
            current_bet = 1  
        else:
            capital -= current_bet  
            current_bet *= 2  # Удвоение при проигрыше

    print(f"Игра окончена. Всего сделано ходов: {steps}. Финальный капитал: {capital}")

double_coin()

double_coin()