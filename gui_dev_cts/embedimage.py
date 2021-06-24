'''from tkinter import *  
from PIL import ImageTk,Image  
root1 = Tk()  
canvas = Canvas(root, width = 700, height = 500)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("board.png"))  
canvas.create_image(20, 20, anchor=NW, image=img) 
root.mainloop() 

# import tkinter module 
from tkinter import *   
  
# create a tkinter window
master = Tk()  
  
# Open window having dimension 200x100
master.geometry('200x100')  
    
# Create a Button
button = Button(master, 
                text = 'Submit', 
                bg='white', 
                activebackground='blue').pack()  
    
master.mainloop()'''
# Import module
'''from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry("400x400")

# Add image file
bg = PhotoImage(file = "board.png")

# Create Canvas
canvas1 = Canvas( root, width = 400,
				height = 400)

canvas1.pack(fill = "both", expand = True)

# Display image
canvas1.create_image( 0, 0, image = bg,
					anchor = "nw")

# Add Text
canvas1.create_text( 200, 250, text = "Welcome")

# Create Buttons
button1 = Button( root, text = "Exit")
button3 = Button( root, text = "Start")
button2 = Button( root, text = "Reset")

# Display Buttons
button1_canvas = canvas1.create_window( 100, 10,
									anchor = "nw",
									window = button1)

button2_canvas = canvas1.create_window( 100, 40,
									anchor = "nw",
									window = button2)

button3_canvas = canvas1.create_window( 100, 70, anchor = "nw",
									window = button3)

# Execute tkinter
root.mainloop()


        
root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.geometry("700x500")
root.mainloop()'''
# Import Required Module
from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x400')   

dwnd = PhotoImage(file = r"C:\Users\Vibhanshu Sharma\Desktop\start.png")
dwnd1=dwnd.subsample(6,6)
Button(ws, image=dwnd1, command=None, border=0).pack(pady=10)

ws.mainloop()