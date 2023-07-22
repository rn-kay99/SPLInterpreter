# Definition der Semantik

## Implizite Boolean-Konvertierung
Was passiert wenn nicht-Boolsche Werte an Stellen genutzt werden, wo diese erwartet werden?
Beispiele: ```if("a string") {...}```, ```while(1)```

**Semantik:**
Die Verwendung von nicht-Boolschen Werten, an Stellen wo ein Boolscher Wert erwartet wird ist nicht erlaubt.
Wenn in visitIfStmt oder visitWhileStmt eine expression übergeben wird, die nicht vom Typ bool ist, dann wird ein Fehler geworfen.

**Begründung:**
Dadurch wird der Code leichter lesbar und es kann zu keiner Fehlinterpretationen des möglich Programmverhaltens kommen, da sich das Programm inuitiv verhält.

---

## Operator-Überladen:
Können arithmetische Operatoren auch für Werte, die keine Zahlen sind, genutzt werden?
Beispiele: ```3 + "4"```, ```"hello" + "world"```, ```"Number: " + 3```, ```true + false```, ```"Text" - 2```

**Semantik:**
Arithmetische Operationen sind nur für Werte des Typ Numbers zulässig und wie üblich definiert.
Für die Datentypen String und Bool sind arithmetische Operationen nicht erlaubt und anderfalls werden in den Funktionen visitFactor() und visitTerm() ein Fehler geworfen.
Der Operator ```!``` ist jedoch für Bool Werte erlaubt und kehrt den Wahrheitswert eines boolschen Wertes um.

**Begründung:**
Die Operationen ```+```, ```-```, ```*``` und ```/``` sind auf Strings und boolschen Werten nicht intuitiv und sind deshalb nicht zulässig.
Die Arithmetische Operationen sind deshalb für diese Werte nicht erlaubt, um Fehlinterpretationen des Programmverhaltens zu vermeiden.

---

## Neudefinition von Variablen:
Dürfen Variablen innerhalb des selben Gültigkeitsbereichs mehrmals definiert werden?
Beispiel: 
```
var a = "before"; 
print a; 
var a = "after"; 
print a;
```

**Semantik:**
Neudefinition von Variablen im selben Gültigkeitsbereich ist erlaubt und führt dazu das die Variable überschrieben wird. Die Deklaration der Variablen wird in der Funktion visitVarDecl() implementiert.

**Begründung:**
Dadurch soll eine vereinfachter Umgang mit Variablen ermöglicht werden.

---

## Shadowing und Scoping
Ist die Neudefinition von Variablen in inneren Scopes erlaubt? Führt dies zu Shadowing oder zum Überschreiben der äußeren Variable?
Beispiel: 
```
var a = "outer"; 
print a; 
{ 
    var a = "inner"; 
    print a; 
    var b = "inner b"; 
} 
print a; 
print b;
```

**Semantik:**
Die Neudefinition von Variablen in inneren Blöcken ist zulässig und führt zum Ersetzen der Variablen im äußeren Block. Eine definierte Variable ist stets im gesamten globalen Ausführungskontext gültig und zugreifbar. Um dies sicherzustellen werden alle erstellten Variablen in einer globalen Hash-Tabelle gespeichert.

**Begründung:**
Dies soll die Lesbarkeit des Programms erleichtern, da eine Variable in verschiedenen Blöcken nie einen unterschiedlichen Wert haben kann.

## Uninitialisierte Werte
Können Variablen verwendet werden, ohne dass ein expliziter Wert zugewiesen wurde (bzw. gibt es null)?
Beispiel: 
```
var a; 
print a; 
// Error
```

**Semantik:**
Wenn eine Variable deklariert, aber nicht mit einem Wert belegt wurde, wird ihr intern der Wert ```None``` zugewiesen. Es ist jedoch nicht zulässig, eine Variable zu verwenden, ohne ihr zuvor einen Wert vom Typ ```NUMBER```, ```String``` oder ```Bool``` zugewiesen zu haben.

**Begründung:**
Die Verwendung einer Variablen ohne Wert führt zu unerwartetem Verhalten und soll daher vermieden werden.