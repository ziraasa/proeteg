from googletrans import Translator
from customtkinter import *
import customtkinter

customtkinter.set_default_color_theme("dark-blue") 

class App(CTk):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
  



        
        self.title("Переводчик")


        main_frame = CTkFrame(self, fg_color=self.cget("bg"))
        main_frame.grid(row=0, column=0, padx=10, pady=60)
        


        user_label = CTkLabel(master=main_frame, text="Любой язык:")
        user_label.grid(row=1, column=0, sticky="w", pady=(0, 20))
        user_entry = CTkEntry(master=main_frame)
        user_entry.grid(row=1, column=1, pady=(0, 20), padx=10)

        login_button = CTkButton(master=main_frame, text="Перевести",
                                 command=self.button_function)
        login_button.grid(row=2, column=1, pady=(0, 10), padx=10, sticky="e")
  

        pass_label = CTkLabel(master=main_frame, text="Английский:")
        pass_label.grid(row=4, column=0, sticky="w", pady=(0, 20))
        pass_entry = CTkEntry(master=main_frame, show="*")
        pass_entry.grid(row=4, column=1, pady=(0, 10), padx=10)
        self.pass_entry = pass_entry
        self.user_entry = user_entry

    def button_function(self):

            source_text = self.user_entry.get()
            translator = Translator()
            translation = translator.translate(source_text, dest='en')
            self.pass_entry.configure(show="")
            self.pass_entry.delete(0, "end")
            self.pass_entry.insert(0,translation.text)
 


  
            

            


app = App()
app.resizable(width=False, height=False)
app.geometry("250x230")

app.mainloop()