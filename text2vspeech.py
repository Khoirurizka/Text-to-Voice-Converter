import os
from gtts import gTTS

def text_to_speech(_text, folder_path='.', file_name='output', language='en'):
    # Ensure the folder exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Define the full path for the file
    file_path = os.path.join(folder_path, f"{file_name}.mp3")
    
    # Convert text to speech and save it
    tts = gTTS(_text, lang=language)
    tts.save(file_path)
    
    return file_path
    
    
if __name__ == "__main__":
    file_path = text_to_speech("Sure, I will put cup 1 back in its previous position.", file_name="11", language='en')
    print(f"Audio saved at: {file_path}")
