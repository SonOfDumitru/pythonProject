'''
cu o bucla while putem executa un set de instructiuni pana ce o conditie este adevarata
'''

count = 0

while count < 3:
    count += 1
    print(f'count:{count}')

l = [1, 2, 3, 4, 5]
index = 0
while index < len(l):
    print(l[index])
    index += 1

print(20 * '-')
# break

i = 1
while i < 6:
    print(i)
    if i == 3:
        break  # opreste iteratia
    i += 1

print(20 * '-')
# continue

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue  # sare peste cod (i==3) si ruleaza mai departe bucla
    print(i)

print(20 * '-')
# else

count = 0
while count < 3:
    count += 1
    print(f'count:{count}')
else: #ruleaza cand bucla se termina
    print('sunt in else')

print(20 * '-','else + break',20 *'-')
# else + break

count = 0
while count < 3:
    count += 1
    print(f'count:{count}')
    if count ==2:
       break
else:#nu ruleaza cand apare break
    print('sunt in else')
