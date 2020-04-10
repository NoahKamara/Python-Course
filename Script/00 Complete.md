---
# 2 Erste Schritte



## 2.1 Die Basics



### 2.1.1 Das Print Statement

Mit dem Print Statement kann das Programm in die Konsole ausgeben

```python
print("Hello World")
print(123)

> Hello World
> 123
```



### 2.1.1 Variablen

Um Werte, temporär im Speicher zu halten definiert man 'Variablen'. Diese müssen deklariert und können danach beliebig verändert werden. Variablen verhalten sich als Objekt des Typs den sie beinhalten

```python
var = "Hallo Welt!"
print(var)

> Hallo Welt!
```

```
num = 1
print(var)
num = num + 1
print(var)

> 1
> 2
```



### 2.1.2 Kommentare

Kommentare werden beim ausführen des Codes ignoriert und sind hilfreich, um den Zweck von Funktionen und Variables zu beschreiben.

```python
greeting = "Hallo" # Begrüßung
print(greeting)
```



### 2.1 Datentypen in Python

#### Zahlen

In Python gibt es zwei Arten von Zahlen: ``float`` 'floating' sind Fließkommazahlen während``int`` 'integer' Ganze Zahlen wiederspiegeln

```python
integer = 1
floating = 1.23817289461892789
arithmetik = 1 + 1 - 2 / 2
```

#### Strings

Strings sind Aneinanderreihungen von Zeichen, bzw. Text

```python
string = "Hallo Welt"
```

#### Booleans

Booleans können die Werte ``False`` und ``True`` einnehmen

```python
booleanTrue     = True
booleanFalse    = False
```

#### Listen

Listen sind Aneinanderreihungen von anderen Objekten (auch anderen Listen). Strings sind (wie hier zu sehen, einfach nur Listen von Symbolen)

```python
listeInt = [1,2,3,4,5,6,7,8,9]
listeFloat = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
listeString = ["H","A","L","L","O"," ","W","E","L","T"]
string = "Hallo Welt"
```

Listen haben spezielle Eigenschaften. Diese besprechen wir später noch genauer.











---
# 3 Kontrollfluss



## 3.1 Bedingungen und Ausdrücke

### 3.1.1 Bedingungen

Bedingungen können genutzt werden, um zwei Objekte zu vergleichen oder ein Objekt zu validieren

#### Operatoren

**== (ist gleich)** Mit ist gleich ergibt der Ausdruck ``True `` wenn beide Elemente identisch sind

**> , < (größer als, kleiner als)** Mit kleiner und größer kann man zwei Zahlen vergleichen

**!= (nicht gleich)** Das Ungleich ist die Inversion des Gleichzeichens ``==``

**not (nicht)** Inversiert den nachstehjenden Ausdruck



### 3.1.2 Verknüpfen mehrerer Ausdrücke

Mit einem 'und', bzw 'oder' können zwei (oder mehr) Ausdrücke verknüpft werden und so einen neuen Ausdruck bilden.

**and (und)** Wenn zwei Ausdrücke mit einem und verknüpft sind ergibt der Gesamt-Ausdruck nur dann ``True`` wenn beide Ausdrücke ``True`` sind

**or (oder)** Wenn zwei Ausdrücke mit einem oderverknüpft sind ergibt der Gesamt-Ausdruck dann ``True`` wenn einer der beiden Ausdrücke ``True`` ist

```python
alter = 16
mindestalter = 18
muttiZettel = True
einlass = (alter >= mindestalter) or (muttiZettel and alter >= 16)
print(einlass)

> True
```



> Um von Hand zu prüfen, ob der Ausdruck so stimmt, gehe immer von den innersten Ausdrücken nach außen. Man kann die verknüpften Ausdrücke zusammenfassen



### 3.1.3 IF - Statements

Das ``if`` Statement kann genutzt werden zu steuern, welche Teile des Programms ausgeführt werden sollen. Dazu werden Boolsche Ausdrücke benutzt.

**if** Wenn die 'IF-Bedingung' erfüllt ist wird der darunter eingerückte Code ausgeführt, ansonsten nicht:

**else** Mit dem setzen eines ``else`` kann bestimmt werden was im fall einer nicht erfüllten Bedingung passieren soll.

**elif** Ein Elif ist die Verbindung eines else mit anschließendem if

```python
if age > 18: 
    print("Einlass")
elif age > 16 and muttiZettel:
    print("Einlass bis 12")
else:
    print("Kein Einlass")
```



### 3.1.4 Schleifen

Mit Schleifen kann man Code-Abschnitte mehrfach ausführen lassen (auch mit verschiedenen Parametern).

#### FOR Schleifen

For-Schleifen führen Code bestimmt häufig aus und übergeben dabei eine Variable an diesen.

```python
liste = ["Sven","Simon","Nikolas","Tom"]

for name in liste:
    print("Hallo "+name)
    
> Hallo Sven
> Hallo Simon
...
```

#### WHILE Schleifen

For-Schleifen führen Code bestimmt häufig aus und übergeben dabei eine Variable an diesen.

```python
, language=Python]
liste = ["Sven","Simon","Nikolas","Tom"]
length = len(liste)
i = 0

while i < length:
	print(str(i)+" Hallo "+liste[i])

> 0 Hallo Sven
> 1 Hallo Simon
...
```

> Die Verwendung der while Schleife hier ist fraglich. Die for-Schleife darüber erfüllt den selben Zweck ist jedoch übersichtlicher und kürzer (!)
>
> Je nach Zweck muss man sich überlegen, welche der Schleifen besser ist

---
# 4 Listen und Objektorientierung

## 4.1 Mehr über Listen

### 4.1.1 Listen-Abschnitte erhalten

##### Einzelnes Element mit Index

```python
arr = [1,2,3]
print(arr[0])

> 0
```

##### Teil der Liste mit Start und End-Index

```python
arr = [1,2,3,4,5,6,7,8]
print(arr[1:3])

> [2, 3]
```

##### Teil der Liste mit nur Start oder End-Index

```python
arr = [1,2,3,4,5,6,7,8]
print(arr[:3])
print(arr[4:])

> [1, 2, 3]
> [5, 6, 7, 8]
```
``arr[:x]`` ist äquivalent zu ``arr[0:x]``     
``arr[x:]`` ist äquivalent zu ``arr[x:len(arr)]``

### 4.1.2 Elemente zur Liste hinzufügen und von dieser entfernen

##### Einzelnes Element zum Ende hinzufügen

```python
arr = [1,2,3]
arr.append(4)
print(arr)

> [1, 2, 3]
```
Äquivalent zu ``arr[len(arr):] = [4]``

##### Liste hinzufügen

```python
arr = [1,2,3]
arr.extend([4,5,6])
print(arr)

> [1, 2, 3, 4, 5, 6]
```
Äquivalent zu ``arr[len(arr):] = [4,5,6]``

##### Element an bestimmter Stelle einfügen

```python
arr = [1,2,3]
arr.insert(2, 4)
print(arr)

> [1, 2, 4, 3]
```
##### Gewisses Element entfernen

```python
arr = [1,2,3]
arr.remove(2)
print(arr)

> [1, 3]
```



### 4.1.3 Andere Funktionen

##### Frequenz eines Elements in der Liste 

```python
arr = [1,2,3,1]
print(arr.count(1))

> 2
```

##### Liste sortieren

```python
arr = [1,2,3,1]
arr.sort(reverse=False)
print(arr)
arr.sort(reverse=True)
print("reversed", arr)
> [1, 1, 2, 3]
> [3, 2, 1, 1]
```

##### Reihenfolge umkehren

```python
arr = [1,2,3,1]
arr.reverse()
print(arr)
> [1, 3, 2, 1]
```



## 4.2 Dictionaries und Klassen

### 4.2.1 Dictionaries

Dictionaries (auch assoziative Arrays) genannt sind nicht wie Listen mit einer Zahl indexiert, sondern mit 'Schlüsseln'.

```python
dic = {'hello': 'hallo', 'wine':'Wein'}
print(dic['hello'])

> hallo
```

Ähnlich wie Listen kann man auch durch Wörterbücher iterieren:

#### Schleifen mit Dictionaries

##### Durch 'Elemente' iterieren

```python
tel = {
    'Jens': '1234567',
    'Angela': '0275839',
    'Martin': '1948573',
    'Hans-Georg': '01873573'
}

for key, value in tel.items():
    print(key, value)
          
> Jens 1234567
> Angela 0275839
> ...
```



##### Durch 'Schlüssel' iterieren

```python
for key in tel.keys():
    print(key, tel[key])
          
> Jens 1234567
> Angela 0275839
> ...
```



##### Durch 'Werte' iterieren

```python
for value in tel.values():
    print(value)
          
> 1234567
> 0275839
> ...
```



#### Elemente hinzufügen oder ändern

Elemente können ähnlich zur Liste hinzugefügt und verändert werden:

```
dic = {'hello': 'hallo', 'wine':'Wein'}
dic['beer'] = 'Bier'
print(dic)

> {'hello': 'hallo', 'wine':'Wein', 'beer':'Bier'}
```



#### Was tun mit Dictionaries?

Elemente können ähnlich zur Liste hinzugefügt und verändert werden:

```
profile = {
	'last_name': 'Merkel',
	'first_name': 'Angela',
	'birthday': {
		'year': 1954
		'month': 06
		'day': 17
	}
}
```



### 4.2.2 Klassen

Klassen bietet eine Möglichkeit Daten und Funktionalität zu bündeln. Das Erstellen einer Klasse erstellt einen neuen Objekt-Typ. Somit können neue Instanzen dieser Objekte erstellt werden.

```python
class Profile:
    def __init__(self, last_name, first_name, birthday):
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        
profile = Profile("Merkel","Angela", date(1954,6,7))
print(profile.last_name, profile.first_name)

> Merkel  Angela
```



#### Funktionen in Klassen

Die Besonderheit bei Klassen ist, dass diese auch Funktionen haben können, die sich die Attribute (und Funktionen) der Klasse zu nutze machen können. Dazu wird als erster Parameter der Funktion das Objekt selbst ``self`` übergeben. (Beim Aufrufen der Funktion muss dieser nicht angegeben werden)

```python
class Profile:
    def __init__(self, last_name, first_name, birthday):
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        
	def name(self):
    	return self.first_name+" "+self.last_name

profile = Profile("Merkel","Angela", date(1954,6,7))
print(profile.name())

> Angela Merkel
```



##### Klassen in einem anderen Kontext

Klassen können auch genutzt werden um eigene Module zu erstellen, die mit Parametern initialisiert werden (Zum Beispiel einem Passwort oder einer Bedingung):

