klass Test {
    def __init__($själv, $namn) {
        $själv.$namn = $namn
    }
}

$mittTest = Test('name')
skriv ($mittTest.$namn)

$var = in("Skriv ett nummer lägre en 5: ")
försök {
  om ($var < 5) {
    skriv ("OK!")
  } annars {
    kasta("För stort!")
  }
}
fånga $error {
  skriv (typ($error))
}