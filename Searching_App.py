#pip install pyttsx3
import os
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[1].id)  #male voice=0 and female voice=1

engine = pyttsx3.init()
engine.say("Your App is Launching  Mohit sir\n I am Your Assistant\n u can write your choice here")
engine.runAndWait()
while True:
   voices = engine.getProperty('voices')       
   engine.setProperty('voice', voices[1].id)  #male voice=0 and female voice=1

   print('1.Google \t5.LinkedIn\n2.MySQL \t6.Udemy\n3.WhatsApp \t7.Gmail\n4.YouTube \t8.VLC Player')
   n=input('Write Here :')
   if ('open' in n or 'start' in n or 'excecute' in n or 'run' in n or 'launch' in n or 'google' in n or 'chrome' in n or 'play' in n or 'net' in n or 'internet' in n or 'surf' in n or 'surfing' in n) and ('chrome' in n or 'google' in n or 'browser' in n or 'net' in n or 'internet' in n  or 'surf' in n or 'surfing' in n):
     engine = pyttsx3.init()
     engine.say("Google Chrome is opening..")
     engine.runAndWait()
     os.system('chrome')
    
   elif ('open' in n or 'start' in n or 'excecute' in n or 'run' in n or 'launch' in n or 'whatsapp' in n or 'chat' in n or 'send' in n or 'sending' in n or 'msg' in n or 'message' in n or 'social media' in n or 'text' in n or 'txt' in n or 'reply' in n)  and ('chatting social media' in n or 'social media' in n or 'send' in n or 'sending' in n or 'msg' in n or 'message' in n  or 'text' in n or 'txt' in n or 'reply' in n or 'chat' in n or 'chatting' in n or 'whatsapp' in n):
     engine = pyttsx3.init()
     engine.say("WhatsApp is opening")
     engine.runAndWait()
     os.system('chrome web.whatsapp.com')
    
   elif ('open' in n or 'start' in n or 'excecute' in n or 'run' in n or 'launch' in n  ) and ('mysql' in n or 'MYSQL' in n or 'MySql' in n or 'DB' in n or 'database' in n or 'my database' in n):
     engine = pyttsx3.init()
     engine.say("MY SQL is opening")
     engine.runAndWait()
     os.system('Mysql')
    
   elif ('open' in n or 'start' in n or 'excecute' in n or 'run' in n or 'launch' in n or 'listen' in n or 'watches' in n or 'watch' in n or 'youtube' in n or 'play' in n or 'playing' in n ) and ('youtube' in n or 'listen' in n or 'songs' in n or 'song' in n or 'videos' in n or 'video' in n  or 'play' in n or 'playing' in n):
     engine = pyttsx3.init()
     engine.say("Youtube is opening")
     engine.runAndWait()
     os.system('chrome Youtube.com')
   elif ('open' in n or 'start' in n or 'excecute' in n or 'run' in n or 'launch' in n or 'linkedin' in n or 'watches' in n or 'watch' in n or 'professional' in n or 'surfing' in n or 'search' in n  or 'searching' in n ) and ('linkedin' in n or 'surfing' in n or 'search' in n  or 'searching' in n or 'song' in n or 'videos' in n or 'video' in n):
     engine = pyttsx3.init()
     engine.say("LinkeIn is opening")
     engine.runAndWait()
     os.system(' chrome www.linkedin.com/feed/')
   elif ('open' in n or 'start' in n or 'excecute' in n or 'run' in n or 'launch' in n or 'udemy' in n or 'learning' in n or 'learn' in n or 'course' in n or 'courses' in n) and ('udemy' in n or 'learning' in n or 'learn' in n or 'course' in n or 'courses' in n):
     engine = pyttsx3.init()
     engine.say("Udemy is opening")
     engine.runAndWait()
     os.system('chrome www.udemy.com')
   elif ('open' in n or 'start' in n or 'excecute' in n or 'run' in n or 'launch' in n or 'listen' in n or 'watches' in n or 'watch' in n or 'VLC' in n or 'play' in n or 'playing' in n or 'vlc' in n or  'player' in n) and ('listen' in n or 'songs' in n or 'song' in n or 'videos' in n or 'video' in n  or 'play' in n or 'playing' in n or 'VLC' in n or 'play' in n or 'playing' in n or 'vlc' in n or  'player' in n):
     engine = pyttsx3.init()
     engine.say("VLC PLAYER is opening")
     engine.runAndWait()
     os.system('VLC') 
   elif ('open' in n or 'start' in n or 'excecute' in n or 'run' in n or 'launch' in n or 'send' in n or 'mail' in n or 'gmail' in  n) and ('mail' in n or 'chrome' in n or 'google' in n or 'browser' in n):
     engine = pyttsx3.init()
     engine.say("G-mail is opening")
     engine.runAndWait()
     os.system('chrome Gmail.com')
    
   elif ('open' in n or 'start' in n or 'excecute' in n or 'run' in n or 'launch' in n or 'notepad' in n ) and ('notepad' in n or 'text editor' in n or 'note' in n or 'to do list'):
     engine = pyttsx3.init()
     engine.say("Notepad is opening")
     engine.runAndWait()
     os.system('notepad')
     
   elif('exit' in n) or ('end' in n) or ('stop' in n):
     engine = pyttsx3.init()
     engine.say("Thank you so much sir...Have a nice day")
     engine.runAndWait()
     break
   else:
     engine = pyttsx3.init()
     engine.say("mmm.....sorry.....I didn't recognize your text sir\n write again please....")
     engine.runAndWait()
     