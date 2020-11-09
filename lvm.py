import os
while True:
	print(" Enter your choice ")
	print("1: View the list of all the hard disks that you have ")
	print("2: Create physical hard-disk (PV)")
	print("3: View the details of the PV's you have created")
	print("4: Create volume-group (VG)")
	print("5: View the details of VG")
	print("6: Create LV partition ")
	print("7: View the details of LV")
	print("8: format and mount")
	print("9: increase the size of the hard-disk on the fly ")
	ch=int(input())

	if ch==1:
		os.system("fdisk -l") 
	elif ch==2:
		pv1=input(" Enter the name of the 1st hard-disk")
		pv2=input(" Enter the name of the 2nd hard-disk")		
		os.system("pvcreate {}".format(pv1)) 
		os.system("pvcreate {}".format(pv2))		
	elif ch==3:
		os.system("pvdisplay")
	elif ch==4:
		vg=input(" Enter the name of the volume group")
		os.system("vgcreate {} {} {}".format(vg,pv1,pv2))
	elif ch==5:
		os.system("vgdisplay {}".format(vg))
	elif ch==6:
		size=int(input(" Enter the size of LV"))
		lv=input(" Enter the name of the logical volume")
		os.system("lvcreate --size {}G --name {} {}".format(size,lv,vg))
	elif ch==7:
		os.system("lvdisplay")
	elif ch==8:
		os.system("mkfs.ext4 /dev/{}/{}".format(vg,lv))
		folder=input(" Enter the name of the folder you want to create ")
		os.system(" mount /dev/{}/{} {}".format(vg,lv,folder))
	elif ch==9:
		size=input(" Enter the size you want to extend to ")
		os.system("lvextend --size +{}G".format(size))
		os.system("resize2fs /dev/{}/{}".format(vg,lv))
	
	
