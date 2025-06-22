import openai
import base64
import configparser
import sys

# OCR対象の画像ファイルパス
if len(sys.argv) < 2:
    print("Usage: python DigikeyOcr.py <image_path>")
    sys.exit(1)
image_path = sys.argv[1]

# OpenAI APIキー
config = configparser.ConfigParser()
config.read('../config.ini')
openai.api_key = config['OPENAI']['API_KEY']

# 画像をBase64に変換
def encode_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")
base64_image = encode_image(image_path)

# 指定プロンプト
instruction_text = """Please extract the part name and quantity from the uploaded photo.
- The part name is located next to the label "MFR PN".
- The quantity is located next to the label "Quantity".
- Do not include any information other than the name and quantity.
- Format your response as follows:
{
 "name" : "",
 "quantity" : ""
}
"""

# Chat APIへのリクエスト
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                        "detail": "high"
                    }
                },
                {
                    "type": "text",
                    "text": instruction_text
                }
            ]
        }
    ],
    max_tokens=500,
)

# 結果の表示
print("OCR結果:")
print(response.choices[0].message.content)
