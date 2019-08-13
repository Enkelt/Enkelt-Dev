def enkelt_print(data):
	data = str(data)
	data = data.replace("True", "Sant").replace("False", "Falskt").replace("<class \'float\'>", "decimaltal").replace("<class \'str\'>", "sträng").replace("<class \'int\'>", "heltal").replace("<class \'list\'>", "lista").replace("<class \'dict\'>", "lexikon").replace("<class \'bool\'>", "boolesk").replace("<class \'NoneType\'>", "inget")
	print(data)
