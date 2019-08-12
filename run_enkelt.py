# -*- coding: utf-8 -*-

import sys
import re
import os


def check_for_updates(version_nr):
	import urllib.request
	import json
	
	global repo_location
	
	url = repo_location + '/master/VERSION.json'
	
	response = urllib.request.urlopen(url)
	
	data_store = json.loads(response.read())
	
	if data_store['version'] > float(version_nr):
		print('Uppdatering tillgänglig! Du har version ' + str(version_nr) + ' men du kan uppdatera till Enkelt version ' + str(
			data_store['version']))


def has_numbers(input_string):
	return any(char.isdigit() for char in input_string)


class ErrorClass:
	
	def __init__(self, error_msg):
		self.error = error_msg
		self.error_list = error_msg.split()
		self.errors = {
			'SyntaxError': 'Syntaxfel',
			'IndexError': 'Indexfel',
			'TypeError': 'Typfel',
			'ValueError': 'Värdefel',
			'NameError': 'Namnfel',
			'ZeroDivisionError': 'Nolldelningsfel',
			'AttributeError': 'Attributfel'
		}
	
	def set_error(self, new_error_msg):
		self.error = new_error_msg
	
	def get_error_type(self):
		for part in self.errors:
			if 'Error' in part:
				return self.errors[part]
		return ''
	
	def get_error_message_data(self):
		
		from googletrans import Translator
		
		translator = Translator()
		
		error_type = self.get_error_type()
		
		if error_type == '':
			self.set_error(self.error.replace("Traceback (most recent call last):", ''))
			self.set_error(self.error.replace('File "tmp.py", ', ''))
			self.set_error(self.error.replace(", in <module>", ''))
			return translator.translate(self.error, dest = 'sv').text.replace('linje', 'rad')
		
		# Get line number
		for index, item in enumerate(self.error_list):
			if 'line' in item and has_numbers(self.error_list[index + 1]):
				line_index = index + 1
				return error_type + " (rad " + self.error_list[line_index]
		else:
			return error_type


def _import(module):
	import_file = module + ".e" # change to be the path of the code being run

	if os.path.isfile(import_file):
		print("yay")
	else:
		import_file = "libs/" + module + ".e"
		if os.path.isfile(import_file):
			print("yay")

	# do stuff


