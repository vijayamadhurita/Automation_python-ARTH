import main
def web():
	while True:
		main.system("clear; tput setaf 5")
		print("\n\n\n\t\t\t\t___________WEB SERVER_____________")
		main.system("tput setaf 2")
		print('''\n\n
		\t\t1. Install Apache Web Server
		\t\t2. Start Web Server
		\t\t3. Stop web server
		\t\t4. Edit/create webpage
		\t\t5. Your Webpages
		\t\t6. stop firewall      
		\t\t7. Go back to main menu''')
		main.system("tput setaf 1")
		print("\t\t\t\t8. Exit")
		main.system("tput setaf 5")
		ch = input("\nEnter your choice: ")
		main.system("tput setaf 2")
		if ch == '1':
			main.system("yum install httpd -y")
		elif ch == '2':
			main.system("systemctl start httpd")
		elif ch == '3':
			main.system("systemctl stop httpd")
		elif ch == '4':
			a = input("Enter name(like page.html): ")
			main.system("cd /var/www/html; gedit {}".format(a))
		elif ch == '5':
			main.system("ls /var/www/html")
		elif ch == '6':
			main.system("systemctl stop firewalld")
		elif ch == '7':
			main.mainf()
		elif ch == '8':
			print("...Exited!")
			main.system("tput setaf 7")
			exit()
		else:
			print("Option NOT available...")
		input("press Enter to continue.")
