@echo off
set /p "pydownload=You Installed python? ( y / n ) : "
echo Installing app...
timeout /t 3 /nobreak > nul
echo Step 1, Downloading python...
if pydownload==n goto pysetup
if pydownload==y goto install
:install
echo Step 2, Add to path ( appgeter , parent\pysetuper.py )
echo Opening for step 1 python script to add path...
call natives\addtopath.py
echo Installed.
echo.
pause
exit
:pysetup
echo Installing python...
echo.
call natives\python.exe
goto install
