# coding=utf-8

# Enkelt 5.0
# Copyright 2018, 2019, 2020 Edvard Busck-Nielsen
# This file is part of Enkelt.
#
#     Enkelt is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     Enkelt is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with Enkelt.  If not, see <https://www.gnu.org/licenses/>.


from sys import argv, version_info
from os import system, getcwd, path, name
from collections import abc
import urllib.request

# ############################################### #
# Modules Used When Executing The Transpiled Code #
# ############################################### #


def enkelt_print(data):
	print(translate_output_to_swedish(data))


def enkelt_input(prompt=''):
	tmp = input(prompt)

	try:
		tmp = int(tmp)
		return tmp
	except ValueError:
		try:
			tmp = float(tmp)
			return tmp
		except ValueError:
			return str(tmp)


# ################################################################## #
# Helper Methods for Modules Used When Executing the Transpiled Code #
# ################################################################## #

def translate_output_to_swedish(data):
	if isinstance(data, abc.KeysView):
		data = list(data)

	replace_dict = {
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
		"<class 'IngetType'>": 'Inget',
		"<class 'Exception'>": 'Feltyp',
		"<class 'datetime.date'>": 'Datum',
		"<class 'datetime.datetime'>": 'Datum & tid',
		"<class 'range'>": 'Område'
	}

	data = str(data)
	for key in replace_dict:
		data = data.replace(key, replace_dict[key])

	return data


def translate_error(error_msg):
	error_msg = error_msg.args[0]

	translations = {
		'unmatched': 'Syntaxfel, ' + error_msg[-3:] + ' saknas!',
		'division by zero': 'Nolldelningsfel!',
		'index': 'Indexfel!',
		'key': 'Nyckelfel!',
		'lookup': 'Sökfel!',
		'attribute': 'Attribut/Parameterfel!',
		'unexpected EOF': 'Oväntat programslut!',
		'result too large': 'Resultatet för stort!',
		'import': 'Importeringsfel!',
		'module': 'Modulfel',
		'syntax': 'Syntaxfel',
		'KeyboardInterrupt': 'Avbruten!',
		'memory': 'Minnefel!',
		'name': 'Namnfel!',
		'recursion': 'Rekursionsfel',
		'argument': 'Argumentfel!',
		'type': 'Typfel!',
		'referenced before': 'Referensfel!',
		'unicode': 'Unicode-fel!',
		'value': 'Värdefel!',
		'file': 'Filfel!',
		'timeout': 'Avbrottsfel!',
		'warning': 'Varning!',
	}

	sv_error_message = ''

	for key in translations.keys():
		if key in error_msg:
			sv_error_message = translations[key]

	if not sv_error_message:
		sv_error_message = 'Fel! ENG: ' + error_msg

	return sv_error_message


# ############ #
# Main Methods #
# ############ #

def check_for_updates(version):
	import json

	repo_location = 'https://raw.githubusercontent.com/Enkelt/Enkelt/'

	url = repo_location + '/master/VERSION.json'

	response = urllib.request.urlopen(url)

	data_store = json.loads(response.read())

	if data_store['version'] > float(version):
		print('Uppdatering tillgänglig! Du har version ' + str(
			version) + ' men du kan uppdatera till Enkelt version ' + str(data_store['version']))


def transpile_var(var):
	vars = {
		'själv': 'self',
	}

	try:
		return vars[var]
	except KeyError:
		return var


def maybe_place_space_before(parsed, token_val):
	prefix = ' '

	if parsed:
		if parsed[-1] in ['\n', '\t', '(', ' ', '.']:
			prefix = ''
	parsed += prefix + token_val + ' '

	return parsed


def translate_function(func):
	function_translations = functions_and_keywords()['functions']

	translation = function_translations[func] if func in function_translations.keys() else func
	if 'system("c' not in translation:
		translation += '('

	return translation


def translate_keyword(keyword):
	keyword_translations = functions_and_keywords()['keywords']

	return keyword_translations[keyword] if keyword in keyword_translations.keys() else 'error'


# Transpiles the source code of the library being imported.
def transpile_library_code(library_code, library_name):
	global is_extension
	global additional_library_code

	source_code = library_code

	if not is_extension:
		source_code = lexer(library_code)
		source_code = parser(source_code)
		source_code = source_code.split('\n')

	class_boilerplate_for_library = 'class ' + library_name + ':\n'
	for line in source_code:
		if line:
			if line[-1] != '\n':
				class_boilerplate_for_library += '\n'

		class_boilerplate_for_library += '\t' + line

	additional_library_code = class_boilerplate_for_library

	is_extension = False


