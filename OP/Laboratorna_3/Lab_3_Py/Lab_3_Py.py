x=float(input("Введіть число x:\n")) #Вводимо задане число
s=x/2 #Оголошуємо змінну суми, у якій уже присутній перший елемент a1=((x**1)/(2*1)!)=x/2
a=x/2 #Оголошуємо змінну елемента послідовности, яка спершу дорівнює першому члену
k=1 #Оголошуємо змінну для рахунку елементів послідовности
while (abs(a)>=10**(-5) or k<=10): #Цикл, що виконуватиметься, допоки задані в задачі умови не будуть досягнуті
    k+=1 #Додаємо одиницю для лічильника
    fac=1 #Змінна для вирахунку факторіалу числа
    for i in range(1,2*k+1): #Шукаємо (2k)!
       fac*=i
    a=(x**k)/fac #Рахуємо елементи послідовности
    s+=a #Додаємо вирахувані елементи до суми
print("Сума елементів послідовности =",s,"при k =",k)
