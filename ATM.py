#dictionary the holds all the ids of the customers with their names
IDs ={
		"Alaa Tarek" :"1234",
		"Engi Emad" :"0000"
	}
#ask for the use passkey
ID = input("enter your passkey")
#flag to further detect if the is is correct
flag = 0
#passing through the dictionary to search the is and print a welcoing message
for key, value in IDs.items():
	if ID == value:
		print("hello ",key)
		flag = 1
if flag	!= 1:
	print ("wrong id")
#let the user know the amout of money they can withdraw
money_withdraw = (500,1000,2000,3000,4000,5000,10000)

print ("The amounts of money you can withdraw are : ")
print (money_withdraw)


		
	