def maybe_load_from_file_then_transpile(file_or_code, is_file, library_name):
	library_code = file_or_code

	if is_file:
		with open(file_or_code) as library_file:
			library_code = library_file.readlines()

	while '' in library_code:
		library_code.pop(library_code.index(''))

	transpile_library_code(library_code, library_name)


# Fetches the source code of the remote library being imported.
def load_library_from_remote(url, library_name):
	response = urllib.request.urlopen(url)
	library_code = response.read().decode('utf-8')

	library_code = library_code.split('\n')

	maybe_load_from_file_then_transpile(library_code, False, library_name)


def import_library(library_name):
	from urllib.error import HTTPError

	global source_file_name
	global is_extension
	global additional_library_code

	web_import_location = 'https://raw.githubusercontent.com/Enkelt/EnkeltWeb/master/bibliotek/bib/'

	# Checks if the library is user-made (i.e. local not remote).
	import_file = ''.join(source_file_name.split('/')[:-1]) + '/' + library_name + '.e'

	if path.isfile(import_file):
		maybe_load_from_file_then_transpile(import_file, True, library_name)
	else:
		# The library might be a local extension (.epy file)
		import_file += 'py'
		if path.isfile(import_file):
			is_extension = True
			maybe_load_from_file_then_transpile(import_file, True, library_name)

		# The library might be remote (i.e. needs to be fetched)
		else:
			url = web_import_location + library_name + '.e'

			try:
				load_library_from_remote(url, library_name)
			except HTTPError:
				# The library might be a remote extension (.epy file)
				url += 'py'
				is_extension = True

				try:
					load_library_from_remote(url, library_name)
					return additional_library_code
				except HTTPError:
					print('Det inträffade ett fel! Kunde inte importera ' + library_name)


def parser(tokens):
	global built_in_vars

	is_skip = False

	parsed = ''

	for token_index, token in enumerate(tokens):
		if is_skip:
			is_skip = False
			continue

		token_type = token[0]
		token_val = token[1]

		if token_type in ['FORMAT', 'ASSIGN', 'NUM']:
			parsed += token_val
		elif token_type == 'OP':
			if token_val in ['.', ')', ',', ':'] and parsed:
				if parsed[-1] == ' ':
					parsed = parsed[:-1]

			parsed += token_val

			if token_val in [',', '=', '%']:
				parsed += ' '
		elif token_type == 'STR':
			token_val = token_val.replace('|-ENKELT_ESCAPED_BACKSLASH-|', '\\').replace('|-ENKELT_ESCAPED_QUOTE-|', '\\"')
			parsed += '"' + token_val + '"'
		elif token_type == 'IMPORT':
			import_library(token_val)
		elif token_type == 'KEYWORD':
			token_val = translate_keyword(token_val)
			parsed = maybe_place_space_before(parsed, token_val)
		elif token_type == 'VAR':
			if token_val not in built_in_vars:
				parsed = maybe_place_space_before(parsed, token_val)
			else:
				parsed += transpile_var(token_val)
		elif token_type == 'FUNC':
			token_val = translate_function(token_val)
			parsed += token_val
		elif token_type == 'CLASS':
			parsed += '\nclass ' + token_val
		elif token_type == 'OBJ_NOTATION':
			parsed += '\n' + translate_keyword(token_val) + ':'
		elif token_type == 'FUNC_DEF':
			parsed += 'def ' + token_val + '('
		elif token_type == 'KEY':
			parsed += '\'' + token_val + '\''

		if len(parsed) > 3:
			if parsed[-1] == ' ' and parsed[-2] == '=' and parsed[-3] == ' ' and parsed[-4] == '=':
				parsed = parsed[:-4]
				parsed += ' == '

	return parsed


