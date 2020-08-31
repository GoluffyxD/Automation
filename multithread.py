import speech_recognition as sr
import pyautogui
import concurrent.futures
import time


EXIT_STATUS = False
PLAY_STATUS= False
PREVIOUS_STATUS = False
FORWARD_SPEED = 2
NEXT_STATUS = False
DELETE_STATUS = False
def def_thread():
    global PLAY_STATUS,PREVIOUS_STATUS,EXIT_STATUS,FORWARD_SPEED,NEXT_STATUS,DELETE_STATUS
    while not EXIT_STATUS:
        if PLAY_STATUS:
            pyautogui.press('right')
            print('r')
            time.sleep(FORWARD_SPEED)
        elif DELETE_STATUS:
            pyautogui.press('delete')
            pyautogui.press('tab')
            pyautogui.press('enter')
            DELETE_STATUS = False
            PLAY_STATUS = True
        elif NEXT_STATUS:
            pyautogui.press('right')
            NEXT_STATUS = False
        elif PREVIOUS_STATUS:
            pyautogui.press('left')
            PREVIOUS_STATUS = False
    print("Exited Default Thread")



def voice_thread():
    r2 = sr.Recognizer()
    r3 = sr.Recognizer()

    global EXIT_STATUS,PREVIOUS_STATUS,PLAY_STATUS,FORWARD_SPEED,NEXT_STATUS,DELETE_STATUS

    while True:
        with sr.Microphone() as source:
            try:
                r3.adjust_for_ambient_noise(source)
                audio = r3.listen(source,timeout = 5)
                text = r2.recognize_google(audio)
                print(text)
            except Exception as e:
                print("Exception occured")
                print(e)
                continue
        if 'exit' in text:
            EXIT_STATUS = True
            break
        elif 'next' in text:
            NEXT_STATUS = True
            PLAY_STATUS = False
        elif 'previous' in text or 'left' in text:
            PREVIOUS_STATUS= True
        elif 'pause' in text:
            PLAY_STATUS = False
        elif 'play' in text or 'start' in text:
            PLAY_STATUS = True
        elif 'slow' in text:
            FORWARD_SPEED+=0.5
        elif 'fast' in text:
            FORWARD_SPEED-=0.5
            if FORWARD_SPEED <=1:
                FORWARD_SPEED=1
        elif 'delete' in text:
            PLAY_STATUS = False
            DELETE_STATUS = True
        else:
            continue
    print("Exited Voice Thread")



if __name__ == '__main__':

    with concurrent.futures.ThreadPoolExecutor() as executor:
        f1 = executor.submit(def_thread)
        f2 = executor.submit(voice_thread)

    print("Exited Program Successfullyy")