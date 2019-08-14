# coding=utf-8

# Enkeltpip 1.0
# Copyright 2018, 2019 Edvard Busck-Nielsen, 2019 Morgan Willliams
# This file is part of Enkelt.
#
#     Enkelt is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     Foobar is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with Enkelt.  If not, see <https://www.gnu.org/licenses/>.

import urllib.request
import sys
import os


def install(enkelt_module):
	local_path = 'bib/' + enkelt_module + '.e'
	web_path = web_import_location + enkelt_module + '.e'

	if os.path.isfile(local_path):
		print('Modul', enkelt_module, 'redan installerad.')
		ans = input('Vill du uppdatera? (J/N) ')

		if ans.lower() == 'j':
			update(enkelt_module)

	else:
		try:
			response = urllib.request.urlopen(web_path)
			module_code = response.read().decode('utf-8')

			with open(local_path, 'w') as f:
				f.write(module_code)
				f.close()

			if os.path.isfile(local_path):
				print('Modulen', enkelt_module, 'installerad lyckade.')
		except:
			print('Modul', enkelt_module, 'hittades inte.')


def update(enkelt_module):
	local_path = 'bib/' + enkelt_module + '.e'
	web_path = web_import_location + enkelt_module + '.e'

	if os.path.isfile(local_path):
		try:
			response = urllib.request.urlopen(web_path)
			web_module_code = response.read().decode('utf-8')

			with open(local_path, 'r') as f:
				local_module_code = f.read()
				f.close()
				
			if local_module_code != web_module_code:

				with open(local_path, 'w') as f:
					f.write(web_module_code)
					f.close()

					print('Modulen', enkelt_module, 'uppdaterad lyckade.')
			else:
				print('Redan uppdaterad.')

		except:
			print('Modul', enkelt_module, 'hittades inte.')

	else:
		print('Ingen installerad modul', enkelt_module, '.')
		ans = input('Vill du installera? (J/N) ')

		if ans.lower() == 'j':
			install(enkelt_module)


def uninstall(enkelt_module):
	local_path = 'bib/' + enkelt_module + '.e'

	if os.path.isfile(local_path):
		os.remove(local_path)

		if not os.path.isfile(local_path):
			print('Modulen', enkelt_module, 'avinstallerad lyckade.')
	else:
		print('Ingen installerad modul', enkelt_module, '.')


def list_installed_modules():

	for file_name in os.listdir('bib'):
		if file_name.endswith('.e'):
			print(file_name[:-2])


web_import_location = 'https://raw.githubusercontent.com/Enkelt/EnkeltBibliotek/master/bib/'
help_message = '''
Användande:
  python3 enkeltpip.py <kommando> [modul_namn]

Kommandon:
  installera 				installera moduler
  uppdatera 				uppdatera moduler
  avinstallera 				avinstallera moduler
  lista        				lista över installerade moduler
  hjälp       				visa det här meddelandet

'''

args = sys.argv

if args[1].lower() == 'installera':
	install(args[2])
elif args[1].lower() == 'uppdatera':
	update(args[2])
elif args[1].lower() == 'avinstallera':
	uninstall(args[2])
elif args[1].lower() == 'lista':
	list_installed_modules()
elif args[1].lower() == 'hjälp':
	print(help_message)
else:
	print('\nOgiltigt argument:', args[1])
	print('Prova hjälpkommandot\npython3 enkeltpip.py hjälp\n')