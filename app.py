from flask import Flask

app = Flask(__name__)


from matching_utils import get_best_available_user_match
from audio_utils import download_audio, transcribe_audio

@app.route('/transcribe-audio', methods=['POST'])
def transcribe_audio(request):
    '''Downloads the audio file at the given url and returns the string transcribed by openAI whisper'''
    url = request.form['url']
    path = download_audio(url)
    transcribed = transcribe_audio(path)
    
    # Returns transcribed for now, but should instead update the firestore database with the transcribed text
    return transcribed


@app.route('/match-user', methods=['POST'])
def match_user(request):
    '''Finds the closest match for a user and opens a chatorom with them.'''
    # TODO: implement this function
