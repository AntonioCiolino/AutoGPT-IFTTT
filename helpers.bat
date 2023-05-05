@echo off

set GPT_HOME=C:\Users\anton\Auto-GPT

if "%1" == "clean" (
  echo Removing build artifacts and temporary files...
  call :clean
) else if "%1" == "qa" (
  echo Running static analysis tools...
  call :qa
) else if "%1" == "style" (
  echo Running code formatters...
  call :style
) else if "%1" == "package" (
  echo Packaging archive...
  call :package
) else if "%1" == "unittest" (
  echo Running tests
  call :unittest
) else (
  echo Usage: %0 [clean^|qa^|style^|package]
  exit /b 1
)

exit /b 0

:clean
  rem Remove build artifacts and temporary files
  @del /s /q build 2>nul
  @del /s /q dist 2>nul
  @del /s /q __pycache__ 2>nul
  @del /s /q *.egg-info 2>nul
  @del /s /q **\*.egg-info 2>nul
  @del /s /q *.pyc 2>nul
  @del /s /q **\*.pyc 2>nul
  @del /s /q reports 2>nul
  echo Done!
  exit /b 0

:qa
  rem Run static analysis tools
  @flake8 .
  @python run_pylint.py
  echo Done!
  exit /b 0

:style
  rem Format code
  @isort .
  @black --exclude=".*\/*(dist|venv|.venv|test-results)\/*.*" .
  echo Done!
  exit /b 0

:package
   python -m zipfile -c AutoGPT_IFTTT.zip  src/AutoGPT_IFTTT
   copy AutoGPT_IFTTT.zip %GPT_HOME%\plugins
   python -m autogpt --debug 
   exit /b 0

:unittest
   python -m unittest src/AutoGPT_IFTTT/ifttt_test.py -v
   exit /b 0