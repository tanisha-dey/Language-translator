import sys
from googletrans import Translator, LANGUAGES

# Initialize the translator
translator = Translator()

# Reverse lookup dictionary for language codes
lang_code_map = {v: k for k, v in LANGUAGES.items()}


# Function to translate text
def translate_text(source_text, src_lang_name, dest_lang_name):
    try:
        # Get the language codes from the names
        src_lang = lang_code_map.get(src_lang_name)
        dest_lang = lang_code_map.get(dest_lang_name)

        if not src_lang or not dest_lang:
            raise ValueError("Invalid source or destination language selected.")

        translation = translator.translate(source_text, src=src_lang, dest=dest_lang)
        return translation.text
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python translator.py <source_text> <source_lang> <dest_lang>")
        sys.exit(1)

    source_text = sys.argv[1]
    src_lang_name = sys.argv[2].lower()
    dest_lang_name = sys.argv[3].lower()

    translation_result = translate_text(source_text, src_lang_name, dest_lang_name)
    print("Translated text:")
    print(translation_result)