def parse(lexed, token_index):
	global source_code
	global indent_layers
	global is_if
	global is_math
	global is_for
	global look_for_loop_ending
	
	is_comment = False
	
	forbidden = ['in', 'str', 'int', 'list', 'num']
	
	token_type = str(lexed[token_index][0])
	token_val = lexed[token_index][1]
	
	if indent_layers:
		for indent in indent_layers:
			source_code.append('\t')
	
	if token_type == 'COMMENT':
		source_code.append(token_val)
		is_comment = True
	elif token_type == 'FUNCTION':
		if token_val == 'skriv':
			source_code.append('print(')
		elif token_val == 'matte':
			is_math = True
		elif token_val == 'in':
			source_code.append('input(')
		elif token_val == 'om':
			source_code.append('if ')
			is_if = True
		elif token_val == 'anom':
			source_code.append('elif ')
			is_if = True
		elif token_val == 'Text':
			source_code.append('str(')
		elif token_val == 'Nummer':
			source_code.append('int(')
		elif token_val == 'Flyt':
			source_code.append('float(')
		elif token_val == 'Bool':
			source_code.append('bool(')
		elif token_val == 'längd':
			source_code.append('len(')
		elif token_val == 'töm':
			if os.name == 'nt':
				source_code.append('os.system("cls"')
			elif os.name == 'posix':
				source_code.append('print("\x1b[3J\x1b[H\x1b[2J"')
			else:
				source_code.append('os.system("clear"')
		elif token_val == 'till':
			source_code.append('append(')
		elif token_val == 'bort':
			source_code.append('pop(')
		elif token_val == 'ärnum':
			source_code.append('isdigit(')
		elif token_val == 'sortera':
			source_code.append('sorted(')
		elif token_val == 'slump':
			source_code.append('__import__("random").randint(')
		elif token_val == 'slumpval':
			source_code.append('__import__("random").choice(')
		elif token_val == 'blanda':
			source_code.append('__import__("random").shuffle(')
		elif token_val == 'området':
			source_code.append('range(')
		elif token_val == 'abs':
			source_code.append('abs(')
		elif token_val == 'lista':
			source_code.append('list(')
		elif token_val == 'runda':
			source_code.append('round(')
		elif token_val == 'versal':
			source_code.append('upper(')
		elif token_val == 'gemen':
			source_code.append('lower(')
		elif token_val == 'ersätt':
			source_code.append('replace(')
		elif token_val == 'infoga':
			source_code.append('insert(')
		elif token_val == 'index':
			source_code.append('index(')
		elif token_val == 'dela':
			source_code.append('split(')
		elif token_val == 'foga':
			source_code.append('join(')
		elif token_val == 'typ':
			source_code.append('type(')
		elif token_val == 'sin':
			source_code.append('__import__("math").sin(')
		elif token_val == 'cos':
			source_code.append('__import__("math").cos(')
		elif token_val == 'tan':
			source_code.append('__import__("math").tan(')
		elif token_val == 'potens':
			source_code.append('__import__("math").pow(')
		elif token_val == 'asin':
			source_code.append('__import__("math").asin(')
		elif token_val == 'acos':
			source_code.append('__import__("math").acos(')
		elif token_val == 'atan':
			source_code.append('__import__("math").atan(')
		elif token_val == 'tak':
			source_code.append('__import__("math").ceil(')
		elif token_val == 'golv':
			source_code.append('__import__("math").floor(')
		elif token_val == 'log':
			source_code.append('__import__("math").log(')
		elif token_val == 'kvadratrot':
			source_code.append('__import__("math").sqrt(')
		elif token_val == 'grader':
			source_code.append('__import__("math").degrees(')
		elif token_val == 'radianer':
			source_code.append('__import__("math").radians(')
		elif token_val == 'fakultet':
			source_code.append('__import__("math").factorial(')
		elif token_val == 'datum':
			source_code.append('__import__("datetime").date(')
		elif token_val == 'veckodag':
			source_code.append('weekday(')
		elif token_val == 'för':
			source_code.append('for ')
			is_for = True
			look_for_loop_ending = True
		elif token_val == 'medan':
			source_code.append('while ')
			look_for_loop_ending = True
		elif token_val == 'epok':
			source_code.append('__import__("time").time(')
		elif token_val == 'tid':
			source_code.append('__import__("time").ctime(')
		elif token_val == 'nu':
			source_code.append('__import__("datetime").datetime.now(')
		elif token_val == 'idag':
			source_code.append('__import__("datetime").date.today(')
	elif token_type == 'VAR':
		if token_val not in forbidden:
			source_code.append(token_val)
		else:
			print('Error namnet ' + token_val + " är inte tillåtet som variabelnamn!")
	elif token_type == 'STRING':
		source_code.append('"' + token_val + '"')
	elif token_type == 'PNUMBER' or token_type == 'NNUMBER':
		source_code.append(token_val)
	elif token_type == 'IMPORT':
		_import(token_val)
	elif token_type == 'OPERATOR':
		if is_if and token_val == ')':
			source_code.append('')
			is_if = False
		elif is_math and token_val == ')':
			is_math = False
		elif is_for and token_val == ',':
			is_for = False
		elif look_for_loop_ending and token_val == ')':
			look_for_loop_ending = False
		else:
			source_code.append(token_val)
	elif token_type == 'LIST_START':
		source_code.append('[')
	elif token_type == 'LIST_END':
		source_code.append(']')
	elif token_type == 'START':
		if len(lexed) - 1 == token_index:
			source_code.append(':')
		else:
			source_code.append(':' + '\n')
		indent_layers.append(True)
	elif token_type == 'END':
		indent_layers.pop(-1)
		if len(lexed) - 1 == token_index:
			source_code.append('')
		else:
			source_code.append('\n')
	elif token_type == 'BOOL':
		if token_val == 'Sant':
			source_code.append('True')
		elif token_val == 'Falskt':
			source_code.append('False')
	elif token_type == 'KEYWORD':
		if token_val == 'inom':
			source_code.append(' in ')
		elif token_val == 'bryt':
			source_code.append('break')
		elif token_val == 'fortsätt':
			source_code.append('continue')
		elif token_val == 'returnera':
			source_code.append('return')
		elif token_val == 'inte':
			source_code.append('not ')
		elif token_val == 'passera':
			source_code.append('pass') 
		elif token_val == 'matte_e':
			source_code.append('__import__("math").e')
		elif token_val == 'matte_pi':
			source_code.append('__import__("math").pi')
		elif token_val == 'år':
			source_code.append('year')
		elif token_val == 'månad':
			source_code.append('month')
		elif token_val == 'dag':
			source_code.append('day')
		elif token_val == 'timme':
			source_code.append('hour')
		elif token_val == 'minut':
			source_code.append('minute')
		elif token_val == 'sekund':
			source_code.append('second')
		elif token_val == 'mikrosekund':
			source_code.append('microsecond')
		elif token_val == 'töm':
			if os.name == 'nt':
				source_code.append('os.system("cls")')
			elif os.name == 'posix':
				source_code.append('print("\x1b[3J\x1b[H\x1b[2J")')
			else:
				source_code.append('os.system("clear")')
		elif token_val == 'annars':
			source_code.append('else')
	elif token_type == 'USER_FUNCTION':
		source_code.append('def ' + token_val + '(')
	elif token_type == 'USER_FUNCTION_CALL':
		source_code.append(token_val + '(')
	
	if len(lexed) - 1 >= token_index + 1 and is_comment is False:
		parse(lexed, token_index + 1)


