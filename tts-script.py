import warnings
warnings.filterwarnings("ignore")

from TTS.api import TTS
import os

model_name = TTS.list_models()[0]
tts = TTS(model_name)

selected_speaker = tts.speakers[0]
selected_language = tts.languages[0]

os.makedirs("output", exist_ok=True)
text = "First, solve the problem. Then, write the code."

tts.tts_to_file(
    text=text,
    speaker=selected_speaker,
    language=selected_language,
    file_path="output/output.wav"
)

print("TTS complete! Check the output folder for the audio file.")