def parse(code, token_index):
	import os
	global variables
	token_type = code[token_index][0]
	token_val = code[token_index][1]

	calculation = 0
	last_action = ''

	if token_type == 'FUNCTION':
		if token_val == 'skriv':
			output = str(parse(code, token_index+1))
			if output is None:
				print('Ogiltig')
			elif output is True:
				print('Sant')
			elif output is False:
				print('Falskt')
			else:
				print(output)
		elif token_val == 'töm':
			os.system('clear')
		elif token_val == 'matte':
			calculation = 0
			last_action = ''
			while len(code)-1 >= token_index+1:
				if code[token_index+1][0] == 'PNUMBER' or code[token_index+1][0] == 'NNUMBER' or code[token_index+1][0] == 'OPERATOR':
					token_index += 1
					if last_action == '' and calculation == 0:
						calculation = int(code[token_index][1])
					elif last_action == '' and code[token_index][0] != 'OPERATOR':
						tmp_calculation = str(calculation)+code[token_index][1]
						calculation = int(tmp_calculation)
					elif code[token_index][0] == 'OPERATOR':
						last_action = code[token_index][1]
					elif code[token_index][0] == 'PNUMBER':
						if last_action == '+':
							calculation = calculation + int(code[token_index][1])
							last_action = ''
						elif last_action == '-':
							calculation = calculation - int(code[token_index][1])
							last_action = ''
						elif last_action == '*':
							calculation = calculation * int(code[token_index][1])
							last_action = ''
				else:
					break

			return calculation
		elif token_val == 'in':
			if len(code)-1 >= token_index+1:
				title = parse(code, token_index+1)
				return input(title)
			else:
				return input()
		elif token_val == 'längd':
			if len(code)-1 >= token_index+1:
				data = parse(code, token_index+1)
				return len(data)
			else:
				return None
	elif token_type == 'STRING':
		if len(code)-1 >= token_index+1:
			if code[token_index+1][0] == 'OPERATOR':
				return token_val+str(parse(code, token_index+1))
			else:
				return token_val
		else:
			return token_val
	elif token_type == 'PNUMBER' or token_type == 'NNUMBER':
		if len(code) - 1 >= token_index + 1:
			if code[token_index + 1][0] == 'OPERATOR':
				return token_val + str(parse(code, token_index + 1))
		else:
			return token_val
	elif token_type == 'VAR':
		if len(code)-1 >= token_index+1:
			if code[token_index+1][0] == 'OPERATOR' and code[token_index+1][1] == '=':
				variables[token_val] = parse(code, token_index+2)
			else:
				return_val = variables[token_val]
				token_index += 1
				while len(code)-1 >= token_index and code[token_index][1] == '+':
					return_val += str(parse(code, token_index+1))
					token_index += 1
				return return_val
		else:
			return variables[token_val]
	elif token_type == 'BOOL':
		if token_val == 'Sant':
			return True
		elif token_val == 'Falskt':
			return False
	elif token_type == 'OPERATOR':
		if token_val == '+' and len(code)-1 >= token_index+1:
			return parse(code, token_index+1)
	elif token_type == 'LIST_START':
		print('list starts here')


def lex(line):
	functions = ['skriv', 'matte', 'till', 'bort', 'töm', 'om', 'annars', 'anom', 'längd', 'in']
	operators = ['+', '-', '*', '/', '%', '<', '>', '=', '!', '.', ',']
	tmp = ''
	is_string = False
	is_var = False
	is_list = False
	data = []
	last_action = ''
	might_be_negative_num = False
	data_index = -1
	for chr_index, chr in enumerate(line):
		if chr == '{':
			data.append(['START', chr])
		elif chr == '}':
			data.append(['END', chr])
		elif chr == '#' and is_string is False:
			break
		elif chr.isdigit() and is_string is False:
			if might_be_negative_num or last_action == 'NNUMBER':
				if last_action == 'NNUMBER':
					data[data_index-1] = ['NNUMBER', data[data_index-1][1]+chr]
				else:
					data.append(['NNUMBER', '-'+chr])
					data_index += 1
				last_action = 'NNUMBER'
				might_be_negative_num = False
			else:
				if last_action == 'PNUMBER':
					data[data_index-1] = ['PNUMBER', data[data_index-1][1]+chr]
				else:
					data.append(['PNUMBER', chr])
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
				data.append(['STRING', tmp])
				tmp = ''
			elif is_string:
				tmp += chr
			else:
				if chr == '[' and is_list is False:
					is_list = True
					data.append(['LIST_START', '['])
				elif chr == ']' and is_list:
					is_list = False
					data.append(['LIST_END', ']'])
				else:
					if chr == '$':
						is_var = True
						tmp = ''
					elif is_var:
						if chr != ' ' and chr != '=' and chr not in operators and chr != ')':
							tmp += chr
						elif chr == '=' or chr == ')' or chr in operators:
							is_var = False
							data.append(['VAR', tmp])
							data.append(['OPERATOR', chr])
							tmp = ''
					elif chr in operators:
						if is_var:
							is_var = False
							data.append(['VAR', tmp])
							tmp = ''
						elif is_list and chr == ',':
							continue
						else:
							data.append(['OPERATOR', chr])
					else:
						if tmp == 'Sant' or tmp == 'Falskt':
							data.append(['BOOL', tmp])
							tmp = ''
						else:
							if chr == "(" and tmp in functions:
								data.append(['FUNCTION', tmp])
								tmp = ""
							elif chr == "(" and tmp not in functions:
								print("ERROR! Funktionen "+tmp+" hittades inte!")
								tmp = ""
							else:
								tmp += chr
								if tmp == 'Sant' or tmp == 'Falskt':
									data.append(['BOOL', tmp])
									tmp = ''

	return data


def main(statement):
	statement = statement.replace('\n', '').replace('\t', '').replace("'", '"')
	current_line = ''
	is_string = False
	for chr_index, chr in enumerate(statement):
		if chr == ' ' and is_string:
			current_line += chr
		elif chr == ' ' and is_string is False:
			continue
		elif chr == '"' and is_string:
			is_string = False
			current_line += chr
		elif chr == '"' and is_string is False:
			is_string = True
			current_line += chr
		else:
			current_line += chr

	return current_line


variables = {}
with open('EX/test.e', 'r') as f:
	data = f.readlines()
for line in data:
	if line != '\n' and line[0] != '#':
		data = main(line)
		data = lex(data)
		parse(data, 0)
