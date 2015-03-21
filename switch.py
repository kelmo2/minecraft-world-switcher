#Script to switch the world on a server in minecraft
import os

#Change the world to start on the minecraft server
def changeWorld(list, world):
	for index, str in enumerate(list):
		if "level-name" in list[index]:
			list[index] = "level-name:{}\n".format(world)

#Change the world to start on the minecraft server
def changeMode(list, mode):
	for index, str in enumerate(list):
		if "gamemode" in list[index]:
			list[index] = "gamemode={}\n".format(mode)

#Read in the server.properties file line by line and store in a list
with open('server.properties', 'r') as file:
    # read a list of lines into data
    data = file.readlines()

#Get a list of all minecraft folders, remove all hidden folders
folders = [name for name in os.listdir(".") if os.path.isdir(name)]
for folder in folders:
	if folder[0] == '.':
		folders.remove(folder)

#Get user input
for i, folder in enumerate(folders):
	print "{}: {}".format(i+1, folder)

size = len(folders)-1

##############################################################
###################CHANGE GAME WORLD##########################
##############################################################
response = raw_input("Please pick a world from the list: ")
flag = "false"

while flag == "false":
	response = int(response)
	response -= 1
	if (0 <= response <= size):
		flag = "true"
	else:
		response = raw_input("Wrong input, try again: ")

changeWorld(data, folders[response])

##############################################################
###################CHANGE GAME MODE###########################
##############################################################
modes = ["1: Survial", "2: Creative", "3: Adventure", "4: Spectator"]

for i, mode in enumerate(modes):
	print "{}".format(mode)
size = len(modes)-1

response = raw_input("Please pick a mode from the list: ")
flag = "false"

while flag == "false":
	response = int(response)
	response -= 1
	if (0 <= response <= size):
		flag = "true"
	else:
		response = raw_input("Wrong input, try again: ")

done = raw_input("press any key to continue...")

#Call function to change the world
changeMode(data, response)

# and write everything back
with open('server.properties', 'w') as file:
    file.writelines( data )