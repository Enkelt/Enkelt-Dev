import unittest

import enkelt
import sample_code_manager
import generate_test_resources

generate_test_resources.generate()


class TestEnkelt(unittest.TestCase):
	functions = enkelt.functions_keywords_and_obj_notations()['functions'].keys()
	keywords = enkelt.functions_keywords_and_obj_notations()['keywords'].keys()
	obj_notations = enkelt.functions_keywords_and_obj_notations()['obj_notations'].keys()
	operators = enkelt.operator_symbols()

	def index_calculator(self, loop_counter):
		return ((len(self.non_real_sample_code) - 1) * loop_counter) + loop_counter

	def expected_output_index_calculator(self, loop_counter, x):
		index = 0

		if loop_counter > 0:
			index = self.index_calculator(loop_counter)
		index += x

		return index

	# ###################### #
	#  NON REAL SAMPLE CODE  #
	# ###################### #

	non_real_sample_code = sample_code_manager.get_non_real_sample_code()

	# Lexer output
	non_real_sample_code_in_all_functions_expected_lexer_output = sample_code_manager.get_non_real_sample_code_in_all_functions_expected_lexer_output()

	# Parser output
	non_real_sample_code_in_all_functions_expected_parser_output = sample_code_manager.get_non_real_sample_code_in_all_functions_expected_parser_output()

	# ################## #
	#  REAL SAMPLE CODE  #
	# ################## #

	real_sample_code = sample_code_manager.get_real_sample_code()

	# Lexer output
	real_sample_code_in_all_functions_expected_lexer_output = sample_code_manager.get_real_sample_code_in_all_functions_expected_lexer_output()

	# Parser output
	real_sample_code_in_all_functions_expected_parser_output = sample_code_manager.get_real_sample_code_in_all_functions_expected_parser_output()

	# ####### #
	#  TESTS  #
	# ####### #

	def test_fix_up_code_line(self):
		# Tests space removal, multiple space removal, tab & newline removal,
		# comment removal and quote conversion.
		expected_for_standard_skriv = 'skriv("text")'

		self.assertEqual(enkelt.fix_up_code_line("skriv ('text')"), expected_for_standard_skriv)
		self.assertEqual(enkelt.fix_up_code_line("skriv  ('text')"), expected_for_standard_skriv)
		self.assertEqual(enkelt.fix_up_code_line("skriv   ('text')"), expected_for_standard_skriv)
		self.assertEqual(enkelt.fix_up_code_line("skriv    ('text')\n"), expected_for_standard_skriv)
		self.assertEqual(enkelt.fix_up_code_line("skriv\t('text')"), expected_for_standard_skriv)
		self.assertEqual(enkelt.fix_up_code_line("skriv\t('text text2')"), 'skriv("text text2")')
		self.assertEqual(enkelt.fix_up_code_line('importera test'), 'importera test')
		self.assertEqual(enkelt.fix_up_code_line('\\"'), '|-ENKELT_ESCAPED_QUOTE-|')
		self.assertEqual(enkelt.fix_up_code_line('\\'), '|-ENKELT_ESCAPED_BACKSLASH-|')

	def test_has_numbers(self):
		self.assertEqual(enkelt.has_numbers('text'), False)
		self.assertEqual(enkelt.has_numbers('t1e2x3t4'), True)

	def test_translate_function(self):
		self.assertEqual(enkelt.translate_function('skriv'), 'print')
		self.assertEqual(enkelt.translate_function('definitely_not_a_function'), 'error')

	def test_translate_keyword(self):
		self.assertEqual(enkelt.translate_keyword('Sant'), 'True')
		self.assertEqual(enkelt.translate_keyword('definitely_not_a_keyword'), 'error')

	def test_translate_obj_notation(self):
		self.assertEqual(enkelt.translate_obj_notation('försök'), 'try')
		self.assertEqual(enkelt.translate_obj_notation('definitely_not_an_obj_notation'), 'error')

	def test_translate_output_to_swedish(self):
		to_be_translated = {
			'True': 'Sant',
			'False': 'Falskt',
		}

		data_types_to_be_translated = {
			'float': 'decimaltal',
			'str': 'sträng',
			'int': 'heltal',
			'list': 'lista',
			'dict': 'lexikon',
			'bool': 'boolesk',
			'NoneType': 'inget',
			'Exception': 'Errortyp'
		}

		for english in data_types_to_be_translated.keys():
			to_be_translated['<class \'' + english + '\'>'] = data_types_to_be_translated[english]

		for english in to_be_translated.keys():
			self.assertEqual(enkelt.translate_output_to_swedish(english), to_be_translated[english])

	def test_translate_clear(self):
		self.assertEqual(enkelt.translate_clear(), 'clear')

	def test_lex(self):
		# ###################### #
		#  NON REAL SAMPLE CODE  #
		# ###################### #
		loop_counter = 0

		for function in self.functions:
			for x, sample in enumerate(self.non_real_sample_code):
				index = self.expected_output_index_calculator(loop_counter, x)

				self.assertEqual(
					enkelt.lex(
						enkelt.fix_up_code_line(
							function + '(' + sample + ')'
						)
					),
					self.non_real_sample_code_in_all_functions_expected_lexer_output[index]
				)
			loop_counter += 1

		# ################## #
		#  REAL SAMPLE CODE  #
		# ################## #
		loop_counter = 0

		for x, sample in enumerate(self.real_sample_code):
			index = self.expected_output_index_calculator(loop_counter, x)

			self.assertEqual(
				enkelt.lex(
					enkelt.fix_up_code_line(
						sample
					)
				),
				self.real_sample_code_in_all_functions_expected_lexer_output[index]
			)
		loop_counter += 1

	def test_parse(self):
		# ###################### #
		#  NON REAL SAMPLE CODE  #
		# ###################### #
		loop_counter = 0

		for function in self.functions:
			for x, sample in enumerate(self.non_real_sample_code):
				index = self.expected_output_index_calculator(loop_counter, x)

				enkelt.parse(enkelt.lex(enkelt.fix_up_code_line(function + '(' + sample + ')')), 0)

				self.assertEqual(
					''.join(enkelt.source_code),
					self.non_real_sample_code_in_all_functions_expected_parser_output[index]
				)

				enkelt.source_code = []

			loop_counter += 1

		# ################## #
		#  REAL SAMPLE CODE  #
		# ################## #
		loop_counter = 0

		for x, sample in enumerate(self.real_sample_code):
			index = self.expected_output_index_calculator(loop_counter, x)

			enkelt.parse(enkelt.lex(enkelt.fix_up_code_line(sample)), 0)

			self.assertEqual(
				''.join(enkelt.source_code).replace('\n', ''),
				self.real_sample_code_in_all_functions_expected_parser_output[index]
			)

			enkelt.source_code = []

		loop_counter += 1
