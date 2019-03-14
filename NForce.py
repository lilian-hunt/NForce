import sys
height = input("Enter height: ")
if height.isdigit() == False:
	print("\nInvalid height.")
	sys.exit()
elif int(height) <1 or int(height) >20:
	print("\nInvalid height.")
	sys.exit()
rows = input("Enter number of rows: ")
if rows.isdigit() == False :
	print("\nInvalid number of rows.")
	sys.exit()
elif int(rows) <1 or int(rows) >20:
	print("\nInvalid number of rows.")
	sys.exit()
onetriangle = [""]*int(height)
x = 1
y = 0
print("\n",end="")
for i in range(len(onetriangle)):
	if i != len(onetriangle)-1:
		onetriangle[i] = " "*(int(height)-x)+ "/" + ' '*y+"\\" + " "*(int(height)-x)
	else:
		onetriangle[i] = " "*(int(height)-x)+ "/" + '_'*y+"\\" + " "*(int(height)-x)	
	x +=1
	y +=2
x = 1
hh = int(height)*int(rows)
for xx in range(int(rows)):
	for ii in onetriangle:
		f = (" "*(hh-x)+ ii.lstrip()+ ii*(xx))
		print(f.rstrip())
		x+=1		
