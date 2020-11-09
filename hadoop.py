import main
from subprocess import getoutput
def hadoopf():
	while True:
		main.system("clear; tput setaf 5")
		print("\n\n\n\n\t\t\t\t_______________HADOOP MANAGEMENT______________")
		main.system("tput setaf 2")
		print('''
		\t\t 1. Download and install hadoop & JDK software
		\t\t 2. Configure as Name Node
		\t\t 3. Configure as Data Node
		\t\t 4. Configure as client
		\t\t 5. Upload a file
		\t\t 6. Read a file
		\t\t 7. Remove a file
		\t\t 8. List all files
		\t\t 9. Stop Name Node
		\t\t10. Stop Data Node
		\t\t11. Go back to main menu''')
		main.system("tput setaf 1")
		print("\t\t\t\t12. Exit")
		main.system("tput setaf 5")
		hopt = input("\nEnter your choice: ")
		main.system("tput setaf 2")
		if hopt=='1':
			out = getoutput("if pip3 list | grep gdown;then echo y;else echo n;fi")
			if out[-1]=='y':
				print("gdown is already installed.. downloading the softwares using it")
			else:
				print("installing gdown first to download the softwares...")
				main.system("pip3 install gdown")
			print("\n-----------------downloading hadoop-1.2.1-1.x86_64.rpm----------------")
			main.system("gdown https://drive.google.com/uc?id=1s2reXxZVA-uf4fnDynG66ARti1vJz48V")	
			print("\n\n-----------------downloading jdk-8u171-linux-x64.rpm------------------")
			main.system("gdown https://drive.google.com/uc?id=1et8aZHciCpeFk0zzInSdPUAOQM9Kx48B")
			print("\n\n------------------installing JDK-------------------------")
			main.system("rpm -ivh jdk-8u171-linux-x64.rpm")
			print("\n\n------------------installing hadoop----------------------")
			main.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm")
			print("\nDONE :)")			
		elif hopt=='2':
			nnip = input("Enter the Name Node ip address: ")
			nndir = input("give the Name Node directory (path): ")
			ch = input("Is this directory exists, if not type 'n' to craete it(y/n): ")
			if ch=='n':
				main.system(f"mkdir {nndir}")
				print("Path is created.")
			nnport = input("Enter port number for your name node: ")
			print("writing configuration files...")
			main.system(f"echo -e '<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>{nndir}</value>\n</property>\n</configuration>' > /etc/hadoop/hdfs-site.xml")
			main.system(f"echo -e '<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{nnip}:{nnport}</value>\n</property>\n</configuration>' > /etc/hadoop/core-site.xml")
			print("\nFormating Name Node directory...")
			main.system("hadoop namenode -format")
			main.system("systemctl disable firewalld")
			print("\nStarting Name Node service...")
			main.system("hadoop-daemon.sh start namenode")
		elif hopt=='3':
			nnip = input("Enter the Name Node ip address: ")
			nndir = input("give the Data Node directory (path): ")
			ch = input("Is this directory exists, if not type 'n' to craete it(y/n): ")
			if ch=='n':
				main.system(f"mkdir {nndir}")
				print("Path is created.")
			nnport = input("Enter port number of your name node: ")
			print("writing configuration files...")
			main.system(f"echo -e '<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>{nndir}</value>\n</property>\n</configuration>' > /etc/hadoop/hdfs-site.xml")
			main.system(f"echo -e '<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{nnip}:{nnport}</value>\n</property>\n</configuration>' > /etc/hadoop/core-site.xml")
			main.system("systemctl disable firewalld")
			print("\nStarting Data Node service...")
			main.system("hadoop-daemon.sh start datanode")
		elif hopt=='4':
			nnip = input("Enter the Name Node ip address: ")
			nnport = input("Enter port number of your name node: ")
			main.system(f"echo -e '<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{nnip}:{nnport}</value>\n</property>\n</configuration>' > /etc/hadoop/core-site.xml")
			print("Configured as client.")
		elif hopt=='5':
			path = input("Give the file path to upload: ")
			main.system(f"hadoop fs -put {path} /")
		elif hopt=='6':
			file = input("Give file path you want to read: ")
			main.system(f"hadoop fs -cat {file}")
		elif hopt=='7':
			file = input("Give file path you want to remove: ")
			main.system("hadoop fs -rm {file}")
		elif hopt=='8':
			main.system("hadoop fs -ls /")
		elif hopt=='9':
			main.system("hadoop-daemon.sh stop namenode")
		elif hopt=='10':
			main.system("hadoop-daemon.sh stop datanode")			
		elif hopt=='11':
			main.mainf()
		elif hopt=='12':
			print("...Exited!")
			main.system("tput setaf 7")
			exit()
		else:
			print("Option NOT available...")
		input("press Enter to continue.")
