from pywinauto.application import Application


INSTALLER_PATH = r"C:\Users\WDAGUtilityAccount\Desktop\VKTeamsTest\vkteamssetup.exe"

def install_app():
    app = Application(backend="uia").start(INSTALLER_PATH)
    # Ждём основное окно установщика
    dlg = app.window(title="VK Teams")
    dlg.wait('visible', timeout=10)
    # Нажимаем кнопку "Установить"
    dlg.child_window(title="Install", control_type="Button").click_input()
    # Ждём закрытия окна установщика
    dlg.wait_not('visible', timeout=120)

    return not dlg.exists()
