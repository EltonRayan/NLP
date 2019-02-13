import winsound
import time 
import sys
from gtts import gTTS
import os
import pyttsx
ttm = { 
    "A" : ".- ",
"B": "-... ",
"C":"-.-. ",
"D":"-.. ",
"E":". ",
"F" :"..-. ",
"G":"--. ",
"H":".... ",
"I":".. ",
"J":".--- ",
"K":"-.- ",
"L":".-.. ",
"M":"-- ",
"N":"-. ",
"O":"--- ",
"P":".--. ",
"Q":"--.- ",
"R":".-. ",

"S":"... ",
"T":"- ",
"U":"..- ",
"V":"...- ",
"W":".-- ",
"X":"-..- ",
"Y":"-.-- ",
"Z":"--.. ",
"0":"----- ",
"1":".---- ",
"2":"..--- ",
"3":"...-- ",
"4":"....- ",
"5":"..... ",
"6":"-.... ",
"7":"--... ",
"8":"---.. ",
"9":"----. "
}

mtt = { 
    ".-":"A",
"-...":"B",
"-.-.":"C",
"-..":"D",
".":"E",
"..-.":"F",
"--.":"G",
"....":"H",
"..":"I",
".---":"J",
"-.-":"K",
".-..":"L",
"--":"M",
"-.":"N",
"---":"O",
".--.":"P",
"--.-":"Q",
".-.":"R",
"...":"S",
"-":"T",
"..-":"U",
"...-":"V",
".--":"W",
"-..-":"X",
"-.--":"Y",
"--..":"Z",
"-----":"0",
".----":"1",
"..---":"2",
"...--":"3",
"....-":"4",
".....":"5",
"-....":"6",
"--...":"7",
"---..":"8",
"----.":"9",
"/": " ",
"?":"[]"
}
def text():
    
    morse=""
    t = raw_input("Enter your text: ")
    
    for letter in t.upper():
        if letter == " ":
            morse = morse + "/ "
    
        elif letter in ttm:
           morse = morse + ttm[letter]
        else:
            morse = morse +"? "
    print("\n\nTEXT: \n" + t + "\n\nMORSE: \n" + morse )
    #ch = raw_input("\n\n DO YOU WANT TO TRANSLATE THIS IN THE FORM OF A SOUND? (Y:N): ")
    #print(ch)
    print("\n\nMORSE CODE IN SOUND: ")
    time.sleep(2)
    for x in morse:
            if x == '-':

                winsound.Beep(3500,200)
                time.sleep(.2)    
            elif x == '.':
                #print(x)
                winsound.Beep(3500,100)
                time.sleep(.2)
            elif x==' ' or x=='?':
                time.sleep(2)
            elif x=='/':
                time.sleep(4)
   # elif ch.upper() == "N":
    time.sleep(5)
             
def morse():
    t=""
    mors = raw_input("\n\nEnter the morse code: ")
    for x in mors.split():
        if x in mtt:
          t= t + mtt[x]
    
    print("\n\nMORSE: \n" + mors + "\n\nTEXT: \n" + t )
    print("\n\nTEXT IN SPEECH: ")
    time.sleep(2)
    #p = vlc.MediaPlayer("good.mp3")
    #p.play()
    
    engine = pyttsx.init()
    engine.say(t)
    engine.runAndWait()
    time.sleep(4)
        


while 1: 

    print("\n\n\t\t\tMENU")
    print("\n\n\t\t\t----")
    print("\n\t\t 1. TEXT TO MORSE ")
    print("\n\t\t 2. MORSE TO TEXT ")
    print("\n\t\t 3. EXIT ")
    op=input("\n\nEnter your option: ")
    if op== 1:
        text()
    elif op == 2:










        
        morse()
    elif op==3:
        sys.exit()
    else:
      print("\n\nINVALID OPTION")





