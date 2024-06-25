import logging
from click import exceptions
from googletrans import Translator


def translate_text(text, src_lang, dest_lang):
    translator = Translator()

    try:
        translation = translator.translate(text, src=src_lang, dest=dest_lang)
        translated_text = translation.text
        logging.info(f"Translated '{text}' from {src_lang} to {dest_lang}: {translated_text}")
        return translated_text
    except exceptions.GoogleTranslateException as e:
        logging.error(f"Google Translate API error: {e}")
        return None
    except Exception as e:
        logging.error(f"Translation error: {e}")
        return None
