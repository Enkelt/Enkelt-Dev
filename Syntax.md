# Enkelts syntax
Här beskrivs hur Enkelts syntax är uppbyggd

### Funktioner
Uppbyggnad:

`funktion (parameterar)`

Exempel:

`skriv ("Hej, Världen!")`

`matte (1+2)`

#### Abstrakt
* Exempel 1

`skriv ("Hej, Världen!`)

> [["FUNCTION", "skriv"], ["STRING", "Hej, Världen!"]]


* Exempel 2

`matte (1+2)`

> [["FUNCTION", "matte"], ["PNUMBER", "1"], ["OPERATOR", "+"], ["PNUMBER", "2"]]


* Exempel 3

`skriv (matte($num*1))`

> [["FUNCTION", "skriv"], ["FUNCTION", "matte"], ["VAR", "num"], ["OPERATOR", "*"], ["PNUMBER", "1"]]