```python
class Filter:
    def __init__(self, filterList, isWhiteList = True):
        self.filterList = filterList
        self.isWhiteList = isWhiteList
        
    def filter(self, text):
        wasFiltered = False
        text = text.casefold()
        for filterWord in self.filterList:
            if filterWord in text:
                wasFiltered = True
                continue
        
        if self.isWhiteList:
            return wasFiltered
       	else:
            return not wasFiltered
        
        
f1 = Filter(['testwort'])
f2 = Filter(['testwort'], isWhiteList = False)
text = "Das Testwort"
print( f1.filter(text) )
print( f2.filter(text) )

> True
> False
```



## 4.3 Objektorientierung

Unter Objektorientierung versteht man eine Sichtweise auf komplexe Systeme, bei der ein System durch das Zusammenspiel kooperierender Objekte beschrieben wird.

##### Alles sind Objekte

Ein (sehr komplexes) Beispiel:

```python
class Car:
    def __init__(self, manufacturer, model, paint, engine):
        self.manufacturer = manufacturer
        self.model = model
        self.paint = paint
        self.engine = engine

    def specs(self):
        makerAndModel = self.maker+" "+self.model
        return makerAndModel+" | "+self.engine.specs()+" | "+self.paint.specs()
        
        
class Paint:
    def __init__(self, code, description):
        self.code = code
        self.description = description 

    def specs(self):
        return self.description+"  ("+self.code+")"


class Engine:
    def __init__(self, horsepower, cylinders):
        self.horsepower = horsepower
        self.cylinders = cylinders

    def specs(self):
        return str(self.horsepower)+" PS (V"+str(self.cylinders)+")"



car = Car(
    manufacturer = 'Ford',
    model = 'Mustang GT',
    paint = Paint(code='ABCDEFG', description='red'),
    engine = Engine(horsepower=350, cylinders=8)
)

print(car.specs())

> Ford Mustang GT     350 PS (V8)     red  (ABCDEFG)
```

---
# 5 Fehlermeldungen und 'Debugging'

# 5.1 Fehlermeldungen und Ausnahmen
## 5.1.1 Syntaxfehler
Obwohl Python einen relativ laschen Umgang mit korrektem Syntax hat, müssen gewisse Regeln befolgt werden. Ein gutes Beispiel dafür ist das Einrücken von Code-Abschnitten in Schleifen, IF-Bedingungen und Funktionen:
```python
while True print('Hello World')
>  File "<stdin>", line 1
>    while True print('Hello world')
>               ^
>SyntaxError: invalid syntax
```
Python wiederholt die problematische Zeile und zeigt einen kleinen Pfeil unter der Stelle die den Fehler erzeugt hat. In diesem Beispiel fehlt der Doppelpunkt ':' nach dem 'while True'-Statement. Aus der Fehlermeldung kann man auch den Dateinamen und die Zeile herauslesen.

## 5.1.2 Ausnahmen ('Exceptions')
Selbst wenn eine Aussage syntaktisch korrekt ist, kann diese einen Fehler erzeugen, wenn der Code ausgeführt wird.
```python
print( 10 * (1/0) )

>Traceback (most recent call last):
>  File "<stdin>", line 1, in <module>
>ZeroDivisionError: division by zero
```
```python
print( 4 + spam*3 )

>Traceback (most recent call last):
>  File "<stdin>", line 1, in <module>
>NameError: name 'spam' is not defined
```

```python
print( '2' + 2 )

>Traceback (most recent call last):
>  File "<stdin>", line 1, in <module>
>TypeError: Can't convert 'int' object to str implicitly
```
Die letzte Zeile der Fehlermeldung gibt die Art des Fehlers und eine Beschreibung an.
'ZeroDivisionError' zum Beispiel gibt an, dass versucht wurde eine Zahl durch '0' zu teilen, während 'TypeError' angibt, dass ein Objekt den falschen Typ aufweist (hier: String statt Integer)

## 5.1.3 Ausnahmenbehandlung
Um Abbrüche in der Ausführung zu vermeiden, können Aussagen in ein 'try'-'except' gepackt werden. Falls es zu einer 'Exception' kommt wird der Code im 'except' ausgeführt. 
```python
gspaces=false, language=Python]
grades = ["1","Z","3","0"]
for grade in grades:
    try:
        integer = int(grade)
        print(10 / integer)
    except ValueError:
        print("Ein ValueError ist aufgetreten")
        
> 1
> Ein ValueError ist aufgetreten
> 3
>Traceback (most recent call last):
>  File "<stdin>", line 5, in <module>
>ZeroDivisionError: division by zero
```

Beim obigen Beispiel wird nur ein Fehler der art 'ValueError' behandelt. Aus diesem Grund bricht das Programm trotzdem mit einem 'ZeroDivisionError' ab. Dieses Problem könnten wir auf zwei Arten lösen:
1. **Zusätzliches 'except':**
```python
try:
    integer = int(grade)
    print(10 / int)
except ValueError:
    print("Ein ValueError ist aufgetreten")
except ZeroDivisionError:
    print("Ein ZeroDivisionError ist aufgetreten")
```
2. **'except' ohne genau Angabe des Typs:**
```python
try:
    integer = int(grade)
    print(10 / int)
except:
    print("Ein Fehler ist aufgetreten")
```
Welche der beiden Lösungen man verwenden sollte hängt alleinig von der Situation ab. Wenn das Programm zum Beispiel jegliche fehlerhaften Werte überspringen soll eignet sich Variante 2. Wenn es jedoch zum Beispiel einen 'ZeroDivisionError' behandelm soll indem es einfach $0$ ausgibt, dann sollte man Variante 1 verwenden.

> **Tipp**
>
> 'try' und 'except' verhalten sich ähnlich wie ein IF-ELIF-ELSE
```python
try:
    # raise erhebt einen Error
    raise ZeroDivisionError 
except ZeroDivisionError: # if error = ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError: # elif error == ValueError:
    print("ValueError")
except AttributeError: # elif error == AttributeError:
    print("AttributeError")
except: # else:
    print("Anderer Fehler")
```



## 5.1.4 Fehler erheben

```python
raise NameError("das ist ein Fehler")
> Traceback (most recent call last):
>  File "<stdin>", line 1, in <module>
> NameError: HiThere
```



# 5.2 Fehler 'debuggen' und Vermeidung

Jeder macht Fehler. Das wichtige ist nur, dass man weiß, wie man diese korrigiert!



## 5.2.1 Was ist "Debugging"?

