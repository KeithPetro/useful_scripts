@ECHO ON
SETLOCAL EnableDelayedExpansion

for %%i in (*.*) do if not %%~xi==.bat (
	set "TEMP_STRING=%%~ni"

	for /f "delims=-" %%a in ("!TEMP_STRING!") do (
		set "FOLDER=%%a"
	)

	if not exist "!FOLDER!" mkdir "!FOLDER!"
	MOVE "%%i" "!FOLDER!^\%%i"
)

ENDLOCAL

pause
