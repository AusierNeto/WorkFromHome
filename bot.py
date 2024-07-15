import os
from pathlib import Path
import time
import chromedriver_autoinstaller

from botcity.core import DesktopBot
from botcity.web import WebBot, Browser, By
from botcity.maestro import *

from selenium.webdriver import Chrome

from utils.constants import FILENAME, URL

BotMaestroSDK.RAISE_NOT_CONNECTED = False


def webbot_download():
    chromedriver_autoinstaller.install()
    webbot = WebBot()
    webbot.headless = True

    webbot.browse(URL)
    webbot.wait(3000)
    webbot.stop_browser()

def desktop_bot_download():
    desktop_bot = DesktopBot()
    desktop_bot.browse(URL)
    time.sleep(2)

def clean_downloaded_files():
    downloads_directory = Path.home() / "Downloads"
    downloaded_file_list = [f for f in os.listdir(downloads_directory) if FILENAME in f]
    for file in downloaded_file_list:
        os.remove(downloads_directory / file)

def action():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    clean_downloaded_files()
    desktop_bot_download()

    return True


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    action()
