@echo off
REM ============================================================================
REM  ship.cmd - Scavenger & Hunt Co.  Written s55, HARDENED s57.
REM
REM  WHY THIS EXISTS: every session ended with Claude pasting the same four git
REM  lines and the owner retyping them, in cmd.exe, one at a time.
REM
REM  WHY IT NOW REFUSES THINGS (s57): three process rules were written down,
REM  read, and broken anyway in a single day. A rule in prose is a suggestion;
REM  a rule in the script is a rule. Each gate below is one real s57 failure:
REM
REM    GATE 1  index.html's hash must appear in HANDOFF.md.
REM            s57 shipped the PRE-rename build and recorded it as done. The
REM            proof block printed the committed hash and nobody read it. This
REM            also enforces "SS0 is updated in the SAME EDIT as the ship".
REM    GATE 2  if index.html changed, the buildmark must have changed too (SS8i).
REM    GATE 3  the battery must have run against THIS exact index.html.
REM            33e, 33f and 33g all shipped untested.
REM
REM  USE:   ship "s57: 33l - what changed"
REM         ship /force "..."     skip the gates. Say WHY in the message.
REM
REM  Stages everything git will take, honouring .gitignore - so Worker sources,
REM  docs-private\ and _to_delete\ are never committed by accident.
REM
REM  IF THIS SCRIPT ITSELF IS BROKEN: the pre-s57 version is at
REM  claude\ship-s55-backup.cmd - copy it back over ship.cmd and carry on.
REM ============================================================================
setlocal EnableDelayedExpansion
cd /d "%~dp0"

set "FORCE="
if /i "%~1"=="/force" (set "FORCE=1" & shift)

set "MSG=%~1"
if "%MSG%"=="" set "MSG=session commit %DATE% %TIME%"

echo.
echo ===== WHAT IS ABOUT TO GO =====
git status --short
echo.
echo Message: %MSG%

REM ---------- the hash of the file we are about to commit ----------
set "HASH="
for /f "delims=" %%H in ('certutil -hashfile index.html SHA256 ^| findstr /r "^[0-9a-f]"') do if not defined HASH set "HASH=%%H"
set "HASH=%HASH: =%"

echo.
echo ===== PRE-FLIGHT =====
echo   index.html  %HASH%

if defined FORCE (
  echo   /force - GATES SKIPPED. The message had better say why.
  goto :gatesdone
)

REM ---------- GATE 1: SS0 must already name this hash ----------
findstr /c:"%HASH%" HANDOFF.md >nul 2>&1
if errorlevel 1 (
  echo.
  echo ***** REFUSED - GATE 1: HANDOFF.md does not contain this hash.
  echo       SS0 is updated in the SAME EDIT as the ship, never afterwards.
  echo       Either the doc was not updated, or you are shipping a different
  echo       build than the one written up. s57 shipped the wrong build exactly
  echo       this way. Ask Claude to reconcile SS0, then ship again.
  echo       Override with:  ship /force "..."
  goto :end
)
echo   GATE 1  ok - HANDOFF.md names this hash

REM ---------- GATE 2: changed file must carry a new buildmark ----------
git show HEAD:index.html > "%TEMP%\shco_prev.html" 2>nul
if exist "%TEMP%\shco_prev.html" (
  set "PREVHASH="
  for /f "delims=" %%H in ('certutil -hashfile "%TEMP%\shco_prev.html" SHA256 ^| findstr /r "^[0-9a-f]"') do if not defined PREVHASH set "PREVHASH=%%H"
  set "PREVHASH=!PREVHASH: =!"
  if not "!PREVHASH!"=="%HASH%" (
    set "BMNOW="
    set "BMWAS="
    REM s61 (SS127): READ THE MARK WITH PYTHON, NOT findstr. index.html holds a
    REM 506,884-character base64 line; findstr cannot get past it and returned NOTHING
    REM for BOTH files, so the gate compared empty to empty and refused every ship.
    for /f "delims=" %%B in ('python "%~dp0test\buildmark.py" index.html') do if not defined BMNOW set "BMNOW=%%B"
    for /f "delims=" %%B in ('python "%~dp0test\buildmark.py" "%TEMP%\shco_prev.html"') do if not defined BMWAS set "BMWAS=%%B"
    REM A READ FAILURE IS NOT A RESULT. Refuse with a DIFFERENT message so it can never
    REM be mistaken for "the buildmark did not change".
    if "!BMNOW!"=="" set "BMNOW=UNREADABLE"
    if "!BMWAS!"=="" set "BMWAS=UNREADABLE"
    if "!BMNOW!"=="UNREADABLE" goto :bmunread
    if "!BMWAS!"=="UNREADABLE" goto :bmunread
    if "!BMNOW!"=="!BMWAS!" (
      echo.
      echo ***** REFUSED - GATE 2: index.html changed but the buildmark did not.
      echo       SS8i: every DELIVERED index.html carries a new #buildmark, and
      echo       the colour rotates with the letter. Bump it, tell Claude, ship.
      echo       Override with:  ship /force "..."
      del "%TEMP%\shco_prev.html" >nul 2>&1
      goto :end
    )
    echo   GATE 2  ok - buildmark !BMWAS! -^> !BMNOW!
  ) else (
    echo   GATE 2  n/a - index.html unchanged since the last commit
  )
  del "%TEMP%\shco_prev.html" >nul 2>&1
) else (
  echo   GATE 2  skipped - no previous index.html in HEAD
)

