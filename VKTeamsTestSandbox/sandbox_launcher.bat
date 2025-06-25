@echo off
setlocal

set TEST_DIR=C:\VKTeamsTest
set WSB_FILE=sandbox_test.wsb

(
echo ^<Configuration^>
echo   ^<MappedFolders^>
echo     ^<MappedFolder^>
echo       ^<HostFolder^>%TEST_DIR%^</HostFolder^>
echo       ^<ReadOnly^>false^</ReadOnly^>
echo     ^</MappedFolder^>
echo   ^</MappedFolders^>
echo   ^<LogonCommand^>
echo     ^<Command^>cmd.exe /c %TEST_DIR%\run_tests.bat^</Command^>
echo   ^</LogonCommand^>
echo ^</Configuration^>
) > "%TEST_DIR%\%WSB_FILE%"

start "" "%TEST_DIR%\%WSB_FILE%"
endlocal