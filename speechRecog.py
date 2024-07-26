import speech_recognition as sr

#initialize the recognizer
r = sr.Recognizer()

def recordText():
    try:
        #use the microphone as source of input.
        with sr.Microphone() as source2:
            #prepare recognizer to receive input
            r.adjust_for_ambient_noise(source2, duration=0.01)
            print("Listening : ")

            #listens for the user's input
            audio2 = r.listen(source2)
                
            #using google to recognize audio
            MyText = r.recognize_google(audio2)

            return MyText

    except sr.RequestError as e:
        print("Could not request results: {0}".format(e))
        
    except sr.UnknownValueError:
        print("Unknown error occured")
    return

def outputText(text):
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return

while(1):
    text = recordText()
    outputText(text)
    print(f"Recognized Text: {text}")

    print("wrote text")