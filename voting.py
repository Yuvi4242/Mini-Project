#VOTING SYSTEM
age=int(input('Enter age of the voter : '))
if age>=18 and age<=100:
	print('Welcome, you are eligible for voting.')
	ask=int(input('Enter Aadhar number to continue : '))
	print('Press : 1 for BJP ; 2 for INC ; 3 for AAP ; 4 for BSP ; 5 for RJD')
	ch=input('Enter your decision : ')
	ch=int(ch)
	if ch==1:
		print('You voted for BJP.Thank you.')
	elif ch==2:
		print('You voted for INC.Thank you.')
	elif ch==3:
		print('You voted for AAP.Thank you.')
	elif ch==4:
		print('You voted for BSP.Thank you.')
	elif ch==5:
		print('You voted for RJD.Thank you.')
	else:
		print('Invalid Choice.')
else:
	print('YOU CANNOT VOTE.')