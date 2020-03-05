klass MinKlass {
     $text = ''
     def __init__($själv, $text) {
         $själv.$text = $text
     }
    def getText($själv) {
        returnera $själv.$text
    }
}

$textobjekt = MinKlass("Hej")
skriv ($textobjekt.getText())