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