def lex(line):
	if line[0] == '#':
		return ['COMMENT', line]

	global functions
	global user_functions
	operators = ['+', '-', '*', '/', '%', '<', '>', '=', '!', '.', ',', ')', ':']
	tmp = ''
	is_string = False
	is_var = False
	is_function = False
	is_import = False
	lexed_data = []
	last_action = ''
	might_be_negative_num = False
	data_index = -1
	for chr_index, chr in enumerate(line):
		if is_import and chr != ';':
			tmp += chr
		elif is_import and chr == ';':
			lexed_data.append(['IMPORT', tmp])
			is_import = False
			tmp = ''
		if is_function and chr not in operators and chr != '(':
			tmp += chr
		elif is_function and chr == '(':
			lexed_data.append(['USER_FUNCTION', tmp])
			user_functions.append(tmp)
			tmp = ''
			is_function = False
		elif chr == '{':
			lexed_data.append(['START', chr])
		elif chr == '}':
			lexed_data.append(['END', chr])
		elif chr == '#' and is_string is False:
			break
		elif chr.isdigit() and is_string is False and is_var is False:
			if might_be_negative_num or last_action == 'NNUMBER':
				if last_action == 'NNUMBER':
					lexed_data[data_index - 1] = ['NNUMBER', lexed_data[data_index - 1][1] + chr]
				else:
					lexed_data.append(['NNUMBER', '-' + chr])
					data_index += 1
				last_action = 'NNUMBER'
				might_be_negative_num = False
			else:
				if last_action == 'PNUMBER':
					lexed_data[-1] = ['PNUMBER', lexed_data[-1][1] + chr]
				else:
					lexed_data.append(['PNUMBER', chr])
					data_index += 1
				
				last_action = 'PNUMBER'
		elif chr == '-' and is_string is False:
			might_be_negative_num = True
		else:
			last_action = ''
			if chr == '"' and is_string is False:
				is_string = True
				tmp = ''
			elif chr == '"' and is_string:
				is_string = False
				lexed_data.append(['STRING', tmp])
				tmp = ''
			elif is_string:
				tmp += chr
			else:
				if chr == '[' and is_var is False:
					lexed_data.append(['LIST_START', '['])
				elif chr == ']' and is_var is False:
					lexed_data.append(['LIST_END', ']'])
				else:
					if chr == '$':
						is_var = True
						tmp = ''
					elif is_var:
						if chr != ' ' and chr != '=' and chr not in operators and chr != '[' and chr != ']':
							tmp += chr
							if len(line) - 1 == chr_index:
								is_var = False
								lexed_data.append(['VAR', tmp])
								lexed_data.append(['FUNCTION', tmp])
								tmp = ''
						elif chr == '=' or chr in operators:
							is_var = False
							lexed_data.append(['VAR', tmp])
							lexed_data.append(['OPERATOR', chr])
							tmp = ''
						elif chr == '[':
							is_var = False
							lexed_data.append(['VAR', tmp])
							lexed_data.append(['LIST_START', '['])
							tmp = ''
						elif chr == ']':
							is_var = False
							lexed_data.append(['VAR', tmp])
							lexed_data.append(['LIST_END', '['])
							tmp = ''
						elif chr == '{':
							is_var = False
							lexed_data.append(['VAR', tmp])
							lexed_data.append(['START', chr])
							tmp = ''
					elif chr in operators:
						lexed_data.append(['OPERATOR', chr])
					else:
						if tmp == 'Sant' or tmp == 'Falskt':
							lexed_data.append(['BOOL', tmp])
							tmp = ''
						else:
							if chr == '(' and tmp in functions:
								if tmp == 'matte':
									tmp = 'Nummer'
								lexed_data.append(['FUNCTION', tmp])
								tmp = ''
							elif chr == '(' and tmp not in functions and tmp not in user_functions:
								print('ERROR! Funktionen ' + tmp + ' hittades inte!')
								tmp = ''
							elif chr == '(' and tmp in user_functions:
								lexed_data.append(['USER_FUNCTION_CALL', tmp])
								tmp = ''
							else:
								if is_import is False:
									tmp += chr
								if tmp == 'Sant' or tmp == 'Falskt':
									lexed_data.append(['BOOL', tmp])
									tmp = ''
								else:
									if tmp == 'annars':
										lexed_data.append(['KEYWORD', tmp])
										tmp = ""
									elif tmp == 'inom':
										lexed_data.append(['KEYWORD', tmp])
										tmp = ''
									elif tmp == 'bryt':
										lexed_data.append(['KEYWORD', tmp])
										tmp = ''
									elif tmp == 'fortsätt':
										lexed_data.append(['KEYWORD', tmp])
										tmp = ''
									elif tmp == 'def':
										is_function = True
										tmp = ''
									elif tmp == 'returnera':
										lexed_data.append(['KEYWORD', tmp])
										tmp = ''
									elif tmp == 'var' or tmp == 'num':
										is_var = True
										tmp = ''
									elif tmp == 'importera ':
										is_import = True
										tmp = ''
									elif tmp == 'inte':
										lexed_data.append(['KEYWORD', tmp])
										tmp = ''
									elif tmp == 'passera':
										lexed_data.append(['KEYWORD', tmp])
										tmp = ''
									elif tmp == 'matte_pi':
										lexed_data.append(['KEYWORD', tmp])
										tmp = ''
									elif tmp == 'år':
										lexed_data.append(['KEYWORD', tmp])
										tmp = ''
									elif tmp == 'månad':
										lexed_data.append(['KEYWORD', tmp])
										tmp = ''
									elif tmp == 'dag':
										lexed_data.append(['KEYWORD', tmp])
										tmp = ''
									elif tmp == 'timme':
										lexed_data.append(['KEYWORD', tmp])
										tmp = ''
									elif tmp == 'minut':
										lexed_data.append(['KEYWORD', tmp])
										tmp = ''
									elif tmp == 'sekund':
										lexed_data.append(['KEYWORD', tmp])
										tmp = ''
									elif tmp == 'mikrosekund':
										lexed_data.append(['KEYWORD', tmp])
										tmp = ''
									elif tmp == 'töm' and line[-3:] == 'töm':
										lexed_data.append(['KEYWORD', tmp])
										tmp = ''
									elif tmp == 'matte_e':
										lexed_data.append(['KEYWORD', tmp])
										tmp = ''
	
	return lexed_data


