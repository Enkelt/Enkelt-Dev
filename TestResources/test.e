skriv('Hej, Världen!')
skriv("Hej, Världen!")

var = 1
var_min = 2
_variable  =[]
min_1_variabel = 75
num1 = {}
längd('abc')
längd([1, 2, 'a', var])

input = in('Test')

töm()

typen = typ(4)

konv1 = Sträng(20) + "3"
konv2 = skriv(Heltal("20") + 3)

skriv(Bool(0))
skriv(Bool(1))
skriv(Bool(""))

skriv(Decimal("3.3") + 3)
skriv(Lista("abc"))

skriv("hej".versal())

skriv(runda(8.5673, 3))

lista = ['a', 'b']
skriv(lista[0])
lista.till("c")
lista.infoga(1, "c")

annat = "".foga(lista)

öppna('enkelt.py', 'r') som minFil:
	skriv(minFil.läs())

var = {"a": "alpha", "b": "beta", "namn": "Edvard"}
skriv(var["a"])
skriv(var["namn"])

num1 = 1+1
tal2 = 2 /2
tal3 = 3 % 3
num_2 = 4  *   4

var = Sant
om var == Sant:
	skriv("Sant!")
anom var == Falskt:
	skriv('Falskt!')
annars:
	skriv('Vet ej!')

namn = 'Kalle'
skriv('hej' + namn)

skriv("Hej" + namn om namn != "" annars "Inget namn givet!")

för i inom området(0, 11):
	skriv(i)
	bryt

för sak inom lista:
	skriv(sak)
	fortsätt

def min_funktion(a, b, c):
	skriv(a + b)

	returnera c + a

min_funktion("a", 'b', 'c')

klass Person:
	def __init__(själv, namn, ålder):
		själv.namn = namn
		själv.ålder = ålder

	def åldra(själv):
		själv.ålder += 1

person1 = Person('Karl', 25)
skriv(person1.namn)
person1.åldra()
skriv(person1.ålder)

försök:
	a = 1 + 2
fånga fel:
	skriv(fel)
slutligen:
	skriv(4)

importera matte
matte.abs(1)

var => a, b: a + b
skriv(var(1, 2))

skriv('hej \'Edvard\' ett annat tecken: \\ <-- där')