> 1947 hatte während der Arbeiten am [Mark II](https://de.wikipedia.org/w/index.php?title=Mark_II_(Computer)&action=edit&redlink=1) eine Motte für den Ausfall eines Relais dieses Computers gesorgt. Das Team von Grace Hoppers fand die Motte und klebte sie in das Logbuch zusammen mit dem Satz „First actual case of bug being found.“

## 5.2.2 Typische Fehler und wie man sie "debugged"

#### Programm produziert eine ausnahme ("Exception")}
In diesem Fall packe ich den Teil, der eine "Exception" produziert in ein "try-except" und lasse mir mögliche Fehlerquellen ausgeben: 
```python
def doSomething(param1, param2):
    result = param1 / param2
params = [0,1,2,3,4]
for param in params:
    param1 = param
    param2 = param - 1
    doSomething(param1, param2)
    
>Traceback (most recent call last):
>  File "<stdin>", line 2, in <module>
>ZeroDivisionError: division by zero
```
Also: die Aussage 'result = param1 / param2' produziert einen 'ZeroDivisionError', bedeutet, dass param2 '0' ist. Ich packe nun diese Zeile in ein "try - except" und lasse mir im Falle einer Exception die parameter ausgeben.

```python
def doSomething(param1, param2):
    try:
        result = param1 / param2
    except:
        print("except", param1, param2)
params = [0,1,2,3,4]
for param in params:
    param1 = param
    param2 = param - 1
    doSomething(param1, param2)
    
> except  1  0
```
Aha! Wenn $param1 = 1$, also wenn $param = 1$ (wegen $param1 = param$), dann ist param2 eine $0$. Und das weil $param2 = param - 0$. 
Fehler gefunden!

#### Das Programm läuft aber das Ergbenis ist (manchmal) falsch.
---
# 6 Funktionen & Module

## 6.1 Funktionen

Funktionen können an einer stelle des Codes "definiert" und an zu späteren Zeitpunkten aufgerufen werden.

### 6.1.1 Funktionen definieren

```python
def greeting():
print("Hallo Welt")

greeting()
greeting()

> Hallo Welt
> Hallo Welt
```

Dies lohnt sich natürlich vor Allem bei längeren Abschnitten, die im Programm öfter gebraucht werden.

#### Parameter

Parameter können an Funktionen übergeben und von diesen auch zurückgegeben werden.

```python
def makeGreeting(name):
greeting = "Hallo "+name+". Wie geht's?"
return greeting 

greeting = makeGreeting("Sven")
print(greeting)

> Hallo Sven. Wie geht's?
```



### 6.1.2 Warum benutzt man Funktionen?

Funktionen sind ...

- **platzsparend**: Funktionen können einmal geschrieben und mehrfach im Code verwendet werden
- **übersichtlich**: Funktionen machen das Programm übersichtlicher, da man Abschnitte so leicht zusammenfassen kann.
- **gut für die Nerven**: wenn ein Abschnitt, den man mehrfach verwendet einen Fehler hat muss man im Falle einer Funktion nur einmal korrigieren.

```python
grades = [3.75, ... , 2.5]

# Ohne Funktionen (6 Zeilen):
summe = 0
length = 0
for grade in grades:
summe += grade
length += 1
average = summe / length
print(average)

# Mit Funktionen (1 Zeile):
average = sum(grades) / len(grades)
```



## 6.2 Module
Module sind Erweiterungen mit Funktionen und Klassen, die einem das Leben einfacher machen

### 6.2.1 Module importieren
Module müssen importiert werden, um deren Benutzung zu erlauben. Hierbei kann man entweder ein ganzes Modul importieren oder auch nur einzelne Klassen oder Funktionen dieses

##### Gesamtes Modul

```python
import math
print( math.sqrt( 16 ) )

> 4
```



##### Bestimmte Funktion(en)

Falls man nur eine oder zwei Funktionen benötigt kann man auch nur bestimmte Teile des Moduls importieren (so dass nicht alle Teile geladen werden müssen)

```python
from math import sqrt, ceil

print( sqrt( 16 ) )
print( ceil( 2.341 ) )

> 4
> 3
```



##### Umbenennung

Um Namenskonflikte zu vermeiden können Imports unter einem eigens definierten Namen importiert werden

```python
from math import sqrt as root
sqrt = 0 # Kein Konflikt mit math.sqrt
print( root( 16 ) )

> 4
```



### 6.2.2 Die Python Standard Library

Die Standardbibliothek ist eine der größten Stärken von Python, wodurch es sich für viele Anwendungen eignet. Der überwiegende Teil davon ist plattformunabhängig, so dass auch größere Python-Programme oft auf Unix, Windows, macOS und anderen Plattformen ohne Änderung laufen. \\
Teile dieser Bibliothek sind unter anderem auch das 'print' statement und funktionen, wie 'len()' und 'sum()'



### 6.2.3 Third Party Module

Die Standardbibliothek kann mit 'Packages' erweitert werden. Download und Installation des Packages und seiner Abhängigkeiten dient das Paketverwaltungsprogram PIP. Dazu muss lediglich der name des Packages genannt werden.

```bash
> pip install requests

Collecting pylib3
  Downloading https://files.pythonhosted.org/example
Collecting termcolor==1.1.0 (from pylib3)
  Downloading https://files.pythonhosted.org/example
Installing collected packages: termcolor, pylib3
  Running setup.py install for termcolor ... done
  Running setup.py install for pylib3 ... done
Successfully installed pylib3-0.0.3 termcolor-1.1.0
```

Im Terminal kann mit ``pip install <packagename>`` das Modul heruntergeladen und installiert werden. Nun kann es von überall importiert werden.

> **Tipp**
>
> [PyPi](https://pypi.org/) bietet eine große Auswahl an Python Packages. Das beste Verzeichnis dafür bleibt jedoch nach wie vor [Google](https://google.de)



### 6.2.4 Eigene Module

Es können auch Funktionen aus eigenen Dateien importiert werden. Beispielsweise kann sich die Funktion ``doSomething()`` in Datei ``MyModule.py`` befinden und in ``MyApplication.py`` importiert werden.

```python
# MyModule.py
def doSomething():
	print("Dew it!")
```

```python
# MyApplication.py
from MyModule import doSomething as dewIt
dewIt()

> Dew It!
```



> **Achtung**
>
> Befinden sich Fehler in ``MyModule.py``87878787878787878799 kann auch ``MyApplication.py``nicht ausgeführt werden. 

---
# 7 Dokumentation & Dateien

## 7.1 Dokumentation 



## 7.2 Dateien

### 7.2.1 Lesen

### 7.2.2 Schreiben

### 7.2.3 Exkurs: Dateiformate



## 7.2 JSON

Die JavaScript Object Notation(JSON)  ist ein kompaktes Datenformat in einer einfach lesbaren Textform. Es ist Vergleichbar mit Dictionaries in Python.



---

---
# 9 Emails



## 9.1 Sending Emails

#### 9.1.1 Templates

"Template Strings" enthalten Platzhalter, die mit anderen Strings ausgetauscht werden können. ``${identifier}``

> Hallo ${RECEIVER_NAME}, 
> 
> Dies ist eine Test-Nachricht.
> Das ist deine Email: ${RECEIVER_MAIL}
> 
> Liebe Grüße,
> ${SENDER_NAME}

Wir können einen String in ein Template verwandeln, indem wir mit ihm eine Entität der ``Template``-Klasse initialisieren

```python
from string import Template

string = """
Hallo ${RECIPIENT_NAME}, 

Dies ist eine Test-Nachricht.
Das ist deine Email: ${RECIPIENT_MAIL}

Liebe Grüße,
${SENDER_NAME}
"""

template = Template(string)
```



#### 9.1.2 SMTP

SMTP steht für Simple Mail Transfer Protocol und wird von Mail-Servern zum Senden von Emails genutzt. Das Package ``smtplib`` implementiert dieses Protokoll für Python

```python
import smtplib
# set up the SMTP server
s = smtplib.SMTP(host='your_host_address_here', port=your_port_here)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)
```



#### 9.1.3 Das Email Package

Das Email Package kann zum erstellen von Mails verwendet werden. (Um den gängigen Standards für Mails gerecht zu werden)

```python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


msg = MIMEMultipart()
# META-Daten der Email setzen
msg['From'] = SENDER_ADDRESS
msg['To'] = RECIPIENT_ADRESS
msg['Subject']="This is TEST"

msg.attach(MIMEText(MESSAGE, 'plain')) # Den Text hinzufügen 

    
```



#### 9.1.4 Mails versenden

```
import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Contact:
    def __init__(self, last, first, adress):
        self.last_name = last
        self.first_name = first
        self.email = adress


def connectServer(host, port, adress, password):
    """Returns a Server connection.

    Arguments:
        host {str} -- hostname of the server
        port {int} -- port for the server
        adress {str} -- email adress of the account
        password {str} -- password of the account

    Returns:
        smtplib.SMTP -- SMTP-Server-Client
    """    
    s = smtplib.SMTP(host=host, port=port)
    s.starttls()
    s.connect(host=host, port=port)
    s.login(adress, password)
    
    return s

def loadTemplate(filename):
    """Loads a Template file from Disk
    
    Arguments:
        filename {str} -- path of the file
    
    Returns:
        Template -- String Template object
    """    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def getContacts(filename):
    """retrieves the contacts from a CSV file
    
    Arguments:
        filename {str} -- path of the file

    Returns:
        list[Contact] -- list of Contact entities
    """    
    contacts = []
    with open(filename, mode='r') as f:
        for contact in f:
            contacts.append( Contact(contact[0],contact[1],contact[2]) )
    return contacts

def makeMessage(sender, recipient, subject, msg_body, msg_type):
    """Generates and returns a MIMEMultipart Message
    
    Arguments:
        sender {str} -- Sender's Email
        recipient {str} -- Recipient's Email
        subject {str} -- Email Subject
        msg_body {str} -- Email body
        msg_type {str} -- The type of the body (e.g. 'plain' or 'html')
    
    Returns:
        MIMEMultipart -- MIMEMultipart Message
    """    
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(msg_body, msg_type))
    return msg


# Server Config
cfg = {
    'host': 'smtp.ionos.de',
    'port': 587,
    'user': 'test@dev.noahkamara.com',
    'pass': '988-xyQ-6Vp-NEp'
}


# Initialize Server-Client
server = connectServer(cfg['host'], cfg['port'], cfg['user'], cfg['pass'])

# Retrieve Contacts
# contacts = getContacts('contacts.csv')
contacts = [
    Contact('Kamara','Test01','test01@login.noahkamara.com'),
    Contact('Kamara','Test02','test02@login.noahkamara.com'),
    Contact('Kamara','Test03','test03@login.noahkamara.com'),
    Contact('Kamara','Test04','test04@login.noahkamara.com')
]

# For each contact
for contact in contacts:
    # Load template
    template = loadTemplate('live/template')
    # substitute placehoders in template
    msg_body = template.substitute(RECIPIENT_NAME=contact.first_name, RECIPIENT_MAIL=contact.email, SENDER_NAME='Python Script')
    msg_type = 'plain' # Message Type
    # make a MIMEMUltipart message
    msg = makeMessage(cfg['user'], contact.email, f"Hallo {contact.first_name}", msg_body, msg_type)
    # Send Message
    server.send_message(msg)

# Close server Connection
server.quit()
```

---

---

# 2 Erste Schritte



## 2.1 Die Basics



### 2.1.1 Das Print Statement

Mit dem Print Statement kann das Programm in die Konsole ausgeben

```python
print("Hello World")
print(123)

> Hello World
> 123
```



### 2.1.1 Variablen

Um Werte, temporär im Speicher zu halten definiert man 'Variablen'. Diese müssen deklariert und können danach beliebig verändert werden. Variablen verhalten sich als Objekt des Typs den sie beinhalten

```python
var = "Hallo Welt!"
print(var)

> Hallo Welt!
```

```
num = 1
print(var)
num = num + 1
print(var)

> 1
> 2
```



### 2.1.2 Kommentare

Kommentare werden beim ausführen des Codes ignoriert und sind hilfreich, um den Zweck von Funktionen und Variables zu beschreiben.

```python
greeting = "Hallo" # Begrüßung
print(greeting)
```



### 2.1 Datentypen in Python

#### Zahlen

In Python gibt es zwei Arten von Zahlen: ``float`` 'floating' sind Fließkommazahlen während``int`` 'integer' Ganze Zahlen wiederspiegeln

```python
integer = 1
floating = 1.23817289461892789
arithmetik = 1 + 1 - 2 / 2
```

#### Strings

Strings sind Aneinanderreihungen von Zeichen, bzw. Text

```python
string = "Hallo Welt"
```

#### Booleans

Booleans können die Werte ``False`` und ``True`` einnehmen

```python
booleanTrue     = True
booleanFalse    = False
```

#### Listen

Listen sind Aneinanderreihungen von anderen Objekten (auch anderen Listen). Strings sind (wie hier zu sehen, einfach nur Listen von Symbolen)

```python
listeInt = [1,2,3,4,5,6,7,8,9]
listeFloat = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
listeString = ["H","A","L","L","O"," ","W","E","L","T"]
string = "Hallo Welt"
```

Listen haben spezielle Eigenschaften. Diese besprechen wir später noch genauer.





















---

# 3 Kontrollfluss



## 3.1 Bedingungen und Ausdrücke

### 3.1.1 Bedingungen

Bedingungen können genutzt werden, um zwei Objekte zu vergleichen oder ein Objekt zu validieren

#### Operatoren

**== (ist gleich)** Mit ist gleich ergibt der Ausdruck ``True `` wenn beide Elemente identisch sind

**> , < (größer als, kleiner als)** Mit kleiner und größer kann man zwei Zahlen vergleichen

**!= (nicht gleich)** Das Ungleich ist die Inversion des Gleichzeichens ``==``

**not (nicht)** Inversiert den nachstehjenden Ausdruck



### 3.1.2 Verknüpfen mehrerer Ausdrücke

Mit einem 'und', bzw 'oder' können zwei (oder mehr) Ausdrücke verknüpft werden und so einen neuen Ausdruck bilden.

**and (und)** Wenn zwei Ausdrücke mit einem und verknüpft sind ergibt der Gesamt-Ausdruck nur dann ``True`` wenn beide Ausdrücke ``True`` sind

**or (oder)** Wenn zwei Ausdrücke mit einem oderverknüpft sind ergibt der Gesamt-Ausdruck dann ``True`` wenn einer der beiden Ausdrücke ``True`` ist

```python
alter = 16
mindestalter = 18
muttiZettel = True
einlass = (alter >= mindestalter) or (muttiZettel and alter >= 16)
print(einlass)

> True
```



> Um von Hand zu prüfen, ob der Ausdruck so stimmt, gehe immer von den innersten Ausdrücken nach außen. Man kann die verknüpften Ausdrücke zusammenfassen



### 3.1.3 IF - Statements

Das ``if`` Statement kann genutzt werden zu steuern, welche Teile des Programms ausgeführt werden sollen. Dazu werden Boolsche Ausdrücke benutzt.

**if** Wenn die 'IF-Bedingung' erfüllt ist wird der darunter eingerückte Code ausgeführt, ansonsten nicht:

**else** Mit dem setzen eines ``else`` kann bestimmt werden was im fall einer nicht erfüllten Bedingung passieren soll.

**elif** Ein Elif ist die Verbindung eines else mit anschließendem if

```python
if age > 18: 
    print("Einlass")
elif age > 16 and muttiZettel:
    print("Einlass bis 12")
else:
    print("Kein Einlass")
```



### 3.1.4 Schleifen

Mit Schleifen kann man Code-Abschnitte mehrfach ausführen lassen (auch mit verschiedenen Parametern).

#### FOR Schleifen

For-Schleifen führen Code bestimmt häufig aus und übergeben dabei eine Variable an diesen.

```python
liste = ["Sven","Simon","Nikolas","Tom"]

for name in liste:
    print("Hallo "+name)
    
> Hallo Sven
> Hallo Simon
...
```

#### WHILE Schleifen

For-Schleifen führen Code bestimmt häufig aus und übergeben dabei eine Variable an diesen.

```python
, language=Python]
liste = ["Sven","Simon","Nikolas","Tom"]
length = len(liste)
i = 0

while i < length:
	print(str(i)+" Hallo "+liste[i])

> 0 Hallo Sven
> 1 Hallo Simon
...
```

> Die Verwendung der while Schleife hier ist fraglich. Die for-Schleife darüber erfüllt den selben Zweck ist jedoch übersichtlicher und kürzer (!)
>
> Je nach Zweck muss man sich überlegen, welche der Schleifen besser ist



---

# 4 Listen und Objektorientierung

## 4.1 Mehr über Listen

### 4.1.1 Listen-Abschnitte erhalten

##### Einzelnes Element mit Index

```python
arr = [1,2,3]
print(arr[0])

> 0
```

##### Teil der Liste mit Start und End-Index

```python
arr = [1,2,3,4,5,6,7,8]
print(arr[1:3])

> [2, 3]
```

##### Teil der Liste mit nur Start oder End-Index

```python
arr = [1,2,3,4,5,6,7,8]
print(arr[:3])
print(arr[4:])

> [1, 2, 3]
> [5, 6, 7, 8]
```
``arr[:x]`` ist äquivalent zu ``arr[0:x]``     
``arr[x:]`` ist äquivalent zu ``arr[x:len(arr)]``

### 4.1.2 Elemente zur Liste hinzufügen und von dieser entfernen

##### Einzelnes Element zum Ende hinzufügen

```python
arr = [1,2,3]
arr.append(4)
print(arr)

> [1, 2, 3]
```
Äquivalent zu ``arr[len(arr):] = [4]``

##### Liste hinzufügen

```python
arr = [1,2,3]
arr.extend([4,5,6])
print(arr)

> [1, 2, 3, 4, 5, 6]
```
Äquivalent zu ``arr[len(arr):] = [4,5,6]``

##### Element an bestimmter Stelle einfügen

```python
arr = [1,2,3]
arr.insert(2, 4)
print(arr)

> [1, 2, 4, 3]
```
##### Gewisses Element entfernen

```python
arr = [1,2,3]
arr.remove(2)
print(arr)

> [1, 3]
```



### 4.1.3 Andere Funktionen

##### Frequenz eines Elements in der Liste 

```python
arr = [1,2,3,1]
print(arr.count(1))

> 2
```

##### Liste sortieren

```python
arr = [1,2,3,1]
arr.sort(reverse=False)
print(arr)
arr.sort(reverse=True)
print("reversed", arr)
> [1, 1, 2, 3]
> [3, 2, 1, 1]
```

##### Reihenfolge umkehren

```python
arr = [1,2,3,1]
arr.reverse()
print(arr)
> [1, 3, 2, 1]
```



## 4.2 Dictionaries und Klassen

### 4.2.1 Dictionaries

Dictionaries (auch assoziative Arrays) genannt sind nicht wie Listen mit einer Zahl indexiert, sondern mit 'Schlüsseln'.

```python
dic = {'hello': 'hallo', 'wine':'Wein'}
print(dic['hello'])

> hallo
```

Ähnlich wie Listen kann man auch durch Wörterbücher iterieren:

#### Schleifen mit Dictionaries

##### Durch 'Elemente' iterieren

```python
tel = {
    'Jens': '1234567',
    'Angela': '0275839',
    'Martin': '1948573',
    'Hans-Georg': '01873573'
}

for key, value in tel.items():
    print(key, value)
          
> Jens 1234567
> Angela 0275839
> ...
```



##### Durch 'Schlüssel' iterieren

```python
for key in tel.keys():
    print(key, tel[key])
          
> Jens 1234567
> Angela 0275839
> ...
```



##### Durch 'Werte' iterieren

```python
for value in tel.values():
    print(value)
          
> 1234567
> 0275839
> ...
```



#### Elemente hinzufügen oder ändern

Elemente können ähnlich zur Liste hinzugefügt und verändert werden:

```
dic = {'hello': 'hallo', 'wine':'Wein'}
dic['beer'] = 'Bier'
print(dic)

> {'hello': 'hallo', 'wine':'Wein', 'beer':'Bier'}
```



#### Was tun mit Dictionaries?

Elemente können ähnlich zur Liste hinzugefügt und verändert werden:

```
profile = {
	'last_name': 'Merkel',
	'first_name': 'Angela',
	'birthday': {
		'year': 1954
		'month': 06
		'day': 17
	}
}
```



### 4.2.2 Klassen

Klassen bietet eine Möglichkeit Daten und Funktionalität zu bündeln. Das Erstellen einer Klasse erstellt einen neuen Objekt-Typ. Somit können neue Instanzen dieser Objekte erstellt werden.

```python
class Profile:
    def __init__(self, last_name, first_name, birthday):
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        
profile = Profile("Merkel","Angela", date(1954,6,7))
print(profile.last_name, profile.first_name)

> Merkel  Angela
```



#### Funktionen in Klassen

Die Besonderheit bei Klassen ist, dass diese auch Funktionen haben können, die sich die Attribute (und Funktionen) der Klasse zu nutze machen können. Dazu wird als erster Parameter der Funktion das Objekt selbst ``self`` übergeben. (Beim Aufrufen der Funktion muss dieser nicht angegeben werden)

```python
class Profile:
    def __init__(self, last_name, first_name, birthday):
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        
	def name(self):
    	return self.first_name+" "+self.last_name

profile = Profile("Merkel","Angela", date(1954,6,7))
print(profile.name())

> Angela Merkel
```



##### Klassen in einem anderen Kontext

Klassen können auch genutzt werden um eigene Module zu erstellen, die mit Parametern initialisiert werden (Zum Beispiel einem Passwort oder einer Bedingung):

```python
class Filter:
    def __init__(self, filterList, isWhiteList = True):
        self.filterList = filterList
        self.isWhiteList = isWhiteList
        
    def filter(self, text):
        wasFiltered = False
        text = text.casefold()
        for filterWord in self.filterList:
            if filterWord in text:
                wasFiltered = True
                continue
        
        if self.isWhiteList:
            return wasFiltered
       	else:
            return not wasFiltered
        
        
f1 = Filter(['testwort'])
f2 = Filter(['testwort'], isWhiteList = False)
text = "Das Testwort"
print( f1.filter(text) )
print( f2.filter(text) )

> True
> False
```



## 4.3 Objektorientierung

Unter Objektorientierung versteht man eine Sichtweise auf komplexe Systeme, bei der ein System durch das Zusammenspiel kooperierender Objekte beschrieben wird.

##### Alles sind Objekte

Ein (sehr komplexes) Beispiel:

```python
class Car:
    def __init__(self, manufacturer, model, paint, engine):
        self.manufacturer = manufacturer
        self.model = model
        self.paint = paint
        self.engine = engine

    def specs(self):
        makerAndModel = self.maker+" "+self.model
        return makerAndModel+" | "+self.engine.specs()+" | "+self.paint.specs()
        
        
class Paint:
    def __init__(self, code, description):
        self.code = code
        self.description = description 

    def specs(self):
        return self.description+"  ("+self.code+")"


class Engine:
    def __init__(self, horsepower, cylinders):
        self.horsepower = horsepower
        self.cylinders = cylinders

    def specs(self):
        return str(self.horsepower)+" PS (V"+str(self.cylinders)+")"



car = Car(
    manufacturer = 'Ford',
    model = 'Mustang GT',
    paint = Paint(code='ABCDEFG', description='red'),
    engine = Engine(horsepower=350, cylinders=8)
)

print(car.specs())

> Ford Mustang GT     350 PS (V8)     red  (ABCDEFG)
```



---

# 5 Fehlermeldungen und 'Debugging'

# 5.1 Fehlermeldungen und Ausnahmen
## 5.1.1 Syntaxfehler
Obwohl Python einen relativ laschen Umgang mit korrektem Syntax hat, müssen gewisse Regeln befolgt werden. Ein gutes Beispiel dafür ist das Einrücken von Code-Abschnitten in Schleifen, IF-Bedingungen und Funktionen:
```python
while True print('Hello World')
>  File "<stdin>", line 1
>    while True print('Hello world')
>               ^
>SyntaxError: invalid syntax
```
Python wiederholt die problematische Zeile und zeigt einen kleinen Pfeil unter der Stelle die den Fehler erzeugt hat. In diesem Beispiel fehlt der Doppelpunkt ':' nach dem 'while True'-Statement. Aus der Fehlermeldung kann man auch den Dateinamen und die Zeile herauslesen.

## 5.1.2 Ausnahmen ('Exceptions')
Selbst wenn eine Aussage syntaktisch korrekt ist, kann diese einen Fehler erzeugen, wenn der Code ausgeführt wird.
```python
print( 10 * (1/0) )

>Traceback (most recent call last):
>  File "<stdin>", line 1, in <module>
>ZeroDivisionError: division by zero
```
```python
print( 4 + spam*3 )

>Traceback (most recent call last):
>  File "<stdin>", line 1, in <module>
>NameError: name 'spam' is not defined
```

```python
print( '2' + 2 )

>Traceback (most recent call last):
>  File "<stdin>", line 1, in <module>
>TypeError: Can't convert 'int' object to str implicitly
```
Die letzte Zeile der Fehlermeldung gibt die Art des Fehlers und eine Beschreibung an.
'ZeroDivisionError' zum Beispiel gibt an, dass versucht wurde eine Zahl durch '0' zu teilen, während 'TypeError' angibt, dass ein Objekt den falschen Typ aufweist (hier: String statt Integer)

## 5.1.3 Ausnahmenbehandlung
Um Abbrüche in der Ausführung zu vermeiden, können Aussagen in ein 'try'-'except' gepackt werden. Falls es zu einer 'Exception' kommt wird der Code im 'except' ausgeführt. 
```python
gspaces=false, language=Python]
grades = ["1","Z","3","0"]
for grade in grades:
    try:
        integer = int(grade)
        print(10 / integer)
    except ValueError:
        print("Ein ValueError ist aufgetreten")
        
> 1
> Ein ValueError ist aufgetreten
> 3
>Traceback (most recent call last):
>  File "<stdin>", line 5, in <module>
>ZeroDivisionError: division by zero
```

Beim obigen Beispiel wird nur ein Fehler der art 'ValueError' behandelt. Aus diesem Grund bricht das Programm trotzdem mit einem 'ZeroDivisionError' ab. Dieses Problem könnten wir auf zwei Arten lösen:
1. **Zusätzliches 'except':**
```python
try:
    integer = int(grade)
    print(10 / int)
except ValueError:
    print("Ein ValueError ist aufgetreten")
except ZeroDivisionError:
    print("Ein ZeroDivisionError ist aufgetreten")
```
2. **'except' ohne genau Angabe des Typs:**
```python
try:
    integer = int(grade)
    print(10 / int)
except:
    print("Ein Fehler ist aufgetreten")
```
Welche der beiden Lösungen man verwenden sollte hängt alleinig von der Situation ab. Wenn das Programm zum Beispiel jegliche fehlerhaften Werte überspringen soll eignet sich Variante 2. Wenn es jedoch zum Beispiel einen 'ZeroDivisionError' behandelm soll indem es einfach $0$ ausgibt, dann sollte man Variante 1 verwenden.

> **Tipp**
>
> 'try' und 'except' verhalten sich ähnlich wie ein IF-ELIF-ELSE
```python
try:
    # raise erhebt einen Error
    raise ZeroDivisionError 
except ZeroDivisionError: # if error = ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError: # elif error == ValueError:
    print("ValueError")
except AttributeError: # elif error == AttributeError:
    print("AttributeError")
except: # else:
    print("Anderer Fehler")
```



## 5.1.4 Fehler erheben

```python
raise NameError("das ist ein Fehler")
> Traceback (most recent call last):
>  File "<stdin>", line 1, in <module>
> NameError: HiThere
```



# 5.2 Fehler 'debuggen' und Vermeidung

Jeder macht Fehler. Das wichtige ist nur, dass man weiß, wie man diese korrigiert!



## 5.2.1 Was ist "Debugging"?

> 1947 hatte während der Arbeiten am [Mark II](https://de.wikipedia.org/w/index.php?title=Mark_II_(Computer)&action=edit&redlink=1) eine Motte für den Ausfall eines Relais dieses Computers gesorgt. Das Team von Grace Hoppers fand die Motte und klebte sie in das Logbuch zusammen mit dem Satz „First actual case of bug being found.“

## 5.2.2 Typische Fehler und wie man sie "debugged"

#### Programm produziert eine ausnahme ("Exception")}
In diesem Fall packe ich den Teil, der eine "Exception" produziert in ein "try-except" und lasse mir mögliche Fehlerquellen ausgeben: 
```python
def doSomething(param1, param2):
    result = param1 / param2
params = [0,1,2,3,4]
for param in params:
    param1 = param
    param2 = param - 1
    doSomething(param1, param2)
    
>Traceback (most recent call last):
>  File "<stdin>", line 2, in <module>
>ZeroDivisionError: division by zero
```
Also: die Aussage 'result = param1 / param2' produziert einen 'ZeroDivisionError', bedeutet, dass param2 '0' ist. Ich packe nun diese Zeile in ein "try - except" und lasse mir im Falle einer Exception die parameter ausgeben.

```python
def doSomething(param1, param2):
    try:
        result = param1 / param2
    except:
        print("except", param1, param2)
params = [0,1,2,3,4]
for param in params:
    param1 = param
    param2 = param - 1
    doSomething(param1, param2)
    
> except  1  0
```
Aha! Wenn $param1 = 1$, also wenn $param = 1$ (wegen $param1 = param$), dann ist param2 eine $0$. Und das weil $param2 = param - 0$. 
Fehler gefunden!

#### Das Programm läuft aber das Ergbenis ist (manchmal) falsch.

---

# 6 Funktionen & Module

## 6.1 Funktionen

Funktionen können an einer stelle des Codes "definiert" und an zu späteren Zeitpunkten aufgerufen werden.

### 6.1.1 Funktionen definieren

```python
def greeting():
print("Hallo Welt")

greeting()
greeting()

> Hallo Welt
> Hallo Welt
```

Dies lohnt sich natürlich vor Allem bei längeren Abschnitten, die im Programm öfter gebraucht werden.

#### Parameter

Parameter können an Funktionen übergeben und von diesen auch zurückgegeben werden.

```python
def makeGreeting(name):
greeting = "Hallo "+name+". Wie geht's?"
return greeting 

greeting = makeGreeting("Sven")
print(greeting)

> Hallo Sven. Wie geht's?
```



### 6.1.2 Warum benutzt man Funktionen?

Funktionen sind ...

- **platzsparend**: Funktionen können einmal geschrieben und mehrfach im Code verwendet werden
- **übersichtlich**: Funktionen machen das Programm übersichtlicher, da man Abschnitte so leicht zusammenfassen kann.
- **gut für die Nerven**: wenn ein Abschnitt, den man mehrfach verwendet einen Fehler hat muss man im Falle einer Funktion nur einmal korrigieren.

```python
grades = [3.75, ... , 2.5]

# Ohne Funktionen (6 Zeilen):
summe = 0
length = 0
for grade in grades:
summe += grade
length += 1
average = summe / length
print(average)

# Mit Funktionen (1 Zeile):
average = sum(grades) / len(grades)
```



## 6.2 Module
Module sind Erweiterungen mit Funktionen und Klassen, die einem das Leben einfacher machen

### 6.2.1 Module importieren
Module müssen importiert werden, um deren Benutzung zu erlauben. Hierbei kann man entweder ein ganzes Modul importieren oder auch nur einzelne Klassen oder Funktionen dieses

##### Gesamtes Modul

```python
import math
print( math.sqrt( 16 ) )

> 4
```



##### Bestimmte Funktion(en)

Falls man nur eine oder zwei Funktionen benötigt kann man auch nur bestimmte Teile des Moduls importieren (so dass nicht alle Teile geladen werden müssen)

```python
from math import sqrt, ceil

print( sqrt( 16 ) )
print( ceil( 2.341 ) )

> 4
> 3
```



##### Umbenennung

Um Namenskonflikte zu vermeiden können Imports unter einem eigens definierten Namen importiert werden

```python
from math import sqrt as root
sqrt = 0 # Kein Konflikt mit math.sqrt
print( root( 16 ) )

> 4
```



### 6.2.2 Die Python Standard Library

Die Standardbibliothek ist eine der größten Stärken von Python, wodurch es sich für viele Anwendungen eignet. Der überwiegende Teil davon ist plattformunabhängig, so dass auch größere Python-Programme oft auf Unix, Windows, macOS und anderen Plattformen ohne Änderung laufen. \\
Teile dieser Bibliothek sind unter anderem auch das 'print' statement und funktionen, wie 'len()' und 'sum()'



### 6.2.3 Third Party Module

Die Standardbibliothek kann mit 'Packages' erweitert werden. Download und Installation des Packages und seiner Abhängigkeiten dient das Paketverwaltungsprogram PIP. Dazu muss lediglich der name des Packages genannt werden.

```bash
> pip install requests

Collecting pylib3
  Downloading https://files.pythonhosted.org/example
Collecting termcolor==1.1.0 (from pylib3)
  Downloading https://files.pythonhosted.org/example
Installing collected packages: termcolor, pylib3
  Running setup.py install for termcolor ... done
  Running setup.py install for pylib3 ... done
Successfully installed pylib3-0.0.3 termcolor-1.1.0
```

Im Terminal kann mit ``pip install <packagename>`` das Modul heruntergeladen und installiert werden. Nun kann es von überall importiert werden.

> **Tipp**
>
> [PyPi](https://pypi.org/) bietet eine große Auswahl an Python Packages. Das beste Verzeichnis dafür bleibt jedoch nach wie vor [Google](https://google.de)



### 6.2.4 Eigene Module

Es können auch Funktionen aus eigenen Dateien importiert werden. Beispielsweise kann sich die Funktion ``doSomething()`` in Datei ``MyModule.py`` befinden und in ``MyApplication.py`` importiert werden.

```python
# MyModule.py
def doSomething():
	print("Dew it!")
```

```python
# MyApplication.py
from MyModule import doSomething as dewIt
dewIt()

> Dew It!
```



> **Achtung**
>
> Befinden sich Fehler in ``MyModule.py``87878787878787878799 kann auch ``MyApplication.py``nicht ausgeführt werden. 



---

# 7 Dokumentation & Dateien

## 7.1 Dokumentation 



## 7.2 Dateien

### 7.2.1 Lesen

### 7.2.2 Schreiben

### 7.2.3 Exkurs: Dateiformate



## 7.2 JSON

Die JavaScript Object Notation(JSON)  ist ein kompaktes Datenformat in einer einfach lesbaren Textform. Es ist Vergleichbar mit Dictionaries in Python.





---



---

# 9 Emails



## 9.1 Sending Emails

#### 9.1.1 Templates

"Template Strings" enthalten Platzhalter, die mit anderen Strings ausgetauscht werden können. ``${identifier}``

> Hallo ${RECEIVER_NAME}, 
> 
> Dies ist eine Test-Nachricht.
> Das ist deine Email: ${RECEIVER_MAIL}
> 
> Liebe Grüße,
> ${SENDER_NAME}

Wir können einen String in ein Template verwandeln, indem wir mit ihm eine Entität der ``Template``-Klasse initialisieren

```python
from string import Template

string = """
Hallo ${RECIPIENT_NAME}, 

Dies ist eine Test-Nachricht.
Das ist deine Email: ${RECIPIENT_MAIL}

Liebe Grüße,
${SENDER_NAME}
"""

template = Template(string)
```



#### 9.1.2 SMTP

SMTP steht für Simple Mail Transfer Protocol und wird von Mail-Servern zum Senden von Emails genutzt. Das Package ``smtplib`` implementiert dieses Protokoll für Python

```python
import smtplib
# set up the SMTP server
s = smtplib.SMTP(host='your_host_address_here', port=your_port_here)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)
```



#### 9.1.3 Das Email Package

Das Email Package kann zum erstellen von Mails verwendet werden. (Um den gängigen Standards für Mails gerecht zu werden)

```python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


msg = MIMEMultipart()
# META-Daten der Email setzen
msg['From'] = SENDER_ADDRESS
msg['To'] = RECIPIENT_ADRESS
msg['Subject']="This is TEST"

msg.attach(MIMEText(MESSAGE, 'plain')) # Den Text hinzufügen 

    
```



#### 9.1.4 Mails versenden

```
import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Contact:
    def __init__(self, last, first, adress):
        self.last_name = last
        self.first_name = first
        self.email = adress


def connectServer(host, port, adress, password):
    """Returns a Server connection.

    Arguments:
        host {str} -- hostname of the server
        port {int} -- port for the server
        adress {str} -- email adress of the account
        password {str} -- password of the account

    Returns:
        smtplib.SMTP -- SMTP-Server-Client
    """    
    s = smtplib.SMTP(host=host, port=port)
    s.starttls()
    s.connect(host=host, port=port)
    s.login(adress, password)
    
    return s

def loadTemplate(filename):
    """Loads a Template file from Disk
    
    Arguments:
        filename {str} -- path of the file
    
    Returns:
        Template -- String Template object
    """    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def getContacts(filename):
    """retrieves the contacts from a CSV file
    
    Arguments:
        filename {str} -- path of the file

    Returns:
        list[Contact] -- list of Contact entities
    """    
    contacts = []
    with open(filename, mode='r') as f:
        for contact in f:
            contacts.append( Contact(contact[0],contact[1],contact[2]) )
    return contacts

def makeMessage(sender, recipient, subject, msg_body, msg_type):
    """Generates and returns a MIMEMultipart Message
    
    Arguments:
        sender {str} -- Sender's Email
        recipient {str} -- Recipient's Email
        subject {str} -- Email Subject
        msg_body {str} -- Email body
        msg_type {str} -- The type of the body (e.g. 'plain' or 'html')
    
    Returns:
        MIMEMultipart -- MIMEMultipart Message
    """    
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(msg_body, msg_type))
    return msg


# Server Config
cfg = {
    'host': 'smtp.ionos.de',
    'port': 587,
    'user': 'test@dev.noahkamara.com',
    'pass': '988-xyQ-6Vp-NEp'
}


# Initialize Server-Client
server = connectServer(cfg['host'], cfg['port'], cfg['user'], cfg['pass'])

# Retrieve Contacts
# contacts = getContacts('contacts.csv')
contacts = [
    Contact('Kamara','Test01','test01@login.noahkamara.com'),
    Contact('Kamara','Test02','test02@login.noahkamara.com'),
    Contact('Kamara','Test03','test03@login.noahkamara.com'),
    Contact('Kamara','Test04','test04@login.noahkamara.com')
]

# For each contact
for contact in contacts:
    # Load template
    template = loadTemplate('live/template')
    # substitute placehoders in template
    msg_body = template.substitute(RECIPIENT_NAME=contact.first_name, RECIPIENT_MAIL=contact.email, SENDER_NAME='Python Script')
    msg_type = 'plain' # Message Type
    # make a MIMEMUltipart message
    msg = makeMessage(cfg['user'], contact.email, f"Hallo {contact.first_name}", msg_body, msg_type)
    # Send Message
    server.send_message(msg)

# Close server Connection
server.quit()
```



---



---

# 2 Erste Schritte



## 2.1 Die Basics



### 2.1.1 Das Print Statement

Mit dem Print Statement kann das Programm in die Konsole ausgeben

```python
print("Hello World")
print(123)

> Hello World
> 123
```



### 2.1.1 Variablen

Um Werte, temporär im Speicher zu halten definiert man 'Variablen'. Diese müssen deklariert und können danach beliebig verändert werden. Variablen verhalten sich als Objekt des Typs den sie beinhalten

```python
var = "Hallo Welt!"
print(var)

> Hallo Welt!
```

```
num = 1
print(var)
num = num + 1
print(var)

> 1
> 2
```



### 2.1.2 Kommentare

Kommentare werden beim ausführen des Codes ignoriert und sind hilfreich, um den Zweck von Funktionen und Variables zu beschreiben.

```python
greeting = "Hallo" # Begrüßung
print(greeting)
```



### 2.1 Datentypen in Python

#### Zahlen

In Python gibt es zwei Arten von Zahlen: ``float`` 'floating' sind Fließkommazahlen während``int`` 'integer' Ganze Zahlen wiederspiegeln

```python
integer = 1
floating = 1.23817289461892789
arithmetik = 1 + 1 - 2 / 2
```

#### Strings

Strings sind Aneinanderreihungen von Zeichen, bzw. Text

```python
string = "Hallo Welt"
```

#### Booleans

Booleans können die Werte ``False`` und ``True`` einnehmen

```python
booleanTrue     = True
booleanFalse    = False
```

#### Listen

Listen sind Aneinanderreihungen von anderen Objekten (auch anderen Listen). Strings sind (wie hier zu sehen, einfach nur Listen von Symbolen)

```python
listeInt = [1,2,3,4,5,6,7,8,9]
listeFloat = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
listeString = ["H","A","L","L","O"," ","W","E","L","T"]
string = "Hallo Welt"
```

Listen haben spezielle Eigenschaften. Diese besprechen wir später noch genauer.





















---

# 3 Kontrollfluss



## 3.1 Bedingungen und Ausdrücke

### 3.1.1 Bedingungen

Bedingungen können genutzt werden, um zwei Objekte zu vergleichen oder ein Objekt zu validieren

#### Operatoren

**== (ist gleich)** Mit ist gleich ergibt der Ausdruck ``True `` wenn beide Elemente identisch sind

**> , < (größer als, kleiner als)** Mit kleiner und größer kann man zwei Zahlen vergleichen

**!= (nicht gleich)** Das Ungleich ist die Inversion des Gleichzeichens ``==``

**not (nicht)** Inversiert den nachstehjenden Ausdruck



### 3.1.2 Verknüpfen mehrerer Ausdrücke

Mit einem 'und', bzw 'oder' können zwei (oder mehr) Ausdrücke verknüpft werden und so einen neuen Ausdruck bilden.

**and (und)** Wenn zwei Ausdrücke mit einem und verknüpft sind ergibt der Gesamt-Ausdruck nur dann ``True`` wenn beide Ausdrücke ``True`` sind

**or (oder)** Wenn zwei Ausdrücke mit einem oderverknüpft sind ergibt der Gesamt-Ausdruck dann ``True`` wenn einer der beiden Ausdrücke ``True`` ist

```python
alter = 16
mindestalter = 18
muttiZettel = True
einlass = (alter >= mindestalter) or (muttiZettel and alter >= 16)
print(einlass)

> True
```



> Um von Hand zu prüfen, ob der Ausdruck so stimmt, gehe immer von den innersten Ausdrücken nach außen. Man kann die verknüpften Ausdrücke zusammenfassen



### 3.1.3 IF - Statements

Das ``if`` Statement kann genutzt werden zu steuern, welche Teile des Programms ausgeführt werden sollen. Dazu werden Boolsche Ausdrücke benutzt.

**if** Wenn die 'IF-Bedingung' erfüllt ist wird der darunter eingerückte Code ausgeführt, ansonsten nicht:

**else** Mit dem setzen eines ``else`` kann bestimmt werden was im fall einer nicht erfüllten Bedingung passieren soll.

**elif** Ein Elif ist die Verbindung eines else mit anschließendem if

```python
if age > 18: 
    print("Einlass")
elif age > 16 and muttiZettel:
    print("Einlass bis 12")
else:
    print("Kein Einlass")
```



### 3.1.4 Schleifen

Mit Schleifen kann man Code-Abschnitte mehrfach ausführen lassen (auch mit verschiedenen Parametern).

#### FOR Schleifen

For-Schleifen führen Code bestimmt häufig aus und übergeben dabei eine Variable an diesen.

```python
liste = ["Sven","Simon","Nikolas","Tom"]

for name in liste:
    print("Hallo "+name)
    
> Hallo Sven
> Hallo Simon
...
```

#### WHILE Schleifen

For-Schleifen führen Code bestimmt häufig aus und übergeben dabei eine Variable an diesen.

```python
, language=Python]
liste = ["Sven","Simon","Nikolas","Tom"]
length = len(liste)
i = 0

while i < length:
	print(str(i)+" Hallo "+liste[i])

> 0 Hallo Sven
> 1 Hallo Simon
...
```

> Die Verwendung der while Schleife hier ist fraglich. Die for-Schleife darüber erfüllt den selben Zweck ist jedoch übersichtlicher und kürzer (!)
>
> Je nach Zweck muss man sich überlegen, welche der Schleifen besser ist



---

# 4 Listen und Objektorientierung

## 4.1 Mehr über Listen

### 4.1.1 Listen-Abschnitte erhalten

##### Einzelnes Element mit Index

```python
arr = [1,2,3]
print(arr[0])

> 0
```

##### Teil der Liste mit Start und End-Index

```python
arr = [1,2,3,4,5,6,7,8]
print(arr[1:3])

> [2, 3]
```

##### Teil der Liste mit nur Start oder End-Index

```python
arr = [1,2,3,4,5,6,7,8]
print(arr[:3])
print(arr[4:])

> [1, 2, 3]
> [5, 6, 7, 8]
```
``arr[:x]`` ist äquivalent zu ``arr[0:x]``     
``arr[x:]`` ist äquivalent zu ``arr[x:len(arr)]``

### 4.1.2 Elemente zur Liste hinzufügen und von dieser entfernen

##### Einzelnes Element zum Ende hinzufügen

```python
arr = [1,2,3]
arr.append(4)
print(arr)

> [1, 2, 3]
```
Äquivalent zu ``arr[len(arr):] = [4]``

##### Liste hinzufügen

```python
arr = [1,2,3]
arr.extend([4,5,6])
print(arr)

> [1, 2, 3, 4, 5, 6]
```
Äquivalent zu ``arr[len(arr):] = [4,5,6]``

##### Element an bestimmter Stelle einfügen

```python
arr = [1,2,3]
arr.insert(2, 4)
print(arr)

> [1, 2, 4, 3]
```
##### Gewisses Element entfernen

```python
arr = [1,2,3]
arr.remove(2)
print(arr)

> [1, 3]
```



### 4.1.3 Andere Funktionen

##### Frequenz eines Elements in der Liste 

```python
arr = [1,2,3,1]
print(arr.count(1))

> 2
```

##### Liste sortieren

```python
arr = [1,2,3,1]
arr.sort(reverse=False)
print(arr)
arr.sort(reverse=True)
print("reversed", arr)
> [1, 1, 2, 3]
> [3, 2, 1, 1]
```

##### Reihenfolge umkehren

```python
arr = [1,2,3,1]
arr.reverse()
print(arr)
> [1, 3, 2, 1]
```



## 4.2 Dictionaries und Klassen

### 4.2.1 Dictionaries

Dictionaries (auch assoziative Arrays) genannt sind nicht wie Listen mit einer Zahl indexiert, sondern mit 'Schlüsseln'.

```python
dic = {'hello': 'hallo', 'wine':'Wein'}
print(dic['hello'])

> hallo
```

Ähnlich wie Listen kann man auch durch Wörterbücher iterieren:

#### Schleifen mit Dictionaries

##### Durch 'Elemente' iterieren

```python
tel = {
    'Jens': '1234567',
    'Angela': '0275839',
    'Martin': '1948573',
    'Hans-Georg': '01873573'
}

for key, value in tel.items():
    print(key, value)
          
> Jens 1234567
> Angela 0275839
> ...
```



##### Durch 'Schlüssel' iterieren

```python
for key in tel.keys():
    print(key, tel[key])
          
> Jens 1234567
> Angela 0275839
> ...
```



##### Durch 'Werte' iterieren

```python
for value in tel.values():
    print(value)
          
> 1234567
> 0275839
> ...
```



#### Elemente hinzufügen oder ändern

Elemente können ähnlich zur Liste hinzugefügt und verändert werden:

```
dic = {'hello': 'hallo', 'wine':'Wein'}
dic['beer'] = 'Bier'
print(dic)

> {'hello': 'hallo', 'wine':'Wein', 'beer':'Bier'}
```



#### Was tun mit Dictionaries?

Elemente können ähnlich zur Liste hinzugefügt und verändert werden:

```
profile = {
	'last_name': 'Merkel',
	'first_name': 'Angela',
	'birthday': {
		'year': 1954
		'month': 06
		'day': 17
	}
}
```



### 4.2.2 Klassen

Klassen bietet eine Möglichkeit Daten und Funktionalität zu bündeln. Das Erstellen einer Klasse erstellt einen neuen Objekt-Typ. Somit können neue Instanzen dieser Objekte erstellt werden.

```python
class Profile:
    def __init__(self, last_name, first_name, birthday):
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        
profile = Profile("Merkel","Angela", date(1954,6,7))
print(profile.last_name, profile.first_name)

> Merkel  Angela
```



#### Funktionen in Klassen

Die Besonderheit bei Klassen ist, dass diese auch Funktionen haben können, die sich die Attribute (und Funktionen) der Klasse zu nutze machen können. Dazu wird als erster Parameter der Funktion das Objekt selbst ``self`` übergeben. (Beim Aufrufen der Funktion muss dieser nicht angegeben werden)

```python
class Profile:
    def __init__(self, last_name, first_name, birthday):
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        
	def name(self):
    	return self.first_name+" "+self.last_name

profile = Profile("Merkel","Angela", date(1954,6,7))
print(profile.name())

> Angela Merkel
```



##### Klassen in einem anderen Kontext

Klassen können auch genutzt werden um eigene Module zu erstellen, die mit Parametern initialisiert werden (Zum Beispiel einem Passwort oder einer Bedingung):

```python
class Filter:
    def __init__(self, filterList, isWhiteList = True):
        self.filterList = filterList
        self.isWhiteList = isWhiteList
        
    def filter(self, text):
        wasFiltered = False
        text = text.casefold()
        for filterWord in self.filterList:
            if filterWord in text:
                wasFiltered = True
                continue
        
        if self.isWhiteList:
            return wasFiltered
       	else:
            return not wasFiltered
        
        
f1 = Filter(['testwort'])
f2 = Filter(['testwort'], isWhiteList = False)
text = "Das Testwort"
print( f1.filter(text) )
print( f2.filter(text) )

> True
> False
```



## 4.3 Objektorientierung

Unter Objektorientierung versteht man eine Sichtweise auf komplexe Systeme, bei der ein System durch das Zusammenspiel kooperierender Objekte beschrieben wird.

##### Alles sind Objekte

Ein (sehr komplexes) Beispiel:

```python
class Car:
    def __init__(self, manufacturer, model, paint, engine):
        self.manufacturer = manufacturer
        self.model = model
        self.paint = paint
        self.engine = engine

    def specs(self):
        makerAndModel = self.maker+" "+self.model
        return makerAndModel+" | "+self.engine.specs()+" | "+self.paint.specs()
        
        
class Paint:
    def __init__(self, code, description):
        self.code = code
        self.description = description 

    def specs(self):
        return self.description+"  ("+self.code+")"


class Engine:
    def __init__(self, horsepower, cylinders):
        self.horsepower = horsepower
        self.cylinders = cylinders

    def specs(self):
        return str(self.horsepower)+" PS (V"+str(self.cylinders)+")"



car = Car(
    manufacturer = 'Ford',
    model = 'Mustang GT',
    paint = Paint(code='ABCDEFG', description='red'),
    engine = Engine(horsepower=350, cylinders=8)
)

print(car.specs())

> Ford Mustang GT     350 PS (V8)     red  (ABCDEFG)
```



---

# 5 Fehlermeldungen und 'Debugging'

# 5.1 Fehlermeldungen und Ausnahmen
## 5.1.1 Syntaxfehler
Obwohl Python einen relativ laschen Umgang mit korrektem Syntax hat, müssen gewisse Regeln befolgt werden. Ein gutes Beispiel dafür ist das Einrücken von Code-Abschnitten in Schleifen, IF-Bedingungen und Funktionen:
```python
while True print('Hello World')
>  File "<stdin>", line 1
>    while True print('Hello world')
>               ^
>SyntaxError: invalid syntax
```
Python wiederholt die problematische Zeile und zeigt einen kleinen Pfeil unter der Stelle die den Fehler erzeugt hat. In diesem Beispiel fehlt der Doppelpunkt ':' nach dem 'while True'-Statement. Aus der Fehlermeldung kann man auch den Dateinamen und die Zeile herauslesen.

## 5.1.2 Ausnahmen ('Exceptions')
Selbst wenn eine Aussage syntaktisch korrekt ist, kann diese einen Fehler erzeugen, wenn der Code ausgeführt wird.
```python
print( 10 * (1/0) )

>Traceback (most recent call last):
>  File "<stdin>", line 1, in <module>
>ZeroDivisionError: division by zero
```
```python
print( 4 + spam*3 )

>Traceback (most recent call last):
>  File "<stdin>", line 1, in <module>
>NameError: name 'spam' is not defined
```

```python
print( '2' + 2 )

>Traceback (most recent call last):
>  File "<stdin>", line 1, in <module>
>TypeError: Can't convert 'int' object to str implicitly
```
Die letzte Zeile der Fehlermeldung gibt die Art des Fehlers und eine Beschreibung an.
'ZeroDivisionError' zum Beispiel gibt an, dass versucht wurde eine Zahl durch '0' zu teilen, während 'TypeError' angibt, dass ein Objekt den falschen Typ aufweist (hier: String statt Integer)

## 5.1.3 Ausnahmenbehandlung
Um Abbrüche in der Ausführung zu vermeiden, können Aussagen in ein 'try'-'except' gepackt werden. Falls es zu einer 'Exception' kommt wird der Code im 'except' ausgeführt. 
```python
gspaces=false, language=Python]
grades = ["1","Z","3","0"]
for grade in grades:
    try:
        integer = int(grade)
        print(10 / integer)
    except ValueError:
        print("Ein ValueError ist aufgetreten")
        
> 1
> Ein ValueError ist aufgetreten
> 3
>Traceback (most recent call last):
>  File "<stdin>", line 5, in <module>
>ZeroDivisionError: division by zero
```

Beim obigen Beispiel wird nur ein Fehler der art 'ValueError' behandelt. Aus diesem Grund bricht das Programm trotzdem mit einem 'ZeroDivisionError' ab. Dieses Problem könnten wir auf zwei Arten lösen:
1. **Zusätzliches 'except':**
```python
try:
    integer = int(grade)
    print(10 / int)
except ValueError:
    print("Ein ValueError ist aufgetreten")
except ZeroDivisionError:
    print("Ein ZeroDivisionError ist aufgetreten")
```
2. **'except' ohne genau Angabe des Typs:**
```python
try:
    integer = int(grade)
    print(10 / int)
except:
    print("Ein Fehler ist aufgetreten")
```
Welche der beiden Lösungen man verwenden sollte hängt alleinig von der Situation ab. Wenn das Programm zum Beispiel jegliche fehlerhaften Werte überspringen soll eignet sich Variante 2. Wenn es jedoch zum Beispiel einen 'ZeroDivisionError' behandelm soll indem es einfach $0$ ausgibt, dann sollte man Variante 1 verwenden.

> **Tipp**
>
> 'try' und 'except' verhalten sich ähnlich wie ein IF-ELIF-ELSE
```python
try:
    # raise erhebt einen Error
    raise ZeroDivisionError 
except ZeroDivisionError: # if error = ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError: # elif error == ValueError:
    print("ValueError")
except AttributeError: # elif error == AttributeError:
    print("AttributeError")
except: # else:
    print("Anderer Fehler")
```



## 5.1.4 Fehler erheben

```python
raise NameError("das ist ein Fehler")
> Traceback (most recent call last):
>  File "<stdin>", line 1, in <module>
> NameError: HiThere
```



# 5.2 Fehler 'debuggen' und Vermeidung

Jeder macht Fehler. Das wichtige ist nur, dass man weiß, wie man diese korrigiert!



## 5.2.1 Was ist "Debugging"?

> 1947 hatte während der Arbeiten am [Mark II](https://de.wikipedia.org/w/index.php?title=Mark_II_(Computer)&action=edit&redlink=1) eine Motte für den Ausfall eines Relais dieses Computers gesorgt. Das Team von Grace Hoppers fand die Motte und klebte sie in das Logbuch zusammen mit dem Satz „First actual case of bug being found.“

## 5.2.2 Typische Fehler und wie man sie "debugged"

#### Programm produziert eine ausnahme ("Exception")}
In diesem Fall packe ich den Teil, der eine "Exception" produziert in ein "try-except" und lasse mir mögliche Fehlerquellen ausgeben: 
```python
def doSomething(param1, param2):
    result = param1 / param2
params = [0,1,2,3,4]
for param in params:
    param1 = param
    param2 = param - 1
    doSomething(param1, param2)
    
>Traceback (most recent call last):
>  File "<stdin>", line 2, in <module>
>ZeroDivisionError: division by zero
```
Also: die Aussage 'result = param1 / param2' produziert einen 'ZeroDivisionError', bedeutet, dass param2 '0' ist. Ich packe nun diese Zeile in ein "try - except" und lasse mir im Falle einer Exception die parameter ausgeben.

```python
def doSomething(param1, param2):
    try:
        result = param1 / param2
    except:
        print("except", param1, param2)
params = [0,1,2,3,4]
for param in params:
    param1 = param
    param2 = param - 1
    doSomething(param1, param2)
    
> except  1  0
```
Aha! Wenn $param1 = 1$, also wenn $param = 1$ (wegen $param1 = param$), dann ist param2 eine $0$. Und das weil $param2 = param - 0$. 
Fehler gefunden!

#### Das Programm läuft aber das Ergbenis ist (manchmal) falsch.

---

# 6 Funktionen & Module

## 6.1 Funktionen

Funktionen können an einer stelle des Codes "definiert" und an zu späteren Zeitpunkten aufgerufen werden.

### 6.1.1 Funktionen definieren

```python
def greeting():
print("Hallo Welt")

greeting()
greeting()

> Hallo Welt
> Hallo Welt
```

Dies lohnt sich natürlich vor Allem bei längeren Abschnitten, die im Programm öfter gebraucht werden.

#### Parameter

Parameter können an Funktionen übergeben und von diesen auch zurückgegeben werden.

```python
def makeGreeting(name):
greeting = "Hallo "+name+". Wie geht's?"
return greeting 

greeting = makeGreeting("Sven")
print(greeting)

> Hallo Sven. Wie geht's?
```



### 6.1.2 Warum benutzt man Funktionen?

Funktionen sind ...

- **platzsparend**: Funktionen können einmal geschrieben und mehrfach im Code verwendet werden
- **übersichtlich**: Funktionen machen das Programm übersichtlicher, da man Abschnitte so leicht zusammenfassen kann.
- **gut für die Nerven**: wenn ein Abschnitt, den man mehrfach verwendet einen Fehler hat muss man im Falle einer Funktion nur einmal korrigieren.

```python
grades = [3.75, ... , 2.5]

# Ohne Funktionen (6 Zeilen):
summe = 0
length = 0
for grade in grades:
summe += grade
length += 1
average = summe / length
print(average)

# Mit Funktionen (1 Zeile):
average = sum(grades) / len(grades)
```



## 6.2 Module
Module sind Erweiterungen mit Funktionen und Klassen, die einem das Leben einfacher machen

### 6.2.1 Module importieren
Module müssen importiert werden, um deren Benutzung zu erlauben. Hierbei kann man entweder ein ganzes Modul importieren oder auch nur einzelne Klassen oder Funktionen dieses

##### Gesamtes Modul

```python
import math
print( math.sqrt( 16 ) )

> 4
```



##### Bestimmte Funktion(en)

Falls man nur eine oder zwei Funktionen benötigt kann man auch nur bestimmte Teile des Moduls importieren (so dass nicht alle Teile geladen werden müssen)

```python
from math import sqrt, ceil

print( sqrt( 16 ) )
print( ceil( 2.341 ) )

> 4
> 3
```



##### Umbenennung

Um Namenskonflikte zu vermeiden können Imports unter einem eigens definierten Namen importiert werden

```python
from math import sqrt as root
sqrt = 0 # Kein Konflikt mit math.sqrt
print( root( 16 ) )

> 4
```



### 6.2.2 Die Python Standard Library

Die Standardbibliothek ist eine der größten Stärken von Python, wodurch es sich für viele Anwendungen eignet. Der überwiegende Teil davon ist plattformunabhängig, so dass auch größere Python-Programme oft auf Unix, Windows, macOS und anderen Plattformen ohne Änderung laufen. \\
Teile dieser Bibliothek sind unter anderem auch das 'print' statement und funktionen, wie 'len()' und 'sum()'



### 6.2.3 Third Party Module

Die Standardbibliothek kann mit 'Packages' erweitert werden. Download und Installation des Packages und seiner Abhängigkeiten dient das Paketverwaltungsprogram PIP. Dazu muss lediglich der name des Packages genannt werden.

```bash
> pip install requests

Collecting pylib3
  Downloading https://files.pythonhosted.org/example
Collecting termcolor==1.1.0 (from pylib3)
  Downloading https://files.pythonhosted.org/example
Installing collected packages: termcolor, pylib3
  Running setup.py install for termcolor ... done
  Running setup.py install for pylib3 ... done
Successfully installed pylib3-0.0.3 termcolor-1.1.0
```

Im Terminal kann mit ``pip install <packagename>`` das Modul heruntergeladen und installiert werden. Nun kann es von überall importiert werden.

> **Tipp**
>
> [PyPi](https://pypi.org/) bietet eine große Auswahl an Python Packages. Das beste Verzeichnis dafür bleibt jedoch nach wie vor [Google](https://google.de)



### 6.2.4 Eigene Module

Es können auch Funktionen aus eigenen Dateien importiert werden. Beispielsweise kann sich die Funktion ``doSomething()`` in Datei ``MyModule.py`` befinden und in ``MyApplication.py`` importiert werden.

```python
# MyModule.py
def doSomething():
	print("Dew it!")
```

```python
# MyApplication.py
from MyModule import doSomething as dewIt
dewIt()

> Dew It!
```



> **Achtung**
>
> Befinden sich Fehler in ``MyModule.py``87878787878787878799 kann auch ``MyApplication.py``nicht ausgeführt werden. 



---

# 7 Dokumentation & Dateien

## 7.1 Dokumentation 



## 7.2 Dateien

### 7.2.1 Lesen

### 7.2.2 Schreiben

### 7.2.3 Exkurs: Dateiformate



## 7.2 JSON

Die JavaScript Object Notation(JSON)  ist ein kompaktes Datenformat in einer einfach lesbaren Textform. Es ist Vergleichbar mit Dictionaries in Python.





---



---

# 9 Emails



## 9.1 Sending Emails

#### 9.1.1 Templates

"Template Strings" enthalten Platzhalter, die mit anderen Strings ausgetauscht werden können. ``${identifier}``

> Hallo ${RECEIVER_NAME}, 
> 
> Dies ist eine Test-Nachricht.
> Das ist deine Email: ${RECEIVER_MAIL}
> 
> Liebe Grüße,
> ${SENDER_NAME}

Wir können einen String in ein Template verwandeln, indem wir mit ihm eine Entität der ``Template``-Klasse initialisieren

```python
from string import Template

string = """
Hallo ${RECIPIENT_NAME}, 

Dies ist eine Test-Nachricht.
Das ist deine Email: ${RECIPIENT_MAIL}

Liebe Grüße,
${SENDER_NAME}
"""

template = Template(string)
```



#### 9.1.2 SMTP

SMTP steht für Simple Mail Transfer Protocol und wird von Mail-Servern zum Senden von Emails genutzt. Das Package ``smtplib`` implementiert dieses Protokoll für Python

```python
import smtplib
# set up the SMTP server
s = smtplib.SMTP(host='your_host_address_here', port=your_port_here)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)
```



#### 9.1.3 Das Email Package

Das Email Package kann zum erstellen von Mails verwendet werden. (Um den gängigen Standards für Mails gerecht zu werden)

```python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


msg = MIMEMultipart()
# META-Daten der Email setzen
msg['From'] = SENDER_ADDRESS
msg['To'] = RECIPIENT_ADRESS
msg['Subject']="This is TEST"

msg.attach(MIMEText(MESSAGE, 'plain')) # Den Text hinzufügen 

    
```



#### 9.1.4 Mails versenden

```
import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Contact:
    def __init__(self, last, first, adress):
        self.last_name = last
        self.first_name = first
        self.email = adress


def connectServer(host, port, adress, password):
    """Returns a Server connection.

    Arguments:
        host {str} -- hostname of the server
        port {int} -- port for the server
        adress {str} -- email adress of the account
        password {str} -- password of the account

    Returns:
        smtplib.SMTP -- SMTP-Server-Client
    """    
    s = smtplib.SMTP(host=host, port=port)
    s.starttls()
    s.connect(host=host, port=port)
    s.login(adress, password)
    
    return s

def loadTemplate(filename):
    """Loads a Template file from Disk
    
    Arguments:
        filename {str} -- path of the file
    
    Returns:
        Template -- String Template object
    """    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def getContacts(filename):
    """retrieves the contacts from a CSV file
    
    Arguments:
        filename {str} -- path of the file

    Returns:
        list[Contact] -- list of Contact entities
    """    
    contacts = []
    with open(filename, mode='r') as f:
        for contact in f:
            contacts.append( Contact(contact[0],contact[1],contact[2]) )
    return contacts

def makeMessage(sender, recipient, subject, msg_body, msg_type):
    """Generates and returns a MIMEMultipart Message
    
    Arguments:
        sender {str} -- Sender's Email
        recipient {str} -- Recipient's Email
        subject {str} -- Email Subject
        msg_body {str} -- Email body
        msg_type {str} -- The type of the body (e.g. 'plain' or 'html')
    
    Returns:
        MIMEMultipart -- MIMEMultipart Message
    """    
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(msg_body, msg_type))
    return msg


# Server Config
cfg = {
    'host': 'smtp.ionos.de',
    'port': 587,
    'user': 'test@dev.noahkamara.com',
    'pass': '988-xyQ-6Vp-NEp'
}


# Initialize Server-Client
server = connectServer(cfg['host'], cfg['port'], cfg['user'], cfg['pass'])

# Retrieve Contacts
# contacts = getContacts('contacts.csv')
contacts = [
    Contact('Kamara','Test01','test01@login.noahkamara.com'),
    Contact('Kamara','Test02','test02@login.noahkamara.com'),
    Contact('Kamara','Test03','test03@login.noahkamara.com'),
    Contact('Kamara','Test04','test04@login.noahkamara.com')
]

# For each contact
for contact in contacts:
    # Load template
    template = loadTemplate('live/template')
    # substitute placehoders in template
    msg_body = template.substitute(RECIPIENT_NAME=contact.first_name, RECIPIENT_MAIL=contact.email, SENDER_NAME='Python Script')
    msg_type = 'plain' # Message Type
    # make a MIMEMUltipart message
    msg = makeMessage(cfg['user'], contact.email, f"Hallo {contact.first_name}", msg_body, msg_type)
    # Send Message
    server.send_message(msg)

# Close server Connection
server.quit()
```



---

