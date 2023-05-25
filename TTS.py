from gtts import gTTS
import subprocess
global process

def returnedTTS(text):
    myobj = gTTS(text=text, lang='es', slow=False)

    myobj.save("sound.mp3")
    subprocess.call(['nvlc',"sound.mp3",'--play-and-exit'])