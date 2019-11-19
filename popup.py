from tkinter import *
from tkinter import messagebox

window=Tk()

window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
window.withdraw()

messagebox.showinfo('System Message', 'Reading process is finished, Please proceed!')

window.deiconify()
window.destroy
window.quit()