# Enkelt: Programming Language
# Enkelt: Programeringsspråk
# A simple programming language with Swedish syntax.
# Ett simpelt programeringspråk med Svensk syntax.
# https://buscedv.github.io/Enkelt
# 2.5

# Edvard Busck-Nielsen, hereby disclaims all copyright interest in the program “Enkelt” (which is a programming language with swedish syntax) written by Edvard Busck-Nielsen.

# signature of Edvard Busck-Nielsen 11 December 2018
# Edvard Busck-Nielsen, Developer of Enkelt

# © Copyright 2018, 2019 Edvard Busck-Nielsen

# This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
import os



def interpreter(code):

	global global_if
	global global_is_if
	global global_if_history
	global global_is_an
	global global_an_history
	can_continue = True

	for i, line in enumerate(code):
		if "$" in line and ".till" in line and "(" in line and ")" in line:
			list_add(line, i)
		elif "$" in line and ".bort" in line and "[" in line and "]" in line:
			list_remove(line, i)
		cmd = ""
		i = i+1
		if cmd == "}" or "}" in line:
			if global_is_if:
				global_is_if = False
				global_if_history = True
				cmd = ""
			elif global_is_an:
				global_is_an = False
				global_an_history == True
				global_if_history = True
				cmd = ""
			continue
		if (
				global_is_if == False and global_is_an == False or
				global_is_if and global_if or
				global_is_an and global_if == False and global_if_history or
				global_if == False and "annars" in line or
				global_is_if and global_if and global_is_an

			):
				for chr in line:
					if cmd == "#":
						cmd = ""
						break
					elif cmd == "töm":
						os.system('clear')
						cmd = ""
						break
					elif cmd == "skriv" and ")" in line and "(" in line:
						print(print_func(line, i))
						cmd = ""
						break
					elif cmd == "var" and "=" in line:
						var_func(line, i)
						cmd = ""
						break
					elif cmd == "matte" and "(" in line and ")" in line:
						print (math_func(line, i))
						cmd = ""
						break
					elif cmd == "om" and "(" in line and ")" in line:
						if_func(line, i)
						cmd = ""
						break
					elif cmd == "annars" and global_if_history:
						annars_func(line, i)
						cmd = ""
						break
					elif cmd == "längd" and "(" in line and ")" in line and "var" not in line and "=" not in line:
						print (lenght_func(line, i))
						cmd = ""
						break
					else:
						if chr != " ":
							cmd += chr
							if cmd == "#":
								cmd = ""
								break
							elif cmd == "töm":
								os.system('clear')
								cmd = ""
								break
							elif cmd == "skriv" and ")" in line and "(" in line:
								print(print_func(line, i))
								cmd = ""
								break
							elif cmd == "var" and "=" in line:
								var_func(line, i)
								cmd = ""
								break
							elif cmd == "matte" and "(" in line and ")" in line:
								print (math_func(line, i))
								cmd = ""
								break
							elif cmd == "om" and "(" in line and ")" in line:
								if_func(line, i)
								cmd = ""
								break
							elif cmd == "annars" and global_if_history:
								annars_func(line, i)
								cmd = ""
								break
							elif cmd == "längd" and "(" in line and ")" in line:
								print (lenght_func(line, i))
								cmd = ""
								break
				continue

		else:
			continue

def lenght_func(code, line):
	lex_data = False
	data1 = ""
	data = ""
	for chr in code:
		if lex_data:
			if chr == ")":
				break
			data1 += chr
		elif chr == "(":
			lex_data = True
	if data1[0] == "$":
		for chr in data1:
			if chr != " " and chr != "$":
				data += chr
		if data in Global_Variables:
			data = Global_Variables[data]
		else:
			print ("Error linje "+str(line)+" variabeln '"+data+"' hittades inte!")
			return "error!"
	elif data1[0] == '"':
		for chr in data1:
			if chr != '"':
				data += chr
	else:
		data = data1
	return len(data)

