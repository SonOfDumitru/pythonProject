'''
Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.

'''

'''
1. Declară o listă note_muzicale în care să pui do re mi etc până la do
Afișeaz-o.
Inversează ordinea folosind slicing și suprascrie această listă.
Printează varianta actuală (inversată).
Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea. Nu trebuie să o suprascrii 
în acest caz, deoarece metoda face asta automat.
Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.

Concluzii: slicing e temporar, dacă vrei să păstrezi nouă variantă va trebui să suprascrii lista sau să o salvezi într-o listă nouă. 
Metoda găsită de tine face suprascrierea automat și permanentizează aceste modificări. Ambele variante își găsesc utilitatea în 
funcție de ce ne dorim în acel moment. 
'''

note_muzicale = ['do', 're', 'mi','fa','sol','la','si','do']
print(note_muzicale)
print(note_muzicale[::-1])
note_muzicale.reverse()
print(note_muzicale)
print(note_muzicale[:])
print(note_muzicale.count('do'))


note_muzicale2 = ('do', 're', 'mi','fa','sol','la','si','do')

note_muzicale2 +=('BLA',)
print(note_muzicale2)

note_muzicale3 = {'do' : input('do '),
                  're' : input('re '),
                  'mi' : input('mi '),
                  'fa' : input('fa '),
                  'sol' : input('sol '),
                  'la' : input('la '),
                  'si' : input('si '),
                  'd0' : input('do '),

}
print(note_muzicale3)
