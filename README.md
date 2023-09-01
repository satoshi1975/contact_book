# API документация

Добро пожаловать в документацию API. Здесь вы найдете информацию о доступных конечных точках и их использовании.

## Установка
- клонируйте репозиторий в вашу деректорию
- создайте роль, пароль к ней и базу данных postgres, указанные в docker-compose.yml
      (POSTGRES_DB: contact_book
      POSTGRES_USER: contact_admin
      POSTGRES_PASSWORD: contact)
```sql
CREATE ROLE contact_admin WITH LOGIN PASSWORD 'contact';
CREATE DATABASE contact_book OWNER contact_admin;
GRANT ALL PRIVILEGES ON DATABASE contact_book TO contact_admin;
```
- перейдите в папку с docker-compose.yml и запустите сборку (docker-compose build)
- запустите контейнеры (docker-compose up)
- создайте и примените миграции
- Для доступа к эндпоинтам api создайте суперпользователя (django-admin createsuperuser) и пройдите базовую аутентификацию
- api доступно на хосте http://127.0.0.1:8000/
- swagger документация будет доступна по url http://127.0.0.1:8000/swagger



### Вывод всех контактов

`GET /v1/contacts/`

Параметры:
- `?page_size=(count)` (количество): количество контактов на одной странице
- `?page=(number)` (номер): номер страницы


Ответ:
```json
{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "id": 0,
      "first_name": "string",
      "last_name": "string",
      "phone": "string",
      "email": "user@example.com"
    }
  ]
}
```

### Добавление контакта

`POST /v1/contacts/`

Тело запроса:
```json
{
  "first_name": "string",
  "last_name": "string",
  "phone": "string",
  "email": "user@example.com"
}
```

Ошибки(400):
```json
{
    "error": [
        "This phone number is already used."
    ]
}
```

```json
{
    "error": [
        "This email is already used."
    ]
}
```
```json

{
    "email": [
        "Enter a valid email address."
    ]
}
```


### Получение контакта по идентификатору


`GET /v1/contacts/{id}`


Ответ:
```json
{
  "id": 0,
  "first_name": "string",
  "last_name": "string",
  "phone": "string",
  "email": "user@example.com"
}
```

Ошибка(404):
```json
{
    "detail": "Contact not found."
}
```
### Изменение данных контакта по идентификатору

`PUT /v1/contacts/{id}`
`PATCH /v1/contacts/{id}`

Тело запроса:
```json
{
  "first_name": "string",
  "last_name": "string",
  "phone": "string",
  "email": "user@example.com"
}
```

Ошибки(400):
```json
{
    "error": [
        "This phone number is already used."
    ]
}
```

```json
{
    "error": [
        "This email is already used."
    ]
}
```
```json

{
    "email": [
        "Enter a valid email address."
    ]
}
```

### Удаление контакта по идентификатору


`DELETE /v1/contacts/{id}`


Ошибка(404):
```json
{
    "detail": "Contact not found."
}
```

### Поиск контактов по имени

`GET /v1/contacts/search/name/`

Параметры:
- `?name=(string)` (Имя): ввод имени контакта(допустим ввод не до конца)
- `?page_size=(count)` (количество): количество контактов на одной странице
- `?page=(number)` (номер): номер страницы


Ответ:
```json
{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "id": 0,
      "first_name": "string",
      "last_name": "string",
      "phone": "string",
      "email": "user@example.com"
    }
  ]
}
```
Ошибка(404):
```json
{
    "detail": "Contact not found."
}
```
### Поиск контактов по фамилии

`GET /v1/contacts/search/last_name/`

Параметры:
- `?last_name=(string)` (Имя): ввод фамилии контакта(допустим ввод не до конца)
- `?page_size=(count)` (количество): количество контактов на одной странице
- `?page=(number)` (номер): номер страницы


Ответ:
```json
{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "id": 0,
      "first_name": "string",
      "last_name": "string",
      "phone": "string",
      "email": "user@example.com"
    }
  ]
}
```
Ошибка(404):
```json
{
    "detail": "Contact not found."
}
```

