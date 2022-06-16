from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import nltk
import datetime
import pywhatkit
import train
import cv2
import os
import pyautogui
import webbrowser

nltk.download('omw-1.4')

recognizer = speech_recognition.Recognizer()

speaker=tts.init('sapi5')
speaker.setProperty('rate',200)

dict_path={}
file_path='path.txt'
with open(file_path) as f:
    for line in f:
        line=line.strip()
        al = line.split('=')
        dict_path[al[0]] = al[1]
    
def face_rec():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    while True:
        ret, frame = cap.read()
        image,face = train.face_detector(frame)
        
        try:
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            result = train.model.predict(face)
            
            if result[1] < 500:
                confidence = int((1-(result[1])/300)*100)
                display_string = str(confidence)+'% Chances of being a correct user'
            cv2.putText(image,display_string,(50,120),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),4)
            
            if confidence>85:
                cv2.putText(image,"Unlocked",(250,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),4)
                cv2.imshow('Face Scanner', image)
                break
            
            else:
                cv2.tText(image,"Locked",(250,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),4)
                cv2.imshow('Face Scanner', image)
        
        except:
            cv2.putText(image,"Face Not Found",(250,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255), 4)		
            cv2.imshow('Face Scanner', image)
            pass
        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video

    cap.release()
    cv2.destroyAllWindows()

def hello():
    speaker.say('hello. what can i do for you?')
    speaker.runAndWait()

def exi():
    speaker.say('goodbye sir')
    speaker.runAndWait() 
    face_rec()
    speaker.say('verification success. Hello sir. Welcome back')
    speaker.runAndWait()
    
def time():
    strTime=datetime.datetime.now().strftime("%H:%M:%S")
    speaker.say(f"the time is {strTime}")
    speaker.runAndWait()
    
def yt():
    global recognizer
    speaker.say('what youtube do you wanna watch?')
    speaker.runAndWait()
    
    done=False
    
    while not done:
        try:
            
            with speech_recognition.Microphone() as mic:
                
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.record(mic,duration=3)
                
                item = recognizer.recognize_google(audio,language='id-ID')
                item=item.lower()
                speaker.say('okey. play youtube'+str(item))
                speaker.runAndWait()
                pywhatkit.playonyt(item)
                done=True
                
            
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say('i did not understand you! please say it slowly')                
            speaker.runAndWait()
def t_yt():
    os.system("taskkill /im msedge.exe /f")
    speaker.say('oke, close youtube')                
    speaker.runAndWait()

def openMsWord():
    speaker.say('okey sir, open microsoft word')                
    speaker.runAndWait()
    os.startfile(dict_path['msword'])

def openExcel():
    speaker.say('okey sir, open microsoft excel')                
    speaker.runAndWait()
    os.startfile(dict_path['excel'])    

def openPPoint():
    speaker.say('okey sir, open microsoft power point')                
    speaker.runAndWait()
    os.startfile(dict_path['powerpoint'])    

def openWA():
    speaker.say('okey sir, open whatsapp')                
    speaker.runAndWait()
    os.startfile(dict_path['whatsapp'])
    
def new_file():
    pyautogui.hotkey('ctrl', 'n')
    
def next_window():
    pyautogui.hotkey('alt', 'tab')

def enter():
    pyautogui.press('enter')

def closeWord():
    speaker.say('okey sir, close microsoft word')                
    speaker.runAndWait()
    split_path=dict_path['msword'].split('/')
    os.system('taskkill /im '+str(split_path[-1]))

def closeExcel():
    speaker.say('okey sir, close microsoft excel')                
    speaker.runAndWait()
    split_path=dict_path['excel'].split('/')
    os.system('taskkill /im '+str(split_path[-1]))

def closePoint():
    speaker.say('okey sir, close microsoft power point')                
    speaker.runAndWait()
    split_path=dict_path['powerpoint'].split('/')
    os.system('taskkill /im '+str(split_path[-1]))

def closeWa():
    speaker.say('okey sir, close whatsapp')                
    speaker.runAndWait()
    split_path=dict_path['whatsapp'].split('/')
    os.system('taskkill /im '+str(split_path[-1]))
    
