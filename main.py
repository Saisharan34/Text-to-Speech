from gtts import gTTS 

text = "Hello guys. how are you. All fine?"

language ='en'
obj = gTTS(text=text,lang=language,slow =False )

obj.save("sample.mp3")