REM ---------- GATE 3: the battery must have run on THIS file ----------
if not exist "test\.last-battery" (
  echo.
  echo ***** REFUSED - GATE 3: no record that the battery has ever run.
  echo       Run:  battery          then ship again.
  echo       Override with:  ship /force "..."
  goto :end
)
set "BATHASH="
set /p BATHASH=<test\.last-battery
if not "%BATHASH%"=="%HASH%" (
  echo.
  echo ***** REFUSED - GATE 3: the battery last passed on a DIFFERENT build.
  echo         tested:  %BATHASH%
  echo         shipping: %HASH%
  echo       33e, 33f and 33g all shipped untested this way.
  echo       Run:  battery          then ship again.
  echo       Override with:  ship /force "..."
  goto :end
)
echo   GATE 3  ok - the battery passed on this exact file

:gatesdone
echo.
choice /c YN /m "Push this"
if errorlevel 2 goto :cancelled

git add -A
git commit -m "%MSG%"
if errorlevel 1 echo   (commit reported nothing to do - VERIFY THIS BELOW. A stale
if errorlevel 1 echo    .git\index.lock makes `git add` fail and produces this same line.)
git push origin main
if errorlevel 1 goto :pushfailed

echo.
echo ===== THE PROOF =====
echo   Local  HEAD:
git rev-parse HEAD
echo   Origin HEAD:
git rev-parse origin/main
echo.
REM s66 (SS135): THIS BLOCK USED TO PRINT %HASH% - THE HASH OF THE FILE ON DISK -
REM under the heading "COMMITTED", and read the buildmark off the working file too.
REM It could therefore only ever confirm what you already knew. At s64 a stale
REM .git\index.lock made `git add` fail, NOTHING was committed, and this block
REM printed a flawless green proof anyway. It now reads the file BACK OUT OF THE
REM COMMIT and compares. THE COMPARISON IS THE PROOF.
REM PIPED, NOT REDIRECTED TO A TEMP FILE. The first cut of this wrote `git show`
REM to %TEMP% and cmd answered "The filename, directory name, or volume label
REM syntax is incorrect" - no file was produced, so the proof cried UNREADABLE on
REM a ship that was perfectly fine. A pipe has no filename to get wrong.
REM Both sides are hashed with line endings NORMALISED - `.gitattributes` carries
REM `* text=auto`, so git may hand the blob back as CRLF while disk is LF. A raw
REM hash would then differ after a PERFECTLY GOOD ship, and a gate that cries wolf
REM gets forced past. See test\commithash.py.
set "COMMITHASH="
set "DISKHASH="
for /f "delims=" %%H in ('git show HEAD:index.html ^| python "%~dp0test\commithash.py" -') do if not defined COMMITHASH set "COMMITHASH=%%H"
for /f "delims=" %%H in ('python "%~dp0test\commithash.py" index.html') do if not defined DISKHASH set "DISKHASH=%%H"
if "%COMMITHASH%"=="" set "COMMITHASH=UNREADABLE"
if "%DISKHASH%"=="" set "DISKHASH=UNREADABLE"
echo   index.html READ BACK OUT OF THE COMMIT:
echo   %COMMITHASH%
echo   index.html on disk (same normalising):
echo   %DISKHASH%
echo   index.html on disk (raw, as the gates above read it):
echo   %HASH%
if "%COMMITHASH%"=="UNREADABLE" goto :notcommitted
if not "%COMMITHASH%"=="%DISKHASH%" goto :notcommitted
echo   THEY MATCH. This is the proof. Local==Origin is not - it only says the
echo   push agreed with the commit, never which build the commit carried.
echo.
echo   Buildmark IN THE COMMIT:
REM buildmark.py takes a path, so the commit is piped through a scratch file INSIDE
REM the repo (gitignored) rather than %TEMP%, for the same reason as above.
git show HEAD:index.html > "%~dp0test\.shipped.html" 2>nul
for /f "delims=" %%B in ('python "%~dp0test\buildmark.py" "%~dp0test\.shipped.html"') do echo      %%B
echo.
echo   Pages can lag a minute. Ask Claude to hash Pages and probe the Worker
echo   before recording it as live.
goto :end

:notcommitted
echo.
echo ***** THE COMMIT DOES NOT CARRY THE FILE ON DISK. NOTHING YOU TESTED IS LIVE.
echo       The two hashes above disagree, so whatever was pushed, it was not this
echo       build. COMMONEST CAUSE: a stale lock made `git add` fail silently.
echo       Clear it:   del C:\Users\tony\Documents\Hunt\.git\index.lock
echo       then run ship again. Do NOT record this as shipped.
goto :end

:pushfailed
echo.
echo ***** THE PUSH FAILED. Nothing above is live. Read the error, do not retry blind.
goto :end

:cancelled
echo Cancelled. Nothing staged, nothing committed.

:bmunread
echo.
echo ***** REFUSED - GATE 2: the buildmark could NOT BE READ.
echo       This is NOT "the buildmark did not change" - the check itself failed.
echo       working copy: !BMNOW!    HEAD copy: !BMWAS!
echo       Try:  python test\buildmark.py index.html
echo       If python is missing, install it or override with:  ship /force "..."
del "%TEMP%\shco_prev.html" >nul 2>&1
goto :end

:end
echo.
pause
endlocal
