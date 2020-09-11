import unittest
import enkelt

sample_code_for_testing = 'skriv(\'Hej, Världen!\')\nskriv("Hej, Världen!")\n\nvar = 1\nvar_min = 2\n_variable  =[]\nmin_1_variabel = 75\nnum1 = {}\nlängd(\'abc\')\nlängd([1, 2, \'a\', var])\n\ninput = in(\'Test\')\n\ntöm()\n\ntypen = typ(4)\n\nkonv1 = Sträng(20) + "3"\nkonv2 = skriv(Heltal("20") + 3)\n\nskriv(Bool(0))\nskriv(Bool(1))\nskriv(Bool(""))\n\nskriv(Decimal("3.3") + 3)\nskriv(Lista("abc"))\n\nskriv("hej".versal())\n\nskriv(runda(8.5673, 3))\n\nlista = [\'a\', \'b\']\nskriv(lista[0])\nlista.till("c")\nlista.infoga(1, "c")\n\nannat = "".foga(lista)\n\nöppna(\'enkelt.py\', \'r\') som minFil:\n\tskriv(minFil.läs())\n\nvar = {"a": "alpha", "b": "beta", "namn": "Edvard"}\nskriv(var["a"])\nskriv(var["namn"])\n\nnum1 = 1+1\ntal2 = 2 /2\ntal3 = 3 % 3\nnum_2 = 4  *   4\n\nvar = Sant\nom var == Sant:\n\tskriv("Sant!")\nanom var == Falskt:\n\tskriv(\'Falskt!\')\nannars:\n\tskriv(\'Vet ej!\')\n\nnamn = \'Kalle\'\nskriv(\'hej\' + namn)\n\nskriv("Hej" + namn om namn != "" annars "Inget namn givet!")\n\nför i inom området(0, 11):\n\tskriv(i)\n\tbryt\n\nför sak inom lista:\n\tskriv(sak)\n\tfortsätt\n\ndef min_funktion(a, b, c):\n\tskriv(a + b)\n\n\treturnera c + a\n\nmin_funktion("a", \'b\', \'c\')\n\nklass Person:\n\tdef __init__(själv, namn, ålder):\n\t\tsjälv.namn = namn\n\t\tsjälv.ålder = ålder\n\n\tdef åldra(själv):\n\t\tsjälv.ålder += 1\n\nperson1 = Person(\'Karl\', 25)\nskriv(person1.namn)\nperson1.åldra()\nskriv(person1.ålder)\n\nförsök:\n\ta = 1 + 2\nfånga fel:\n\tskriv(fel)\nslutligen:\n\tskriv(4)\n\nimportera matte\nmatte.abs(1)\n\nvar => a, b: a + b\nskriv(var(1, 2))\n\nskriv(\'hej \\\'Edvard\\\' ett annat tecken: \\\\ <-- där\')\n'
sample_code_for_testing_lexed = [['FUNC', 'skriv'], ['STR', 'Hej, Världen!'], ['OP', ')'], ['FORMAT', '\n'], ['FUNC', 'skriv'], ['STR', 'Hej, Världen!'], ['OP', ')'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['VAR', 'var'], ['OP', '='], ['NUM', '1'], ['FORMAT', '\n'], ['VAR', 'var_min'], ['OP', '='], ['NUM', '2'], ['FORMAT', '\n'], ['VAR', '_variable'], ['OP', '='], ['OP', '['], ['OP', ']'], ['FORMAT', '\n'], ['VAR', 'min_1_variabel'], ['OP', '='], ['NUM', '75'], ['FORMAT', '\n'], ['VAR', 'num1'], ['OP', '='], ['OP', '{'], ['OP', '}'], ['FORMAT', '\n'], ['FUNC', 'längd'], ['STR', 'abc'], ['OP', ')'], ['FORMAT', '\n'], ['FUNC', 'längd'], ['OP', '['], ['NUM', '1'], ['OP', ','], ['NUM', '2'], ['OP', ','], ['STR', 'a'], ['OP', ','], ['VAR', 'var'], ['OP', ']'], ['OP', ')'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['VAR', 'input'], ['OP', '='], ['FUNC', 'in'], ['STR', 'Test'], ['OP', ')'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['FUNC', 'töm'], ['OP', ')'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['VAR', 'typen'], ['OP', '='], ['FUNC', 'typ'], ['NUM', '4'], ['OP', ')'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['VAR', 'konv1'], ['OP', '='], ['FUNC', 'Sträng'], ['NUM', '20'], ['OP', ')'], ['OP', '+'], ['STR', '3'], ['FORMAT', '\n'], ['VAR', 'konv2'], ['OP', '='], ['FUNC', 'skriv'], ['FUNC', 'Heltal'], ['STR', '20'], ['OP', ')'], ['OP', '+'], ['NUM', '3'], ['OP', ')'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['FUNC', 'skriv'], ['FUNC', 'Bool'], ['NUM', '0'], ['OP', ')'], ['OP', ')'], ['FORMAT', '\n'], ['FUNC', 'skriv'], ['FUNC', 'Bool'], ['NUM', '1'], ['OP', ')'], ['OP', ')'], ['FORMAT', '\n'], ['FUNC', 'skriv'], ['FUNC', 'Bool'], ['STR', ''], ['OP', ')'], ['OP', ')'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['FUNC', 'skriv'], ['FUNC', 'Decimal'], ['STR', '3.3'], ['OP', ')'], ['OP', '+'], ['NUM', '3'], ['OP', ')'], ['FORMAT', '\n'], ['FUNC', 'skriv'], ['FUNC', 'Lista'], ['STR', 'abc'], ['OP', ')'], ['OP', ')'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['FUNC', 'skriv'], ['STR', 'hej'], ['OP', '.'], ['FUNC', 'versal'], ['OP', ')'], ['OP', ')'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['FUNC', 'skriv'], ['FUNC', 'runda'], ['NUM', '8'], ['OP', '.'], ['NUM', '5673'], ['OP', ','], ['NUM', '3'], ['OP', ')'], ['OP', ')'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['VAR', 'lista'], ['OP', '='], ['OP', '['], ['STR', 'a'], ['OP', ','], ['STR', 'b'], ['OP', ']'], ['FORMAT', '\n'], ['FUNC', 'skriv'], ['VAR', 'lista'], ['OP', '['], ['NUM', '0'], ['OP', ']'], ['OP', ')'], ['FORMAT', '\n'], ['VAR', 'lista'], ['OP', '.'], ['FUNC', 'till'], ['STR', 'c'], ['OP', ')'], ['FORMAT', '\n'], ['VAR', 'lista'], ['OP', '.'], ['FUNC', 'infoga'], ['NUM', '1'], ['OP', ','], ['STR', 'c'], ['OP', ')'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['VAR', 'annat'], ['OP', '='], ['STR', ''], ['OP', '.'], ['FUNC', 'foga'], ['VAR', 'lista'], ['OP', ')'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['FUNC', 'öppna'], ['STR', 'enkelt.py'], ['OP', ','], ['STR', 'r'], ['OP', ')'], ['KEYWORD', 'som'], ['VAR', 'minFil'], ['OP', ':'], ['FORMAT', '\n'], ['FORMAT', '\t'], ['FUNC', 'skriv'], ['VAR', 'minFil'], ['OP', '.'], ['FUNC', 'läs'], ['OP', ')'], ['OP', ')'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['VAR', 'var'], ['OP', '='], ['OP', '{'], ['STR', 'a'], ['OP', ':'], ['STR', 'alpha'], ['OP', ','], ['STR', 'b'], ['OP', ':'], ['STR', 'beta'], ['OP', ','], ['STR', 'namn'], ['OP', ':'], ['STR', 'Edvard'], ['OP', '}'], ['FORMAT', '\n'], ['FUNC', 'skriv'], ['VAR', 'var'], ['OP', '['], ['STR', 'a'], ['OP', ']'], ['OP', ')'], ['FORMAT', '\n'], ['FUNC', 'skriv'], ['VAR', 'var'], ['OP', '['], ['STR', 'namn'], ['OP', ']'], ['OP', ')'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['VAR', 'num1'], ['OP', '='], ['NUM', '1'], ['OP', '+'], ['NUM', '1'], ['FORMAT', '\n'], ['VAR', 'tal2'], ['OP', '='], ['NUM', '2'], ['OP', '/'], ['NUM', '2'], ['FORMAT', '\n'], ['VAR', 'tal3'], ['OP', '='], ['NUM', '3'], ['OP', '%'], ['NUM', '3'], ['FORMAT', '\n'], ['VAR', 'num_2'], ['OP', '='], ['NUM', '4'], ['OP', '*'], ['NUM', '4'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['VAR', 'var'], ['OP', '='], ['KEYWORD', 'Sant'], ['FORMAT', '\n'], ['KEYWORD', 'om'], ['VAR', 'var'], ['OP', '='], ['OP', '='], ['KEYWORD', 'Sant'], ['OP', ':'], ['FORMAT', '\n'], ['FORMAT', '\t'], ['FUNC', 'skriv'], ['STR', 'Sant!'], ['OP', ')'], ['FORMAT', '\n'], ['KEYWORD', 'anom'], ['VAR', 'var'], ['OP', '='], ['OP', '='], ['KEYWORD', 'Falskt'], ['OP', ':'], ['FORMAT', '\n'], ['FORMAT', '\t'], ['FUNC', 'skriv'], ['STR', 'Falskt!'], ['OP', ')'], ['FORMAT', '\n'], ['KEYWORD', 'annars'], ['OP', ':'], ['FORMAT', '\n'], ['FORMAT', '\t'], ['FUNC', 'skriv'], ['STR', 'Vet ej!'], ['OP', ')'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['VAR', 'namn'], ['OP', '='], ['STR', 'Kalle'], ['FORMAT', '\n'], ['FUNC', 'skriv'], ['STR', 'hej'], ['OP', '+'], ['VAR', 'namn'], ['OP', ')'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['FUNC', 'skriv'], ['STR', 'Hej'], ['OP', '+'], ['VAR', 'namn'], ['KEYWORD', 'om'], ['VAR', 'namn'], ['OP', '!'], ['OP', '='], ['STR', ''], ['KEYWORD', 'annars'], ['STR', 'Inget namn givet!'], ['OP', ')'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['KEYWORD', 'för'], ['VAR', 'i'], ['KEYWORD', 'inom'], ['FUNC', 'området'], ['NUM', '0'], ['OP', ','], ['NUM', '11'], ['OP', ')'], ['OP', ':'], ['FORMAT', '\n'], ['FORMAT', '\t'], ['FUNC', 'skriv'], ['VAR', 'i'], ['OP', ')'], ['FORMAT', '\n'], ['FORMAT', '\t'], ['KEYWORD', 'bryt'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['KEYWORD', 'för'], ['VAR', 'sak'], ['KEYWORD', 'inom'], ['VAR', 'lista'], ['OP', ':'], ['FORMAT', '\n'], ['FORMAT', '\t'], ['FUNC', 'skriv'], ['VAR', 'sak'], ['OP', ')'], ['FORMAT', '\n'], ['FORMAT', '\t'], ['KEYWORD', 'fortsätt'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['FUNC_DEF', 'min_funktion'], ['VAR', 'a'], ['OP', ','], ['VAR', 'b'], ['OP', ','], ['VAR', 'c'], ['OP', ')'], ['OP', ':'], ['FORMAT', '\n'], ['FORMAT', '\t'], ['FUNC', 'skriv'], ['VAR', 'a'], ['OP', '+'], ['VAR', 'b'], ['OP', ')'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['FORMAT', '\t'], ['KEYWORD', 'returnera'], ['VAR', 'c'], ['OP', '+'], ['VAR', 'a'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['FUNC', 'min_funktion'], ['STR', 'a'], ['OP', ','], ['STR', 'b'], ['OP', ','], ['STR', 'c'], ['OP', ')'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['CLASS', 'Person'], ['OP', ':'], ['FORMAT', '\n'], ['FORMAT', '\t'], ['FUNC_DEF', '__init__'], ['VAR', 'själv'], ['OP', ','], ['VAR', 'namn'], ['OP', ','], ['VAR', 'ålder'], ['OP', ')'], ['OP', ':'], ['FORMAT', '\n'], ['FORMAT', '\t'], ['FORMAT', '\t'], ['VAR', 'själv'], ['OP', '.'], ['VAR', 'namn'], ['OP', '='], ['VAR', 'namn'], ['FORMAT', '\n'], ['FORMAT', '\t'], ['FORMAT', '\t'], ['VAR', 'själv'], ['OP', '.'], ['VAR', 'ålder'], ['OP', '='], ['VAR', 'ålder'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['FORMAT', '\t'], ['FUNC_DEF', 'åldra'], ['VAR', 'själv'], ['OP', ')'], ['OP', ':'], ['FORMAT', '\n'], ['FORMAT', '\t'], ['FORMAT', '\t'], ['VAR', 'själv'], ['OP', '.'], ['VAR', 'ålder'], ['OP', '+'], ['OP', '='], ['NUM', '1'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['VAR', 'person1'], ['OP', '='], ['FUNC', 'Person'], ['STR', 'Karl'], ['OP', ','], ['NUM', '25'], ['OP', ')'], ['FORMAT', '\n'], ['FUNC', 'skriv'], ['VAR', 'person1'], ['OP', '.'], ['VAR', 'namn'], ['OP', ')'], ['FORMAT', '\n'], ['VAR', 'person1'], ['OP', '.'], ['FUNC', 'åldra'], ['OP', ')'], ['FORMAT', '\n'], ['FUNC', 'skriv'], ['VAR', 'person1'], ['OP', '.'], ['VAR', 'ålder'], ['OP', ')'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['KEYWORD', 'försök'], ['OP', ':'], ['FORMAT', '\n'], ['FORMAT', '\t'], ['VAR', 'a'], ['OP', '='], ['NUM', '1'], ['OP', '+'], ['NUM', '2'], ['FORMAT', '\n'], ['KEYWORD', 'fånga'], ['VAR', 'fel'], ['OP', ':'], ['FORMAT', '\n'], ['FORMAT', '\t'], ['FUNC', 'skriv'], ['VAR', 'fel'], ['OP', ')'], ['FORMAT', '\n'], ['KEYWORD', 'slutligen'], ['OP', ':'], ['FORMAT', '\n'], ['FORMAT', '\t'], ['FUNC', 'skriv'], ['NUM', '4'], ['OP', ')'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['IMPORT', 'matte'], ['VAR', 'matte'], ['OP', '.'], ['FUNC', 'abs'], ['NUM', '1'], ['OP', ')'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['VAR', 'var'], ['OP', '='], ['KEYWORD', '>'], ['VAR', 'a'], ['OP', ','], ['VAR', 'b'], ['OP', ':'], ['VAR', 'a'], ['OP', '+'], ['VAR', 'b'], ['FORMAT', '\n'], ['FUNC', 'skriv'], ['FUNC', 'var'], ['NUM', '1'], ['OP', ','], ['NUM', '2'], ['OP', ')'], ['OP', ')'], ['FORMAT', '\n'], ['FORMAT', '\n'], ['FUNC', 'skriv'], ['STR', 'hej |-ENKELT_ESCAPED_BACKSLASH-|'], ['VAR', 'Edvard|'], ['OP', '-'], ['VAR', 'ENKELT_ESCAPED_BACKSLASH'], ['OP', '-'], ['STR', ' ett annat tecken: |-ENKELT_ESCAPED_BACKSLASH-||-ENKELT_ESCAPED_BACKSLASH-| <-- där'], ['OP', ')'], ['FORMAT', '\n']]
sample_code_for_testing_parsed = 'enkelt_print("Hej, Världen!")\nenkelt_print("Hej, Världen!")\n\nvar= 1\nvar_min= 2\n_variable= []\nmin_1_variabel= 75\nnum1= {}\nlen("abc")\nlen([1, 2, "a", var])\n\ninput= enkelt_input("Test")\n\nsystem("clear")\n\ntypen= type(4)\n\nkonv1= str(20)+"3"\nkonv2= enkelt_print(int("20")+3)\n\nenkelt_print(bool(0))\nenkelt_print(bool(1))\nenkelt_print(bool(""))\n\nenkelt_print(float("3.3")+3)\nenkelt_print(list("abc"))\n\nenkelt_print("hej".upper())\n\nenkelt_print(round(8.5673, 3))\n\nlista= ["a", "b"]\nenkelt_print(lista[0])\nlista.append("c")\nlista.insert(1, "c")\n\nannat= "".join(lista)\n\nwith open("enkelt.py", "r") as minFil:\n\tenkelt_print(minFil.read())\n\nvar= {"a":"alpha", "b":"beta", "namn":"Edvard"}\nenkelt_print(var["a"])\nenkelt_print(var["namn"])\n\nnum1= 1+1\ntal2= 2/2\ntal3= 3% 3\nnum_2= 4*4\n\nvar= True \nif var == True:\n\tenkelt_print("Sant!")\nelif var == False:\n\tenkelt_print("Falskt!")\nelse:\n\tenkelt_print("Vet ej!")\n\nnamn= "Kalle"\nenkelt_print("hej"+namn)\n\nenkelt_print("Hej"+namn if namn!= "" else "Inget namn givet!")\n\nfor i in range(0, 11):\n\tenkelt_print(i)\n\tbreak \n\nfor sak in lista:\n\tenkelt_print(sak)\n\tcontinue \n\ndef min_funktion(a, b, c):\n\tenkelt_print(a+b)\n\n\treturn  c+a\n\nmin_funktion("a", "b", "c")\n\n\nclass Person:\n\tdef __init__(self, namn, ålder):\n\t\tself.namn= namn\n\t\tself.ålder= ålder\n\n\tdef åldra(self):\n\t\tself.ålder+= 1\n\nperson1= Person("Karl", 25)\nenkelt_print(person1.namn)\nperson1.åldra()\nenkelt_print(person1.ålder)\n\ntry:\n\ta= 1+2\nexcept Exception as fel:\n\tenkelt_print(fel)\nfinally:\n\tenkelt_print(4)\n\nmatte.abs(1)\n\nvar= lambda a, b:a+b\nenkelt_print(var(1, 2))\n\nenkelt_print("hej \\"Edvard|-ENKELT_ESCAPED_BACKSLASH-" ett annat tecken: \\\\ <-- där")\n'


class TestEnkelt(unittest.TestCase):
	maxDiff = None

	def test_translate_output_to_swedish(self):
		to_test = {
			"True": 'Sant',
			"False": 'Falskt',
			"None": 'Inget',
			"<class 'float'>": 'Decimaltal',
			"<class 'str'>": 'Sträng',
			"<class 'int'>": 'Heltal',
			"<class 'list'>": 'Lista',
			"<class 'dict'>": 'Lexikon',
			"<class 'dict_keys'>": 'Lexikonnycklar',
			"<class 'bool'>": 'Boolesk',
			"<class 'NoneType'>": 'Inget',
			"<class 'Exception'>": 'Feltyp',
			"<class 'datetime.date'>": 'Datum',
			"<class 'datetime.datetime'>": 'Datum & tid',
			"<class 'range'>": 'Område'
		}

		for datatype in to_test:
			self.assertEqual(to_test[datatype], enkelt.translate_output_to_swedish(datatype))

		self.assertEqual('Sant', enkelt.translate_output_to_swedish('True'))

	def test_maybe_place_space_before(self):
		# With space
		expectation = [char for char in 'a suffix ']
		self.assertEqual(expectation, enkelt.maybe_place_space_before(['a'], 'suffix'))

		# No space
		indicators = ['\n', '\t', '(', ' ', '.']
		for indic in indicators:
			expectation = [char for char in indic + 'suffix ']
			self.assertEqual(expectation, enkelt.maybe_place_space_before([indic], 'suffix'))

	def test_translate_function(self):
		# Enkelt built-in functions
		self.assertEqual('enkelt_print(', enkelt.translate_function('skriv'))
		self.assertEqual('enkelt_input(', enkelt.translate_function('in'))
		self.assertEqual('unknown_function_name(', enkelt.translate_function('unknown_function_name'))

		# Special cases
		self.assertEqual('system("clear"', enkelt.translate_function('töm'))

	def test_translate_keyword(self):
		# Standard
		self.assertEqual('for', enkelt.translate_keyword('för'))

		# No matching translation
		self.assertEqual('error', enkelt.translate_keyword('unknown_keyword'))

	def test_transpile_library_code(self):
		library_enkelt_code = 'def min_lib_funk():\n\tskriv(\'hej\')'
		enkelt.transpile_library_code(library_enkelt_code, 'my_lib')

		expected = 'class my_lib:\n\n\tdef min_lib_funk():\n\t\tenkelt_print("hej")'
		self.assertEqual(expected, enkelt.additional_library_code)

	def test_lex_var_keyword(self):
		test_data = {
			'my_var': ['VAR', 'my_var'],
			'själv': ['VAR', 'själv'],
			'för': ['KEYWORD', 'för'],
			'annars': ['KEYWORD', 'annars'],
			'för_var': ['VAR', 'för_var'],
		}

		for var_keyword, value in test_data.items():
			tokens, _, _, _, _ = enkelt.lex_var_keyword([], var_keyword)
			self.assertEqual(value, tokens[-1])

	def fix_up_code_line(self):
		self.assertEqual('" |-ENKELT_ESCAPED_QUOTE-| |-ENKELT_ESCAPED_QUOTE-|', enkelt.fix_up_code_line('\' \\", \\'))

	def test_translate_clear(self):
		from os import name

		if name == 'nt':
			self.assertEqual('cls', enkelt.translate_clear())
		else:
			self.assertEqual('clear', enkelt.translate_clear())

	def test_lexer(self):
		self.assertEqual(sample_code_for_testing_lexed, enkelt.lexer(sample_code_for_testing))

	def test_parser(self):
		self.assertEqual(sample_code_for_testing_parsed, enkelt.parser(sample_code_for_testing_lexed))


if __name__ == '__main__':
	unittest.main()
