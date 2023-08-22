from tkinter import *
from tkinter.messagebox import *
import math



calculation=""


def add_calc(symbol):
	global calculation
	calculation+=str(symbol)
	text_res.delete(1.0,"end")
	text_res.insert(1.0,calculation)

def eval_calc():
	global calculation
	try:
		result=str(eval(calculation))
		calculation=""
		text_res.delete(1.0,"end")
		text_res.insert(1.0,result)
	except:
		clear_field()
		text_res.insert(1.0,"Error")
		showerror("Error","Please input the right value")	
		

def clear_field():
	global calculation
	calculation=""
	text_res.delete(1.0,"end")

def delete():
	global calculation
	if calculation :
		calculation=calculation[:-1]	
		text_res.delete(1.0,"end")
		text_res.insert(1.0,calculation)
		
	else:
		text_res.insert(1.0,"Empty")
		showerror("Error","Please input the right value")	
		
		

root=Tk()
root.title("Calculator")
root.geometry("492x550+100+100")
f=("Calibri",30,"bold")

image=PhotoImage(file="calc.png")

root.iconphoto(True,image)

text_res=Text(root,height=2,width=24,font=f)
text_res.grid(columnspan=6)



btn_1=Button(root,text="1",command=lambda: add_calc(1),width=4,font=f)
btn_1.grid(row=2,column=1)

btn_2=Button(root,text="2",command=lambda: add_calc(2),width=4,font=f)
btn_2.grid(row=2,column=2)

btn_3=Button(root,text="3",command=lambda: add_calc(3),width=4,font=f)
btn_3.grid(row=2,column=3)

btn_4=Button(root,text="4",command=lambda: add_calc(4),width=4,font=f)
btn_4.grid(row=3,column=1)

btn_5=Button(root,text="5",command=lambda: add_calc(5),width=4,font=f)
btn_5.grid(row=3,column=2)

btn_6=Button(root,text="6",command=lambda: add_calc(6),width=4,font=f)
btn_6.grid(row=3,column=3)

btn_7=Button(root,text="7",command=lambda: add_calc(7),width=4,font=f)
btn_7.grid(row=4,column=1)


btn_8=Button(root,text="8",command=lambda: add_calc(8),width=4,font=f)
btn_8.grid(row=4,column=2)

btn_9=Button(root,text="9",command=lambda: add_calc(9),width=4,font=f)
btn_9.grid(row=4,column=3)

btn_0=Button(root,text="0",command=lambda: add_calc(0),width=4,font=f)
btn_0.grid(row=5,column=1)


btn_x10=Button(root,text="x10",command=lambda: add_calc( "*10"),width=4,font=f)
btn_x10.grid(row=5,column=2)



btn_point=Button(root,text=".",command=lambda: add_calc("."),width=4,font=f,fg="#fff",bg="#2a2d36")
btn_point.grid(row=5,column=3)



btn_plus=Button(root,text="+",command=lambda: add_calc("+"),width=4,font=f,fg="#fff",bg="#2a2d36")
btn_plus.grid(row=2,column=4)


btn_minus=Button(root,text="-",command=lambda: add_calc("-"),width=4,font=f,fg="#fff",bg="#2a2d36")
btn_minus.grid(row=3,column=4)


btn_division=Button(root,text="/",command=lambda: add_calc("/"),width=4,font=f,fg="#fff",bg="#2a2d36")
btn_division.grid(row=4,column=4)





btn_AC=Button(root,text="AC",command=clear_field,width=4,font=f,fg="#fff",bg="#3697f5")
btn_AC.grid(row=2,column=5)


btn_del=Button(root,text="DEL",command=delete,width=4,font=f,fg="#fff",bg="#2a2d36")
btn_del.grid(row=3,column=5)


btn_equal=Button(root,text="=",command=eval_calc,width=4,font=f,fg="#fff",bg="#fe9037")
btn_equal.grid(row=4,column=5)


btn_lparan=Button(root,text="(",command=lambda :add_calc("("),width=4,font=f,fg="#fff",bg="#2a2d36")
btn_lparan.grid(row=5,column=4)

btn_rparan=Button(root,text=")",command=lambda :add_calc(")"),width=4,font=f,fg="#fff",bg="#2a2d36")
btn_rparan.grid(row=5,column=5)



btn_percentage=Button(root,text="%",command=lambda :add_calc("%"),width=4,font=f,fg="#fff",bg="#2a2d36")
btn_percentage.grid(row=6,column=1)

btn_mult=Button(root,text="*",command=lambda :add_calc("*"),width=4,font=f,fg="#fff",bg="#2a2d36")
btn_mult.grid(row=6,column=2,columnspan=1)


btn_sqroot=Button(root,text="x^0.5",command=lambda :add_calc("**0.5"),width=4,font=f,fg="#fff",bg="#2a2d36")
btn_sqroot.grid(row=6,column=3,columnspan=1)


btn_root=Button(root,text="x^2",command=lambda :add_calc("**2"),width=9,font=f,fg="#fff",bg="#2a2d36")
btn_root.grid(row=6,column=4,columnspan=2)


root.mainloop()