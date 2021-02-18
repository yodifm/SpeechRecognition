from gtts import gTTS
import speech_recognition as sr
import os
import time
import webbrowser


r = sr.Recognizer()
order = "what can i do for you?"
tts = gTTS(order)
tts.save("order.mp3")
os.startfile(r"C:\Users\Yodi\PycharmProjects\try\order.mp3")
time.sleep(3)

arr = [["Paradise", "someone"], ["kZ2xL_Nuzag", "XsHWQdriEO8"]]

with sr.Microphone() as source:
    print(order)
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("command: {}".format(text))

        if any(word in "play music" for word in text):
            print("Music Option is Activated")

            songorder = "which coldplay song should i play?"
            tts = gTTS(songorder)
            tts.save("indonesia.mp3")
            os.startfile(r"C:\Users\Yodi\PycharmProjects\try\indonesia.mp3")
            time.sleep(3)
            try:
                print("mention the song")

                audio = r.listen(source)
                song = r.recognize_google(audio)
                print("Song Selected: {}".format(song))

                for i in range(len(arr)):
                    if song.lower() in arr[0][i]:

                        song_url = arr[1][i]
                        base_url = "https://www.youtube.com/watch?v="
                        main_url = base_url + song_url

                        webbrowser.open(main_url, new=2)

                        time.sleep(3)

                        print("music option exit")

            except:
                print("sorry could not hear your request")

    except:
        print("sorry could not hear from you")
