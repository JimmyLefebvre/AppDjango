@echo off

echo Deleting database files in progress ...
for /d %%d in (*.*) do (
    IF EXIST %CD%\%%d\migrations (
        for %%i in (%CD%\%%d\migrations\*) do (
            if %%i NEQ  %CD%\%%d\migrations\__init__.py DEL %%i /Q
        )
    )
)
DEL db.sqlite3 /Q
echo The database was erased with success !

:Prompt
echo Do you want to create a new clean database? [Y/N]
set INPUT=
set /P INPUT= %=%
If /I "%INPUT%"=="Y" goto yes
If /I "%INPUT%"=="y" goto yes
If /I "%INPUT%"=="yes" goto yes
If /I "%INPUT%"=="Yes" goto yes
If /I "%INPUT%"=="YES" goto yes
If /I "%INPUT%"=="N" goto no
If /I "%INPUT%"=="n" goto no
If /I "%INPUT%"=="No" goto no
If /I "%INPUT%"=="no" goto no
If /I "%INPUT%"=="NO" goto no
echo Incorrect input & goto Prompt

:yes
echo Do you want to initial
echo Migrations in progress ...
python manage.py makemigrations
echo Migrate in progress ...
python manage.py migrate
echo create super user ...
python manage.py createsuperuser
goto :no

:no
echo Work done !