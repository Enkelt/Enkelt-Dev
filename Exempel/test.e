def inköp_ändra($inköp) {
	$index = in("Ändra (index eller produkt): ")
	om ($index.ärnum()) {
		$sak = in("Ändra till: ")
		$inköp[Nummer($index)] = $sak
	} annars {
		$sak = in("Ändra till: ")
		$inköp[$inköp.index($index)] = $sak
	}
	start($inköp)
}
def inköp_bort($inköp) {
	$index = in("Bort (index eller produkt): ")
	om ($index.ärnum()) {
		$inköp.bort(Nummer($index))
	} annars {
		$inköp.bort($inköp.index($index))
	}
	start($inköp)
}
def inköp_till($inköp) {
	$sak = in("Till: ")
	$inköp.till($sak)
	start($inköp)
}
def start($inköp) {
	töm()
	för ($index, $sak; inom numrera($inköp)) {
		skriv(Text($index)+". "+$sak)
	}
	$händelse = in("Till/Bort/Ändra: ")
	om ($händelse == "till") {
		inköp_till($inköp)
	} anom ($händelse == "bort") {
		inköp_bort($inköp)
	} anom ($händelse == "ändra") {
		inköp_ändra($inköp)
	} annars {
		start($inköp)
	}
}
start([])