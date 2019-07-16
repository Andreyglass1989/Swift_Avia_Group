# Imports the Google Cloud client library
from google.cloud import translate
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/root/Рабочий стол/Avia-Logistic-503d3df31fe1.json"
# Instantiates a client
translate_client = translate.Client()

# The text to translate
text = u'Hello, world!'
# The target language
target = 'ru'

# Translates some text into Russian
translation = translate_client.translate(
    text,
    target_language=target)

print(u'Text: {}'.format(text))
print(u'Translation: {}'.format(translation['translatedText']))