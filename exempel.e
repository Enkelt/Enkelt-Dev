# Skriv sträng
skriv ("Hej, Världen!")
# Strängvariabel
$str = "Sträng"
# Nummervariabel
$num = 5
# Skriv strängvariabel
skriv ($str)
# Skriv nummervariabel
skriv ($num)
# Skriv sträng- + nummer-variabel
skriv ($str+$num)
# Skriv resultatet av två nummer variabler
skriv ($num+$num)
# Variabel till flera variabler
$var = $str+$num+$str
# Nummervariabel till flera nummervariabler
$num_var = $num*$num
# Skriv
skriv ($var)
# Skriv
skriv ($num_var)
# Inputvariabel
$in = in('Hej :')
# Skriv
skriv ($in)
# Om & Annars
om ($in = "test") {
	skriv ("Du skrev test")
} annars {
	skriv ("Du skrev inte test")
}

