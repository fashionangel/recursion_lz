def per(n, g=1, s=0):
    if n<=0:
        return False
    if g == n:
        if n == s:
            print("совершенное число")
            return True
        else:
            print("не совершенное число")
            return False
    if n % g == 0:
        return per(n, g+1, s+g) 
    return per(n, g+1, s)      
        


def main():    #общий запуск функций
    n = int(input("Введите Ваше число для проверки на совершенное : "))         #вводим элемент на проверку
    per(n)                #выводим функцию

    
if __name__ == '__main__':  #инструкция для запуска, для импорта в другие файлы
    main()