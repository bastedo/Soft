
import Tkinter

from Tkinter import *
import chessboard
from PIL import Image
from PIL import ImageTk
import node


from tkFileDialog import askopenfilename

global game_board, turn, wcastle, bcastle, wcaptured, bcaptured

turn = 1
wcastle = 0
bcastle = 0
selected = None
moves = []
captures = []
wcaptured = []
bcaptured = []
game_board = [None for i in range(64)]
en_passent = None




class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
    def setup_game(self, positions, figures):
        """Puts all of the pieces on board"""

        

        turn = 1
        wcastle = 0
        bcastle = 0
        wcaptured = []
        bcaptured = []
        
        for i in range(64):
            game_board[i] = None
                
        for i in range(len(positions)):
            temp1 = positions[i]
            position = temp1[0]-1+(8-temp1[1])*8
            s = figures[i]
            s+=str(temp1[2])
            game_board[position]= s
            
           # print  game_board[5]
            



        
        
    def initialize(self):
        self.grid()

        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"/home/student/Desktop/primer1/puzzz2.jpg")

        button = Tkinter.Button(self,text=u"...",
                                command=self.OnButtonClick1)
        button.grid(column=1,row=0)        
        
        button = Tkinter.Button(self,text=u"Click me !",
                                command=self.OnButtonClick2)
        button.grid(column=2,row=0)
        
        button = Tkinter.Button(self,text=u"Click me !",
                                command=self.OnButtonClick3)
        button.grid(column=3,row=1)
        
        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        self.labelVariable.set(u"/home/student/Desktop/primer1/puzzz2.jpg")

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,True)
        self.update()
        self.geometry(self.geometry())       
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnButtonClick1(self):
        filename = askopenfilename()
        self.labelVariable.set( filename+" (You clicked the button)" )
        self.entryVariable.set(filename)
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        self.update()
        self.geometry(self.geometry())       
    def OnButtonClick2(self):

        filepath = self.entryVariable.get()
        img = ImageTk.PhotoImage(Image.open(filepath).resize((200,200)))
        #self.labelVariable.set(img)
        
        w = Label(self, image=img)
        w.photo = img
        w.pack(side = "bottom", fill = "both", expand = "yes")

        w.grid(column=0,row=1,columnspan=2, rowspan=2,sticky='EW')
        positions, figures = chessboard.main(filepath)
        self.setup_game(positions, figures)
        
        #print positions
        #print figures
        print game_board
        
        nodeA = node.Node(game_board, 0, 1, "", 1, 1, None)
        #nodeA.generate_nodes()
        self.update()
        self.geometry(self.geometry())       
       # display_image(img)

    
    def OnButtonClick3(self):
        print game_board[48]
        select_piece(48)
        print moves
        print captures
        self.update()
        self.geometry(self.geometry())       
        
    def OnPressEnter(self,event):
        self.labelVariable.set( self.entryVariable.get()+" (You pressed ENTER)" )
        self.update()
        self.geometry(self.geometry())       
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.geometry("400x300")
    app.mainloop()