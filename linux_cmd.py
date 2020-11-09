import os
while True:
	print("\t\tBASIC LINUX COMMANDS\t\t\t\n")
	print("Enter your choice")
	print("1: view the date")
	print("2: view the calendar")
	print("3: view the folders/files in the current directory")
	print("4: create a directory")
	print("5: add a user")
	print("6: launch applications")
	print("7: navigate to a directory ") 
	print("8: check the current directoy u are in ")
	print("9: See the details of your network information")
	print("10: exit")
	n=int(input())
	if n==1:
		print(os.system("date"))
	elif n==2:
		os.system("cal")
	elif n==3:
		os.system("ls")
	elif n==4:
		print(" Enter the directory name you want to create")
		name=input()
		os.system("mkdir {}".format(name))
	elif n==5:
		name=input(" Enter the username")
		os.system("useradd {}".format(name))
		print(" Enter the password")
		os.system("passwd {}".format(name))
	elif n==6:
		print("Enter 1 to launch gedit")
		print("Enter 2 to launch firefox")
		ch=int(input())
		if ch==1:
			os.system("gedit &")
		if ch==2:
			os.system("firefox &")
	elif n==7:
		name=input("Enter the name of the directory you want to navigate to ")
		os.system("cd /{}".format(name))
	elif n==8:
		os.system("pwd")
	elif n==9:
		os.system("ifconfig")
	elif n==10:
		exit()
	else:
		print(" Enter a valid choice !!")
					
