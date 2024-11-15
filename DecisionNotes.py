
num = 47
if num >= 90:
    print("Hello")
print("Folks")

# the 6 relational operators
#   >, <, >=, <=, ==, and !=

seconds=100
if seconds >= 60:
    print("over a minute")
else:
    print("less than a minute")

num = 97
if not num % 2 == 0:  # same as num%2 != 0
    print("odd")
else:
    print("even")

seconds = 100
if seconds < 60:
    print("less than a minute")
elif seconds < 120:  #short for else-if
    print("over a minute")
else:
    print("over two minutes")

# logical operators
# or     and      not

x = 50
y = 700
if x < 10 or y < 50:  #one or the other or both
    print("fun")
elif x < 400 or y < 300:
    print("wow")

x = 500
y = 100
if x < 400 and y < 300:  #both must be true to engage
    print("upper right")
elif x < 400 and y > 300:
    print("upper left")

grade = 87
if grade >= 70:
    print("passing")
    if grade >=90: #nesting ifs
        print("A")
else:
    print("failing")

