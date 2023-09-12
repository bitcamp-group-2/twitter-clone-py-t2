- [English](https://github.com/bitcamp-group-2/twitter-clone-py-t2/blob/george/readme.md)
- [ქართული](https://github.com/bitcamp-group-2/twitter-clone-py-t2/blob/george/redme.ge.md)
- [Русский](https://github.com/bitcamp-group-2/twitter-clone-py-t2/blob/george/readme.ru.md)

## პროექტის შესახებ
    ეს არის twitter ის მინიმალური კლონი

## ინსტრუქცია:
- იმისთვის რომ კოდი გადაიტანოთ(გადააკოპირო) ლოკალურ მანქანაზე:
```
https://github.com/bitcamp-ge/twitter-clone-py-t2.git
```

- შექმენით Python -ის ვირტუალური ყუთი (Python venv (environment)):
```
python -m venv venv
```

- ვირტუალური ყუთის აქტივაციის ინსთრუქცია ქვემოთ წერია თუ გაინტერესებს

- საჭირო ბიბლიოთეკების ინსტალაცია:
```
pip install -r requirements.txt
```

- მიგრაციების შექმნა:
```
python manage.py makemigrations
```

- მიგრაციების გაშვება:
```
python manage.py migrate
```

- Django სერვერის გაშვება (start):
```
python manage.py runserver
```


# ინსტრუქცია - ვირტუალური ყუთის აქტივაცია:

## Windows - ის მომხმარებლებისთვის:
- cmd.exe:
```
.\venv\Scripts\activate.bat
```

## Linux ის მომხმარებლებისთვის:
- bash/zsh:
```
source ./venv/bin/activate
```

- fish:
```
source ./venv/bin/activate.fish
```

- csh/tch:
```
source ./venv/bin/activate.csh
```
