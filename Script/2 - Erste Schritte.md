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




















