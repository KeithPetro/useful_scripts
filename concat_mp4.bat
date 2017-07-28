@ECHO ON
SETLOCAL EnableDelayedExpansion

set TEMP_FILES_STRING=

for /l %%x in (1, 1, %1) do (
	ffmpeg -i %%x.mp4 -c copy -bsf:v h264_mp4toannexb temp%%x.ts
	set TEMP_FILES_STRING=!TEMP_FILES_STRING!^|temp%%x.ts
)

ffmpeg -i "concat:%TEMP_FILES_STRING:~1%" -c copy out.ts
ffmpeg -i out.ts -c copy -bsf:a aac_adtstoasc out.mp4

ENDLOCAL

pause
