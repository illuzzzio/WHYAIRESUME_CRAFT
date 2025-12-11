from tkinter import Tk, Entry , Label, Button , messagebox
from turtle import title
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from textwrap import wrap
from tkinter import messagebox, filedialog





def upload_photo():
    global profile_photo_path
    profile_photo_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    messagebox.showinfo("Photo Selected", f"Selected: {profile_photo_path}")

def generate():
    name = gg1.get()
    age =  gg2.get()
    # validation...
    if not name or not age.isdigit():
        messagebox.showerror(title= "Something went Wrong", message="Something is wrong with name or the age is not in integer format..")
        return 
    
    file_name = f"{name.replace(' ','_')}.pdf"
# initialization of the canvas
    blank_pdf_page = canvas.Canvas(file_name)

    blank_pdf_page.drawString(x= 100, y= 750, text= f"Name: {name}")
    blank_pdf_page.drawString(x= 100 ,y= 750, text= f"Age: {age}" )
    blank_pdf_page.save()

    messagebox.showinfo(title= "Success", message= "You PDF file has been saved successfully")

# from this code over here , user can start writing his own stuff , the above code is for name and age field initilization
main_window = Tk()
main_window.title("WHYAIRESUME")


Label(main_window, text="Name").pack()
gg1 = Entry(main_window)
gg1.pack()

Label(main_window,text= "Age" ).pack()
gg2 = Entry(main_window)
gg2.pack()

Button(main_window,text="Generate Resume", command=generate).pack() # pyright: ignore[reportUndefinedVariable]

main_window.mainloop()