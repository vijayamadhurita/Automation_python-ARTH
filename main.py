from os import system
from getpass import getpass
import hadoop
import aws
import docker
import linux_cmd
import lvm
import webserver
def mainf():
	while True:
		system("clear;tput setaf 5")
		print('''\n\n
		\t\t\t\t \\\         // ||==== ||     /====  /====\\  ||      || ||====
		\t\t\t\t  \\\       //  ||     ||    ||     ||    || ||\\\   /|| ||
		\t\t\t\t   \\\ /\\\ //   ||===  ||    ||     ||    || || \\\ / || ||===
		\t\t\t\t    \\// \\//    ||     ||    ||     ||    || ||  \\/  || ||
		\t\t\t\t     /   /     ||____ ||___  \\____  \\____/  ||      || ||____
		''')
		system("tput setaf 2")
		print("\n\n\t\t\tWhat would you like to manage...Select from options below.")
		print('''
		\t\t1. Hadoop
		\t\t2. AWS
		\t\t3. Docker
		\t\t4. Linux Commands
		\t\t5. LVM
		\t\t6. WebServer''')
		system("tput setaf 1")
		print("\t\t\t\t7. EXIT")
		system("tput setaf 5")
		opt = input("\nEnter your choice: ")
		system("tput setaf 2")
		if opt=='1':
			hadoop.hadoopf()
		elif opt=='2':
			aws.aws()
		elif opt=='3':
			docker.docker()
		elif opt=='4':
			linux_cmd.cmd()
		elif opt=='5':
			lvm.lvm()
		elif opt=='6':
			webserver.web()
		elif opt=='7':
			print("...Exited!")
			system("tput setaf 7")
			exit()
		else:
			print("Option NOT available...")
		input("press Enter.")
if __name__=="__main__":
	system("tput setaf 2")
	passwd = 1234
	if getpass("Give password to enter the menu: ")=='1234':
		print("You are Authenticated")
		input("press Enter...")
	else:
		system("tput setaf 1")
		print("Wrong Password! Terminating...")
		system("tput setaf 7")
		exit()
	mainf()
	

