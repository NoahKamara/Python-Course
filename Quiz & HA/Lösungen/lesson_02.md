# Lesson 02 - Kontrollfluss

## Bedingungen & Ausdrücke
1. Was ist hier das Ergebnis?
    ```python 
        varA = 1
        varB = 2
        varC = 3

        a = (varA == varB) # > False
        b = (varA == varB) or (varA < varB) # > True
        c = (not (varA == varB)) or (2 > varB) # > True
    ```
2. Erstelle einen Lichtschalter mit IF, ELSE und ELIF
    ```python 
        switch = True
        if switch:
            print("AN")
    ```

## Schleifen
1. Grüße jeden Namen persönlich (IF oder WHILE):
    ```python 
        names = ["Joshua","David","Friedolin","Hans"]
        for name in names:
            print("Hallo "+name)
    ```
