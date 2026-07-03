import whisper 
import os

WHISPER_MODEL = os.getenv("WHISPER_MODEL", "small")

_model = None

SERVAM_API_KEY = os.getenv("SERVAM_API_KEY")
SARVAM_STT_TRANSLATE_URL = "https://api.sarvam.ai/speech-to-text-translate"
SARVAM_MODEL = os.getenv("SARVAM_STT_MODEL", "saaras:v2.5")

def load_model():

    global _model

    if _model is None:
        print(f"Loading Whisper model: {WHISPER_MODEL} ...")
        _model = whisper.load_model(WHISPER_MODEL) 
        print("Whisper model loaded.")

    return _model

def transcribe_chunk(chunk_path : str, translate : bool = False) -> str:
    model = load_model()

    task = "translate" if translate else "transcribe"

    result = model.transcribe(chunk_path , task = task)

    return result['text']

def transcribe_all(chunks : list, translate : bool = False):
    
    full_transcript = ""

    for i, chunk in enumerate(chunks):
        print(f"Transcribing chunk {i+1}")
        text = transcribe_chunk(chunk, translate=translate)

        full_transcript += text + " "

    print("Transcribing completed")

    return full_transcript

