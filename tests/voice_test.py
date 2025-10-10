import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.voice import narrate_text
from src.utils import log_event

if __name__ == "__main__":
    log_event("Starting voice test")

    sample_text = "This is a test of the voice synthesis module. If you can hear this, narration is working."

    # Speak aloud
    narrate_text(sample_text)

    # Save to file
    narrate_text(sample_text, save_to_file=True, filename="test_voice.wav")