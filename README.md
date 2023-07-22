# SPL' Interpreter 

**Compilerbau -- Projekt SoSe 2023**

In diesem Projekt sollte ein Parser und ein simpler Interpreter für die Structured Programming Language (SPL') entwickelt werden. Für die Implementierung wurde die Programmiersprache Python gewählt.
Der Code für den Interpreter lässt sich in der ```./python_generated/SPLInterpreterVisitor.py``` finden.

Im Verzeichnis ```./spl_programs``` finden sich Beispielprogramme für den Interpreter in der Sprache SPL'.

### Testen des Interpreters
Um den Interpreter zu testen muss in dem Hauptverzeichnis der folgende Befehl ausgeführt werden:
```shell
python main.py input.txt
```
wobei input.txt ein beliebiger Pfad zu einer Datei in SPL' Format ist. Die Ausgabe wird auf auf die Standardausgabe geschrieben.

### Was ist SPL'?
SPL' (SPL Prime) ist eine einfache Programmiersprache und basiert auf der Lox-Sprache, die von Robert Nystrom in seinem Buch "Crafting Interpreters" verwendet wird, mit einigen Änderungen und Vereinfachungen.
Die Grammatik der Sprache ist in ```/grammar/SPL.g4``` definiert und die Semantik der Sprache in der ```SEMANTICS.md``` angegeben.