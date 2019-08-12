$var = {"a": "alpha", "b": "beta", "c": "gamma"}
skriv($var)
skriv($var["c"])
$var["a"] = "alphaa"

för ($x, inom $var.element()) {
	skriv($x)
}

för ($x, inom $var.värden()) {
	skriv($x)
}