def list_remove(code, line):
	get_list_name = False
	get_cmd = False
	get_item = False
	cmd = ""
	list_name = ""
	index = ""
	the_list = []

	for chr in code:
		if get_item:
			if chr != " ":
				if chr == "]":
					break
				else:
					index += chr

		elif get_cmd:
			if chr == "[":
				get_item = True
				get_cmd = False
			elif chr != " ":
				cmd += chr
		elif get_list_name:
			if chr == ".":
				get_cmd = True
				get_list_name = False
			elif chr != " ":
				list_name += chr
		elif chr == "$":
			get_list_name = True
	if index[0] == "$":
		if index[1:] in Global_Variables:
			index = Global_Variables[index[1:]]
		else:
			print ("Error linje "+str(line)+" variabeln '"+index[1:]+"' hittades inte!")
	if list_name in Global_Variables:
		the_list = Global_Variables[list_name]
	else:
		print ("Error linje "+str(line)+" variabeln '"+list_name+"' hittades inte!")

	del the_list[int(index)]


def list_add(code, line):
	get_list_name = False
	get_cmd = False
	get_item = False
	get_var_item = False
	get_string_item = False
	cmd = ""
	list_name = ""
	list_item = ""
	the_list = []

	for chr in code:
		if get_var_item:
			if chr == ")":
				if list_item in Global_Variables:
					list_item = Global_Variables[list_item]
				else:
					print ("Error linje "+str(line)+" variabeln '"+list_item+"' hittades inte!")
				break
			elif chr != " ":
				list_item += chr
		elif get_string_item:
			if chr == '"':
				break
			else:
				list_item += chr
		elif get_item:
			if chr != ")":
				if chr == '"':
					get_string_item = True
					get_item = False
				elif chr == "$":
					get_var_item = True
					get_item = False
				else:
					if chr == ")":
						break
					else:
						list_item += chr

		elif get_cmd:
			if chr == "(":
				get_item = True
				get_cmd = False
			elif chr != " ":
				cmd += chr
		elif get_list_name:
			if chr == ".":
				get_cmd = True
				get_list_name = False
			elif chr != " ":
				list_name += chr
		elif chr == "$":
			get_list_name = True
	if list_name in Global_Variables:
		the_list = Global_Variables[list_name]
		the_list.append(list_item)
	else:
		print ("Error linje "+str(line)+" variabeln '"+list_name+"' hittades inte!")

def annars_func(code, line):
	global global_is_an
	global global_an_history
	global_is_an = True
	global_an_history = True

