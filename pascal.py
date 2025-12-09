#функция треугольника Паскаля
def pascal_triangle(x):     
    #если количество рядов 1 то вывести [[1]]
    if x == 1:              
        return [[1]]
    #Если количество рядов 2, то вывести [[1], [1,1]]
    elif x == 2:                        
        return [[1], [1,1]]
    else:
        #переменная для треугольника без последнего ряда
        treug = pascal_triangle(x-1)            
        last_elem = treug[-1]     
        #берем за первый элемент в треугольнике единицу              
        first_elem = [1]                                
        for a in range(1, len(last_elem)):         
            #добавляем к единице сумму смежных элементов из верхнего ряда
            first_elem.append(last_elem[a-1] + last_elem[a])        
        first_elem.append(1)
        #возвращаем треугольник с новыми рядами
        return treug + [first_elem]     

def main():                
    rows = int(input("Введите количество рядов : "))       
    treug = pascal_triangle(rows) 
    #вывод
    for rows in treug:                  
        print(rows)

if __name__ == '__main__': 
    main()