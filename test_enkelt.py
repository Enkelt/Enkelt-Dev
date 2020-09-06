import unittest
import enkelt


class TestEnkelt(unittest.TestCase):
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
		self.assertEqual('Enkelt.enkelt_print(', enkelt.translate_function('skriv'))
		self.assertEqual('Enkelt.enkelt_input(', enkelt.translate_function('in'))
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

		expected = 'class my_lib:\n\n\tdef min_lib_funk():\n\t\tEnkelt.enkelt_print("hej")'
		self.assertEqual(expected, enkelt.additional_library_code)

	def test_lex_var_keyword(self):
		test_data = {
			'my_var': ['VAR', 'my_var'],
			'själv': ['VAR', 'själv'],
			'för': ['KEYWORD', 'för'],
			'annars': ['KEYWORD', 'annars'],
			'för_var': ['VAR', 'för_var'],
		}

		for var_keyword in test_data.keys():
			tokens, _, _, _, _ = enkelt.lex_var_keyword([], var_keyword)
			self.assertEqual(test_data[var_keyword], tokens[-1])

	def fix_up_code_line(self):
		self.assertEqual('" |-ENKELT_ESCAPED_QUOTE-| |-ENKELT_ESCAPED_QUOTE-|', enkelt.fix_up_code_line('\' \\", \\'))

	def test_translate_clear(self):
		from os import name

		if name == 'nt':
			self.assertEqual('cls', enkelt.translate_clear())
		else:
			self.assertEqual('clear', enkelt.translate_clear())

	def test_lexer(self):



if __name__ == '__main__':
	unittest.main()