def main(statement):
	statement = statement.replace('\n', '').replace('\t', '').replace("'", '"')
	current_line = ''
	is_string = False
	is_import = False

	for chr_index, char in enumerate(statement):
		if char == ' ' and is_string:
			current_line += char
		elif char == ' ' and is_string is False and is_import is False:
			continue
		elif char == ' ' and is_string is False and is_import:
			current_line += char
		elif char == '"' and is_string:
			is_string = False
			current_line += char
		elif char == '"' and is_string is False:
			is_string = True
			current_line += char
		else:
			current_line += char

		if current_line == 'importera':
			is_import = True

	# Legacy removals
	if '.bort[' in current_line:
		current_line = current_line.replace('.bort[', '.bort(')
		
		tmp = ''
		is_index = False
		
		current_line = list(current_line)
		
		for index, text in enumerate(current_line):
			if '.bort(' in tmp and is_index is False:
				tmp = ''
				is_index = True
			elif is_index and text == ']':
				is_index = False
				current_line[index] = ')'
				current_line = ''.join(current_line)
				break
			else:
				tmp += text

	return current_line


def execute():
	global final
	global is_developer_mode
	
	# Inserts necessary code to make importing a temporary python file work.
	code_to_append = "def __Enkelt__():\n\tprint('')\n\n"
	final.insert(0, code_to_append)
	
	# Removes unnecessary tabs
	for line_index, line in enumerate(final):
		tmp_line = list(line)
		chars_started = False
		for char_index, char in enumerate(tmp_line):
			if char != '\t' and char != '\n' and chars_started is False:
				chars_started = True
			elif chars_started and char == '\t' and char_index > 0:
				tmp_line[char_index] = ' '
				
		final[line_index] = ''.join(tmp_line)
	
	# Turn = = into == and ! = into != and + = into +=
	final = list(''.join(final).replace('= =', '==').replace('! =', '==').replace('+ =', '+='))
	
	# Remove empty lines from final
	final = list(re.sub(r'\n\s*\n', '\n\n', ''.join(final)))

	code = ''.join(final)
	
	if is_developer_mode:
		print(code)
	
	# Writes the transpiled code to a file temporarily.
	with open('final_transpiled.py', 'w+')as f:
		f.writelines(code)
	
	# Executes the code transpiled to python and catches Exceptions
	try:
		import final_transpiled
		final_transpiled.__Enkelt__()
	except Exception as e:
		if is_developer_mode:
			print(e)
		
		# Print out error(s) if any
		error = ErrorClass(str(e).replace('(<string>, ', '('))
		print(error.get_error_message_data())
	
	# Removes the temporary python code
	with open('final_transpiled.py', 'w+')as f:
		f.writelines('')


