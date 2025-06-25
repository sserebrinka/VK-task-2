import os
import psutil


def is_app_running():
    for proc in psutil.process_iter(['name']):
        if "vkteams.exe" in proc.info['name']:
            return True
    return False