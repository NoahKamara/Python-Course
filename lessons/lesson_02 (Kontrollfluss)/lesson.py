# 2.1 BEDINGUNGEN & AUSDRÜCKE

# 2.1.1 Boolsche Ausdrücke
## Operatoren
a = (1 == 2) #> False
b = (1 < 2) #> True
c = (1 > 2) #> False

## Verknüpfungen

a = True and False #> False
b = True or False #> True
c = not (True and False) #> True


# 2.1.2 IF Statements
## IF
if True:
    print("True")

## ELSE
if True:
    print("True")
else: 
    print("False")

## ELIF
alter = 16
mindestalter = 18
muttiZettel = True

if alter > mindestalter:
    print("Einlass")
elif alter > 16 and muttiZettel:
    print("Einlass bis 24 Uhr")
else:
    print("Kein Einlass")

# ---------------------------------- #

# 2.2 SCHLEIFEN
## 2.2.1 while Schleifen

namen = ["Klaus","Simon","Sven","Markus","Simone","Nikolas"]
i = 0
while i < len(namen):
    print("Hallo "+namen[i])
    
## 2.2.2 For Schleifen

namen = ["Klaus","Simon","Sven","Markus","Simone","Nikolas"]

for name in namen:
    print("Hallo "+name)