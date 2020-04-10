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

