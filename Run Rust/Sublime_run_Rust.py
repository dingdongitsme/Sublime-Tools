# C:\Users\Jo\Documents\Sublime Text Build 3083 x64\Data\Packages\User
# view.run_command('example')
import sublime
import sublime_plugin
import os
import subprocess

class rustCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#self.view.insert(edit, 0, "Hello, World!")
		rustfile = self.view.file_name()
		batch = os.path.dirname(os.path.realpath(__file__)) + "\\runRust.bat" 

		x = subprocess.call([batch, rustfile])
		
		print(x)
		if x == 0:
			d = os.path.dirname(rustfile)
			f = os.path.splitext(os.path.basename(rustfile))[0]
			os.system( d + "\\" + f + ".exe && pause")

		#x = os.system(cmd)
		#x = check_output(cmd, shell=True)
		#print(x)
		#os.system("pause")

