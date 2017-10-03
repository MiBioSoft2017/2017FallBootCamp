#Python Tutorial

# Variables
print('----Variable Stuff-----')
x = 10
y = 6
print(x + y)
print(x / y) #Integer division
print(x / float(y))  #Cast at least one operand to float to get float as result

s = 'Hello'
t = "Bye"
longString = """
This
Is
On
Multiple Lines
"""

print(s + ' ' + t + " " + str(x)) #"Hello 10"
print(longString)
print("Hello 'hello'")

#None
c = 5
print(c)
c = None
print(c)
print(type(c))

print(int(True))

#Cleaner way to deal with strings
answer = 5
print("Answer: {} {}".format(answer, 7))

#Lists
print('\n---------Lists----------')

L = [1, 2, 3, 4, 'Hello', 5.3, True, False]
print(L)
L.append('BioSoft')
print(L)
L.remove('Hello')
print(L)

s = ""
for item in L:
	s += str(item) + ' ' #s = s + item
print(s + "\n")

print(range(10, 0, -2))
for i in reversed(range(10)):
	print(i)

print("--While--")
x = 0
while x < 5:
	print(x)
	x += 1

print("\n----Dictionary------")
Q = {
	'Ali': 20,
	'Catherine': 19,
	'Josh': 29,
}
print(Q['Ali'])

message_form = {
	'username': ['user1', 'user2'],
	'message': 'Hello',
}

for key in message_form:
	print(key, message_form[key])

#-----Functions------
print("\n-------Functions-------")

def MyFunction(name, SSN):
	if len(str(SSN)) < 5:
		return False
	else:
		return True

if not MyFunction('Ali', 4):
	print("pass")
else:
	print("fail")

print("\n--------Class------")
class MyClass:
	a = 23
	b = 76
	
obj = MyClass
print(obj.a)

def testFunction(p):
	print(p.a)
	print(p.b)

testFunction(obj)


