x = y = z = 0

x = int(input('Input the first number '))
y = int(input('Input the second number '))
z = int(input('Input the third number '))

l = [x, y, z]
odd = [(i,num) for (i,num) in enumerate(l) if num % 2 != 0]
odd.sort(key=lambda x:x[1])
