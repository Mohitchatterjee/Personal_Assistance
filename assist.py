#pip install pyttsx3
import os
import pyttsx3
import pywhatkit as kit
import speech_recognition as sr
import psutil
import smtplib as s
import datetime
import winsound
import phonenumbers 
from phonenumbers import geocoder
from win10toast import ToastNotifier
engine = pyttsx3.init()
voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[1].id)  #male voice=0 and female voice=1
def battery_info():
            a=psutil.sensors_battery()
            p=str(a.percent)
            engine = pyttsx3.init()
            print('Your system has '+p+'% battery now') 
            engine.say(" your system has "+p+" percent battery now")
            engine.runAndWait()
def system_info():
             a=psutil.sensors_battery()
             p=str(a.percent)
             engine = pyttsx3.init()
             print('Manufacturer - Hewlett Packard\nDevice Name - Desktop Lattc6e\nProcessor - Intel Core i5-8230u @ 1.60 GHz  1.80 GHz \nRAM - 4 GB \nSystem Type - 64 bit operating system \nOS Edition- Windows 10 Pro')
             engine.say('manufacturer is hewlett packard\ndevice name is desktop latt c 6 e\n processor is intel core i 5 8230u @ 1.60 giga hertz  or 1.80 giga hertz \n rem is 4 giga byte \n system type is 64 bit operating system and windows 10 pro is installed in here')
             engine.runAndWait()
             engine = pyttsx3.init()
             print('Your system has '+p+'% battery now') 
             engine.say(" and your system has "+p+" percent battery now")
             engine.runAndWait()
def shutdown():
           os.system('shutdown /s /t 30')
def sendWhatsapp():
           num=str(input('Number: '))
           num1='+91'+str(num)
           msg=input('Messege: ')
           hr=int(input('Hour: '))
           mi=int(input('Minute: '))
           engine = pyttsx3.init()
           engine.say("Thank you sir...i will sent your message to this number at right time.")
           engine.runAndWait()
           kit.sendwhatmsg(num1,msg,hr,mi)
def searching():
          r=sr.Recognizer()
          with sr.Microphone() as mic:
                 audio=r.listen(mic)
          print(r.recognize_google(audio)) 
          find=r.recognize_google(audio)
            #find=input()
          print('Searching........')
          kit.search(find)  
def phn_num_valid(num):
               phn_num=phonenumbers.parse(num)
               possible=phonenumbers.is_possible_number(phn_num)
               if possible==True:
                     valid=phonenumbers.is_valid_number(phn_num)
                     if valid==True:
                          engine = pyttsx3.init()
                          engine.say("Yes, Phone Number is valid.")
                          engine.runAndWait()
                          print('This number is from :')
                          print( geocoder.description_for_number(phn_num,'en'))
                          return "Yes, Phone Number is valid."
                     else:
                          engine = pyttsx3.init()
                          engine.say("No sir..,phone Number is not valid.")
                          engine.runAndWait()
                          return "No valid Phone Number."
               else:
                    engine = pyttsx3.init()
                    engine.say("sir.....Please Enter 10 Digit valid Number follow by +91.")
                    engine.runAndWait()
                    return "Please Enter 10 Digit valid Number with +91 in the starting."
def alrm():
               engine = pyttsx3.init()
               engine.say("Sure sir.. Could you enter which time i remind u..and what i remind for u")
               engine.runAndWait()
               print('In 24 Hour format')
               timing =input('Enter Time here:  ')
               msg=input('Whats the Reminder: ')
               engine = pyttsx3.init()
               engine.say("I remind u on time sir...don't... worry....")
               engine.runAndWait()
               while True:
                     current_time=datetime.datetime.now()
                     alarm_time=str(current_time.hour)+':'+str(current_time.minute)
                     if alarm_time==timing:
                      notify=ToastNotifier()
                      winsound.Beep(frequency=250,duration=10000)
                      notify.show_toast('Alarm',msg,duration=50)
                      return 'over' 
