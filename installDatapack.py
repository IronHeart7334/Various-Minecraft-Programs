from os import listdir
from os.path import isdir, exists
from shutil import copyfile, copytree, rmtree
from tkinter import Tk, filedialog

done = False
ip = ""
packs = listdir("./datapacks")
target = ""
Tk().withdraw()

print("Welcome to Matt's Minecraft Datapack install utility")
print("First, choose the 'datapacks' folder of the world where you want to install datapacks")
while target == "":
    mode = input("First, enter 1 to manually enter the path, or enter 2 to use a gui, or q to quit:")
    if mode == "1":
        print("Enter the full path to the directory where you wish to install datapacks (you don't need quote marks around multi-word folders, nor do you need backquoted spaces)")
        print("Example: /Users/xxxx/Library/Application Support/minecraft/saves/WORLD/datapacks")
        target = input("Enter path: ")
        if not isdir(target):
            target = ""
    if mode == "2":
        target = filedialog.askdirectory()        
    if mode == "q":
        target = "NO"
        done = True

print("Data packs will be installed to " + target)

while not done:
    #todo: just enter the world name, this finds the proper directory
    #print("(minecraft/saves/WORLD/datapacks)")
    
    
    print("Available datapacks:")
    for datapack in packs:
        print("* " + datapack)
    ip = input("Select a datapack to install in this world, or type 'exit' to quit: ")
    if ip == "exit":
        break;
    if ip in packs:
        copyTo = target + "/" + ip
        if exists(copyTo):
            print("This datapack is already installed, so I'll delete it and reinstall")
            rmtree(copyTo)
        copytree("./datapacks/" + ip, copyTo)
    else:
        print("'" + ip + "\' is not in the list of datapacks")