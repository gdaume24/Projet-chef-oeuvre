@echo off

rem Activer api
cd api
call venv_api\Scripts\activate.bat
start  cmd /k "python api.py"

rem Lancer tracker
start  cmd /k "python tracking.py"

rem Lancer appli
cd ../app
call venv_app\Scripts\activate.bat
start cmd /k "streamlit run app.py "

