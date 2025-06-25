import os
import psutil
import time
from pywinauto.application import Application


APP_NAME = "vkteams.exe"

def wait_for_app_launch(timeout=5):
    # Пытаемся найти процесс в течение timeout секунд
    for _ in range(timeout):
            for proc in psutil.process_iter(['name']):
                if "vkteams.exe" in proc.info['name']:
                    print("Процесс vkteams.exe найден. Подключаемся к окну...")
                try:
                    app = Application(backend="uia").connect(process=proc.pid)
                    dlg = app.window(title="VK Teams")
                    dlg.wait("visible", timeout=5)

                    dlg.child_window(title="Принять и продолжить", control_type="Button").click_input()
                    
                    return
                except Exception as e:
                    print("Не удалось подключиться к окну VK Teams")