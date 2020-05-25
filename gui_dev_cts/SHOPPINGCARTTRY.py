import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox


root=Tk()


while True: 
	try: 
		bg = float(input("Enter your budget : ")) 
		
		s = bg 
	except ValueError: 
		print("PRINT NUMBER AS A AMOUNT") 
		continue
	else: 
		break


a ={"name":[], "quant":[], "price":[]} 


b = list(a.values()) 


na = b[0] 


qu = b[1] 


pr = b[2] 


while True: 
	try: 
		ch = int(input("1.ADD\n2.EXIT\nEnter your choice : ")) 
	except ValueError: 
		print("\nERROR: Choose only digits from the given option") 
		continue
	else: 
		
		if ch == 1 and s>0:	 

						 
			pn = input("Enter product name : ") 
			
			q = input("Enter quantity : ") 
			
			p = float(input("Enter price of the product : ")) 

			if p>s: 
				
				print("\nCAN, T BUT THE PRODUCT") 
				continue

			else: 
				
				if pn in na: 
					
					ind = na.index(pn) 

					
					qu.remove(qu[ind]) 

					
					pr.remove(pr[ind]) 

					
					qu.insert(ind, q) 

					
					pr.insert(ind, p) 

					
					s = bg-sum(pr) 

					print("\namount left", s) 
				else: 
					
					na.append(pn) 

					
					qu.append(q) 

					
					pr.append(p)	 

					
					s = bg-sum(pr) 

					print("\namount left", s) 

		
		elif s<= 0: 
			print("\nNO BUDGET") 
		else: 
			break


print("\nAmount left : Rs.", s) 


if s in pr: 
	
	print("\nAmount left can buy you a", na[pr.index(s)]) 

print("\n\n\nGROCERY LIST") 


for i in range(len(na)): 
	print(na[i], qu[i], pr[i]) 








root.title("shopping cart calculator")
item_name=tk.StringVar()

name_label=ttk.Label(root, text='Enter item Name:')
name_label.pack(side='left', padx=(0,10))


t = tk.Text(root, height=4, width=50)
for x in na:
    t.insert(END, x + '\n')
t.pack()
quit_button=ttk.Button(root,text='kill',command=root.destroy)
quit_button.pack(side='right', fill='y',expand=True)


root.mainloop()