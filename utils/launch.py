import os
import psutil
import time
from pywinauto.application import Application

APP_NAME = "vkteams.exe"
APP_PATH = r"C:\Users\serebrinkaa\AppData\Local\Programs\VK Teams\vkteams.exe"

def wait_for_app_launch(timeout=3):
    for _ in range(timeout):
        for proc in psutil.process_iter(['name']):
            if APP_NAME in proc.info['name']:
                print("Процесс vkteams.exe найден. Подключаемся к окну...")
                try:
                    app = Application(backend="uia").connect(process=proc.pid)
                    dlg = app.window(title="VK Teams")
                    dlg.wait("visible", timeout=3)
                    return
                except Exception:
                    print(f"Не удалось подключиться к окну VK Teams")
        time.sleep(1)

    # если приложение не запустилось автоматически, то запускаем его вручную
    print("Процесс vkteams.exe не найден. Запускаем приложение вручную...")
    if not os.path.exists(APP_PATH):
        print("Файл приложения не найден по пути: {APP_PATH}")

    app = Application(backend="uia").start(APP_PATH)
    dlg = app.window(title="VK Teams")
    dlg.wait("visible", timeout=10)


def close_app():
    for proc in psutil.process_iter(['name']):
        if APP_NAME in proc.info['name']:
            proc.kill()
            print(f"Процесс {APP_NAME} завершен")
            break
    else:
        print(f"Процесс {APP_NAME} не найден")