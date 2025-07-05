#Explicit Type Conversion-ს მაგალითები
x = 10
x = float(x)  # გადავიყვანოთ intenger-ი float-ში
print(type(x))  # გამოიყვანს: <class 'float'>
y = 21
y = str(y)  # გადავიყვანოთ intenger-ი string-ში
print(type(y))  # გამოიყვანს: <class 'str'>
a = 4.0
a = int(a)  # გადავიყვანოთ float-ი intenger-ში
print(type(a))  # გამოიყვანს: <class 'int'>
b = 3.14
b = str(b)  # გადავიყვანოთ float-ი string-ში
print(type(b))  # გამოიყვანს: <class 'str'>
c = "123"
c = int(c)  # გადავიყვანოთ string-ი intenger-ში
print(type(c))  # გამოიყვანს: <class 'int'>

#Implicit Type Conversion-ს მაგალითები
intenger1 = 10
intenger1 = intenger1 / 3  # intenger-ი float-ში გადაიქცევა
intenger2 = 20
intenger2 = intenger2 / 3  # intenger-ი float-ში გადაიქცევა
intenger3 = 30
intenger3 = intenger3 / 4  # intenger-ი float-ში გადაიქცევა
intenger4 = 40
intenger4 = intenger4 / 9  # intenger-ი float-ში გადაიქცევა
intenger5 = 50
intenger5 = intenger5 / 8  # intenger-ი float-ში გადაიქცევა