while True:
 engine = pyttsx3.init()
 engine.say("I am Listening")
 engine.runAndWait()
 print("Listening........")
 r=sr.Recognizer()
 with sr.Microphone() as mic:
       r.pause_threshold=0.7
       audio=r.listen(mic)
 print(r.recognize_google(audio)) 
 a=r.recognize_google(audio)
 if ('Infi' in a or 'Infy' in a or 'Hello' in a or 'Hi' in a or 'Hey' in a or 'infi' in a or 'infy' in a or 'hello' in a or 'hi' in a or 'hey' in a or 'ok' in a or 'Ok' in a) and ('Infi' in a or 'Infy' in a or 'Hello' in a or 'Hi' in a or 'Hey' in a or 'infi' in a or 'infy' in a or 'hello' in a or 'hi' in a or 'hey' in a):
   engine = pyttsx3.init()
   engine.say("Hi Mohit sir\n I am Your In-fee\n What can i do for you.....\n I am listening your choice sir")
   engine.runAndWait()
   while True:
     voices = engine.getProperty('voices')       
     engine.setProperty('voice', voices[1].id)  #male voice=0 and female voice=1
     engine = pyttsx3.init()
     r=sr.Recognizer()
     with sr.Microphone() as mic:
       audio=r.listen(mic)
     print(r.recognize_google(audio)) 
     n=r.recognize_google(audio)
     if('menu' in n or 'MENU' in n) and ('menu' in n or 'MENU' in n):
       engine = pyttsx3.init()
       engine.say("Ok sir")
       engine.runAndWait()
       print('1.Google \t5.LinkedIn\n2.MySQL \t6.Udemy\n3.WhatsApp \t7.Gmail\n4.YouTube')
       voices = engine.getProperty('voices')       
       engine.setProperty('voice', voices[1].id)  #male voice=0 and female voice=1
       engine = pyttsx3.init()
       engine = pyttsx3.init()
       engine.say("This is your options")
       engine.say("you can choose here sir")
       engine.runAndWait()
       while True:
        r=sr.Recognizer()
        with sr.Microphone() as mic:
           audio=r.listen(mic)
        print(r.recognize_google(audio)) 
        n=r.recognize_google(audio)
        engine = pyttsx3.init()
        engine.say("Ok sir")
        engine.runAndWait()
        if ('open' in n or 'start' in n or 'excecute' in n or 'run' in n or 'launch' in n or 'google' in n or 'chrome' in n or 'play' in n or 'net' in n or 'internet' in n or 'surf' in n or 'surfing' in n) and ('chrome' in n or 'google' in n or 'browser' in n or 'net' in n or 'internet' in n  or 'surf' in n or 'surfing' in n or 'Chrome' in n or 'Google' in n or 'Browser' in n or 'Net' in n or 'Internet' in n  or 'Surf' in n or 'Surfing' in n):
          engine = pyttsx3.init()
          engine.say("Google Chrome is opening..")
          engine.runAndWait()
          os.system('chrome')
        elif ('can' in n or 'you' in n or 'kya' in n or 'mere' in n or 'play' in n) and('song' in n or 'gaana' in n or 'baja' in n):
          engine = pyttsx3.init()
          engine.say("can you speak the name of your song")
          engine.runAndWait()
          r=sr.Recognizer()
          with sr.Microphone() as mic:
           audio=r.listen(mic)
          song=r.recognize_google(audio)
          print(r.recognize_google(audio)) 
          engine.say("sure sir..")
          engine.runAndWait()
          kit.playonyt(song)
        elif ('open' in n or 'start' in n or 'excecute' in n or 'run' in n or 'launch' in n or 'whatsapp' in n or 'chat' in n or 'send' in n or 'sending' in n or 'msg' in n or 'message' in n or 'social media' in n or 'text' in n or 'txt' in n or 'reply' in n or 'WhatsApp' in n)  and ('chatting social media' in n or 'social media' in n or 'send' in n or 'sending' in n or 'msg' in n or 'message' in n  or 'text' in n or 'txt' in n or 'reply' in n or 'chat' in n or 'chatting' in n or 'whatsapp' in n or 'WhatsApp' in n):
          engine = pyttsx3.init()
          engine.say("ok sir\nWhatsApp is opening")
          engine.runAndWait()
          os.system('chrome web.whatsapp.com')
      
        elif ('open' in n or 'start' in n or 'excecute' in n or 'run' in n or 'launch' in n  ) and ('mysql' in n or 'MYSQL' in n or 'MySql' in n or 'DB' in n or 'database' in n or 'my database' in n):
          engine = pyttsx3.init()
          engine.say("ok sir\nMY SQL is opening")
          engine.runAndWait()
          os.system('Mysql')
     
        elif ('open' in n or 'start' in n or 'excecute' in n or 'run' in n or 'launch' in n or 'listen' in n or 'watches' in n or 'watch' in n or 'youtube' in n or 'play' in n or 'playing' in n ) and ('youtube' in n or 'videos' in n or 'video' in n  or 'play' in n or 'playing' in n):
         engine = pyttsx3.init()
         engine.say("ok sir\nYoutube is opening")
         engine.runAndWait()
         os.system('chrome Youtube.com')
        elif ('open' in n or 'start' in n or 'excecute' in n or 'run' in n or 'launch' in n or 'linkedin' in n or 'watches' in n or 'watch' in n or 'professional' in n or 'surfing' in n or 'search' in n  or 'searching' in n ) and ('linkedin' in n or 'surfing' in n or 'search' in n  or 'searching' in n or 'song' in n or 'videos' in n or 'video' in n):
         engine = pyttsx3.init()
         engine.say("ok sir\nLinkeIn is opening")
         engine.runAndWait()
         os.system(' chrome www.linkedin.com/feed/')
        elif ('open' in n or 'start' in n or 'excecute' in n or 'run' in n or 'launch' in n or 'Udemy' in n or 'learning' in n or 'learn' in n or 'course' in n or 'courses' in n) and ('Udemy' in n or 'learning' in n or 'learn' in n or 'course' in n or 'courses' in n):
         engine = pyttsx3.init()
         engine.say("ok sir\nUdemy is opening")
         engine.runAndWait()
         os.system('chrome www.udemy.com')
        elif ('open' in n or 'start' in n or 'excecute' in n or 'run' in n or 'launch' in n or 'send' in n or 'mail' in n or 'gmail' in  n or 'Gmail' in n) and ('mail' in n or 'chrome' in n or 'google' in n or 'browser' in n or 'Gmail' in n):
         engine = pyttsx3.init()
         engine.say("ok sir\nG-mail is opening")
         engine.runAndWait()
         os.system('chrome Gmail.com')
        elif ('can' in n or 'you' in n or 'kya' in n or 'mere' in n or 'play' in n) and('song' in n or 'gaana' in n or 'baja' in n):
          engine = pyttsx3.init()
          engine.say("can you speak the name of your song")
          engine.runAndWait()
          r=sr.Recognizer()
          with sr.Microphone() as mic:
           audio=r.listen(mic)
          song=r.recognize_google(audio)
          print(r.recognize_google(audio)) 
          engine.say("sure sir..")
          engine.runAndWait()
          kit.playonyt(song)          
        elif('leave' in n or 'stop' in n or 'end' in n) and ('leave' in n or 'stop' in n or 'end' in n ):
           engine = pyttsx3.init()
           engine.say("Thank you so much sir...Have a nice day")
           engine.runAndWait()
           exit()
        else:
          engine = pyttsx3.init()
          engine.say("UHM....sorry.....I didn't recognize your text sir\n speak again please....")
          engine.runAndWait()
     elif('search' in n or 'searching' in n or 'Searching' in n or 'Search' in n):
          engine = pyttsx3.init()
          engine.say("what do u want to search sir..")
          engine.runAndWait()
          searching()
     elif('send a messege' in n or 'message' in n or 'Message' in n and 'whatsapp' in n or 'Whatsapp' in n):
           engine = pyttsx3.init()
           engine.say("sure sir...can you please provide me a number , message and delivered timing here..")
           engine.runAndWait()
           sendWhatsapp()
     elif ("check" in n or 'phone number' in n or 'valid' in n or 'validation' in n):
          engine = pyttsx3.init()
          engine.say("sure sir...can you write a number here..")
          engine.runAndWait()
          nums=input()
          num='+91' +nums
          print(phn_num_valid(num))
     elif ('configuration' in n or 'status' in n) and ('system' in n or ' machine' in n or ' lappy' in n or 'lappi' in n or 'pc' in n or 'computer' in n or 'laptop' in n):
            system_info()
     elif ('battery' in n or 'power' in n) and ('battery' in n or 'power' in n):
            battery_info()
     elif ('Name' in n or 'name' in n or 'MY' in n or 'My' in n or 'my' in n or 'Owner' in n  or 'owner' in n) and ('Tell' in n or 'tell' in n or 'Owner' in n  or 'owner' in n):
             engine = pyttsx3.init() 
             engine.say("His name is Mohit Chatterjee\n He is very talented Guy \n he belongs to shah-dol madh-ya pradesh\n currently he persuing bachelor of technology \n he has quit intrested on computers and coding and you know...\n I am very glad that he create me.........\n you may contact him any time from this mail ")
             engine.runAndWait()
             print('Email : chatterjeemohit160@gmail.com')
             
     elif ('can' in n or 'you' in n or 'kya' in n or 'mere' in n or 'play' in n or 'want') and('songs' in n or 'gaana' in n or 'baja' in n or 'song' in n):
          engine = pyttsx3.init()
          engine.say("can you speak the name of your song")
          engine.runAndWait()
          r=sr.Recognizer()
          with sr.Microphone() as mic:
           audio=r.listen(mic)
          song=r.recognize_google(audio)
          print(r.recognize_google(audio)) 
          engine.say("sure sir..")
          engine.runAndWait()
          kit.playonyt(song)
     elif('shutdown' in n or 'Shutdown' in n or 'shut down' in n or 'Shut down' in n):
           engine = pyttsx3.init()
           engine.say("do you really want me to shutdown")
           engine.runAndWait()
           r=sr.Recognizer()
           with sr.Microphone() as mic:
                    r.pause_threshold=0.7
                    audio=r.listen(mic)
           print(r.recognize_google(audio)) 
           ans=r.recognize_google(audio)
           if('yes' in ans or 'Yes' in ans):
               engine = pyttsx3.init()
               engine.say("sure sir....have a nice day")
               engine.runAndWait()
               shutdown()
           else:
               engine = pyttsx3.init()
               engine.say("ok sir")
               engine.runAndWait()
     elif ('Alarm' in n or 'alarm' in n or 'remind' in n or 'Remind' in n or 'Reminder' in n or 'reminder' in n):
           alrm()
     elif ('How' in n or 'how' in n ) and ('You' in n or 'you' in n ):
              engine = pyttsx3.init()
              engine.say("I am Pretty good sir.\n what about you\n how was your day?")
              engine.runAndWait()
              r=sr.Recognizer()
              with sr.Microphone() as mic:
                   r.adjust_for_ambient_noise(mic,duration=1)
                   audio=r.listen(mic)
              print(r.recognize_google(audio)) 
              ans=r.recognize_google(audio)
              if ('good' in ans or 'Good' in ans or 'fine' in ans or 'Fine' in  ans):
                  engine = pyttsx3.init()
                  engine.say("I am happy to know that")
                  engine.runAndWait()  
              elif ('hectic' in ans or 'busy' in ans or 'Hectic' in ans or 'Busy' in ans or 'day' in ans or 'Day' in ans or 'Schedule' in ans or 'schedule' in ans):
                  engine = pyttsx3.init()
                  engine.say("may be  you are tired..........\n i suggest you to take a nape\n it will help you to refresh\n and \n after that you are more focused towards your work. ")
                  engine.runAndWait()  
              else:
                  engine = pyttsx3.init()
                  engine.say("hmm.....")
                  engine.runAndWait()  
     elif ('Name' in n or 'name' in n or 'MY' in n or 'My' in n or 'my' in n or 'Owner' in n  or 'owner' in n) and ('Tell' in n or 'tell' in n or 'Owner' in n  or 'owner' in n):
             engine = pyttsx3.init() 
             engine.say("His name is Mohit Chatterjee\n He is very talented Guy \n and you know...\n I am very glad that he create me")
             engine.runAndWait() 
     #SENDING ONE MESSAGE TO MULTIPLE USER BY TYPYING NUMBER OF USER AND THEIR MAIL ID AND SUBJECT AND WRITE JUST ONE MESSAGE.
     elif('send' in n or 'Send' in n or 'mail' in n or 'Mail' in n) and ('someone' in n or 'Someone' in n):
        engine = pyttsx3.init() 
        engine.say('sure sir')
        engine.runAndWait()
        ob=s.SMTP('smtp.gmail.com',587)
        ob.starttls()
        ob.login(your_mail,your_mail_pass)
        engine = pyttsx3.init() 
        engine.say('could you please know me the number of receivers...')
        print('Number of Receivers:\n')
        engine.runAndWait()
        num=input()
        engine = pyttsx3.init() 
        engine.say('could you please tell me The subject of your mail')
        print('The subject of your mail:\n')
        engine.runAndWait()
        r=sr.Recognizer()
        with sr.Microphone() as mic:
           audio=r.listen(mic)
        print(r.recognize_google(audio)) 
        subject=r.recognize_google(audio)
        engine = pyttsx3.init() 
        engine.say('could you please tell me what is your message')
        engine.runAndWait()
        r=sr.Recognizer()
        with sr.Microphone() as mic:
           audio=r.listen(mic)
        print(r.recognize_google(audio)) 
        body=r.recognize_google(audio)
        message='subject:{}\n\n{}'.format(subject,body)
        list=[]
        engine = pyttsx3.init() 
        engine.say('You Have To Enter Mail Address here')
        print('You Have To Enter Mail:\n')
        engine.runAndWait()
        for _ in range(int(num)):
           address=input()
           list.append(address)
        ob.sendmail('chatterjeemohit160@gmail.com',list,message)
        engine = pyttsx3.init()
        engine.say('Your mail is succesfully sent')
        print('sucessfully send....')
        engine.runAndWait()
        ob.quit()
     elif('leave' in n or 'stop' in n or 'end' in n) and ('leave' in n or 'stop' in n or 'end' in n ):
           engine = pyttsx3.init()
           engine.say("Thank you so much sir...Have a nice day")
           engine.runAndWait()
           exit()
     else:
        if ('open' in n or 'start' in n or 'excecute' in n or 'run' in n or 'launch' in n or 'Google' in n or 'Chrome' in n or 'play' in n or 'net' in n or 'internet' in n or 'surf' in n or 'surfing' in n) and ('chrome' in n or 'google' in n or 'browser' in n or 'net' in n or 'internet' in n  or 'surf' in n or 'surfing' in n or 'Chrome' in n or 'Google' in n or 'Browser' in n or 'Net' in n or 'Internet' in n  or 'Surf' in n or 'Surfing' in n):
             engine = pyttsx3.init()
             engine.say("ok sir\nGoogle Chrome is opening..")
             engine.runAndWait()
             os.system('chrome')
        elif ('can' in n or 'you' in n or 'kya' in n or 'mere' in n or 'play' in n) and('song' in n or 'gaana' in n or 'baja' in n):
          engine = pyttsx3.init()
          engine.say("can you speak the name of your song")
          engine.runAndWait()
          r=sr.Recognizer()
          with sr.Microphone() as mic:
           audio=r.listen(mic)
          song=r.recognize_google(audio)
          print(r.recognize_google(audio)) 
          engine.say("sure sir..")
          engine.runAndWait()
          kit.playonyt(song)
        elif ('open' in n or 'start' in n or 'excecute' in n or 'run' in n or 'launch' in n or 'Whatsapp' in n or 'Chat' in n or 'Send' in n or 'Sending' in n or 'msg' in n or 'message' in n or 'social media' in n or 'text' in n or 'txt' in n or 'reply' in n)  and ('chatting social media' in n or 'social media' in n or 'Send' in n or 'Sending' in n or 'msg' in n or 'message' in n  or 'text' in n or 'txt' in n or 'reply' in n or 'chat' in n or 'chatting' in n or 'Whatsapp' in n):
           engine = pyttsx3.init()
           engine.say("ok sir\nWhatsApp is opening")
           engine.runAndWait()
           os.system('chrome web.whatsapp.com')
     
        elif ('open' in n or 'start' in n or 'excecute' in n or 'run' in n or 'launch' in n  ) and ('mysql' in n or 'MYSQL' in n or 'MySql' in n or 'DB' in n or 'database' in n or 'my database' in n):
          engine = pyttsx3.init()
          engine.say("MY SQL is opening")
          engine.runAndWait()
          os.system('Mysql')
    
        elif ('open' in n or 'Start' in n or 'excecute' in n or 'run' in n or 'launch' in n or 'Listen' in n or 'watches' in n or 'watch' in n or 'Youtube' in n or 'Play' in n or 'Playing' in n ) and ('Youtube' in n or 'Listen' in n or 'Songs' in n or 'Song' in n or 'Videos' in n or 'Video' in n  or 'Play' in n or 'playing' in n):
         engine = pyttsx3.init()
         engine.say("ok sir\nYoutube is opening")
         engine.runAndWait()
         os.system('chrome Youtube.com')
        elif ('open' in n or 'start' in n or 'excecute' in n or 'run' in n or 'launch' in n or 'linkedin' in n or 'watches' in n or 'watch' in n or 'professional' in n or 'surfing' in n or 'search' in n  or 'searching' in n ) and ('linkedin' in n or 'surfing' in n or 'search' in n  or 'searching' in n or 'song' in n or 'videos' in n or 'video' in n):
           engine = pyttsx3.init()
           engine.say("ok sir \nLinkeIn is opening")
           engine.runAndWait()
           os.system(' chrome www.linkedin.com/feed/')
        elif ('open' in n or 'start' in n or 'excecute' in n or 'run' in n or 'launch' in n or 'udemy' in n or 'learning' in n or 'learn' in n or 'course' in n or 'courses' in n) and ('udemy' in n or 'learning' in n or 'learn' in n or 'course' in n or 'courses' in n):
            engine = pyttsx3.init()
            engine.say("ok sir..\nUdemy is opening")
            engine.runAndWait()
            os.system('chrome www.udemy.com')
        elif ('open' in n or 'start' in n or 'excecute' in n or 'run' in n or 'launch' in n or 'send' in n or 'mail' in n or 'gmail' in  n or 'Gmail' in n) and ('mail' in n or 'chrome' in n or 'google' in n or 'browser' in n or 'Gmail' in n):
            engine = pyttsx3.init()
            engine.say("ok sir..\nG-mail is opening")
            engine.runAndWait()
            os.system('chrome Gmail.com')
        elif ('Name' in n or 'name' in n or 'MY' in n or 'My' in n or 'my' in n or 'Owner' in n  or 'owner' in n) and ('Tell' in n or 'tell' in n or 'Owner' in n  or 'owner' in n):
             engine = pyttsx3.init() 
             engine.say("His name is Mohit Chatterjee\n He is very talented Guy \n and you know...\n I am very glad that he create me")
             engine.runAndWait()
        elif ('How' in n or 'how' in n or 'You' in n or 'you' in n ):
             engine = pyttsx3.init()
             engine.say("I am Pretty good sir.\n what about you\n how was your day?")
             engine.runAndWait()
        elif('leave' in n or 'stop' in n or 'end' in n) and ('leave' in n or 'stop' in n or 'end' in n ):
           engine = pyttsx3.init()
           engine.say("Thank you so much sir...Have a nice day")
           engine.runAndWait()
           exit()
        else:
           engine = pyttsx3.init()
           engine.say("UHM....sorry.....I didn't recognize you sir\n speak again please....")
           engine.runAndWait()
 else:
           engine = pyttsx3.init()
           engine.say("UHM....sorry.....I didn't recognize you sir\n speak again please....")
           engine.runAndWait()   
