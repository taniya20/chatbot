
#Front-end (GUI)
import Tkinter
#import chat_back
from chat_back import chatbot


def ai(x,reply):
    if '@' in x:
        f=open('qlist.txt','a')
        writeup="Email: "+reply+'\n'
        f.write(writeup)
        f.close
        w="Okay I 'll respond back! Tell me if you have any other queries besides this"

    else:
        w="Sorry! I need to think over it. Please leave your email address and I'll respond back"
        f=open('qlist.txt','a')
        writeup="Query: "+x+'\n'
        f.write(writeup)
        f.close

    return w

#class to create window
class myapp(Tkinter.Tk):
    def __init__(self,parent): #self : current object ; parent : widget to act as parent of current object
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        #self.canvas = Canvas(self.Tk, width=500, height=500)
        #self.canvas.pack()
        self.initialize()

    def initialize(self):

        top1=Tkinter.Label(self,text="THE JMI CPP",fg="red",font=("Times New Roman",18,"bold"),bg="yellow")
        top1.grid(row=0,column=0)
        top2=Tkinter.Label(self,text="Ask anything about JMI",fg="black",font=("Times New Roman",14))
        top2.grid(row=1,column=0)
        top3=Tkinter.Label(self)
        top3.grid(row=2,pady=8)
        self.entryvar1=Tkinter.StringVar() #binding entry widget to StringVar() instance and set and get entry through that variable
        entry1=Tkinter.Entry(self,textvariable=self.entryvar1,bd=3,width=32)
        entry1.bind("<Return>", self.OnClick)
        entry1.grid(row=4)
        
        label1=Tkinter.Label(self,text="Enter your query",fg="black",font=("Times New Roman",14,"bold"),bg="grey")
        label1.grid(row=3)
        
        scroll=Tkinter.Scrollbar(self)
        scroll.grid(row=12,column=1,rowspan=10)
        
        self.entryvar2=Tkinter.StringVar()
        self.output=Tkinter.Text(self,wrap=Tkinter.WORD,height=33,width=167,yscrollcommand=scroll.set,bg="grey") #for text window
        self.output.grid(row=12)
      
        scroll.config(command=self.output.yview_pickplace("end")) #to place the cursor at the endline
        
      


        self.output.insert(Tkinter.INSERT, "Hello!")
        self.output.insert(Tkinter.INSERT, "\nIt's nice to see you here!")
        self.output.insert(Tkinter.INSERT, "\nHow may I help you?")

        btn1=Tkinter.Button(self,text="Get Answer",command=self.OnClick)
        btn1.grid(row=5)

        #self.geometry("1080x800+200+200")


    def OnClick(self):
        inp=self.entryvar1.get()
        if (chatbot(inp)=="Sorry! I need to think over it. Please leave your email address and I'll respond back"):
            self.output.insert(Tkinter.END,"\n>>>User  : "+inp)
            x=self.entryvar1.get()
            self.output.insert(Tkinter.END,"\n   JMICPP : "+ai(x,inp))
        else:
            self.output.insert(Tkinter.END,"\n>>>User  : "+inp)
            self.output.insert(Tkinter.END, "\n  JMICPP : "+chatbot(inp))
            self.entryvar1.set("")
            self.output.yview(Tkinter.END)
    def OnPressEnter(self,event):
        inp=self.entryvar1.get()
        if (chatbot(inp)=="Sorry! I need to think over it. Please leave your email address and I'll respond back"):
            self.output.insert(Tkinter.END,"\n>>>User  : "+inp)
            x=self.entryvar1.get()
            self.output.insert(Tkinter.END,"\n   JMICPP : "+ai(x,inp))
        else:
            self.output.insert(Tkinter.END,"\n>>>User  : "+inp)
            self.output.insert(Tkinter.END,"\n   JMICPP : "+chatbot(inp))
            self.entryvar1.set("")
            self.output.yview(Tkinter.END)

if __name__ =="__main__":     
    app = myapp(None)
    app.title('JMI Chatterbot')
    app.geometry('850x600')
    #app['bg'] = 'grey'
    
    app.mainloop() # show window
    