def search():
    global recognizer
    speaker.say('what news do you wanna search?')
    speaker.runAndWait()
    
    done=False
    
    while not done:
        try:
            
            with speech_recognition.Microphone() as mic:
                
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.record(mic,duration=3)
                
                item = recognizer.recognize_google(audio,language='id-ID')
                item=item.lower()
                webbrowser.open_new_tab(item)
                speaker.say('okay sir, searching for'+str(item))
                speaker.runAndWait()
                done=True
                
            
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say('i did not understand you! please say it slowly')                
            speaker.runAndWait()
    
def closeWeb():
    speaker.say('okey sir, close webbrowser')                
    speaker.runAndWait()
    os.system('taskkill /im msedge.exe')

def win():
    pyautogui.hotkey('win','tab')

def next():
    pyautogui.press('left')
          
def openTele():
    speaker.say('okey sir, open Telegram')                
    speaker.runAndWait()
    os.startfile(dict_path['telegram'])      

def closeTele():
    speaker.say('okey sir, close Telegram')                
    speaker.runAndWait()
    os.system('taskkill /im Telegram.exe')

def openSpotify():
    speaker.say('okey sir, open Spotify')                
    speaker.runAndWait()
    os.startfile(dict_path['spotify'])      

def closeSpotify():
    speaker.say('okey sir, close spotify')                
    speaker.runAndWait()
    os.system('taskkill /im Spotify.exe')

def openDiscord():
    speaker.say('okey sir, open Discord')                
    speaker.runAndWait()
    os.startfile(dict_path['discord'])      

def closeDiscord():
    speaker.say('okey sir, close Discord')                
    speaker.runAndWait()
    os.system('taskkill /im Discord.exe')

def openZoom():
    speaker.say('okey sir, open Zoom')                
    speaker.runAndWait()
    os.startfile(dict_path['zoom'])      

def closeZoom():
    speaker.say('okey sir, close Zoom')                
    speaker.runAndWait()
    os.system('taskkill /im Zoom.exe')

def openPs():
    speaker.say('okey sir, open Adobe Photoshop')                
    speaker.runAndWait()
    os.startfile(dict_path['photoshop'])      

def closePs():
    speaker.say('okey sir, close Adobe Photoshop')                
    speaker.runAndWait()
    os.system('taskkill /im Photoshop.exe')
    
def openAi():
    speaker.say('okey sir, open Adobe Illustrator')                
    speaker.runAndWait()
    os.startfile(dict_path['illustrator'])      

def closeAi():
    speaker.say('okey sir, close Adobe Illustrator')                
    speaker.runAndWait()
    os.system('taskkill /im Illustrator.exe')


mappings = {
        
    'greeting':hello,
    'exit':exi,
    'time':time,
    'youtube':yt,
    'close_youtube':t_yt,
    'oMsWord':openMsWord,
    'oMsExcel':openExcel,
    'oMsPoint':openPPoint,
    'oWA':openWA,
    'cWA':closeWa,
    'newfile':new_file,
    'tab':next_window,
    'yes':enter,
    'tMsWord':closeWord,
    'tuMsExcel':closeExcel,
    'ttpMsPoint':closePoint,
    'Search':search,
    'CloseWeb':closeWeb,
    'wintab':win,
    'arrow':next,
    'oTele':openTele,
    'cTele':closeTele,
    'oSpotify':openSpotify,
    'cSpotify':closeSpotify,
    'oDiscord':openDiscord,
    'cDiscord':closeDiscord,
    'oZoom':openZoom,
    'cZoom':closeZoom,
    'oPs':openPs,
    'cPs':closePs,
    'oAi':openAi,
    'cAi':closeAi
    }           

assistant = GenericAssistant('intents.json',intent_methods=mappings)
assistant.train_model()

def main():
    face_rec()
    speaker.say('verification success. Loading your personal assistant BOTAK. Hello sir. Welcome back')
    speaker.runAndWait()
    global recognizer,message
    while True:
        
        try:
            
            with speech_recognition.Microphone() as mic:
                
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.record(mic,duration=3)
                
                message = recognizer.recognize_google(audio,language='id-ID')
                message = message.lower()
                print(message)
            assistant.request(message)
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
