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

