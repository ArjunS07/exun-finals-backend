# TODO: Install and import whisper
# Look at https://github.com/openai/whisper
import requests
import os
import whisper

model = whisper.load_model("base")

def download_audio(url: str) -> str:
    '''Downloads the audio file at the given url and returns the path to the downloaded file'''
    response = requests.get(url)
    print(url)
    filename = url.split('/')[-1]
    download_path = f"audio_uploads/{filename}"
    thefile = open(download_path, "wb").write(response.content)
    return download_path

model = whisper.load_model("small")
def get_audio_transcription(url: str, target_lang: str = 'en') -> str:
    path = download_audio(url)
    audio = whisper.load_audio(path)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    _, probs = model.detect_language(mel)
    options = whisper.DecodingOptions(fp16=False, language=target_lang)
    result = whisper.decode(model, mel, options)
    return (result.text)

if __name__=='__main__':
    url = "https://firebasestorage.googleapis.com/v0/b/exun-finals-c3c44.appspot.com/o/audioMessages%2FJamal%20Says%20'Every%2060%20Seconds%20In%20Africa%2C%20A%20Minute%20Passes'.-7Zm1hPbmzPw.m4a?alt=media&token=523c30ee-f25e-4be0-a12b-1532d9df0f56.m4a"
    transcribed = transcribe_audio(url)
    print(transcribed)