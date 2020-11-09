import os
import main
def docker():
	while(True):
		print("Enter your choice ")
		print("1: start docker services")
		print("2: check the status of the docker services")
		print("3: pull a docker image ")
		print("4: check docker info ")
		print("5: attach a docker image ")
		print("6: install docker")
		print("7: check the details of all the docker images running")
		print("8: stop docker services")
		print("9: search docker images ")
		print("10. Go back to main menu")
		print("11: exit")


		ch=int(input())

		if(ch==1):
			os.system("systemctl start docker")
		elif(ch==2):
			os.system("systemctl status docker")	
		elif(ch==3):
			name=input(" Enter the name of the docker image")
			ver=input(" Enter the version")
			os.system("docker pull {}:{}".format(name,ver))
		elif(ch==4):
			os.system("docker info")
		elif (ch==5):
			name=input(" Enter the name of the docker image to be attached")
			os.system("docker start {}".format(name))		
			os.system("docker attach {}".format(name))
		elif(ch==6):
			name=input(" Enter the image name")
			ver=input(" Enter the version")
			my_name=input(" Enter the name you want to assign to the docker container")
			os.system("docker run -it --name {} {}:{}".format(my_name,name,ver))
		elif(ch==7):
			os.system("docker ps")
		elif(ch==8):
			os.system("systemctl stop docker")
		elif(ch==9):
			name=input(" Enter the docker image you want to search for ")
			os.system("docker search {}".format(name))
		elif(ch==10):
			main.mainf()
		elif(ch==11):
			exit()
		else:
			print("Enter a valid choice")
		input("press Enter to continue.")


