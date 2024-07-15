# test_rpa_example.py
import os
import logging

from bot import action, desktop_bot_download, clean_downloaded_files
from utils.constants import DOWNLOADS_DIRECTORY, FILENAME

logging.basicConfig(level=logging.DEBUG)


# Testes de Funcionalidade
def test_rpa_full_workflow():
    result = action()
    assert result is True

def test_delete_files():
    clean_downloaded_files()
    assert FILENAME not in os.listdir(DOWNLOADS_DIRECTORY)

def test_download_data():
    desktop_bot_download()
    logging.error("File Downloaded")
    assert FILENAME in os.listdir(DOWNLOADS_DIRECTORY)
