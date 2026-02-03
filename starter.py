import tkinter as tk
from tkinter import messagebox # 🔴 You must import message box like here

class HelloName(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Hello Name")           # Set the window title to "Hello Name"
        self.geometry("600x400+300+300")   # Set the window size to 600x400 and position it at (300, 300) on the screen
        self.bg_color = "#d7aefc"          # Define a background color (light purple) for the application
        self.font_size = 20                # Define a font size to be used in the application
        self.config(bg=self.bg_color)      # Apply the background color to the main application window

        # 👇 Creates the instruction text for the user

        self.lbl_instruction = tk.Label(self,
                                        text="Enter your name in the box below",
                                        bg=self.bg_color,
                                        font=('Arial', self.font_size))
        
        # 👇 Shows the instruction label on screen

        self.lbl_instruction.pack(pady=50)

        # 👇 Creates the input box the user name and shows it

        self.input_box = tk.Entry(self,
                                font=('Arial', self.font_size))
        
        self.input_box.pack(pady=10)

        # 👇 Creates the button and shows it

        self.btn_submit = tk.Button(self,
                                    text="Submit",
                                    command=self.get_name,
                                    fg="forest green",
                                    font=('Arial', self.font_size))
        self.btn_submit.pack(pady=10)

        # 👇 Creates the output box and packs it to the window

        self.output_box = tk.Label(self,
                                    text="",
                                    bg=self.bg_color,
                                    font=('Arial', self.font_size))
        self.output_box.pack(pady=10)

    def get_name(self): 
        my_name = self.input_box.get().strip()
        self.display_output(my_name)

    def display_output(self, name):
        if not self.presence_check(name):
            self.error_handler("Name cannot be left blank")
            return "Presence check failed"
        elif not self.length_check(name):
            self.error_handler("The name should be at least 3, and no more than 20 characters long")
            return "Length check failed"
        elif not self.no_numbers_check(name):
            self.error_handler("The name should be alphabetic characters only, 🔴 No numbers 🔴")
        else:
            output = f"Hello 👋{name.title()}💐"
            self.output_box.config(text=output)
            return "Ok"

    def error_handler(self, error_message):
        try:         
             messagebox.showerror("Error", error_message)
        except Exception as e:
            print("Something went wrong: {e}")        
        
    def presence_check(self, name):
        return bool(name)
    
    def length_check(self, name):
        return 3 <= len(name) <= 20
    
    def no_numbers_check(self, name):
        return not any(char.isdigit() for char in name)

if __name__ == "__main__":
    app = HelloName()
    app.mainloop()