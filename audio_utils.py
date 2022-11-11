import whisper

# Look at https://github.com/openai/whisper
model = whisper.load_model("base")

def download_audio(url: str) -> str:
    '''Downloads the audio file at the given url and returns the path to the downloaded file'''
    # TODO

def transcribe_audio(path: str, target_lang: str) -> str:
    '''For an audio file at the given path, uses openAI whisper to translate and transcribe it. 
    Returns the string of the transcription.''' 

    # TODO: implement this function
