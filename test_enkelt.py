import unittest

from enkelt import lex
from enkelt import main


class TestEnkelt(unittest.TestCase):
	def test_main(self):
		# Tests space removal, multiple space removal, tab & newline removal,
		# comment removal and quote conversion.

		self.assertEqual(main("skriv ('hej')"), 'skriv("hej")')
		self.assertEqual(main("skriv  ('hej')"), 'skriv("hej")')
		self.assertEqual(main("skriv   ('hej')"), 'skriv("hej")')
		self.assertEqual(main("skriv    ('hej')\n"), 'skriv("hej")')
		self.assertEqual(main("skriv\t('hej')"), 'skriv("hej")')
		self.assertEqual(main(".bort[123]"), '.bort(123)')

	def test_lex(self):
		# Tests functions, data-types, vars, bools, operators and others tokenized output.
		self.assertEqual(lex('skriv("Hej")'), [
			['FUNCTION', 'skriv'],
			['STRING', 'Hej'],
			['OPERATOR', ')'],
		])
		self.assertEqual(lex('skriv(1)'), [
			['FUNCTION', 'skriv'],
			['PNUMBER', '1'],
			['OPERATOR', ')'],
		])
		self.assertEqual(lex('skriv(-1)'), [
			['FUNCTION', 'skriv'],
			['NNUMBER', '-1'],
			['OPERATOR', ')'],
		])
		self.assertEqual(lex('skriv(1+1)'), [
			['FUNCTION', 'skriv'],
			['PNUMBER', '1'],
			['OPERATOR', '+'],
			['PNUMBER', '1'],
			['OPERATOR', ')'],
		])
		self.assertEqual(lex('skriv(1-1)'), [
			['FUNCTION', 'skriv'],
			['PNUMBER', '1'],
			['NNUMBER', '-1'],
			['OPERATOR', ')'],
		])
		self.assertEqual(lex('skriv(1*1)'), [
			['FUNCTION', 'skriv'],
			['PNUMBER', '1'],
			['OPERATOR', '*'],
			['PNUMBER', '1'],
			['OPERATOR', ')'],
		])
		self.assertEqual(lex('skriv(1/1)'), [
			['FUNCTION', 'skriv'],
			['PNUMBER', '1'],
			['OPERATOR', '/'],
			['PNUMBER', '1'],
			['OPERATOR', ')'],
		])
		self.assertEqual(lex('skriv(1%1)'), [
			['FUNCTION', 'skriv'],
			['PNUMBER', '1'],
			['OPERATOR', '%'],
			['PNUMBER', '1'],
			['OPERATOR', ')'],
		])
		self.assertEqual(lex('skriv("Hej")#Test'), [
			['FUNCTION', 'skriv'],
			['STRING', 'Hej'],
			['OPERATOR', ')'],
		])
		self.assertEqual(lex('$var="a"'), [
			['VAR', 'var'],
			['OPERATOR', '='],
			['STRING', 'a'],
		])
		self.assertEqual(lex('$var=1'), [
			['VAR', 'var'],
			['OPERATOR', '='],
			['PNUMBER', '1'],
		])
		self.assertEqual(lex('$var=-1'), [
			['VAR', 'var'],
			['OPERATOR', '='],
			['NNUMBER', '-1'],
		])
		self.assertEqual(lex('$var=Sant'), [
			['VAR', 'var'],
			['OPERATOR', '='],
			['BOOL', 'Sant'],

		])
		self.assertEqual(lex('$var=Falskt'), [
			['VAR', 'var'],
			['OPERATOR', '='],
			['BOOL', 'Falskt'],

		])
		self.assertEqual(lex('$var="a"+"b"'), [
			['VAR', 'var'],
			['OPERATOR', '='],
			['STRING', 'a'],
			['OPERATOR', '+'],
			['STRING', 'b'],
		])
		self.assertEqual(lex('$var="a"+Text(Nummer(1+2))'), [
			['VAR', 'var'],
			['OPERATOR', '='],
			['STRING', 'a'],
			['OPERATOR', '+'],
			['FUNCTION', 'Text'],
			['FUNCTION', 'Nummer'],
			['PNUMBER', '1'],
			['OPERATOR', '+'],
			['PNUMBER', '2'],
			['OPERATOR', ')'],
			['OPERATOR', ')'],
		])
		self.assertEqual(lex('töm()'), [
			['FUNCTION', 'töm'],
			['OPERATOR', ')'],
		])
		self.assertEqual(lex('['), [
			['LIST_START', '['],
		])
		self.assertEqual(lex('[]'), [
			['LIST_START', '['],
			['LIST_END', ']'],
		])
		self.assertEqual(lex('$var=["a",1]'), [
			['VAR', 'var'],
			['OPERATOR', '='],
			['LIST_START', '['],
			['STRING', 'a'],
			['OPERATOR', ','],
			['PNUMBER', '1'],
			['LIST_END', ']'],
		])
		self.assertEqual(lex('$var=["a",["b"], 1]'), [
			['VAR', 'var'],
			['OPERATOR', '='],
			['LIST_START', '['],
			['STRING', 'a'],
			['OPERATOR', ','],
			['LIST_START', '['],
			['STRING', 'b'],
			['LIST_END', ']'],
			['OPERATOR', ','],
			['PNUMBER', '1'],
			['LIST_END', ']'],
		])
		self.assertEqual(lex('om($var="a"){'), [
			['FUNCTION', 'om'],
			['VAR', 'var'],
			['OPERATOR', '='],
			['STRING', 'a'],
			['OPERATOR', ')'],
			['START', '{'],
		])
		self.assertEqual(lex('om($var=="a"){'), [
			['FUNCTION', 'om'],
			['VAR', 'var'],
			['OPERATOR', '='],
			['OPERATOR', '='],
			['STRING', 'a'],
			['OPERATOR', ')'],
			['START', '{'],
		])
		self.assertEqual(lex('}annars{'), [
			['END', '}'],
			['KEYWORD', 'annars'],
			['START', '{'],
		])
		for operator in ['+', '*', '/', '%', '<', '>', '=', '!', '.', ',', ')', ':', ';']:
			self.assertEqual(lex(operator), [
				['OPERATOR', operator]
			])
		self.assertEqual(lex('längd("hej")'), [
			['FUNCTION', 'längd'],
			['STRING', 'hej'],
			['OPERATOR', ')'],
		])
		self.assertEqual(lex('skriv(längd("x"))'), [
			['FUNCTION', 'skriv'],
			['FUNCTION', 'längd'],
			['STRING', 'x'],
			['OPERATOR', ')'],
			['OPERATOR', ')'],
		])
		self.assertEqual(lex('längd("hej")'), [
			['FUNCTION', 'längd'],
			['STRING', 'hej'],
			['OPERATOR', ')'],
		])
		functions = [
			'skriv',
			'till',
			'bort',
			'töm',
			'om',
			'anom',
			'längd',
			'in',
			'Text',
			'Nummer',
			'Decimal',
			'Bool',
			'området',
			'sortera',
			'slumpval',
			'slump',
			'abs',
			'lista',
			'blanda',
			'runda',
			'versal',
			'gemen',
			'ärnum',
			'ersätt',
			'infoga',
			'index',
			'dela',
			'foga',
			'typ',
			'för',
			'medan',
			'epok',
			'tid',
			'nu',
			'sin',
			'cos',
			'tan',
			'asin',
			'acos',
			'atan',
			'potens',
			'tak',
			'golv',
			'fakultet',
			'kvadratrot',
			'log',
			'grader',
			'radianer',
			'datum',
			'idag',
			'veckodag',
			'värden',
			'element',
			'numrera'
		]
		for function in functions:
			self.assertEqual(lex(function+'("x")'), [
				['FUNCTION', function],
				['STRING', 'x'],
				['OPERATOR', ')'],
			])
		keywords = [
			'annars',
			'inom',
			'bryt',
			'fortsätt',
			'returnera',
			'annars',
			'inte',
			'passera',
			'år',
			'månad',
			'dag',
			'timme',
			'minut',
			'sekund',
			'mikrosekund',
			'annars',
			'matte_e',
			'matte_pi',
		]
		for keyword in keywords:
			self.assertEqual(lex('skriv('+keyword+')'), [
				['FUNCTION', 'skriv'],
				['KEYWORD', keyword],
				['OPERATOR', ')'],
			])
		self.assertEqual(lex('def test($param, $param_b) {'), [
			['USER_FUNCTION', ' test'],
			['VAR', 'param'],
			['OPERATOR', ','],
			['VAR', 'param_b'],
			['OPERATOR', ')'],
			['START', '{'],
			
		])
		self.assertEqual(lex('$lex =  {"a": "alpha", "b": "beta"}'), [
			['VAR', 'lex'],
			['OPERATOR', '='],
			['START', '{'],
			['STRING', 'a'],
			['OPERATOR', ':'],
			['STRING', 'alpha'],
			['OPERATOR', ','],
			['STRING', 'b'],
			['OPERATOR', ':'],
			['STRING', 'beta'],
			['END', '}'],
		])
