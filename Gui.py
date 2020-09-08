import Main
from tkinter import *



def dec_bin():
    try:
        dec_result.config(text = "Binary:    " + Main.decToBin( int(dec_in.get())) , fg = "black")
    except:
        dec_result.config(text = "WRONG NUMBER", fg = "red")
def bin_dec():
    if Main.binToDec(bin_in.get()) == "error":
        bin_result.config(text="WRONG NUMBER", fg = "red")
    else:
        bin_result.config(text = "Decimal: " + Main.binToDec(bin_in.get()), fg = "black")

def ip_stats():
    try:
        network_ = Main.network_ip(ip_in.get(), mask_in.get())
    except:
        result_.insert(END, "Hibás ip cim vagy maszk!!")
        result_.insert(END, "~~~#######################################~~~")

    result_.insert(END, "   Hálózati cím:                      " + network_)
    kioszthato_in = Main.kioszthato_cimek(ip_in.get(), mask_in.get())
    kioszthato = kioszthato_in.split("-")
    result_.insert(END, "   Első kiosztható cím:          " + kioszthato[0])
    result_.insert(END, "   Utolsó kiosztható cím:      " + kioszthato[1])
    result_.insert(END, "   Kiosztható hostok száma: " + kioszthato[2] + " db")
    result_.insert(END, "~~~#######################################~~~")

def clear_():
    result_.delete(0,END)
window = Tk()
window.geometry("770x560")
window.title("IP Calculate")

Label(window, text = "Számrendszer váltás",font=("Calibri Bold", 14), bg = "black", fg = "red" )\
    .place(anchor = N, x = 385, y = 1, width = 200)
Label(window, text = "Dec-To-Bin: ",font=("Calibri Bold", 14,)).place(x = 1, y = 40)
dec_in = Entry(window, font = ("Arial", 13))
dec_in.place(x = 110, y = 43)
Label(window, text = "Bin-To-Dec: ",font = ("Calibri Bold", 14)).place(x = 1, y = 80)
bin_in = Entry(window, font = ("Arial", 13))
bin_in.place(x = 110, y = 83)

button1 = Button(window, text = "Calculate", font = ("Calibri Bold", 12),bg = "green", padx = 50,
                 command = dec_bin)
button1.place(x = 310, y = 38)
button2 = Button(window, text = "Calculate", font = ("Calibri Bold", 12),bg = "green", padx = 50,
                 command = bin_dec)
button2.place(x = 310, y = 78)
dec_result = Label(window, text = "Binary:    xxxxxxxxxx", font = ("Calibri Bold", 14))
dec_result.place(x = 490, y = 40)
bin_result = Label(window, text = "Decimal: xxxxxxxxxx", font = ("Calibri Bold", 14))
bin_result.place(x = 490, y = 80)

Label(window, text = "IPV4 Calculator",font=("Calibri Bold", 14), bg = "black", fg = "red" )\
    .place(anchor = N, x = 385, y = 120, width = 200)
Label(window, text = "IP Cím: ",font=("Calibri Bold", 14,)).place(x = 90 , y = 160)
Label(window, text = "Maszk: ",font=("Calibri Bold", 14,)).place(x = 310, y = 160)
ip_in = Entry(window, font = ("Arial", 13))
ip_in.place(x = 155, y = 162, width = 150)
mask_in = Entry(window, font = ("Arial", 13))
mask_in.place(x = 380, y = 162, width = 150)
ip_in.insert(END,"192.168.1.1")
mask_in.insert(END,"24")

button3 = Button(window, text = "Calculate", font = ("Calibri Bold", 12),bg = "green", padx = 50,
                 command = ip_stats)
button3.place(x = 562, y = 200, width = 150, height = 30)
button4 = Button(window, text = "Clear", font = ("Calibri Bold", 12), padx = 50, bg = "light blue",
                 command = clear_)
button4.place(x = 562, y = 250, width = 150, height = 30)
result_ = Listbox(window, width=45, height=14, font=("Calibri Bold", 15), bg = "gray")
result_.place(x = 90, y = 200)
scrollbar = Scrollbar(window, orient="vertical")
scrollbar.config(command=result_.yview)
scrollbar.place(x = 543, y = 202, height = 350)

result_.config(yscrollcommand=scrollbar.set)



window.mainloop()