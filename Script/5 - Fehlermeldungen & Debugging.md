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