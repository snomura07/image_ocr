import os
import openai
import base64
import configparser

class ModOpenAi:
    def __init__(self, model="gpt-4o-mini"):
        currDir    = os.path.dirname(__file__)
        configPath = os.path.join(f"{currDir}/../config.ini")
        config     = configparser.ConfigParser()
        config.read(os.path.abspath(configPath))

        openai.api_key = config['OPENAI']['API_KEY']
        self.model     = model

    def imageOcrRequest(self, prompt, imagePath, max_tokens=500):
        base64Image = None
        with open(imagePath, "rb") as f:
            base64Image = base64.b64encode(f.read()).decode("utf-8")

        messages = self._formatImageMessages(prompt, base64Image)
        response = openai.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=max_tokens,
        )

        return response

    def _formatImageMessages(self, prompt, base64Image, system_message=None):
        baseMessage = {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt
                }
            ]
        }

        if base64Image:
            baseMessage['content'].append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64Image}",
                    "detail": "high"
                }
            })

        messages = [baseMessage]
        return messages
