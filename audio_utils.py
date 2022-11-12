# TODO: Install and import whisper
# Look at https://github.com/openai/whisper
import requests
import os

model = whisper.load_model("base")

def download_audio(url: str) -> str:
    '''Downloads the audio file at the given url and returns the path to the downloaded file'''
    response = requests.get(url)
    last_10 = url[-10:]
    thefile = open(last_10, "wb").write(response.content)
    path = str(os.path.dirname(thefile))

    # TODO

def transcribe_audio(path: str, target_lang: str) -> str:
    '''For an audio file at the given path, uses openAI whisper to translate and transcribe it. 
    Returns the string of the transcription.''' 

    # TODO: implement this function
