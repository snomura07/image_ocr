#! /usr/bin/python3
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from utils.ModOpenAi import ModOpenAi
from utils.PromptGen import PromptGen

if __name__ == '__main__':
    print("Running the main script...")

    modOpenAi = ModOpenAi(model="gpt-4o-mini")
    promptGen = PromptGen()
    res       = modOpenAi.imageOcrRequest(promptGen.genDigikeyImageOcr(), "IMG_3891.JPEG")
    print(res.choices[0].message.content)
