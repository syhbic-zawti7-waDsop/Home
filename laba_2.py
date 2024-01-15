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