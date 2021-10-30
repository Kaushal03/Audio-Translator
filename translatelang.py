import googletrans
import speech_recognition as sr
import gtts
import playsound

recognizer = sr.Recognizer()
translator = googletrans.Translator()
input_lang = 'en-IN'
output_lang = 'hi'
with sr.Microphone() as source:
    print('Speak Now')
    recognizer.adjust_for_ambient_noise(source)
    voice = recognizer.listen(source)
    print(voice)
    print('Recognizing your voice')
    text = recognizer.recognize_google(voice, language=input_lang)
    print('Wait....')
    print(text)
print('translating...')

translated = translator.translate(text, dest=output_lang)
print(translated.text)
converted_audio = gtts.gTTS(translated.text, lang=output_lang)
print('saving audio')
converted_audio.save('romantic.mp3')
print('playing audio')
playsound.playsound('romantic.mp3')

print(googletrans.LANGUAGES)