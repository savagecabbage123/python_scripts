from sympy import *
fib = 0

def fibonacci(x) -> int:
    #using recurrence solving techniques which I dont want to rewrite in a text editor
    #we can form a formula for fibonacci sequence
    n = symbols('n')
    f = (1/sqrt(5))*(((1 + sqrt(5))/2)**n - ((1 - sqrt(5))/2)**n)
    f = f.subs(n, x)
    return int(f)

#you also dont need sympy for this to work you could use default library or the math library, I just 
#wanted to use sympy for a simple demo
"""you can obviously use a simpler method of solving fibonacci but the upside to doing this is that it runs at a constant
time complexity O(1) since you dont need any loops to solve for an nth term of fibonacci unless you want to print a sequence
of fibonacci terms which would be O(n) time complexity"""

user_input = -1
while (user_input <= 0):
    user_input = int(input("enter a number to print fibonacci sequence up to that term: "))

#print fibonacci terms from term 1 (f0) to term user_input (fn)
for i in range(0, user_input):
    print(f"term {i + 1}:", fibonacci(i))

#print fibonacci term
user_input = -1
while (user_input <= 0):
    user_input = int(input("enter the fibonacci term you would want to find: "))

print(f"term {user_input}:", fibonacci(user_input - 1))