from tkinter import *

root = Tk()
root.title('CourseSearch')
root.geometry("500x300")


#update listbox
def update(data):
#clear the listbox
    my_list.delete(0, END)

#add items to listbox 
    for item in data: 
        my_list.insert(END, item)

#update entry box with listbox clicked

def fillout(e):
    #delete whatever is in entry box
    my_entry.delete(0, END)
    #add clicked list tiem to entry box
    my_entry.insert(0, my_list.get(ANCHOR))

#check entry vs list
 # grab what was typed 
def check(e):
    typed = my_entry.get()

    if typed == '':
        data = list1
    else: 
        data = []
        for item in list1:
            if typed.lower() in item.lower():
                data.append(item)
    #update listbox with selected items

    update(data)



my_label = Label(root, text="Start  Typing...", 
font=("Helvetica", 14), fg="grey")

my_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 20))
my_entry.pack()

my_list = Listbox(root, width=50)
my_list.pack(pady=40)

#create a loop  to loop through database and add classes to list
list1 = ["532525", "5352532", "434224", "54354534", "545435"]

update(list1)
#create a binding on the list onclick

my_list.bind("<<ListboxSelect>>", fillout)
#createa a binding on the entry box

my_entry.bind("<KeyRelease>", check)

root.mainloop()

