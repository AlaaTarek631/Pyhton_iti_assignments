import tkinter as tk

new_value = " "

window_1 = tk.Tk()

window_1.title("Calculator")
display_text = new_value
display = tk.Label(window_1, text=display_text,width=50,height=3, bg="white", fg="black",font=('calibre',10, 'bold')).place(x=0, y=0)
window_1.geometry('280x350')

num=tk.IntVar()  
operation=tk.IntVar()
 
flag1 ,flag2, num2 , result  = 0,0,0,0

def TakeOperands ():
	global num
	global flag1
	global flag2
	global result
	global display_text
	global new_value
	if ((flag1 == 0)and(flag2 == 0)):
		result = num.get()
		new_value = display_text + str(result)
		display_text = new_value
		display = tk.Label(window_1, text=display_text,width=50,height=3, bg="white", fg="black",font=('calibre',10, 'bold')).place(x=0, y=0)
		flag2 = 1
	elif((flag1 == 0)and(flag2 == 1)):
		result = int(str(result) + str(num.get()))
		new_value = display_text + str(num.get())
		display_text = new_value
		display = tk.Label(window_1, text=display_text,width=50,height=3, bg="white", fg="black",font=('calibre',10, 'bold')).place(x=0, y=0)
		print (result)
	else:
		global num2
		num2= num.get()
		new_value = display_text + str(num2)
		display_text = new_value
		display = tk.Label(window_1, text=display_text,width=50,height=3, bg="white", fg="black",font=('calibre',10, 'bold')).place(x=0, y=0)
		print (num2)
		Calculate()
def TakeOperation():
	global flag1
	global operation
	global display_text
	global new_value
	if operation.get()==1:
		new_value = display_text + "+"
		display_text = new_value
		display = tk.Label(window_1, text=display_text,width=50,height=3, bg="white", fg="black",font=('calibre',10, 'bold')).place(x=0, y=0)
	elif operation.get()==2:
		new_value = display_text + "-"
		display_text = new_value
		display = tk.Label(window_1, text=display_text,width=50,height=3, bg="white", fg="black",font=('calibre',10, 'bold')).place(x=0, y=0)
	elif operation.get()==3:
		new_value = display_text + "×"
		display_text = new_value
		display = tk.Label(window_1, text=display_text,width=50,height=3, bg="white", fg="black",font=('calibre',10, 'bold')).place(x=0, y=0)
	elif operation.get()==4:
		new_value = display_text + "/"
		display_text = new_value
		display = tk.Label(window_1, text=display_text,width=50,height=3, bg="white", fg="black",font=('calibre',10, 'bold')).place(x=0, y=0)
	flag1 =1
def Calculate():
	global operation
	global result
	if operation.get()==1:
		result = result + num2
	elif operation.get()==2:
		result= result - num2
	elif operation.get()==3:
		result =result * num2
	elif operation.get()==4:
		result = result / num2
	print (result)
def Finalize():
	global display_text
	global new_value
	new_value = display_text + "="
	display_text = new_value
	display = tk.Label(window_1, text=display_text,width=50,height=3, bg="white", fg="black",font=('calibre',10, 'bold')).place(x=0, y=0)
	new_value = display_text + str(result)
	display_text = new_value
	display = tk.Label(window_1, text=display_text,width=50,height=3, bg="white", fg="black",font=('calibre',10, 'bold')).place(x=0, y=0)
	print (result)
def Escape():
	global num
	global flag1
	global flag2
	global result
	global display_text
	global operation
	flag , num2 , result, flag2  = 0,0,0
	display_text = " "
	display = tk.Label(window_1, text=display_text,width=50,height=3, bg="white", fg="black",font=('calibre',10, 'bold')).place(x=0, y=0)
	flag1 =0

B_1  =tk.Radiobutton(window_1 ,value=1,variable=num, text = "1",width=5,height=1, bd = '3',font=('calibre',15, 'bold'), command = TakeOperands)
B_1.place(x= 0,y = 70)

B_2  =tk.Radiobutton(window_1 ,value=2,variable=num, text = "2",width=5,height=1, bd = '3',font=('calibre',15, 'bold'), command = TakeOperands)
B_2.place(x= 70,y = 70)

B_3  =tk.Radiobutton(window_1 ,value=3,variable=num, text = "3",width=5,height=1, bd = '3',font=('calibre',15, 'bold'), command = TakeOperands)
B_3.place(x= 140,y = 70)

B_4  =tk.Radiobutton(window_1 ,value=1,variable=operation, text = "+",width=5,height=1, bd = '3',font=('calibre',15, 'bold'),command = TakeOperation)
B_4.place(x= 210,y = 70)

B_1  =tk.Radiobutton(window_1 ,value=4,variable=num, text = "4",width=5,height=1, bd = '3',font=('calibre',15, 'bold'), command = TakeOperands)
B_1.place(x= 0,y = 120)

B_2  =tk.Radiobutton(window_1 ,value=5,variable=num, text = "5",width=5,height=1, bd = '3',font=('calibre',15, 'bold'), command = TakeOperands)
B_2.place(x= 70,y = 120)

B_3  =tk.Radiobutton(window_1 ,value=6,variable=num, text = "6",width=5,height=1, bd = '3',font=('calibre',15, 'bold'), command = TakeOperands)
B_3.place(x= 140,y = 120)

B_4  =tk.Radiobutton(window_1 ,value=2,variable=operation, text = "-",width=5,height=1, bd = '3',font=('calibre',15, 'bold'),command = TakeOperation)
B_4.place(x= 210,y = 120)

B_1  =tk.Radiobutton(window_1 ,value=7,variable=num, text = "7",width=5,height=1, bd = '3',font=('calibre',15, 'bold'), command = TakeOperands)
B_1.place(x= 0,y = 170)

B_2  =tk.Radiobutton(window_1 ,value=8,variable=num, text = "8",width=5,height=1, bd = '3',font=('calibre',15, 'bold'), command = TakeOperands)
B_2.place(x= 70,y = 170)

B_3  =tk.Radiobutton(window_1 ,value=9,variable=num, text = "9",width=5,height=1, bd = '3',font=('calibre',15, 'bold'), command = TakeOperands)
B_3.place(x= 140,y = 170)

B_4  =tk.Radiobutton(window_1 ,value=3,variable=operation, text = "*",width=5,height=1, bd = '3',font=('calibre',15, 'bold'), command = TakeOperation)
B_4.place(x= 210,y = 170)

B_1  =tk.Radiobutton(window_1 ,value=4,variable=operation, text = "/",width=5,height=1, bd = '3',font=('calibre',15, 'bold'),command = TakeOperation)
B_1.place(x= 0,y = 220)

B_2  =tk.Button(window_1 , text = "ESC",width=5,height=1, bd = '3',font=('calibre',15, 'bold'), command = Escape)
B_2.place(x= 70,y = 220)

B_3  =tk.Radiobutton(window_1 ,value=0,variable=num, text = "0",width=5,height=1, bd = '3',font=('calibre',15, 'bold'), command = TakeOperands)
B_3.place(x= 140,y = 220)

B_4  =tk.Radiobutton(window_1 , text = "=",width=5,height=1, bd = '3',font=('calibre',15, 'bold'), command = Finalize)
B_4.place(x= 210,y = 220)


B_20  =tk.Button(window_1 , text = "Close the window" , bd = '5' , command = window_1.destroy)
B_20.pack(side = tk.BOTTOM)

window_1.mainloop()

