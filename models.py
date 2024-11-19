import warnings
warnings.filterwarnings("ignore")

from TTS.api import TTS
print(f"Available models: {TTS.list_models()}")