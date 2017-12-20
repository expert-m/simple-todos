# TODO
1. Необходимо реализовать ToDo список и позволить пользователю проводить CRUD-
операции над ним.
2. ToDo списки относятся к различным организациям.
3. Чтобы получить доступ к списку, пользователь должен авторизоваться.
4. Авторизация должна происходить с помощью email и пароля.
5. Возможна регистрация пользователя (сама логика регистрации не входит в задание) с
привязкой к одной и более организации, но с одним и тем же email пользователя.
6. Пользователь должен авторизовываться только в одной организации. То есть, чтобы
получить доступ к ToDo списку другой организации, пользователь должен
переавторизоваться в необходимой ему организации. Фронтенда не нужно.
7. Для авторизации и модели пользователя обязательно использовать
'django.contrib.auth'.
8. Необходимо использовать DRF serializers вместо django-forms.
9. Стек технологий:
- python2
- django 1.10
- django-rest-framework
- любая СУБД

### Install
1. `pip install -r requirements.txt`

### Start
1. `python manage.py runserver`
2. Open `http://127.0.0.1:8000/api/auth/`.
3. Enter a organization id, login and password.
(`http://127.0.0.1:8000/api/auth/` - all organizations)

### API
```
/api/auth/
/api/tasks/
/api/tasks/:id/
/api/organizations/
```

### Login
```
login: user@mail.ru
password: test1010
```
or

```
login: test@mail.ru
password: test1010
```
