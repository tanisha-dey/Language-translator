# Language Translator

## Overview
This project is a **command-line language translator** that utilizes the **Google Translate API** to translate text between different languages. Users can specify the source text, source language, and target language as command-line arguments.

## Features
- **Multi-language support**: Translates text between multiple languages.
- **Command-line interface**: Easily run translations from the terminal.
- **Auto-detect language codes**: Uses Google Translate’s language code mapping.
- **Error handling**: Handles invalid language selections and exceptions.

## Installation
### Prerequisites
Ensure you have **Python 3.x** installed.

### Dependencies
Install the required package using:
```sh
pip install googletrans==4.0.0-rc1
```

## Usage
Run the script from the command line:
```sh
python translator.py "Hello, world!" english french
```
### Example Output:
```sh
Translated text:
Bonjour, le monde!
```

## File Structure
- `translator.py`: Main script handling translation logic.

## Future Enhancements
- Add **GUI support** for a user-friendly interface.
- Integrate **speech-to-text** for voice translations.
- Implement **batch translation** for multiple sentences.

