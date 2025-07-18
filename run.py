#! /usr/bin/python3
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from utils.ModOpenAi import ModOpenAi
from utils.PromptGen import PromptGen

if __name__ == '__main__':
    print("Running the main script...")

    if len(sys.argv) < 2:
        print("Usage: python DigikeyOcr.py <image_path>")
        sys.exit(1)
    image_path = sys.argv[1]
    if not os.path.isfile(image_path):
        print(f"Error: File '{image_path}' does not exist.")
        sys.exit(1)

    modOpenAi = ModOpenAi(model="gpt-4o-mini")
    promptGen = PromptGen()
    res       = modOpenAi.imageOcrRequest(promptGen.genDigikeyImageOcr(), image_path)
    print(res.choices[0].message.content)
