- [English](https://github.com/bitcamp-group-2/twitter-clone-py-t2/blob/george/readme.md)
- [ქართული](https://github.com/bitcamp-group-2/twitter-clone-py-t2/blob/george/redme.ge.md)
- [Русский](https://github.com/bitcamp-group-2/twitter-clone-py-t2/blob/george/readme.ru.md)

## об проекте
    ето MVP (минималное) - twitter-clone

# инструкция как ползоватся и тестироват на локалном
- для клонирование проект в вашем комп
```
https://github.com/bitcamp-ge/twitter-clone-py-t2.git
```

- для создание виртуалное машини (venv - virtual-environment)
```python -m venv venv
```

- если понадобится инструкция как активироват виртуалное манина
нажмите [Here][tutorial] или посмотри нажмите

- для установки библиотеки
```
pip install -r requirements.txt
```

- создание миграции
```
python manage.py makemigrations
```

- запуск миграции
```
python manage.py migrate
```

- для запуск сервера
```
python manage.py runserver
```

# инструкция - как активироват виртуалку

## для Windows 
- cmd.exe
```
.\venv\Scrypts\activate.bat
```

## для линукс (Linux)
- bash/zsh:
```
source ./venv/bin.activate
```
- fish:
```
source ./venv/bin/activate.fish
```
- csh/tch:
```
source ./venv/bin/activate.csh
```