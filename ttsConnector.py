from openai import AsyncOpenAI
from pathlib import Path

class TTSConnector():

    def __init__(self, apiKey):
        self.client = AsyncOpenAI(api_key=apiKey)


    async def synth(self, text: str) -> Path:
        file = Path(__file__).parent / "temp.mp3"
        response = await self.client.audio.speech.create(
            model="tts-1",
            voice="echo",
            input=text
        )
        response.stream_to_file(file)
        return file