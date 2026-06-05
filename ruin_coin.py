import random
def ruin_coin(): 
   print('Привет. Проверям теорию о том, что удвоение проигранного ведёт только к проигрышу.')
   coin_start = int(input('Сколько монет ты хочешь вложить на старте? '))
   
   steps=0

   while True:
    steps+=1
    x = random.randint(0, 1)
    if x ==1:
       coin_start+=1
    else:
        coin_start-=1

    if coin_start==0:
       print(f'Игра окончена. Ты всё потерял за {steps} попыток.')
       break
   
ruin_coin()