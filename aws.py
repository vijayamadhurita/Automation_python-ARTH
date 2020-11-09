import main
def aws():
	while True:
		main.system("clear; tput setaf 5")
		print("\n\n\n\n\n\n\t\t\t\t____________________________AWS Management______________________________")
		main.system("tput setaf 2")
		print('''\n\n
		\t\t 1. Install latest aws-cli            8. Attach a volume to ec2 instance
		\t\t 2. Configure your aws profile        9. Delete a volume
		\t\t 3. Create a key-pair                10. Delete a security group
		\t\t 4. Create a security group          11. Terminate instance
		\t\t 5. Add a security group rule        12. Create a S3 bucket
		\t\t 6. Launch an instance               13. Delete S3 bucket
		\t\t 7. Create a EBS volume              14. Go back to main menu''')
		main.system("tput setaf 1")
		print("\t\t\t\t15. Exit")
		main.system("tput setaf 5")
		aopt = input("\nEnter your choice: ")
		main.system("tput setaf 2")
		if aopt=='1':
			main.system('curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"')
			main.system("unzip awscliv2.zip")
			main.system("sudo ./aws/install; aws --version")
		elif aopt=='2':
			main.system("aws configure")
		elif aopt=='3':
			key_name = input("Enter a key name: ")
			key_file = input("Enter key file name where your key will be stored (like mykey.pem): ")
			main.system(f"aws ec2 create-key-pair --key-name {key_name} > {key_file}")
		elif aopt=='4':
			sname = input("Enter security group name: ")
			desc = input("Add some description: ")
			main.system(f'aws ec2 create-security-group --group-name "{sname}"  --description "{desc}"')		
		elif aopt=='5':
			sname = input("Enter the security group name to which you want to add rule: ")
			protocol = input("Enter protocol: ")
			port = input("Enter port number: ")
			cidr = input("Enter allowed CIDR: ")
			main.system(f"aws ec2 authorize-security-group-ingress   --group-name {sname}  --protocol {protocol}    --port {port}  --cidr {cidr}")
		elif aopt=='6':
			ami_id = input("Enter image id (ex. ami-0e306788ff2473ccb): ")
			type = input("Give instance type(ex. t2.micro): ")
			key = input("Give key name to attached: ")
			name = input("Give your instance any name: ")
			sgroup = input("Add a security group: ")
			main.system(f"aws ec2 run-instances --image-id {ami_id} --instance-type {type} --key-name {key} --tag-specifications  ResourceType=instance,Tags=[{{Key=Name,Value={name}}}]  --security-groups {sgroup}")
		elif aopt=='7':
			vtype = input("Give volume type (ex. gp2): ")
			size = input("Give volume size: ")
			zone = input("Give availabilty zone for volume (ex. ap-south-1a): ")
			vname = input("Any volume name: ")
			main.system(f"aws ec2 create-volume --volume-type {vtype} --size {size}  --availability-zone {zone} --tag-specifications ResourceType=volume,Tags=[{{Key=Name,Value={vname}}}]")
		elif aopt=='8':
			vid = input("Give volume id (it should in same zone as instance): ")
			iid = input("Give your instance id to which volume is to be attached: ")
			dname = input("Give any device name for volume: ")
			main.system(f"aws ec2 attach-volume  --volume-id {vid}  --instance-id  {iid}  --device {dname}")
		elif aopt=='9':
			vid = input("Enter id of volume to be deleted: ")
			main.system(f"aws ec2 delete-volume --volume-id {vid}")
		elif aopt=='10':
			sname = input("Enter security group name to be deleted: ")
			main.system(f"aws ec2 delete-security-group --group-name {sname}")
		elif aopt=='11':
			iid = input("Give id of instance to be terminated: ")
			main.system(f"aws ec2 terminate-instances --instance-id {iid}")
		elif aopt=='12':
			bname = input("Enter bucket name: ")
			acl = input("Apply acl to the bucket (private,public-read,public-read-write,authenticated-read):" )
			region = input("Enter region: ")
			main.system(f"aws s3api create-bucket --bucket {bname} --acl {acl} --region {region} --create-bucket-configuration LocationConstraint={region}")
		elif aopt=='13':
			bname = input("Enter bucket name to be deleted: ")
			main.system(f"aws s3api delete-bucket --bucket {bname}")
		elif aopt=='14':
			main.mainf()
		elif aopt=='15':
			print("...Exited!")
			main.system("tput setaf 7")
			exit()
		else:
			print("Option NOT available...")
		input("press Enter to continue.")