def lex_var_keyword(tokens, tmp):
	global variables
	global keywords
	global special_keywords

	collect = False
	collect_ends = []
	include_collect_end = False

	if tmp:
		if tmp in keywords:
			tokens.append(['KEYWORD', tmp])
			tmp = ''
		elif tmp in special_keywords.keys():
			tokens.append([special_keywords[tmp]['type'], tmp])
			collect = special_keywords[tmp]['collect']
			collect_ends = special_keywords[tmp]['collect_ends']
			include_collect_end = special_keywords[tmp]['include_collect_end']
			tmp = ''
		else:
			tokens.append(['VAR', tmp])
			tmp = ''

	return tokens, tmp, collect, collect_ends, include_collect_end


def lexer(raw):
	tmp = ''
	is_collector = False
	collector_ends = []
	include_collector_end = False
	is_dict = []

	global keywords
	global operators
	global variables

	tokens = []

	for line in raw:
		line = fix_up_code_line(line)
		for char_index, char in enumerate(line):
			if char == '#':
				break

			if is_collector:
				if char not in collector_ends:
					tmp += char
				else:
					tokens[-1][1] = tmp

					if include_collector_end:
						tokens.append(['OP', char])

					is_collector = False
					include_collector_end = False
					tmp = ''

			elif char == '(':
				if tmp:
					if len(tmp) > 3:
						if tmp[:3] == 'def':
							tokens.append(['FUNC_DEF', tmp[3:]])
							tmp = ''
							continue

					tokens.append(['FUNC', tmp])
					tmp = ''
			elif char == '=':
				if tmp:
					tokens.append(['VAR', tmp])
					tokens.append(['ASSIGN', char])

					if tmp not in variables:
						variables.append(tmp)

					tmp = ''
				else:
					tokens.append(['OP', char])
			elif char in ['"', '\'']:
				is_collector = True
				collector_ends = ['"', '\'']
				include_collector_end = False
				tmp = ''
				tokens.append(['STR', ''])
			elif char == '{':
				is_dict.append(True)
				tokens.append(['OP', char])
			elif char == '}':
				is_dict.pop(0)
				tokens.append(['OP', char])
			elif char.isdigit() and not tmp:
				if tokens:
					if tokens[-1][0] == 'NUM':
						tokens[-1][1] += char
						continue
				tokens.append(['NUM', char])
			elif char == '&':
				is_collector = True
				collector_ends = ['\n']
				include_collector_end = True
				tmp = ''
				tokens.append(['DEC', ''])
			elif char in operators:
				if char == ':' and is_dict and tmp:
					tokens.append(['KEY', tmp])
					tmp = ''
				else:
					tokens, tmp, is_collector, collector_ends, include_collector_end = lex_var_keyword(tokens, tmp)

				tokens.append(['OP', char])
			elif char not in ['\n', '\t', ' ']:
				tmp += char
			elif char in ['\n', '\t']:
				tokens, tmp, is_collector, collector_ends, include_collector_end = lex_var_keyword(tokens, tmp)
				tokens.append(['FORMAT', char])
			else:
				tokens, tmp, is_collector, collector_ends, include_collector_end = lex_var_keyword(tokens, tmp)
	return tokens


def fix_up_code_line(statement):
	statement = statement.replace("'", '"') \
		.replace('\\"', '|-ENKELT_ESCAPED_QUOTE-|') \
		.replace('\\', '|-ENKELT_ESCAPED_BACKSLASH-|')

	current_line = ''
	is_string = False

	for char in statement:
		if char == ' ' and not is_string:
			continue
		elif char == '"':
			is_string = not is_string
		current_line += char

	return current_line


def build(tokens):
	global additional_library_code

	parsed = parser(tokens)

	parsed = '\n' + ''.join(additional_library_code) + parsed

	boilerplate = "from os import system\nimport enkelt5 as Enkelt\ndef __enkelt__():\n\tprint('', end='')\n"
	parsed = boilerplate + parsed

	fixed_code = ''

	lines = parsed.split('\n')

	for line_index, line in enumerate(lines):
		line += '\n'

		if line_index < 5:
			fixed_code += line
			continue

		if line:
			line = '\t' + line
		fixed_code += line

	if is_dev:
		print('--DEV: FINAL TRANSPILED CODE')
		print(fixed_code)

	with open('final_transpiled.py', 'w+', encoding='utf-8') as f:
		f.write('')
		f.write(fixed_code)

	# final_transpiled is a module generated by this script, line 454 will always show an error.
	import final_transpiled
	final_transpiled.__enkelt__()


