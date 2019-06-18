# SimpleLanguageTranslator.py
"""Use IBM Watson Speech to Text, Language Translator and Text to Speech 
   APIs to enable English and Spanish speakers to communicate."""
from ibm_watson import SpeechToTextV1
from ibm_watson import LanguageTranslatorV3
from ibm_watson import TextToSpeechV1
import keys  # contains your API keys for accessing Watson services
import pyaudio  # used to record from mic
import pydub  # used to load a WAV file
import pydub.playback  # used to play a WAV file
import wave  # used to save a WAV file

def run_translator():
    """Calls the functions that interact with Watson services."""
    # Step 1: Prompt for then record English speech into an audio file
    input('Press Enter then ask your question in English')
    record_audio('english.wav')

    # Step 2: Transcribe the English speech to English text
    english = speech_to_text(
        file_name='english.wav', model_id='en-US_BroadbandModel')
    print('English:', english)

    # Step 3: Translate the English text into Spanish text
    spanish = translate(text_to_translate=english, model='en-es')
    print('Spanish:', spanish)

    # Step 4: Synthesize the Spanish text into Spanish speech
    text_to_speech(text_to_speak=spanish, voice_to_use='es-US_SofiaVoice',
        file_name='spanish.wav')

    # Step 5: Play the Spanish audio file
    play_audio(file_name='spanish.wav')

    # Step 6: Prompt for then record Spanish speech into an audio file
    input('Press Enter then speak the Spanish answer')
    record_audio('spanishresponse.wav')

    # Step 7: Transcribe the Spanish speech to Spanish text
    spanish = speech_to_text(
        file_name='spanishresponse.wav', model_id='es-ES_BroadbandModel')
    print('Spanish response:', spanish)

    # Step 8: Translate the Spanish text into English text
    english = translate(text_to_translate=spanish, model='es-en')
    print('English response:', english)

    # Step 9: Synthesize the English text into English speech
    text_to_speech(text_to_speak=english,
        voice_to_use='en-US_AllisonVoice',
        file_name='englishresponse.wav')

    # Step 10: Play the English audio
    play_audio(file_name='englishresponse.wav')

def speech_to_text(file_name, model_id):
    """Use Watson Speech to Text to convert audio file to text."""
    # create Watson Speech to Text client 
    stt = SpeechToTextV1(iam_apikey=keys.speech_to_text_key)

    # open the audio file 
    with open(file_name, 'rb') as audio_file:
        # pass the file to Watson for transcription
        result = stt.recognize(audio=audio_file,
            content_type='audio/wav', model=model_id).get_result()
        
    # Get the 'results' list. This may contain intermediate and final
    # results, depending on method recognize's arguments. We asked 
    # for only final results, so this list contains one element.
    results_list = result['results'] 

    # Get the final speech recognition result--the list's only element.
    speech_recognition_result  = results_list[0]

    # Get the 'alternatives' list. This may contain multiple alternative
    # transcriptions, depending on method recognize's arguments. We did
    # not ask for alternatives, so this list contains one element.
    alternatives_list = speech_recognition_result['alternatives']

    # Get the only alternative transcription from alternatives_list.
    first_alternative = alternatives_list[0]

    # Get the 'transcript' key's value, which contains the audio's 
    # text transcription.
    transcript = first_alternative['transcript']

    return transcript  # return the audio's text transcription

def translate(text_to_translate, model):
    """Use Watson Language Translator to translate English to Spanish 
       (en-es) or Spanish to English (es-en) as specified by model."""
    # create Watson Translator client
    language_translator = LanguageTranslatorV3(version='2018-05-01',
        iam_apikey=keys.translate_key)

    # perform the translation
    translated_text = language_translator.translate(
        text=text_to_translate, model_id=model).get_result()

    # Get 'translations' list. If method translate's text argument has 
    # multiple strings, the list will have multiple entries. We passed
    # one string, so the list contains only one element.
    translations_list = translated_text['translations']
    
    # get translations_list's only element
    first_translation = translations_list[0]

    # get 'translation' key's value, which is the translated text
    translation = first_translation['translation']

    return translation  # return the translated string

def text_to_speech(text_to_speak, voice_to_use, file_name):
    """Use Watson Text to Speech to convert text to specified voice
       and save to a WAV file."""
    # create Text to Speech client
    tts = TextToSpeechV1(iam_apikey=keys.text_to_speech_key)

    # open file and write the synthesized audio content into the file
    with open(file_name, 'wb') as audio_file:
        audio_file.write(tts.synthesize(text_to_speak, 
            accept='audio/wav', voice=voice_to_use).get_result().content)

def record_audio(file_name):
    """Use pyaudio to record 5 seconds of audio to a WAV file."""
    FRAME_RATE = 44100  # number of frames per second
    CHUNK = 1024  # number of frames read at a time
    FORMAT = pyaudio.paInt16  # each frame is a 16-bit (2-byte) integer
    CHANNELS = 2  # 2 samples per frame
    SECONDS = 5  # total recording time
 
    recorder = pyaudio.PyAudio()  # opens/closes audio streams

    # configure and open audio stream for recording (input=True)
    audio_stream = recorder.open(format=FORMAT, channels=CHANNELS, 
        rate=FRAME_RATE, input=True, frames_per_buffer=CHUNK)
    audio_frames = []  # stores raw bytes of mic input
    print('Recording 5 seconds of audio')

    # read 5 seconds of audio in CHUNK-sized pieces
    for i in range(0, int(FRAME_RATE * SECONDS / CHUNK)):
        audio_frames.append(audio_stream.read(CHUNK))

    print('Recording complete')
    audio_stream.stop_stream()  # stop recording
    audio_stream.close()  
    recorder.terminate()  # release underlying resources used by PyAudio

    # save audio_frames to a WAV file
    with wave.open(file_name, 'wb') as output_file:
        output_file.setnchannels(CHANNELS)
        output_file.setsampwidth(recorder.get_sample_size(FORMAT))
        output_file.setframerate(FRAME_RATE)
        output_file.writeframes(b''.join(audio_frames))

def play_audio(file_name):
    """Use the pydub module (pip install pydub) to play a WAV file."""
    sound = pydub.AudioSegment.from_wav(file_name)
    pydub.playback.play(sound)

if __name__ == '__main__':
    run_translator()


##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
