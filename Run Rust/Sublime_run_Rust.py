# C:\Users\Jo\Documents\Sublime Text Build 3083 x64\Data\Packages\User
# view.run_command('example')
import sublime, sublime_plugin
import os, subprocess
import threading

class myThread (threading.Thread):

	def __init__(self, rustfile): 
		threading.Thread.__init__(self)
		self.rustfile = rustfile

	def run(self):
		startCommands(self.rustfile)

def startCommands(rustfile):
		#self.view.insert(edit, 0, "Hello, World!")
		batch = os.path.dirname(os.path.realpath(__file__)) + "\\runRust.bat" 
		result = subprocess.call([batch, rustfile])
		#print(x)
		if result == 0:
			d = os.path.dirname(rustfile)
			f = os.path.splitext(os.path.basename(rustfile))[0]
			os.system( d + "\\" + f + ".exe && pause")
		#x = os.system(cmd)
		#x = check_output(cmd, shell=True)
		#print(x)
		#os.system("pause")


class rustCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		rustfile = self.view.file_name()
		thread1 = myThread(rustfile)
		thread1.start()