def startup(file_name):
	global version_nr
	global is_dev

	with open(file_name, encoding='utf-8') as f:
		source_lines = f.readlines()

	source_lines.insert(0, '\n')

	tokens_list = lexer(source_lines)

	if is_dev:
		print('--DEV: TOKENS LIST')
		for token in tokens_list:
			print(token)

	if tokens_list:
		build(tokens_list)
	else:
		print('Filen är tom!')

	check_for_updates(version_nr)


def translate_clear():
	if name == 'nt':
		return 'cls'
	return 'clear'


def functions_and_keywords():
	return {
		'functions': {
			'skriv': 'Enkelt.enkelt_print',
			'in': 'Enkelt.enkelt_input',
			'Sträng': 'str',
			'Heltal': 'int',
			'Decimal': 'float',
			'Lista': 'list',
			'Bool': 'bool',
			'längd': 'len',
			'till': 'append',
			'bort': 'pop',
			'sortera': 'sorted',
			'slump': '__import__("random").randint',
			'slumpval': '__import__("random").choice',
			'blanda': '__import__("random").shuffle',
			'området': 'range',
			'lista': 'list',
			'ärnum': 'isdigit',
			'runda': 'round',
			'versal': 'upper',
			'gemen': 'lower',
			'ärversal': 'isupper',
			'ärgemen': 'islower',
			'ersätt': 'replace',
			'infoga': 'insert',
			'index': 'index',
			'dela': 'split',
			'foga': 'join',
			'typ': 'type',
			'läs': 'read',
			'öppna': 'with open',
			'överför': 'write',
			'veckodag': 'weekday',
			'värden': 'values',
			'element': 'elements',
			'numrera': 'enumerate',
			'töm': 'system("' + translate_clear() + '"',
			'kasta': 'raise Exception',
			'nycklar': 'keys',
		},
		'keywords': {
			'för': 'for',
			'medan': 'while',
			'Sant': 'True',
			'Falskt': 'False',
			'Inget': 'None',
			'inom': 'in',
			'bryt': 'break',
			'fortsätt': 'continue',
			'returnera': 'return ',
			'passera': 'pass',
			'år': 'year',
			'månad': 'month',
			'dag': 'day',
			'timme': 'hour',
			'minut': 'minute',
			'sekund': 'second',
			'mikrosekund': 'microsecond',
			'global': 'global',
			'om': 'if',
			'annars': 'else',
			'anom': 'elif',
			'och': 'and',
			'eller': 'or',
			'som': 'as',
			'försök': 'try',
			'fånga': 'except Exception as',
			'slutligen': 'finally',
			'>': 'lambda',
		},
	}


# Globals
built_in_vars = ['själv']
variables = built_in_vars
keywords = functions_and_keywords()['keywords']
special_keywords = {
	'klass': {
		'type': 'CLASS',
		'collect': True,
		'collect_ends': [':'],
		'include_collect_end': True
	},
	'def': {
		'type': 'FUNC_DEF',
		'collect': True,
		'collect_ends': ['('],
		'include_collect_end': False
	},
	'försök': {
		'type': 'OBJ_NOTATION',
		'collect': True,
		'collect_ends': [':'],
		'include_collect_end': True
	},
	'fånga': {
		'type': 'OBJ_NOTATION',
		'collect': True,
		'collect_ends': [':'],
		'include_collect_end': False
	},
	'slutligen': {
		'type': 'OBJ_NOTATION',
		'collect': True,
		'collect_ends': [':'],
		'include_collect_end': False
	},
	'importera': {
		'type': 'IMPORT',
		'collect': True,
		'collect_ends': ['\n'],
		'include_collect_end': False
	}
}
operators = [':', ')', '!', '+', '-', '*', '/', '%', '.', ',', '[', ']', '&']

source_file_name = ''

is_extension = False
additional_library_code = []

version_nr = 5.0

is_dev = False

# Start
if __name__ == '__main__':
	try:
		if version_info[0] < 3:
			raise Exception("Du måste använda Python 3 eller högre")

		if len(argv) > 1:
			if len(argv) > 2:
				flag = argv[2]
				if flag == '--d':
					is_dev = True

			source_file_name = argv[1]
			if path.isfile(getcwd() + '/' + source_file_name):
				startup(source_file_name)
			else:
				print('Filen kunde inte hittas!')
		else:
			print('Ingen fil specifierad!')
	except Exception as e:
		print(translate_error(e))
