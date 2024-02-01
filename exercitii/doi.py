destinatii = ['nepal', 'canada', 'argentina', 'islanda', 'dolomiti', 'portugalia']
numere = list((1, 2, 3, 4, 5, 6, 7, 8, 9))

results_list = [item.upper() for item in destinatii]
print(results_list)

results_list = []
for item in destinatii:
    results_list.append(item.upper())
print(results_list)

results_doi = [destinatii.index(item) for item in destinatii]
print(results_doi)


results_doi = []
for index, x in enumerate(destinatii):
    results_doi.append(index)
print(results_doi)

destinatii.sort()
print(destinatii)

destinatii.pop(1)
if len(destinatii) < 6:
    print(destinatii, 'putine')

destinatii = ['nepal', 'canada', 'argentina', 'islanda', 'dolomiti', 'portugalia']
destinatii.append('roma')
if len(destinatii) >= 6:
    print(destinatii, 'numere')

destinatii[4] = destinatii[4].upper()
destinatii[3] = destinatii[3].upper()
print(destinatii)

index =  destinatii.index('ISLANDA')
if index > 2:
    print ('is not')
else:
    print(destinatii, ' is')
