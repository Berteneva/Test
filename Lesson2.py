def lesson2(x): 
    x=int(x)
    if x==1: 
        def age(age):
            print(age)
        age("Десять")
    elif x==2: 
        def variable(x):
            x=x+1
            print(x)
        variable(5)
    elif x==3: 
        array = [1, 89.5, 3, "привет"]
        print(array[1])
        print( array[-1] )
        print( len(array) )
    elif x==4:
        full_names = [['Миша', 'Иванов'], ['Саша', 'Петров']]
        print(full_names[1][0])
    elif x==5:
        person = {'name': 'Guido', 'age': 62, 'job': 'programmer'}
        print( person['name'] )
    elif x==6:
        a = 1 
        while a <= 5:
            print("Круг цикла номер: "+ str(a))
            print("Квадрат числа равен: "+ str(a*a)) 
            a = a + 1
    elif x==7:
        studies = ['Ilya', 'Ivan', 'Arseny', 'Aleksei', 'Dmitriy']
        for s in studies:
            print('Добро пожаловать на курс, ' + s)
print ("Введите номер операции:")
c = input () 
lesson2(c)