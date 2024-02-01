'''
o bucla for este folosita pentru a itera teste peste o secventa (lista, set, tuplu, dictionar, string)
'''

for i in range(10):
    print(i)

print(20 * '-')

for i in range(5,10):
    print(i)

print(20 * '-')

for i in range(5,10,2):
    print(i)

print(20 * '-')

l = [1,2,3,4,5]
for i in range(len(l)):
    print(l[i])

print(20 * '-')
# for each

fructe = ['mere','pere','banane']
for x in fructe:
    print(x)

print(20 * '-')

for x in 'Ana are mere':
    print(x)

print(20 * '-')

d= {
    'a':1,
    'b':2,
    }

for x in d: #iterarea in dictionar se face prin chei
    print(x)

for x,value in d.items():
    print(x,value)


print(20 * '-')
#break

for x in fructe:
    if x == 'pere':
        break
    print(x)

print(20 * '-')
#continue

for x in fructe:
    if x == 'mere':
        continue
    print(x)

print(20 * '-')

for x in fructe:
    if x == 'mere' or x == 'banane':
        continue
    print(x)

print(20 * '-')
#else

for x in fructe:
    print(x)
else:
    print('sunt in else')

print(20 * '-')

for x in fructe:
     if x=='pere':
         break
     print(x)
else:
     print('sunt in else')

print(20 * '-')
#nested for

adj =['rosii','mari','delicioase']
for x in fructe:
    for y in adj:
        print (x,y)
        print (len(x),len(y))

print(20 * '-')
#pas

for x in [1,2,3,4]:
    pass


for x in range(100_000_000):
    pass
    print(x,'gata')
