from gtts import gTTS
import os

def generate_voice(text: str, filename: str = "voice.mp3") -> str:
    """
    Генерирует аудиофайл с озвучкой текста.
    :param text: Текст для озвучки.
    :param filename: Имя файла для сохранения голоса.
    :return: Путь к файлу с голосом.
    """
    tts = gTTS(text)
    tts.save(filename)
    return os.path.abspath(filename)
