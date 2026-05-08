import io
import httpx
import soundfile as sf
import tqdm
# Source - https://stackoverflow.com/a/10359645
# Posted by huon, modified by community. See post 'Timeline' for change history
# Retrieved 2026-05-08, License - CC BY-SA 4.0

import numpy as np
from scipy.io.wavfile import write
import subprocess                                                                                                                              

BASE_URL = "http://localhost:8000/v1"
 
payload = {
    "input": "Paris is a beautiful city!",
    "model": "mistralai/Voxtral-4B-TTS-2603",
    "response_format": "wav",
    "voice": "casual_male",
}

with open("livre.txt", "r") as fd :
	lines = fd.readlines()
	print(len(lines))

	S = 100*2//6
	blocks = [ '\n'.join(lines[i:i+S]) for i,l in enumerate(lines[::S])]
	
	print(len(blocks))

	for ib, b in enumerate(tqdm.tqdm(blocks)) :
		#payload["input"] = b

		response = httpx.post(f"{BASE_URL}/audio/speech", json=payload, timeout=120.0)
		response.raise_for_status()

		audio_array, sr = sf.read(io.BytesIO(response.content), dtype="float32")
		print(f"Got audio: {len(audio_array)} samples at {sr} Hz")

		print(audio_array.dtype)
		# you can play the audio with a library like `sounddevice.play` for example


		rate = sr
		data = audio_array
		scaled = np.int16(data / np.max(np.abs(data)) * 32767)
		write('test.wav', rate, scaled)


		# Source - https://stackoverflow.com/a/72738804
		# Posted by ashing, modified by community. See post 'Timeline' for change history
		# Retrieved 2026-05-08, License - CC BY-SA 4.0
		

		res=subprocess.Popen("ffmpeg -hide_banner -loglevel error -y -i test.wav out_%02d.mp3" % ib,shell=True,stdout=subprocess.PIPE)
		res.stdout.read()                                                                                                                              
		#print(res)

		command = 'curl -T out_%02d.mp3 -u "b7_41867395:yZtudpf9jrZHQ" ftp://ftp.byethost7.com/htdocs/' % ib
		print(command)
		res=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
		res.stdout.read()                                                                                                                              

		
		break

