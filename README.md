# AI-Vtuber
This code is designed to read chat messages from YouTube and then utilize OpenAI's GPT-3 language model to generate responses. The output from GPT-3 is then read out loud using a TTS (Text-to-Speech) engine provided by ElevenLabs.



# Setup
Install dependencies
```
git clone https://github.com/Koischizo/AI-Vtuber/
cd AI-Vtuber
pip install pytchat openai pydub pyttsx3 simpleaudio
```
It also requires [`ffmpeg`](https://ffmpeg.org/) to be installed

# Usage

Edit the variables `video_id`, `EL_key`, `EL_voice` and `OAI_key` in `run.py`

`video_id` is the ID of the Youtube stream found in the Youtube link

`EL_key` is the API key for [ElevenLabs](https://beta.elevenlabs.io/). Found in Profile Settings

`EL_voice` is the voice ID for ElevenLabs. Found in the [docs](https://api.elevenlabs.io/docs) in `Get Voices`

`OAI_key` is the API key for OpenAI. Found [here](https://platform.openai.com/account/api-keys)

Then run `run.py`
```
python run.py
```
then you're set


# Live Demo
[Livestream 1](https://www.youtube.com/watch?v=rSrkpsWZjyg)

<a href="http://www.youtube.com/watch?feature=player_embedded&v=rSrkpsWZjyg
" target="_blank"><img src="http://img.youtube.com/vi/rSrkpsWZjyg/0.jpg" 
alt="" width="240" height="180" border="10" /></a>

[Livestream 2](https://www.youtube.com/watch?v=GB4eJUxxNY4)

<a href="http://www.youtube.com/watch?feature=player_embedded&v=GB4eJUxxNY4
" target="_blank"><img src="http://img.youtube.com/vi/GB4eJUxxNY4/0.jpg" 
alt="" width="240" height="180" border="10" /></a>

# Other
I used [This VTS plugin](https://lualucky.itch.io/vts-desktop-audio-plugin) and [VB Audio cable](https://vb-audio.com/Cable/) to make her mouth move and be able to play music at the same time

Please note that this project was created solely for fun and as part of a YouTube video, so the quality and reliability of the code may be questionable. Also, after the completion of the project checklist, there won't be much activity in updating or improving this repository. Nonetheless, we hope that this project can serve as a source of inspiration for anyone interested in building their own AI Vtuber.

- [ ] Clean up
- [ ] GUI
- [ ] Executables (exe, bat or sh)
- [ ] Extra features (maybe) (Prompt injection protection, questions only mode, virtual audio)

# License
This program is under the [MIT license](/LICENSE) 

