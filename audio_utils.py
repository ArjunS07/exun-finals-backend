import whisper

# Look at https://github.com/openai/whisper
model = whisper.load_model("base")

def download_audio(url: str) -> str:
    '''Downloads the audio file at the given url and returns the path to the downloaded file'''
    # TODO

def transcribe_audio(path: str) -> str:
    '''For an audio file at the given path, uses openAI whisper to transcribe it and returns the string ''' 

    # TODO: implement this function
    