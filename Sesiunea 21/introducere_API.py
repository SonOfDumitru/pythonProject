'''
    API-urile sau interfete de programare a aplicatiilor (Aplication Programing Interface)
permit aplicatiilor software sa comunice intre ele
    Actioneaza ca un mediator intre 2 aplicatii, permitand uneia sa solicite date
sau servicii de la cealalta si sa primeasa raspunsul in schimb
    API-urile fac posbil ca aplicatiile sa acceseze functii sau date ale
altor platforme deschizand posibilitati infinite de inovare si integrare
'''


'''
    REST(REpresentational State Transfer) este un stil arhitectural pt furnizarea de standarde
intre sisteme computerizate de pe web, facilitand comunicarea intre ele
    Sistemele compatibile REST, numite si RESTful se caracterizeaza prin modul in care sunt independente
si separa preocuparile clientului si ale serverului 
    Pt ca un API sa fie considerat RESTful trebuie sa respecte urmatoarele constrangeri:

1. Arhitectura client-server: clientul si serverul sunt separate si actioneaza independent 
                              permitand utilizarea a diferite tehnologii pentru fiecare

2. Stateless(fara stare): serverul nu stocheaza niciun context pt client intre cereri astfel incat 
                          fiecare cerere contine toate informatiile necesare pt a o finaliza
                        
3. Capacitate de cache: clientii pot stoca in cache datele de raspuns reducand numarul de solicitari
                        catre server si astfel imbunatatind performanta

4. Utilizarea metodelor HTTP

5. Utilizarea codurilor de stare HTTP: API-urile RESTful folosesc aceste coduri pt a indica starea rezultatului
                                       unei solicitari, cum ar fi succes(200), esec(400) sau negasit(404)
                                       (https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
'''


'''
    Metodele HTTP sunt metode standard utilizate pt a indica actiunea dorita care 
trebuie efectuata pe o resursa din API . Cele 4 metode principale sunt:

1. GET: Preia date dintr-o resursa si este folosit pt citire
2. POST: Creaza o noua resursa si este folosita pt a trimite date catre un server
3. PUT: Actualizeaza o resursa curenta si este folosita pt a modifica datele existente
4. DELETE: Sterge o resursa si este folosit pt a elimina date
    
'''
