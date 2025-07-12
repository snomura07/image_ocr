class PromptGen:
    def __init__(self):
        pass

    def genDigikeyImageOcr(self) -> str:
        prompt = (
            'Please extract the part name and quantity from the uploaded photo. '
            '- The part name is located next to the label "MFR PN". '
            '- The quantity is located next to the label "Quantity". '
            '- Do not include any information other than the name and quantity. '
            '- Format your response as follows: '
            '{'
            '"name": "", '
            '"quantity": ""'
            '}'
        )
        return prompt
