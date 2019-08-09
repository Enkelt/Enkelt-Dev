import unittest

from run_enkelt import lex
from run_enkelt import main
from run_enkelt import parse


class TestEnkelt(unittest.TestCase):
	def test_main(self):
		# Tests space removal, multiple space removal, tab & newline removal,
		# comment removal and quote conversion.

		self.assertEqual(main("skriv ('hej')"), 'skriv("hej")')
		self.assertEqual(main("skriv  ('hej')"), 'skriv("hej")')
		self.assertEqual(main("skriv   ('hej')"), 'skriv("hej")')
		self.assertEqual(main("skriv    ('hej')\n"), 'skriv("hej")')

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
		self.assertEqual(lex('$var="a"+matte(1+2)'), [
			['VAR', 'var'],
			['OPERATOR', '='],
			['STRING', 'a'],
			['OPERATOR', '+'],
			['FUNCTION', 'Nummer'],
			['PNUMBER', '1'],
			['OPERATOR', '+'],
			['PNUMBER', '2'],
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
		self.assertEqual(lex('}annars{'), [
			['END', '}'],
			['KEYWORD', 'annars'],
			['START', '{'],
		])
		for operator in ['+', '*', '/', '%', '<', '>', '=', '!', '.', ',', ')']:
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
