#pip install speechrecognition
#import library
import speech_recognition as sr
MAIN_FOLDER = "/Users/habibhamam/Desktop/Habib19_09_14/Courses/Telecom/English/AdvancedSoftware/Projects/SignalProcessing/_4_TextToSpeech/"


# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Audio file as source
# listening the audio file and store in audio_text variable

with sr.AudioFile(MAIN_FOLDER+'excuseme.wav') as source:
    
    audio_text = r.listen(source)
    
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        
        # using google speech recognition
        text = r.recognize_google(audio_text)
        print('Converting audio transcripts into text ...')
        print(text)
     
    except:
         print('Sorry.. run again...')