def parse_expr(expr, line):
	first = ""
	first1 = ""
	second = ""
	second1 = ""
	evaluation = ""
	index = ""
	the_list = ""
	list_name = ""
	lex_second = False
	found_string = False
	result = False

	first_var_stat = False
	second_var_stat = False
	lex_index = False

	if "=" not in expr and "!" not in expr and "<" not in expr and ">" not in expr and "$" in expr:
		if expr[1:] in Global_Variables:
			if Global_Variables[expr[1:]] == "Sant":
				return (True)
		else:
			print ("Error linje "+str(line)+" variabeln '"+expr[1:]+"' hittades inte!")
			return (False)

	for chr in expr:
		if lex_second:
			if found_string and chr == '"':
				continue
			elif found_string == False and chr == '"':
				found_string = True
			elif found_string:
				second += chr
			elif chr != " ":
				second += chr
		elif chr == "=" or chr == "!" or chr == "<" or chr == ">":
			evaluation += chr
			lex_second = True
		else:
			first += chr
	if first[0] == "$":
		for chr in first:
			if chr != " ":
				first1 += chr
		first = ""
		for chr in first1:
			first += chr
		first_var_stat = True
		if "[" in first and "]" in first:
			for chr in first:
				if lex_index and chr != " " and chr != "]":
					index += chr
				elif chr == "[":
					lex_index = True
				elif chr == "]":
					lex_index = False
				elif chr != " ":
					list_name += chr
			if list_name[1:] in Global_Variables:
				the_list = Global_Variables[list_name[1:]]
				first = the_list[int(index)]
			else:
				print ("Error linje "+str(line)+" variabeln '"+list_name[1:]+"' hittades inte!")
		else:
			if first[1:] in Global_Variables:

				first = Global_Variables[first[1:]]
			else:
				print ("Error linje "+str(line)+" variabeln '"+first[1:]+"' hittades inte!")
	if second[0] == "$":
		for chr in second:
			if chr != " ":
				second1 += chr
		second = ""
		for chr in second1:
			second += chr
		second_var_stat = True
		if "[" in second and "]" in second:
			for chr in second:
				if lex_index and chr != " ":
					index += chr
				elif chr == "[":
					lex_index = True
				elif chr == "]":
					lex_index = False
				elif chr != " ":
					list_name += chr
			if list_name[1:] in Global_Variables:
				the_list = Global_Variables[list_name[1:]]
				second = the_list[int(index)]
			else:
				print ("Error linje "+str(line)+" variabeln '"+list_name[1:]+"' hittades inte!")
		else:
			if second[1:] in Global_Variables:
				second = Global_Variables[second[1:]]
			else:
				print ("Error linje "+str(line)+" variabeln '"+second[1:]+"' hittades inte!")

	if evaluation == "=":
		if str(first) == str(second):
			result = True
		else:
			result = False
	elif evaluation == "!":
		if str(first) != str(second):
			result = True
		else:
			result = False
	elif evaluation == "<":
		if int(first) < int(second):
			result = True
		else:
			result = False
	elif evaluation == ">":
		if int(first) > int(second):
			result = True
		else:
			result = False
	return result



def if_func(code, line):
	cmd = ""
	lex_expr = False
	get_exp = False
	expression = ""
	boolean = False


	global global_if
	global global_is_if
	global global_if_history
	global global_an_history

	for chr in code:
		if lex_expr:
			if get_exp:
				if chr == ")":
					break
				else:
					expression += chr
			elif chr == "(":
				get_exp = True
		elif cmd == "om":
			lex_expr = True
		elif chr != " ":
			cmd += chr
			if cmd == "om":
				lex_expr = True
	boolean = parse_expr(expression, line)

	if boolean:
		global_if = True
	else:
		global_if = False
	global_is_if = True
	global_if_history = True
	global_an_history = False


