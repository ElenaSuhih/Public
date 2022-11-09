Sum=int(0) # вводим переменную для общей суммы билетов
N=int(input('Print the number of tickets you need:')) # вводим счетчик билетов, запрашиваем количество
age=0 # вводим переменную для определения стоимости билета

i=1
while i<N+1: # заходим в цикл до указанного количества билетов
    try: # будем писать исключение по ошибке ввода возраста
        age=int(input(f'Print an age of the person for {i} ticket')) # запрашиваем возраст посетителя
        if 18<=age<=25: # указываем варианты возраста и рассчитываем стоимость каждого билета
            Sum+=990
            print(f'Price of {i} ticket 990 rub')
            i+=1

        elif 18<age<100:
            Sum+=1390
            print(f'Price of {i} ticket 1390 rub')
            i+=1
        elif age<18:
            print(f'Price of {i} ticket 0 rub')
            i+=1
        else:
            raise ValueError("Not a real age") # вызов ошибки при некорректном возрасте
            i+=1
    except ValueError as error:
        print(error)

if N>3: # по условиям - скидка при заказе более 3 билетов
    Sum=Sum/100*90 # считаем общую сумму со скидкой
    print(f'You have a sale 10%')

print(f'You have ask for {N} tickets. All your tickets cost {int(Sum)} rub') # выводим итоговую сумму

