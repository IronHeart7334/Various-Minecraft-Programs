from os import listdir
from os.path import isdir
from shutil import copyfile, copytree

done = False
ip = ""
packs = listdir("./datapacks")
target = ""

print("Welcome to Matt's Minecraft Datapack install utility")
while not done:
    print("Enter the full path to the directory where you wish to install datapacks (you don't need quote marks around multi-word folders, nor do you need backquoted spaces)")
    #todo: just enter the world name, this finds the proper directory
    print("(minecraft/saves/WORLD/datapacks)")
    while not isdir(target):
        target = input("Enter path: ")
    
    print("Available datapacks:")
    for datapack in packs:
        print("* " + datapack)
    ip = input("Select a datapack to install in this world, or type 'exit' to quit: ")
    if ip == "exit":
        break;
    if ip in packs:
        copytree("./datapacks/" + ip, target + "/" + ip)
    else:
        print("'" + ip + "\' is not in the list of datapacks")