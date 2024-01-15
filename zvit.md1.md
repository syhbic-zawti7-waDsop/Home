# Звіт до роботи
## Тема: Основи програмування на Python
### Мета роботи: навчитися працювати з основними конструкціями з Python
---
### Виконання роботи
-  Результати виконання завдання 1;
    1.Перша константа False
    2.Друга константа True
    3.Третя константа True
-  Результаи завдань з 2 по останнє по черзі;

   *2)12.5 є рівним 12.5  

    <class '__main__.X'>
 
    3)0 
    1 
    2 
    3 
    4 
    5 

    *4)Сергій 
    Ребко 
    18 
    Студент який не знає куда себе подіти в житі і чим заробляти 
  
    *5)guess number what i imagimne 
    7
    харош 
    
    *6)Yeah ! Your answer is : 1 
    This is always executed 
    Sorry ! You are dividing by zero 
    This is always executed 
- Код до цієї не розберихи:
```python
a = "Hello world"
b = 1 
c = ["something", 1, 1.25, "something"] 
d = {"something": "я не придумав що написати", "something": 1} 
e = ("something", ) 
f = {"something", } 

print("Перша константа", False)
print("Друга константа", True)
print("Третя константа", True)

print(abs(-12.5), f"є рівним {abs(12.5)}")
def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
class X:
    a = 1

X = type('X', (), dict(a=1))
print(X) 

for i in range(6):
    print(i)
    i = 5  

my_info = ("Сергій", "Ребко", 18, "Студент який не знає куда себе подіти в житі і чим заробляти")

for data in my_info:
  print(data)           

print("guess number what i imagimne")
num=int(input())
if  num != 7:
    print("анлак, не вгадав")
elif num == 7:
    print("харош")
 
def divide(x, y): 
	try: 
		result = x // y 
	except ZeroDivisionError: 
		print("Sorry ! You are dividing by zero ") 
	else:
		print("Yeah ! Your answer is :", result) 
	finally: 
		
		print('This is always executed') 
divide(3, 2) 
divide(3, 0)

with open("README.md", "r") as f:
    for line in f:
        print(line)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

users = [User("Анна", 25), User("Петро", 30), User("Марія", 22), User("Олексій", 28)]

sorted_users_by_name = sorted(users, key=lambda user: user.name)
for user in sorted_users_by_name:
    print(f"{user.name}, {user.age} років")
```
## Код який мені видав чат GPT:
- Завдання з циклами

```python
1.
fruits = ["яблуко", "груша", "апельсин", "банан"]
for fruit in fruits:
    print(f"Я люблю {fruit}.")
2.
n = 5
fact = 1
while n > 0:
    fact *= n
    n -= 1
print(f"Факторіал: {fact}")

3.

for i in range(1, 6):
    print(i)
```
- Завдання з if-else
```python
1.
age = 25
if age >= 18:
    print("Ви повнолітні.")
else:
    print("Ви неповнолітні.")
2.
grade = 85
if grade >= 90:
    print("Відмінно!")
elif grade >= 70:
    print("Добре.")
elif grade >= 50:
    print("Задовільно.")
else:
    print("Не задовільно.")

```
- Конструкція try->except->finally
```python
try:
    # Спробуйте виконати діління на нуль, що спричинить помилку
    result = 5 / 0
except ZeroDivisionError as e:
    # Обробити помилку ділення на нуль
    print(f"Помилка: {e}")
finally:
    # Код, який виконається навіть у випадку помилки
    print("Цей код завжди виконається, навіть після помилки.")

```

### Висновок: 

- написав кучу коду в якому тяжко буде розібратися 
- навчився(вже вмів) писати елементарні конструкції
- я гарно провів свій час (години 2 +-)
- скріншотів нема тому-що я лінуюсь 

