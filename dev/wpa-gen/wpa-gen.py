import sys
import math
import random
import time
from random import choice
import os

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
# Weclome Block #
#Title Block #
print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print "+" + color.GREEN + " $$\      $$\ $$$$$$$\   $$$$$$\           $$$$$$\  $$$$$$$$\ $$\   $$ | " + color.END + "+"
time.sleep(0.1)
print "+" + color.GREEN + " $$ | $\  $$ |$$  __$$\ $$  __$$\         $$  __$$\ $$  _____|$$$\  $$ | "  + color.END + "+"
time.sleep(0.1)
print "+" + color.GREEN + " $$ |$$$\ $$ |$$ |  $$ |$$ /  $$ |        $$ /  \__|$$ |      $$$$\ $$ | " + color.END + "+"
time.sleep(0.1)
print "+" + color.GREEN + " $$ $$ $$\$$ |$$$$$$$  |$$$$$$$$ |$$$$$$\ $$ |$$$$\ $$$$$\    $$ $$\$$ | " + color.END + "+" 
time.sleep(0.1)
print "+" + color.GREEN + " $$$$  _$$$$ |$$  ____/ $$  __$$ |\______|$$ |\_$$ |$$  __|   $$ \$$$$ | " + color.END + "+" 
time.sleep(0.1)
print "+" + color.GREEN + " $$$  / \$$$ |$$ |      $$ |  $$ |        $$ |  $$ |$$ |      $$ |\$$$ | " + color.END + "+" 
time.sleep(0.1)
print "+" + color.GREEN + " $$  /   \$$ |$$ |      $$ |  $$ |        \$$$$$$  |$$$$$$$$\ $$ | \$$ | " + color.END + "+" 
time.sleep(0.1)
print "+" + color.GREEN + " \__/     \__|\__|      \__|  \__|         \______/ \________|\__|  \__| " + color.END + "+"
time.sleep(0.1)
print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
print"                                                           	Version 1.1"
#End Of Title Block#  
time.sleep(1)
try:
    while True:           
	print color.BOLD+"\nPassword types available...\n"+color.END+color.YELLOW+"Uppercase [ABCDEFGHIJKLMNOPQRSTUVWXYZ] = U"+color.END+color.CYAN+"\nLowercase [abcdefghijklmnopqrstuvwxyz] = L\n"+color.END+color.GREEN+"Alpha Numeric Lower [abcdefghijklmnopqrstuvwxyz1234567890] = ANL\n"+color.END+color.PURPLE+"Alpha Numeric Upper [ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890] = ANU\n"+color.END+color.BLUE+"Hexdigits [0123456789abcdefABCDEF] = H\n"+color.END+color.RED+"Digits [0123456789] = D\n"+color.END+color.DARKCYAN+"Upper & Lower [AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz] = UL\n"+color.END+"Custom Character Set [Enter Your Own Characters] = C\n"+color.YELLOW+"Experimental Personal Mode [John,James,1988,England,Usa,Car] - P\n" + color.END
	# End Of Welcome Block #
	custom = ""
	personal = ""
	while True:
		pwchoice = raw_input(color.BOLD+'Enter password type now: '+color.END)
		if pwchoice not in ["U","L","H","UL","D","ANL","ANU","C","P"]:
			print "Please enter a correct password type..."	
			continue
		else:
			break
	if pwchoice == "C":	
		while True:	
			custom = raw_input(color.BOLD+"Enter your custom character set: " +color.END)
			if custom == "":
				print "Please enter some characters..."
				continue
			else:
				break
		
	if pwchoice == "P":
		while True:
			personal = raw_input(color.BOLD+"Enter your custom terms seperated by comma, Example: John,1986,England,2016,Car:\n" +color.END)
			personal = personal.split(",")
			if personal == "":
				print "Please enter some terms..."
				continue
			else:
				break
				
	if pwchoice != "P":
		while True:
			try:
				pwli = int(input(color.BOLD+'Enter the password length: '+color.END))
			except Exception:
				print "Please enter a number..."
				continue
			break
	else:
		pwli = int(2)
	
	
