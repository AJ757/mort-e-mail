from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os

def generate_image(prompt,folder='generated_images'):
    contents="generate an image of"+prompt
    client = genai.Client(api_key='AIzaSyCHL4GqaB_lqSkVSIhyZZTeIagVj73npPA')
    response = client.models.generate_content(
        model='gemini-2.0-flash-preview-image-generation',
        contents=contents,
        config=types.GenerateContentConfig(response_modalities=['TEXT','IMAGE'])
        )
    for part in response.candidates[0].content.parts:
        if part.text is not None:
            continue
        elif part.inline_data is not None:
            image = Image.open(BytesIO(part.inline_data.data))
            if not os.path.exists(folder):
                os.mkdir(folder)
            filename = os.path.join(folder,f'image{len(os.listdir(folder))}.png')
            image.save(filename)