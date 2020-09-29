import pyttsx3
from time import ctime
mytext = pyttsx3.init()
voices = mytext.getProperty('voices')
for voice in voices:
    mytext.setProperty('voice', voice.id)
newvoicerate = 150
mytext.setProperty('rate', newvoicerate)




name = input("you - ")
nam = name.lower()
v1 = "hello"
v2 = "ok bye have a good day"
v3 = "my name is L"
v4 = "sorry i can't understand"
v5 = "ki holo"
v6 = "no"
v7 = "sorry bolar dorkar nai"
v8 = "hello shuvranil, nice to meet you i am l"
v9 = "hmm aektu"
v10 = "you don't have time for me"
v11 = "bolbo naa"
v12 = "not interested at first look at your face"
v13 = "i love you too shuvranil you are so sweet"
v14 = "i will think about it"
v15 = "tumi akta pagol"
v16 = "nothing just wait for your message"
v17 = "my name is l, virtual python text reader , created by shuvranil "
v18 = "i am feeling very lucky but i am not a living being, you should merry with a living person"
v19 = ctime()
v20 = "sorry i can't singing may be in future i will try"
v21 = "i like you too shuvranil but as a friend"
v22 = "hmmmm i don't know may be"
v23 = "i am not a religious , i am a computer program but i believe in positive energy and  dark energy "
v24 = "do you mean sprite , yes  i believe in positive energy and  dark energy  "
v25 = "the age of the women is never to be asked"
v26 = "hmm"
while True:

    if nam=="bye" or nam == "okk bye" or nam == "ok bye":
        print("computer -",v2)
        mytext.say(v2)
        mytext.runAndWait()
        break   
    else:
        if nam== "hii" or nam == 'hi' or nam =="hello":
            print("computer -",v1)
            mytext.say(v1)
            mytext.runAndWait()
            nam = input("you - ")

        elif nam == "what is your name?" or nam== "your name?":
            print("computer -",v3)
            mytext.say(v3)
            mytext.runAndWait()
            nam = input("you - ")
        
        # elif nam != "bye":
        #     print("computer -",v4)
        #     mytext.say(v4)
        #     mytext.runAndWait()
        #     nam = input("you - ")

        elif nam == "oii" or nam == "oi":
            print("computer -",v5)
            mytext.say(v5)
            mytext.runAndWait()
            nam = input("you - ")
        
        elif nam =="sing a song for me":
            print("computer -",v6)
            mytext.say(v6)
            mytext.runAndWait()
            nam = input("you - ")
        
        elif nam== "sorry":
            print("computer -",v7)
            mytext.say(v7)
            mytext.runAndWait()
            nam = input("you - ")
        
        elif nam== "i am shuvranil" or nam=="my self shuvranil" or nam== "my name is shuvranil":
            print("computer -",v8)
            mytext.say(v8)
            mytext.runAndWait()
            nam = input("you - ")
        
        elif nam== "are you angry with me?":
            print("computer -",v9)
            mytext.say(v9)
            mytext.runAndWait()
            nam = input("you - ")

        elif nam== "but why are you angry with me?" or nam=="why are you angry with me?":
            print("computer -",v10)
            mytext.say(v10)
            mytext.runAndWait()
            nam = input("you - ")

        elif nam== "i love you":
            print("computer -",v12)
            mytext.say(v12)
            mytext.runAndWait()
            nam = input("you - ")
        
        elif nam== "i love you l" or nam == "love you l":
            print("computer -",v13)
            mytext.say(v13)
            mytext.runAndWait()
            nam = input("you - ")

        elif nam== "why?":
            print("computer -",v11)
            mytext.say(v11)
            mytext.runAndWait()
            nam = input("you - ")
        
        elif nam == "would you like to be my gf?" or nam == "will you be my gf?":
            print("computer -",v14)
            mytext.say(v14)
            mytext.runAndWait()
            nam = input("you - ")
        
        elif nam == "kichu na":
            print("computer -",v15)
            mytext.say(v15)
            mytext.runAndWait()
            nam = input("you - ")
        
        elif nam== "what's up?" or nam== "ki korcho?" or nam == "what are you doing?":
            print("computer -",v16)
            mytext.say(v16)
            mytext.runAndWait()
            nam = input("you - ")
        
        elif nam== "tell me about yourself" or nam == "who are you?":
            print("computer -",v17)
            mytext.say(v17)
            mytext.runAndWait()
            nam = input("you - ")
        
        elif nam== "will you merry me?":
            print("computer -",v18)
            mytext.say(v18)
            mytext.runAndWait()
            nam = input("you - ")
        
        elif nam=="waht time is it?" or nam== "time?":
            print("computer -",v19)
            mytext.say(v19)
            mytext.runAndWait()
            nam = input("you - ")

        elif nam== "do you like me?" or nam=='do you love me?':
            print("computer -",v22)
            mytext.say(v22)
            mytext.runAndWait()
            nam = input("you - ")

        elif nam == "i like you":
            print("computer -",v21)
            mytext.say(v21)
            mytext.runAndWait()
            nam = input("you - ")
        
        elif nam == "do you believe in god?":
            print("computer -",v23)
            mytext.say(v23)
            mytext.runAndWait()
            nam = input("you - ")
        

        elif nam == "please sing a song" or nam =="please sing a song for me":
            print("computer -",v20)
            mytext.say(v20)
            mytext.runAndWait()
            nam = input("you - ")

        elif nam =="do you believe in ghost?":
            print("computer -",v24)
            mytext.say(v24)
            mytext.runAndWait()
            nam = input("you - ")
        
        elif nam == "what is your age?" or nam == "your age?":
            print("computer -",v25)
            mytext.say(v25)
            mytext.runAndWait()
            nam = input("you - ")
        
        elif nam == "okk" or nam == "ok":
            print("computer -",v26)
            mytext.say(v26)
            mytext.runAndWait()
            nam = input("you - ")
        

        
          
        
    
        
       

        
        elif nam != "bye":
            print("computer -",v4)
            mytext.say(v4)
            mytext.runAndWait()
            nam = input("you - ")


            
        
            
        


            