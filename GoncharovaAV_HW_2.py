a = [[' ', "0", "1", "2"], ["0", '-', '-', '-'], ["1", '-', '-', '-'], ["2", '-', '-', '-']]

def list_copy(a):
    # a_copy = a.copy() использование этой функции в ходе выполнения кода к сожалению меняет и изначальный список а
    a_copy = []
    for i in a:
        cp = []
        for j in i:
            cp.append(j)
        a_copy.append(cp)
    return a_copy

def field_for_game(a_copy): # печать поля игры
    for i in a_copy:
        print(" ".join(i))

def input_char(a_copy, k): # ввод позиции и update поля игры
    print()
    numbers = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
    z = input(f'Игрок {k}: ')

    if z in numbers:
        z_row = int(z[0])
        z_column = int(z[1])
        if a_copy[z_row+1][z_column+1] == '-': 
            a_copy[z_row+1][z_column+1] = k
        else:
            print()
            print(f'позиция {z} занята')
            print("Введите номер свободной позиции")
            input_char(a_copy, k)
    else:
        print(f'позиции {z} не существует')
        print("Введите номер свободной позиции")
        input_char(a_copy, k)
    
def check_wins(a_copy, k): # проверка на выигрыш
    rows = [[a_copy[1][1], a_copy[1][2], a_copy[1][3]], [a_copy[2][1], a_copy[2][2], a_copy[2][3]], [a_copy[3][1], a_copy[3][2], a_copy[3][3]]]
    columns = [[a_copy[1][1], a_copy[2][1], a_copy[3][1]], [a_copy[1][2], a_copy[2][2], a_copy[3][2]], [a_copy[1][3], a_copy[2][3], a_copy[3][3]]]
    diagonals = [[a_copy[1][1], a_copy[2][2], a_copy[3][3]], [a_copy[1][3], a_copy[2][2], a_copy[3][1]]]
    for i in rows:
        if all(j == k for j in i):
            return f'Игрок {k} ПОБЕДИЛ!!!!!'
            
    for i in columns:
        if all(j == k for j in i):
            return f'Игрок {k} ПОБЕДИЛ!!!!!'
        
    for i in diagonals:
        if all(j == k for j in i):
            return f'Игрок {k} ПОБЕДИЛ!!!!!'
        
def start_game(a_copy): 
    for i in range(1, 10, 1):           
        if i % 2 != 0:
            input_char(a_copy, 'X')
            field_for_game(a_copy)
            z = check_wins(a_copy, 'X')
            if z:
                print()
                print(z)
                print()
                want_start()
                break
        else:
            input_char(a_copy, 'O')
            field_for_game(a_copy)
            z = check_wins(a_copy, 'O')
            if z:
                print()
                print(z)
                print()
                want_start()
                break
        b = []
        for i in a_copy:
            for j in i:
                b.append(j)
        if all(el != "-" for el in b):
            print("НИЧЬЯ! ИГРА ОКОНЧЕНА")
            print()        
            want_start()
            
def want_start(): # начало игры, создание копии пустого поля игры        
    a_copy = list_copy(a)
    q = input("Сыграем? (да - y; нет - любой символ): ")
    if q == 'y':
        print("Начнем игру")
        print()
        print("Выбор позиции: вводите номер строки и столбца без пробела")
        print("Пример: 02")
        print()
        field_for_game(a_copy)
        print()
        start_game(a_copy)
    else:
        print("До встречи")
        

want_start()
