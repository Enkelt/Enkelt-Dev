skriv ("hej")
skriv ("test") 
def går_att_dividera($nummer, $num_b) {
	om ($nummer % $num_b == 0) {
		returnera Sant
	} annars {
		returnera Falskt
	}
}
$resultat = går_att_dividera(10, 2)
skriv ($resultat) 