from uuid import uuid4
class Button():
    
    def __init__ (self, text, bgColor="Orange", onClick = None, onActivate = None, relX = 0.5, relY = 0.5, relWidth = 0.6, relHeight = 0.4):
        self.text=text, 
        self.command=button_clicked,
        self.activebackground="blue", 
        self.activeforeground="white",
        anchor="center",
        bd=3,
        bg="lightgray",
        cursor="hand2",
        disabledforeground="gray",
        fg="black",
        font=("Arial", 12),
        height=2,
        highlightbackground="black",
        highlightcolor="green",
        highlightthickness=2,
        justify="center",
        overrelief="raised",
        padx=10,
        pady=5,
        width=15,
        wraplength=100
        
    def buildButton(self,main, command):
        return tk.Button(main, text=self.text, bg=self.bgColor, command=command)
        