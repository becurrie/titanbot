:: Create Virtualenv.
:: Expecting virtualenvwrapper-win
call mkvirtualenv titandash -r requirements.txt

:: Using new virtual environment, make and migrate.
call %WORKON_HOME%/titandash/Scripts/python titanbot/manage.py makemigrations
call %WORKON_HOME%/titandash/Scripts/python titanbot/manage.py migrate

:: Install node modules.
call npm install

:: Collect static files.
call %WORKON_HOME%/Scripts/python titanbot/manage.py collectstatic --noinput

PAUSE