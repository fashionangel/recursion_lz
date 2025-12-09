#функции перестановок
def permutations(elements):         
    res = []                     
    if len(elements) == 0:              #(базовый случай) если длинна списка 0, то выводим пустой список
        return [[]]
    else:
        for i in range(len(elements)):         
            #для эл списка
            taken = elements[i]   
            #далее удаляем эл i   
            remaining = elements[:i] + elements[i+1:]        
            #разбивочка на случаи
            for j in permutations(remaining):       
                 #в списке итоговой перестановки записыаем взятый элемент(taken) к случаям
                res.append([taken] + j)             
        
        return res          
    


def main():    
    #список
    s = (input("Введите Ваши элементы : ")).split()        
    print("Вот Ваши все перестановки : \n")
    #вызов функций
    for b in permutations(s):          
        print(b)

if __name__ == '__main__':  
    main()