def max_dragon_power(N):

    if N <= 7:
        return N
    
    count_3 = N // 3
    remainder = N % 3
    
    if remainder == 0:
        return 3 ** count_3
    
    elif remainder == 1:
        return (3 ** (count_3 - 1)) * (2 * 2)
    
    else:  
        return (3 ** count_3) * 2


def main():
    
    while True:
        try:
            N = int(input("\nВведите общее количество голов N (от 1 до 99 включительно): "))
            
            if N < 1 or N >= 100:
                print("Ошибка: N должно быть в диапазоне 1-99.")
                continue
            
            break
            
        except ValueError:
            print("Ошибка: введите целое число.")
    
    result = max_dragon_power(N)
    
    print(f"Количество голов: {N}")
    print(f"Максимальная сила стаи: {result}")
    

if __name__ == "__main__":
    main()