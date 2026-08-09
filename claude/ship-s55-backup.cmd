@echo off
REM ============================================================================
REM  ship.cmd - Scavenger & Hunt Co.  Written s55.
REM
REM  WHY THIS EXISTS: every session ended with Claude pasting the same four git
REM  lines and the owner retyping them, in cmd.exe, one at a time. Twice in s55
REM  that went wrong - PowerShell syntax in a cmd window, and a verification
REM  block pasted onto the end of a git push line.
REM
REM  USE:   ship "s56: 33f - what changed"
REM         ship                          (uses a dated message)
REM
REM  It stages everything git is willing to take, honouring .gitignore - so the
REM  Worker sources, docs-private\ and _to_delete\ are never committed by
REM  accident. Then it PROVES the push instead of trusting it.
REM ============================================================================
setlocal
cd /d "%~dp0"

set "MSG=%~1"
if "%MSG%"=="" set "MSG=session commit %DATE% %TIME%"

echo.
echo ===== WHAT IS ABOUT TO GO =====
git status --short
echo.
echo Message: %MSG%
echo.
choice /c YN /m "Push this"
if errorlevel 2 goto :cancelled

git add -A
git commit -m "%MSG%"
if errorlevel 1 echo   (nothing new to commit - this usually means it was already committed)
git push origin main
if errorlevel 1 goto :pushfailed

echo.
echo ===== THE PROOF =====
echo   Local  HEAD:
git rev-parse HEAD
echo   Origin HEAD:
git rev-parse origin/main
echo.
echo   index.html on disk:
certutil -hashfile index.html SHA256 | findstr /r "^[0-9a-f]"
echo.
echo   Buildmark:
findstr /c:"test build marker" index.html | findstr /r /c:">3[0-9][a-z]<"
echo.
echo   If Local and Origin match, it is pushed. Pages can lag a minute.
echo   Ask Claude to hash Pages and the Worker before recording it as live.
goto :end

:pushfailed
echo.
echo ***** THE PUSH FAILED. Nothing above is live. Read the error, do not retry blind.
goto :end

:cancelled
echo Cancelled. Nothing staged, nothing committed.

:end
echo.
pause
endlocal
