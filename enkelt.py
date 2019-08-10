# coding=utf-8
import sys
import subprocess
import os


try:
	if sys.version_info[0] < 3:
		raise Exception("Du måste använda python 3")
	else:
		sys_args = []
		
		if len(sys.argv) > 1:
			sys_args = sys.argv[1:]
		
		run_command = 'python3 run_enkelt.py '
		
		for arg in sys_args:
			run_command += arg + ' '
		
		if '.e' in run_command:
		
			process = subprocess.Popen(run_command, stdout = subprocess.PIPE, stderr = None, shell = True).communicate()[
				0].decode('utf-8').split('\n')
			
			for index, line in enumerate(process):
				if line == 'True':
					process[index] = 'Sant'
				elif line == 'False':
					process[index] = 'Falskt'
			
			process = '\n'.join(process)
			print(process)
		else:
			os.system('python3 run_enkelt.py')
except Exception as e:
	print(e)