def math_parse(num1, expr, num2, line):
	num1_var = False
	num2_var = False
	result = 0

	if num1[0] == "$":
		num1_var = True
	if num2[0] == "$":
		num2_var = True
	if expr == "+":
		if num1_var == False and num2_var == False:
			result = int(num1)+int(num2)
			return result
		elif num1_var == True and num2_var == True:
			if num1[1:] in Global_Variables and num2[1:] in Global_Variables:
				num1 = Global_Variables[num1[1:]]
				num2 = Global_Variables[num2[1:]]
				result = int(num1)+int(num2)
				return result
			else:
				if num1[1:] not in Global_Variables:
					print ("Error linje "+str(line)+" variabeln '"+num1[1:]+"' hittades inte!")
				if num2[1:] not in Global_Variables:
					print ("Error linje "+str(line)+" variabeln '"+num2[1:]+"' hittades inte!")
		elif num1_var == True and num2_var == False:
			if num1[1:] in Global_Variables:
				num1 = Global_Variables[num1[1:]]
				result = int(num1)+int(num2)
				return result
			else:
				print ("Error linje "+str(line)+" variabeln '"+num1[1:]+"' hittades inte!")
		elif num1_var == False and num2_var == True:
			if num2[1:] in Global_Variables:
				num2 = Global_Variables[num2[1:]]
				result = int(num1)+int(num2)
				return result
			else:
				print ("Error linje "+str(line)+" variabeln '"+num2[1:]+"' hittades inte!")
	elif expr == "-":
		if num1_var == False and num2_var == False:
			result = int(num1)-int(num2)
			return result
		elif num1_var == True and num2_var == True:
			if num1[1:] in Global_Variables and num2[1:] in Global_Variables:
				num1 = Global_Variables[num1[1:]]
				num2 = Global_Variables[num2[1:]]
				result = int(num1)-int(num2)
				return result
			else:
				if num1[1:] not in Global_Variables:
					print ("Error linje "+str(line)+" variabeln '"+num1[1:]+"' hittades inte!")
				if num2[1:] not in Global_Variables:
					print ("Error linje "+str(line)+" variabeln '"+num2[1:]+"' hittades inte!")
		elif num1_var == True and num2_var == False:
			if num1[1:] in Global_Variables:
				num1 = Global_Variables[num1[1:]]
				result = int(num1)-int(num2)
				return result
			else:
				print ("Error linje "+str(line)+" variabeln '"+num1[1:]+"' hittades inte!")
		elif num1_var == False and num2_var == True:
			if num2[1:] in Global_Variables:
				num2 = Global_Variables[num2[1:]]
				result = int(num1)-int(num2)
				return result
			else:
				print ("Error linje "+str(line)+" variabeln '"+num2[1:]+"' hittades inte!")
	elif expr == "*":
		if num1_var == False and num2_var == False:
			result = int(num1)*int(num2)
			return result
		elif num1_var == True and num2_var == True:
			if num1[1:] in Global_Variables and num2[1:] in Global_Variables:
				num1 = Global_Variables[num1[1:]]
				num2 = Global_Variables[num2[1:]]
				result = int(num1)*int(num2)
				return result
			else:
				if num1[1:] not in Global_Variables:
					print ("Error linje "+str(line)+" variabeln '"+num1[1:]+"' hittades inte!")
				if num2[1:] not in Global_Variables:
					print ("Error linje "+str(line)+" variabeln '"+num2[1:]+"' hittades inte!")
		elif num1_var == True and num2_var == False:
			if num1[1:] in Global_Variables:
				num1 = Global_Variables[num1[1:]]
				result = int(num1)*int(num2)
				return result
			else:
				print ("Error linje "+str(line)+" variabeln '"+num1[1:]+"' hittades inte!")
		elif num1_var == False and num2_var == True:
			if num2[1:] in Global_Variables:
				num2 = Global_Variables[num2[1:]]
				result = int(num1)*int(num2)
				return result
			else:
				print ("Error linje "+str(line)+" variabeln '"+num2[1:]+"' hittades inte!")
	elif expr == "/":
		if num1_var == False and num2_var == False:
			result = int(num1)/int(num2)
			return result
		elif num1_var == True and num2_var == True:
			if num1[1:] in Global_Variables and num2[1:] in Global_Variables:
				num1 = Global_Variables[num1[1:]]
				num2 = Global_Variables[num2[1:]]
				result = int(num1)/int(num2)
				return result
			else:
				if num1[1:] not in Global_Variables:
					print ("Error linje "+str(line)+" variabeln '"+num1[1:]+"' hittades inte!")
				if num2[1:] not in Global_Variables:
					print ("Error linje "+str(line)+" variabeln '"+num2[1:]+"' hittades inte!")
		elif num1_var == True and num2_var == False:
			if num1[1:] in Global_Variables:
				num1 = Global_Variables[num1[1:]]
				result = int(num1)/int(num2)
				return result
			else:
				print ("Error linje "+str(line)+" variabeln '"+num1[1:]+"' hittades inte!")
		elif num1_var == False and num2_var == True:
			if num2[1:] in Global_Variables:
				num2 = Global_Variables[num2[1:]]
				result = int(num1)/int(num2)
				return result
			else:
				print ("Error linje "+str(line)+" variabeln '"+num2[1:]+"' hittades inte!")
	elif expr == "%":
		if num1_var == False and num2_var == False:
			result = int(num1)%int(num2)
			return result
		elif num1_var == True and num2_var == True:
			if num1[1:] in Global_Variables and num2[1:] in Global_Variables:
				num1 = Global_Variables[num1[1:]]
				num2 = Global_Variables[num2[1:]]
				result = int(num1)%int(num2)
				return result
			else:
				if num1[1:] not in Global_Variables:
					print ("Error linje "+str(line)+" variabeln '"+num1[1:]+"' hittades inte!")
				if num2[1:] not in Global_Variables:
					print ("Error linje "+str(line)+" variabeln '"+num2[1:]+"' hittades inte!")
		elif num1_var == True and num2_var == False:
			if num1[1:] in Global_Variables:
				num1 = Global_Variables[num1[1:]]
				result = int(num1)%int(num2)
				return result
			else:
				print ("Error linje "+str(line)+" variabeln '"+num1[1:]+"' hittades inte!")
		elif num1_var == False and num2_var == True:
			if num2[1:] in Global_Variables:
				num2 = Global_Variables[num2[1:]]
				result = int(num1)%int(num2)
				return result
			else:
				print ("Error linje "+str(line)+" variabeln '"+num2[1:]+"' hittades inte!")
	else:
		print ("Error linje nr. "+line+" matte ()")

