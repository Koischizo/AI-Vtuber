import pytchat
import openai
import json
from pytchat import LiveChat, SpeedCalculator
import time
import requests
from pydub import AudioSegment
from pydub.playback import play
import io

import pyttsx3

video_id = ""
EL_key = ""
EL_voice = ""
OAI_key = ""

def init():
    global engine

    # Initialize the engine
    engine = pyttsx3.init()
    # Set the properties for the voice
    engine.setProperty('rate', 180)    # Speed of the speech
    engine.setProperty('volume', 1)  # Volume of the speech
    voice = engine.getProperty('voices') #get the available voices
    engine.setProperty('voice', voice[1].id) #changing voice to index 1 for female voice

def tts(message):

    url = f'https://api.elevenlabs.io/v1/text-to-speech/{EL_voice}'
    headers = {
        'accept': 'audio/mpeg',
        'xi-api-key': EL_key,
        'Content-Type': 'application/json'
    }
    data = {
        'text': message,
        'voice_settings': {
            'stability': 0.75,
            'similarity_boost': 0.75
        }
    }

    response = requests.post(url, headers=headers, json=data, stream=True)

    # Load the audio content from the response
    audio_content = AudioSegment.from_file(io.BytesIO(response.content), format="mp3")

    # Play the audio
    play(audio_content)

    #Comment everything above and uncomment this for crappy TTS
    # Convert the text to speech
    # engine.say(message)
    # # Play the audio
    # engine.runAndWait()

def rchat():

    chat = pytchat.create(video_id=video_id)
    schat = pytchat.create(video_id=video_id, processor = SpeedCalculator(capacity = 20))


    while chat.is_alive():
        for c in chat.get().sync_items():
            print(f"\n{c.datetime} [{c.author.name}]- {c.message}\n")
            message = c.message
            #if worthcheck(message) == False:
            response = llm(message)
            print(response)
            tts(response)

            # reads latest chat if chat is moving too fast
            if schat.get() >= 20:
                chat.terminate()
                schat.terminate()
                return


            time.sleep(1)


def llm(message):

    openai.api_key = OAI_key
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"This is how a paranoid schizophrenic female streamer responded in a conversation. She would respond in a tense manner. \n\nShe would talk about the message and would elaborate on it as well as share some of her experiences if possible. She would also go on a tangent.\n#########\n{message}\n#########\n",
      temperature=0.9,
      max_tokens=128,
      top_p=1,
      frequency_penalty=1,
      presence_penalty=1
    )

    json_object = json.loads(str(response))
    return(json_object['choices'][0]['text'])

if __name__ == "__main__":
    init()
    print("\n\nInitialized!\n\n")
    while True:
        rchat()
        print("\n\nReset!\n\n")
        time.sleep(2)
