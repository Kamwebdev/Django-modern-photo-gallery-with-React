# Django modern photo gallery with React
Nowoczesna aplikacja stworzona z wykorzystaniem Django REST API i React (z użyciem Webpacka). Głównym konceptem było wykorzystanie reacta do dynamicznego wyświetlania galerii zdjęć.

#### Demo aplikacji dostępne pod adresem https://photoforpassion.tk/

### Instalacja :
```
python3 -m venv myvenv
[linux] source myvenv/bin/activate 
[windows] myvenv\Scripts\activate.bat
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py makemigrations gallery
python3 manage.py migrate
npm run build
python3 manage.py runserver
```
