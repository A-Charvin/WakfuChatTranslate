# Wakfu Chat Translator

This script is a Wakfu chat log translator that automatically reads the chat log file of the Wakfu game and translates the messages in real-time using the Google Translate API. It provides a graphical user interface (GUI) where the translated messages are displayed.

## Features

- Reads the latest chat messages from the Wakfu chat log file
- Translates the messages using the Google Translate API
- Supports automatic language detection and translation to English
- Updates the GUI with the translated messages in real-time
- Provides a simple and intuitive user interface

## Prerequisites

Before running the script, make sure you have the following installed:

- Python (version 3.6 or higher)
- Required Python libraries: requests, os, tkinter, PySimpleGUI

## Usage

1. Clone the repository or download the script file to your local machine.
2. Install the required Python libraries using pip: `pip install requests os tkinter PySimpleGUI`
3. Open a terminal or command prompt and navigate to the directory where the script is located.
4. Run the script using the command: `python wakfu_chat_translator.py`
5. The GUI window will open, displaying the translated messages as they are updated in the Wakfu chat log file.
6. Press `Alt + F12` to exit the program.

## Customization

You can customize the translation settings by modifying the following variables in the script:

- `from_lang`: The source language of the messages (default: auto)
- `to_lang`: The target language for translation (default: en)

## License

This project is licensed under the [Creative Commons Zero v1.0 Universal License](LICENSE).Feel free to modify and distribute the code.


## Acknowledgments

- [Google Translate API](https://cloud.google.com/translate) for providing the translation functionality.
- [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI) for the easy-to-use GUI framework.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please feel free to open an issue or submit a pull request.
