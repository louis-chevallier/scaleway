import io
import httpx
import soundfile as sf

BASE_URL = "http://localhost:8000/v1"
 
payload = {
    "input": "Paris is a beautiful city!",
    "model": "mistralai/Voxtral-4B-TTS-2603",
    "response_format": "wav",
    "voice": "casual_male",
}
 
response = httpx.post(f"{BASE_URL}/audio/speech", json=payload, timeout=120.0)
response.raise_for_status()
 
audio_array, sr = sf.read(io.BytesIO(response.content), dtype="float32")
print(f"Got audio: {len(audio_array)} samples at {sr} Hz")

print(audio_array)
# you can play the audio with a library like `sounddevice.play` for example
