@echo off
setlocal

set PYTHON_URL=https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe
set PYTHON_EXE=python_installer.exe
set PYTHON_DIR=C:\Program Files\Python310
set PYTHON_BIN=%PYTHON_DIR%\python.exe
set PIP_BIN=%PYTHON_DIR%\Scripts\pip.exe

echo [INFO] Скачиваем Python...
curl -o %PYTHON_EXE% %PYTHON_URL%

echo [INFO] Устанавливаем Python...
start /wait %PYTHON_EXE% /quiet InstallAllUsers=1 PrependPath=1

echo [INFO] Устанавливаем зависимости...
"%PIP_BIN%" install -r requirements.txt

echo [INFO] Запускаем pytest...
cd vkteams_project
"%PYTHON_BIN%" -m pytest -s -v > ..\test_log.txt 2>&1

echo [INFO] Готово. Лог сохранён в test_log.txt

pause
endlocal
