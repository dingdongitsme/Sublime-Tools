

#C:\Users\Jo\Documents\Sublime Text Build 3083 x64\Data\Packages\User

#view.run_command('example')
#view.run_command('mysave')


import sublime, sublime_plugin
import datetime
import shutil
import os.path

class MysaveCommand(sublime_plugin.TextCommand):

    @staticmethod
    def get_version(n):
        segs = n.split("_")
        if len(segs) != 1:
            return segs[-1]
        else:
            return ""

    @staticmethod
    def strip_version(n):
        segs = n.split("_")
        out = ""
        for s in segs[:-1]:
            out += s + "_"
        return out[:-1]


    def run(self, edit):
        full_name = self.view.file_name()
        fileType = full_name.split(".")[-1]
        fileDir = os.path.dirname(full_name)
        fileName = os.path.basename(full_name)[:-(len(fileType)+1)]

        version = self.get_version(fileName)
        name_only = self.strip_version(fileName)

        print("dir: " + fileDir)
        print("name: " + fileName)
        print("type: " + fileType)
        print("version: " + version)
        print("name_only: " + name_only)

        new_name = fileDir + "\\" + name_only + "." + fileType
        print(full_name)
        print(new_name)
        
        

