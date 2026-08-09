@echo off
REM ============================================================================
REM  battery.cmd - the pre-ship battery.  Written s55.
REM
REM  WHY: Claude CANNOT run this. There is no browser in Claude's sandbox and no
REM  root to install one - proven in s55, 115 MB downloaded to learn it (SS77.2).
REM  This machine is the only place it runs.
REM
REM  PYTHONUTF8=1 IS NOT OPTIONAL. Without it agents.py dies on a Windows cp1252
REM  UnicodeEncodeError writing its own report, because the app is full of
REM  * < > and No. - the battery fails on its OUTPUT, not on the build (SS82.1).
REM
REM  USE:  battery              tests .\index.html
REM        battery some.html    tests a candidate build
REM ============================================================================
setlocal
cd /d "%~dp0"
set PYTHONUTF8=1

where python >nul 2>&1
if errorlevel 1 (
  echo python is not on PATH. Try 'py' instead, or install it with:
  echo    winget install Python.Python.3.12
  goto :end
)

echo Checking the harness is present...
python -c "import playwright" 2>nul
if errorlevel 1 (
  echo   playwright missing - installing it and Chromium. This takes a few minutes.
  python -m pip install playwright
  python -m playwright install chromium
)
where node >nul 2>&1
if errorlevel 1 echo   WARNING: node is not on PATH. Agent A ^(node --check^) will fail. winget install OpenJS.NodeJS.LTS

echo.
python test\run.py %1
set "BATRC=%ERRORLEVEL%"

REM s57: STAMP THE FILE THAT PASSED. ship.cmd's GATE 3 compares this against the
REM index.html it is about to commit, so a build cannot be shipped on a green tick
REM that belonged to a DIFFERENT build - which is how 33e, 33f and 33g all shipped
REM untested. Only a full run counts: `battery some.html` skips SESSION, so it must
REM not leave a stamp claiming the shelf build was tested.
if not "%BATRC%"=="0" goto :nostamp
if not "%~1"=="" goto :nostamp
set "BH="
for /f "delims=" %%H in ('certutil -hashfile index.html SHA256 ^| findstr /r "^[0-9a-f]"') do if not defined BH set "BH=%%H"
set "BH=%BH: =%"
> test\.last-battery echo %BH%
echo   (recorded: the battery passed on %BH%)
:nostamp
echo.
echo ===== READ THIS BEFORE BELIEVING IT =====
echo   A green tick is an exit code, not a result.
echo   If Agent D reports DRIFT, do NOT rebaseline test\baseline.json to make it
echo   pass - a rebaselined test proves nothing. Report the drift instead.
echo   Send Claude the whole output, not just the last line.
:end
echo.
pause
endlocal