def math_func(code, line):
	cmd = ""
	expression = ""
	first_num = ""
	second_num = ""
	cmd_found = False
	lex_math = False
	get_first_num = False
	get_second_num = False
	for chr in code:
		if lex_math and chr != " ":
			if get_first_num and chr != ")" and chr != "(" and chr != "+" and chr != "-" and chr != "*" and chr != "%" and chr != "/":
				first_num += chr
			elif get_second_num and first_num != "" and chr != ")" and chr != "(" and chr != "+" and chr != "-" and chr != "*" and chr != "%" and chr != "/":
				second_num += chr
			elif chr == ")":
				break
			elif chr == "(":
				get_first_num = True
			elif chr == "+" or chr == "-" or chr == "*" or chr == "%" or chr == "/":
				get_second_num = True
				get_first_num = False
				expression = chr
		elif cmd == "matte" and lex_math == False:
			cmd_found = True
			lex_math = True
		elif cmd_found == False:
			if chr != " ":
				cmd += chr
				if cmd == "matte" and lex_math == False:
					cmd_found = True
					lex_math = True
	return math_parse(first_num, expression, second_num, line)

def var_func(code, line):
	cmd = ""
	inp_stat = False
	inp_stat_chr = False
	inp_stat_first = False
	inp_stat_end = False
	inp_lex = False
	inp_lex_name = False
	got_inp_name = False
	inp_title = False
	string = ""
	inp_name = ""
	result = ""
	result1 = ""
	title = ""
	inp_name_res = ""
	inp_stat_space = False
	var_lex_list = False
	list_start = False
	var_list = ""
	var_list_tmp = ""
	var_lex_name = False
	get_list = False
	get_index = False
	open_s = False
	var_name = ""
	index = ""
	list_name = ""
	if "[" in code and "]" in code and "$" in code and "=" in code and "var" in code:
		for chr in code:
			if get_index:
				if chr != " ":
					if chr == "]":
						break
					else:
						index += chr
			elif get_list:
				if chr != " ":
					if chr == "[":
						get_index = True
						get_list = False
					else:
						list_name += chr
			elif var_lex_list:
				if chr == "$":
					get_list = True
					var_lex_list = False
			elif var_lex_name:
				if chr == "=":
					var_lex_name = False
					got_var_name = True
					var_lex_list = True
				elif chr != " ":
					var_name += chr
			elif cmd == "var":
				var_lex_name = True
			elif chr != " ":
				cmd += chr
				if cmd == "var":
					var_lex_name = True
		if index[0] == "$":
			if index[1:] in Global_Variables:
				index = Global_Variables[index[1:]]
				result = Global_Variables[list_name]
				result = result[int(index)]
			else:
				print ("Error linje "+str(line)+" variabeln '"+index[1:]+"' hittades inte!")
	elif "[" in code and "]" in code and "$" not in code and "=" in code:
		for chr in code:
			if var_lex_list:
				if chr == "[":
					list_start = True
				elif list_start:
					if chr == "]":
						var_lex_list = False
						list_start = False
						break
					else:
						var_list += chr
			elif var_lex_name:
				if chr == "=":
					var_lex_name = False
					got_var_name = True
					var_lex_list = True
				elif chr != " ":
					var_name += chr
			elif cmd == "var":
				var_lex_name = True
			elif chr != " ":
				cmd += chr
				if cmd == "var":
					var_lex_name = True
		for chr in var_list:
			if open_s and chr != '"':
				var_list_tmp += chr
			elif open_s and chr == '"':
				open_s = False
			elif open_s == False and chr != " ":
				if chr == '"':
					open_s = True
				else:
					var_list_tmp += chr
		var_list = ""
		for chr in var_list_tmp:
			var_list += chr
		result = var_list.split(',')
	elif "in(" in code or "in (" in code:
		for chr in code:
			if inp_lex_name:
				if chr == "=":
					inp_lex_name = False
					got_inp_name = True
					for chr in inp_name:
						if chr != " ":
							inp_name_res += chr
					inp_name = ""
					for chr in inp_name_res:
						inp_name += chr
					inp_stat = True
				else:
					inp_name += chr
			elif inp_stat:
				if inp_title:
					if chr ==')':
						title = title[:-1]
						result = input(title)
						break
					else:
						title += chr
				elif string == "in(" and code[-1] == ")":
					if '("' in code and '")' in code:
						inp_title = True
					else:
						result = input()
						break
				elif chr != " ":
					string += chr
			elif cmd == "var" and got_inp_name == False:
				inp_lex_name = True
			else:
				if inp_lex == False and got_inp_name == False and chr != " ":
					cmd += chr
		var_name = inp_name
	elif "+" in code and "matte" not in code:
		cmd = ""
		var_stat = False
		var_stat_chr = False
		var_stat_first = False
		var_stat_end = False
		var_lex = False
		var_lex_name = False
		got_var_name = False
		first_val = False
		second_val = False
		get_first = False
		get_second = False
		string = ""
		var_name = ""
		result = ""
		var_name_res = ""
		first = ""
		second = ""
		first1 = ""
		second1 = ""
		var_stat_space = False
		for chr in code:
			if var_lex_name:
				if chr == "=":
					var_lex_name = False
					got_var_name = True
					for chr in var_name:
						if chr != " ":
							var_name_res += chr
					var_name = ""
					for chr in var_name_res:
						var_name += chr
					var_stat = True
					first_val = True
				else:
					if chr != " ":
						var_name += chr

			elif var_stat:
				if chr == '+' and first != "":
					second_val = True
					first_val = False
				elif first_val:
					first += chr
				elif second_val:
					second += chr
			elif cmd == "var" and got_var_name == False:
				var_lex_name = True
			else:
				if var_lex == False and got_var_name == False and chr != " ":
					cmd += chr
					if cmd == "var" and got_var_name == False:
						var_lex_name = True
		if '$' in first:
			for chr in first:
				if chr != " ":
					first1 += chr
			first = ""
			for chr in first1:
				first += chr
		elif '"' in first:
			for chr in first:
				if chr == '"' and get_first:
					get_first = False
					break
				elif get_first:
					first1 += chr
				elif chr == '"' and get_first == False:
					get_first = True
			first = ""
			first = first1

		if '$' in second:
			for chr in second:
				if chr != " ":
					second1 += chr
			second = ""
			for chr in second1:
				second += chr
		elif '"' in second:
			for chr in second:
				if chr == '"' and get_second:
					get_second = False
					break
				elif get_second:
					second1 += chr
				elif chr == '"' and get_second == False:
					get_second = True
			second = ""
			second = second1
		if first[0] == "$":
			if first[1:] in Global_Variables:
				first = Global_Variables[first[1:]]
			else:
				print ("Error linje "+str(line)+" variabeln '"+first[1:]+"' hittades inte!")
		if second[0] == "$":
			if second[1:] in Global_Variables:
				second = Global_Variables[second[1:]]
			else:
				print ("Error linje "+str(line)+" variabeln '"+second[1:]+"' hittades inte!")
		result = str(first)+str(second)

	elif "längd" in code and "(" in code and ")" in code:
		var_lex_data = False
		var_lex_name = False
		lex_data = False
		data = ""
		var_name = ""
		cmd = ""
		result = ""
		for chr in code:
			if lex_data:
				if chr == ")":
					data += chr
					break
				else:
					data += chr
			elif var_lex_data:
				if chr == "l":
					lex_data = True
					data += chr
			elif var_lex_name:
				if chr != " ":
					if chr == "=":
						var_lex_name = False
						var_lex_data = True
					else:
						var_name += chr
			elif cmd == "var":
				var_lex_name = True
			elif chr != " ":
				cmd += chr
				if cmd == "var":
					var_lex_name = True
		result = lenght_func(data, line)
		result = str(result)
	elif '"' in code:
		cmd = ""
		var_stat = False
		var_stat_chr = False
		var_stat_first = False
		var_stat_end = False
		var_lex = False
		var_lex_name = False
		got_var_name = False
		string = ""
		var_name = ""
		result = ""
		var_name_res = ""
		var_stat_space = False
		for chr in code:
			if var_lex_name:
				if chr == "=":
					var_lex_name = False
					got_var_name = True
					for chr in var_name:
						if chr != " ":
							var_name_res += chr
					var_name = ""
					for chr in var_name_res:
						var_name += chr
					var_stat = True
				else:
					if chr != " ":
						var_name += chr


			elif var_stat:
				if chr == '"' and var_stat_first:
					string += chr
					break
				elif var_stat_chr:
					string += chr
				elif chr == '"' and var_stat_first == False:
					var_stat_first = True
					var_stat_chr = True
			elif cmd == "var" and got_var_name == False:
				var_lex_name = True
			else:
				if var_lex == False and got_var_name == False:
					cmd += chr
		result = string[:-1]
	elif "matte" in code:
		cmd = ""
		var_stat = False
		var_stat_chr = False
		var_stat_first = False
		var_stat_end = False
		var_lex = False
		var_lex_name = False
		got_var_name = False
		string = ""
		var_name = ""
		result = ""
		to_claculate = ""
		var_name_res = ""
		var_stat_space = False
		for chr in code:
			if var_lex_name:
				if chr == "=":
					var_lex_name = False
					got_var_name = True
					for chr in var_name:
						if chr != " ":
							var_name_res += chr
					var_name = ""
					for chr in var_name_res:
						var_name += chr
					var_stat = True
				else:
					if chr != " ":
						var_name += chr

			elif var_stat:
				if chr != ")":
					to_claculate += chr
				elif chr == ")" and to_claculate != "":
					to_claculate += chr
					result = math_func(to_claculate, line)
					result = str(result)
			elif cmd == "var" and got_var_name == False:
				var_lex_name = True
			else:
				if var_lex == False and got_var_name == False and chr != " ":
					cmd += chr
					if cmd == "var" and got_var_name == False:
						var_lex_name = True
	elif "$" in code and "matte" not in code:
		cmd = ""
		int_stat = False
		int_stat_chr = False
		int_stat_first = False
		int_stat_end = False
		int_lex = False
		int_lex_name = False
		got_int_name = False
		string = ""
		int_name = ""
		result = ""
		result1 = ""
		int_name_res = ""
		int_stat_space = False
		for chr in code:
			if int_lex_name:
				if chr == "=":
					int_lex_name = False
					got_int_name = True
					for chr in int_name:
						if chr != " ":
							int_name_res += chr
					int_name = ""
					for chr in int_name_res:
						int_name += chr
					int_stat = True
				else:
					if chr != " ":
						int_name += chr
			elif int_stat:
				string += chr
			elif cmd == "var" and got_int_name == False:
				int_lex_name = True
			else:
				if int_lex == False and got_int_name == False and chr != " ":
					cmd += chr
					if cmd == "var" and got_int_name == False:
						int_lex_name = True
		for chr in string:
			if chr != " ":
				result1 += chr
		for chr in result1:
			result += chr
		var_name = int_name
		if result[1:] in Global_Variables:
			result = Global_Variables[result[1:]]
		else:
			print ("Error linje "+str(line)+" variabeln '"+result[1:]+"' hittades inte!")
	else:
		cmd = ""
		int_stat = False
		int_stat_chr = False
		int_stat_first = False
		int_stat_end = False
		int_lex = False
		int_lex_name = False
		got_int_name = False
		string = ""
		int_name = ""
		result = ""
		result1 = ""
		int_name_res = ""
		int_stat_space = False
		for chr in code:
			if int_lex_name:
				if chr == "=":
					int_lex_name = False
					got_int_name = True
					for chr in int_name:
						if chr != " ":
							int_name_res += chr
					int_name = ""
					for chr in int_name_res:
						int_name += chr
					int_stat = True
				else:
					if chr != " ":
						int_name += chr
			elif int_stat:
					string += chr
			elif cmd == "var" and got_int_name == False:
				int_lex_name = True
			else:
				if int_lex == False and got_int_name == False:
					cmd += chr
		for chr in string:
			if chr != " ":
				result1 += chr
		for chr in result1:
			result += chr
		var_name = int_name
	Global_Variables.update({var_name:result})

