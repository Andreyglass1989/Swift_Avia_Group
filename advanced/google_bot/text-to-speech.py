# -*- coding: utf-8 -*-
"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/root/Рабочий стол/Avia-Logistic-503d3df31fe1.json"
# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.types.SynthesisInput(text="Авиационная доставка грузов из Китая – возможность получить товар, который нужен здесь, сейчас и немедленно. Прямая доставка грузов из Китая в Украину позволяет доставить товар в течение 1-2 дней (в случае экспресс-доставки) или 3-5 (обычная доставка) – речь идет о прямом рейсе Пекин – Киев. Возможен и другой вариант, при котором авиаперевозка груза из Китая осуществляется сначала транзитом в один из аэропортов Европы, откуда уже отправляется непосредственно в Украину. Правда, в этом случае время доставки существенно увеличивается, почти в два раза – до 5-9 дней. Но при этом и стоимость транспортировки из Китая уменьшается почти в два раза – средняя стоимость авиадоставки непосредственно в украинский аэропорт составляет порядка 7-8 долларов за килограмм, а при транзите через европейский аэропорт цена снизится до 6-7 долларов. ")

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.types.VoiceSelectionParams(
    language_code='ru-RU',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)

# Select the type of audio file you want returned
audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(synthesis_input, voice, audio_config)

# The response's audio_content is binary.
with open('output.mp3', 'wb') as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')