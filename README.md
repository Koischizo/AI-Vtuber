# AI-Vtuber
This code is designed to read chat messages from YouTube and then utilize OpenAI's GPT-3 language model to generate responses. The output from GPT-3 is then read out loud using a TTS (Text-to-Speech) engine provided by ElevenLabs.



# Setup
Install dependencies
```
git clone https://github.com/Koischizo/AI-Vtuber/
cd AI-Vtuber
pip install -r requirements.txt
```
It also requires [`ffmpeg`](https://ffmpeg.org/) to be installed

# Usage

Edit the variables `EL_key` and `OAI_key` in `config.json`

`EL_key` is the API key for [ElevenLabs](https://beta.elevenlabs.io/). Found in Profile Settings

`OAI_key` is the API key for OpenAI. Found [here](https://platform.openai.com/account/api-keys)

Then run `run.py`

### Default TTS
```
python run.py -id STREAMID 
```
### Elevenlabs TTS
```
python run.py -id STREAMID -tts EL 
```
then you're set
## Notes
Replace `STREAMID` with the stream's ID that you can find on the Youtube Stream link

You can change the voice by changing `voice` in `config.json`. You can find the ID's [here](https://api.elevenlabs.io/docs) in `Get Voices`



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

- [x] Clean up
- [ ] GUI
- [ ] Executables (exe, bat or sh)
- [ ] Extra features (maybe) (Prompt injection protection, questions only mode, virtual audio)

# License
This program is under the [MIT license](/LICENSE) 