def print_func(code, line):
	cmd = ""
	print_stat = False
	print_stat_chr = False
	print_stat_first = False
	print_stat_end = False
	print_lex = False
	was_variable = False
	list_lex_name = False
	list_lex_indx = False
	is_list = False
	indx = ""
	string = ""
	list_name = ""
	the_list = []
	if "$" in code and "[" in code and "]" in code:
		for chr in code:
			if list_lex_indx:
				if chr != " ":
					if chr == "]":
						break
					else:
						indx += chr
			elif list_lex_name:
				if chr != " ":
					if chr == "[":
						list_lex_name = False
						list_lex_indx = True
					else:
						list_name += chr
			elif chr == "$":
				list_lex_name = True
		if list_name in Global_Variables:
			the_list = Global_Variables[list_name]
			string = the_list[int(indx)]
			is_list = True
		else:
			print ("Error linje "+str(line)+" variabeln '"+list_name+"' hittades inte!")
	elif '$' in code and '"' not in code:
		for chr in code:
			if print_lex and chr == ")":
				was_variable = True
				break
			elif print_lex and chr == "(":
				print_stat_first = True
				print_stat = True
			elif print_stat:
				if print_stat_chr and chr != ' ':
					string += chr
				elif chr == '$' and print_stat_first:
					print_stat_chr = True
			elif cmd == "skriv":
				print_lex = True
			elif print_lex == False and chr != " ":
				cmd += chr
				if cmd == "skriv":
					print_lex = True
	else:
		for chr in code:
			if print_lex and chr == ")":
				print_stat_end = True
			elif print_lex and chr == "(":
				print_stat_first = True
				print_stat = True
			elif print_stat:
				if chr == '"' and print_stat_end:
					string += chr
				elif print_stat_chr and chr != '"':
					string += chr
				elif chr == '"' and print_stat_first:
					print_stat_chr = True
			elif cmd == "skriv":
				print_lex = True
			else:
				if print_lex == False and chr != " ":
					cmd += chr
					if cmd == "skriv":
						print_lex = True
	if was_variable:
		if string in Global_Variables:
			string = Global_Variables[string]
			return string
		else:
			print ("Error linje "+str(line)+" variabeln '"+string+"' hittades inte!")
	elif is_list:
		return string
	else:
		return string

Global_Variables = {}
global_if = False
global_is_if = False
global_if_history = False
global_is_an = False
global_an_history = False
code = []
with open(sys.argv[1], "r") as file:
	code1 = file.readlines()
	code = (line.rstrip('\n') for line in code1)
	code = '***'.join(code)
	code = code.replace("\t", "    ")
	code = code.split('***')

interpreter(code)