def run(line):
	global source_code
	global is_developer_mode
	global final
	global variables

	if line != '\n':
		data = main(line)
		data = lex(data)

		if is_developer_mode:
			print(data)

		parse(data, 0)
		final.append(''.join(source_code))
		final.append('\n')
		source_code = []


def execute_run_with_code(data):
	global variables
	
	for var in variables[::-1]:
		final.insert(0, var + '\n')
	
	for line_to_run in data:
		line_to_run = line_to_run.replace('£', ',')
		run(line_to_run)
	execute()
	

def run_with_code(data):
	global is_developer_mode
	global final
	global variables
	global tmp_variables
	
	if is_developer_mode is False and tmp_variables != []:
		# Variable setup
		variables = tmp_variables
		tmp_variables = []

	execute_run_with_code(data)


def console_line_runner(code):
	global variables
	global is_developer_mode
	
	is_developer_mode = False
	
	with open('.enkelt_tmp_source.txt', 'w+')as f:
		f.writelines(str([[code], variables]))

	os.system('python3 run_enkelt.py  --run')
	
	
def start_console(first):
	global version
	global is_developer_mode
	global variables
	global source_code
	
	if first:  # is first console run
		# Checks for updates:
		check_for_updates(version)
		# Print info
		print('Enkelt ' + str(version) + ' © 2018-2019 Edvard Busck-Nielsen' + ". GNU GPL v.3")
		print('Tryck Ctrl+C för att avsluta')
	
	code_line = input('Enkelt >> ')
	if code_line != '':
		test = main(code_line)
		test = lex(test)
		
		if code_line != 'töm' and code_line != 'töm()' and code_line != 'töm ()' and test[0][0] != 'VAR':
			console_line_runner(code_line)
			
		elif code_line == 'töm' or code_line == 'töm()' or code_line == 'töm ()':
			if not os.name == 'nt':
				os.system('clear')
			else:
				os.system('cls')
		else:
			parse(test, 0)
			variables.append(''.join(source_code))
			
	source_code = []
	start_console(False)


def web_editor_runner(event):
	global variables
	
	data = ''
	# These lines should be commented-out
	# data = document["inputCode"].value
	# data = data.split('\n')
	
	variables = []
	execute_run_with_code(data)


# ----- SETUP -----

# Global variable setup
is_list = False
is_if = False
is_math = False
is_for = False
look_for_loop_ending = False

# --- SPECIAL --->
is_web_editor = False
# --- DO NOT CHANGE! --->

source_code = []
indent_layers = []

functions = [
	'skriv',
	'matte',
	'till',
	'bort',
	'töm',
	'om',
	'anom',
	'längd',
	'in',
	'Text',
	'Nummer',
	'Flyt',
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

]
user_functions = []

is_developer_mode = False
version = 3.0
repo_location = 'https://raw.githubusercontent.com/Buscedv/Enkelt/'

final = []
variables = []

tmp_variables = []


if is_web_editor is False:
	# Gets an env. variable to check if it's a test run.
	is_dev = os.getenv('ENKELT_DEV', False)
	
	# ----- START -----
	if not is_dev:
		# Runs code from file or console-style
		if len(sys.argv) >= 2:
			tmp = ''
			with open('.enkelt_tmp_source.txt', 'r+')as f:
				tmp = f.readlines()[0]
				
			with open('.enkelt_tmp_source.txt', 'w+')as f:
				f.writelines('')
			
			import ast
			
			tmp = ast.literal_eval(tmp)
			tmp_code_to_run = tmp[0]
			tmp_variables = tmp[1]
			
			while '' in tmp_code_to_run:
				tmp_code_to_run.pop(tmp_code_to_run.index(''))

			run_with_code(tmp_code_to_run)
			# Checks for updates:
			check_for_updates(version)
		else:
			variables = []
			final = []
			start_console(True)
