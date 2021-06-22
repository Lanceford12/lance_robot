import tkinter as tk
from tkinter import *
import ttsm
import PyPDF2
import threading
from tkinter import filedialog
import nltk
import spell_checker

root = tk.Tk()
root.geometry("600x700")
root.title("TTS Program")

background_image=tk.PhotoImage(file="images/background.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

roboti=tk.PhotoImage(file="images/robot.png")

heading = tk.Label(root,fg="black",text="LIZ TEXT TO SPEECH",font = "Times 16 bold italic")
heading.pack()

# Load 1000 common english words from the text file
def load_words():
    with open("word_database.txt") as json_file:
        valid_words = set(json_file.read().split())
    return valid_words

def menu():
    
    robot_img = tk.Label(root, height=400,image=roboti)
    robot_img.pack()

    label = tk.Label(root,text="Enter Text to convert below: ")
    label.pack()

    global textarea
    textarea = tk.Text(root,height=10,width=50,wrap=tk.WORD)
    textarea.pack()

    # Testing spelling suggestions
    english_words = load_words()
    textarea.insert(INSERT, spell_checker.check_spelling(["Adam", "aandd", "mary"], english_words=english_words))
    
    convert_button = tk.Button(root,bg="aqua",text="convert to speech",font = "Times 15 bold italic",command=lambda:speak(textarea.get("1.0","end")))
    convert_button.pack()

    upload_button = tk.Button(root,bg="green",fg="white",text="upload text file",font = "Times 15 bold italic",command=browseFiles)
    upload_button.pack()
    return



def speak(text):
    tokenize(text)
    x=threading.Thread(target=ttsm.speak,args=(text,))
    x.start()


def tokenize(text):
    print("ORIGINAL TEXT:", text)
    nltk.download('punkt')
    tokens = nltk.word_tokenize(text)
    print("TOKENIZED TEXT:", tokens)

    
#py2pdf
    
def browseFiles():
    f_types = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt'),
              ('CSV files',"*.csv") ]

    file = filedialog.askopenfilename(
          filetypes=f_types)
    try:
        f = open(file, "r")
        speak(f.read())
        f.close()
    except:
        speak("No file was selected")

def read(file):
         pdfFileObj=open(file, 'rb')
         pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
         print(pdfReader.numPages)
         pageObj=pdfReader.getPage(0)
         speak(pageObj.extractText())
         pdfFileObj.close()
     

def main():
    menu()

    #x=threading.Thread(target=ttsm.speak,args=("Hey there, my name is lance, how are you",))
    #x.start()
    
    
    root.mainloop()
    
    return


if __name__=="__main__":
    main()