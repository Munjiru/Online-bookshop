import tkinter
from tkinter import *
#function to delete entries from the fields
def clear_all():
    title_field.delete(0,END)
    author_field.delete(0, END)
    books_field.delete(0, END)
    description_field.delete(0, END)
    price_field.delete(0, END)


#function to add books to the list box

#function to add book to list box
#function to generate report which includes error handling
def generate_report():
    try:
        books_data={
            "Book Title": book_title_entry.get(),
            "Book Author": book_author_entry.get(),
            "Price":price_entry.get()
        }
        books_text=""
        for key,value in books_data.items():
            books_text +=f"{key}: {value}\n"
        with open ("data.txt", "w")as file:
            file.write(books_text)
        label1.config(text=f"Book Title:{book_title}\n Book Author:{book_author}\n Price: {price} ")
    except Exception as e:
        label1.config(text=f"an error occured: {e} ")
#function to delete books from the listbox
#def delete_book()  :

if __name__ =="__main__":
    root=Tk()
    root.configure(background='light gray')
    root.geometry("400x350")
    root.title ("Online Bookshop System")
    #creating labels

    label2 = Label(root, text="Book Title: ", fg='black', bg='teal')
    label2.grid(row=1, column=0, padx=10, pady=10)
    label3 = Label(root, text="Book Author: ", fg='black', bg='teal')
    label3.grid(row=2, column=0, padx=10, pady=10)
    label4 = Label(root, text=" Books: ", fg='black', bg='teal')
    label4.grid(row=3, column=0, padx=10, pady=10)
    label5 = Label(root, text="Description: ", fg='black', bg='teal')
    label5.grid(row=4, column=0, padx=10, pady=10)
    label6= Label(root, text="Price: ", fg='black', bg='teal')
    label6.grid(row=5, column=0, padx=10, pady=10)
    #creating clear button
    button1 = Button(root, text="Clear: ", fg='black', bg='teal',command= clear_all)
    button1.grid(row=9, column=1, pady=10)
    button2= Button(root,text="Generate Report: ", fg='black', bg='teal', command= generate_report)
    button2.grid(row=10, column=1,pady=10)
    # creating a drop down list
    books = ["Game of Thrones-John Roberts: ", "Avatar-Grace Wicks: ", "The Bible-Holy Spirit: "]
    # creating a string var to store the selected items
    selected_item = tkinter.StringVar(root)
    selected_item.set(books[0])
    # creating the drop down menu
    books_menu = tkinter.OptionMenu(root, selected_item, *books)
    books_menu.config(fg='black', bg='teal')
    books_menu.grid(row=3, column=1, padx=10, pady=10)
    #creating entry boxes/fields
    title_field= Entry (root)
    title_field.grid(row=1, column=1,padx=10,pady=10)
    author_field = Entry(root)
    author_field.grid(row=2, column=1, padx=10, pady=10)
    description_field = Entry(root)
    description_field.grid(row=4, column=1, padx=10, pady=10)
    price_field = Entry(root)
    price_field.grid(row=5, column=1, padx=10, pady=10)

    root.mainloop()
