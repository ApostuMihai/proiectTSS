# ProiectTSS
 Proiect pentru materia "Testarea sistemelor software"
 Demo-ul poate fi gasit aici: [CLICK](https://drive.google.com/file/d/1JiF966gVVccqY5-fwnIlKby7l8-UFabV/view?usp=drive_link)
# Descrierea aplicatiei

Aplicatia noastra ofera doua funcitonalitati pentru analiza sirurilor de caractere:

1. Verificarea daca un sir este palindrom (Grup de cuvinte sau cuvânt care poate fi citit de la stânga la dreapta și de la dreapta la stânga fără să-și piardă sensul.)
2. Verificarea daca un sir este isogram (isogram (plural isograms) A word or phrase in which each letter occurs the same number of times.)

Utilizatorul poate sa aleaga intre verificarea daca un sir introdus de la tastatura este palindrom sau isogram. Sirul trebuie sa aiba cel putin 2 caractere, iar programul ignora orice caracter special(@!?.,).

# Testare functionala

Pentru testarea functionala am analizat domeniul de intrari al programului.
Exista 2 intrari:
-un intreg pozitiv n, n trebuie sa fie 1 sau 2
-un sir de caractere x, x trebuie sa aiba lungimea minima 2

Pentru n se disting 4 clase de echivalenta:
n>2
n<1
n=1,2
n nu este intreg

Pentru x se disting 2 clase de echivalenta: lungimea lui x este mai mare sau egala cu 2 si lungimea lui x este mai mica ca 2

Domeniul de iesiri are urmatoarele raspunsuri:
Raspunsul daca stringul dat este palindrom sau isogram

<table>
  <tr><th colspan=2>Intrari</th><th>Rezultat</th></tr>
  <tr><td>n</td><td>x</td></tr>
  <tr><td>t</td><td></td></tr>
  <tr><td>3</td><td></td></tr>
  <tr><td>2</td><td>isogram</td><td>Yes</td></tr>
  <tr><td>2</td><td>abca</td><td>No</td></tr>
  <tr><td>1</td><td>radar</td><td>Yes</td></tr>
  <tr><td>1</td><td>Hello</td><td>No</td></tr>
</table>

# Testare structurala, graful CFG
![main](https://github.com/ApostuMihai/proiectTSS/blob/main/poze/main.jpg "main")
![graf](https://github.com/ApostuMihai/proiectTSS/blob/main/poze/graf.jpg "graf")


Am creat graful pentru functia main si am dedus ca putem folosi doar 2 teste pentru a acoperi tot codul

![Coverage](https://github.com/ApostuMihai/proiectTSS/blob/main/poze/coverage.jpg "Coverage")

# Mutanti

Am folosit libraria mutmut pentru testele cu mutanti.

![mutanti](https://github.com/ApostuMihai/proiectTSS/blob/main/poze/mutanti.jpg "Mutanti")


# Raport utilizare tool AI:

Am folosit Microsoft Copilot pentru a genera teste pentru codul nostru. Acestea sunt testele generate:

![copilot](https://github.com/ApostuMihai/proiectTSS/blob/main/poze/cod_copilot.jpg "Copilot")

O diferenta intre codul nostru si cel generat de AI este ca noi am folosit unittest, iar Copilot a folosit pytest. De asemenea codul de la Copilot nu parcurge functia main si ofera doar cateva teste cu coverage mic.

![Coverage copilot](https://github.com/ApostuMihai/proiectTSS/blob/main/poze/coverage_copilot.jpg "Coverage copilot")
