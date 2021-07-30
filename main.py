import os
from shutil import copyfile
from time import sleep

lat = open('C:/flashtool/temp/v.txt', 'r').read()
pre = open('C:/flashtool/bin/v', 'r').read()

a= int(lat)
b=int(pre)

if a>b:
        os.system('cmd /c "cd C:/flashtool/temp/ && C:/flashtool/bin/curl/bin/curl.exe -L -O https://github.com/harshilk/Patched-imgs/raw/main/Flashtool32.exe"')
        copyfile('C:/flashtool/temp/v.txt','C:/flashtool/bin/v')
        os.remove("C:/flashtool/Flashtool.exe")
        copyfile('C:/flashtool/temp/Flashtool32.exe', 'C:/flashtool/Flashtool.exe')
        os.remove("C:/flashtool/temp/Flashtool32.exe")
        sleep(2)
        os.system('cmd /c "echo Updated to Latest && cd C:/flashtool && Flashtool.exe"')

else:
        print("Already Latest")
        os.system('cmd /c "PAUSE "Already Latest""')