#Set Value Of Main Choice
	mainChoice = "abcdefghijklmnopqrstuvwxyz"
	if pwchoice == "U":
		mainChoice = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	elif pwchoice == "L":
		mainChoice = "abcdefghijklmnopqrstuvwxyz"
	elif pwchoice == "H":
		mainChoice = "0123456789abcdefABCDEF"
	elif pwchoice == "UL":
		mainChoice = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
	elif pwchoice == "D":
		mainChoice = "0123456789"
	elif pwchoice == "ANL":
		mainChoice = "abcdefghiklmnopqrstuvwxyz1234567890"
	elif pwchoice == "ANU":
		mainChoice = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
	elif pwchoice == "C":
		mainChoice = custom
		
	#Calculate Possibilities
	if pwchoice == "P":		
		totalPSBi = len(personal)
	else:
		totalPSBi = len(mainChoice)
	totalPSB = long(math.pow(totalPSBi,pwli))
	print color.BOLD + color.CYAN + "Total password generation possibilities = "+color.GREEN+"%s" % totalPSB + color.END
	while True:
		try:	
			if pwchoice == "P":
				pwgi = input(color.BOLD+'Enter number of passwords you want to generate, 0 Generates all available: '+ color.END)
			else:
				pwgi = input(color.BOLD+'Enter number of passwords you want to generate: '+ color.END)
		except Exception:
			print "Please enter a number..."
			continue
		break
			
	while True:
		fname = raw_input(color.BOLD+'Enter a file name to save to passwords to, include .txt extension: '+color.END)
		if ".txt" not in fname:
			print "You forgot the .txt extension, try again..."
			continue
		else:
			break
	
	
	count = 0
	count2 = pwgi
	f = open(fname,"w")
	
	#WHILE LOOP START
	if pwchoice != "P":
		while count < pwgi:
			f.write(''.join(choice(mainChoice) for i in range (pwli)) + "\r\n")
			count = count + 1
			sys.stdout.write("\033[92m\033[1m\rPasswords left %s" % count2)
			sys.stdout.flush()
			count2 = count2 - 1
	elif pwchoice == "P":
		if pwgi == 0:
			#WORK IN PROGRESS
			totalGen = len(personal)
			countP = 0
			currentIndex = 0
			currentGen = 0
			while currentIndex < totalGen:
				while countP < totalGen:
					f.write(''.join(personal[currentIndex] + personal[currentGen]) + "\r\n")
					countP = countP + 1
					currentGen = currentGen + 1
				countP = 0
				currentGen = 0
				currentIndex = currentIndex + 1
				sys.stdout.write("\033[92m\033[1m\rPasswords left %s" % count2)
				sys.stdout.flush()
				count2 = count2 - 1
	

		else:
			while count < pwgi:
				personalLen = len(personal)
				f.write(''.join(personal[random.randint(0,personalLen)-1] for i in range (pwli)) + "\r\n")
				count = count + 1
				sys.stdout.write("\033[92m\033[1m\rPasswords left %s" % count2)
				sys.stdout.flush()
				count2 = count2 - 1
	#WHILE LOOP END
	f.close()
	sys.stdout.write("\033[0m \r")
	exitMessage = raw_input(color.BOLD +"Would you like to make another list? Y / N : " + color.END)
	if exitMessage == "Y":
		os.system('clear')		
		continue
	else:
		print color.BOLD + "Goodbye!" + color.END	
		sys.exit()

except KeyboardInterrupt:
	sys.stdout.write("\n")
	sys.stdout.write(color.BOLD+"Thanks for using wpa-gen! Goodbye\n"+color.GREEN+"Please subscribe to our youtube for further updates!\n"+color.CYAN+"https://www.youtube.com/channel/UCzjtcz6hVr1RLrF5fq2L6tA\n" + color.END)
	sys.exit()
