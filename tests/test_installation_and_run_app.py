from utils.install import install_app
from utils.verification import is_app_running
from utils.launch import wait_for_app_launch, close_app
import allure


@allure.title("Запуск теста на установку приложения VK Teams")
def test_installation_and_run_app():
    install_app()
    assert install_app(), "Установка VK Teams не завершилась"
    print("Установка VK Teams успешно завершена")

    wait_for_app_launch()

    assert is_app_running() is True, "VK Teams не запущен"
    print("\nVK Teams успешно запущен")

    close_app()