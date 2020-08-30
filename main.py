import speech_recognition as sr
import pyautogui

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()
quitcommand=False

while quitcommand == False:
    with sr.Microphone() as source:
        try:
            print("Recording")
            r3.adjust_for_ambient_noise(source)
            audio = r3.listen(source)
            print("Recording done")
            text = r2.recognize_google(audio)
        except:
            print("Couldnt Recognize")
            continue
        if 'exit' in text or 'stop' in text:
            quitcommand = True
            print('Exiting..')
            break
        if 'next' in text or 'right' in text:
            pyautogui.press('right')
            print('Moved Right')
        elif 'previous' in text or 'left' in text:
            pyautogui.press('left')
            print('Moved left')
        else:
            print(text)