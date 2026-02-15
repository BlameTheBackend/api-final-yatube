# YaTube API — краткое описание

Учебный проект на Django REST Framework. Реализованы несколько моделей с логикой для удобного предоставления данных через API.

## Требования
- Python 3.12

## Установка и запуск (локально)
1. Клонировать репозиторий
    ```
    git clone https://github.com/ThinkLikeHorsie/api-final-yatube
    cd api-final-yatube
    ```
2. Создать виртуальное окружение и установить зависимости
    ```
    python -m venv venv
    source venv/bin/activate   # на Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```
3. Выполнить миграции и запустить сервер
    ```
    python manage.py migrate
    python manage.py runserver
    ```


## Примеры запросов к API

### Создание поста

**POST** `/api/v1/posts/`

**Тело запроса:**

```json
{
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
    "group": 1
}
```

**Пример ответа:**

```json
{
    "id": 14,
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
    "author": "anton",
    "image": null,
    "group": 1,
    "pub_date": "2021-06-01T08:47:11.084589Z"
}
```

---

### Добавление комментария к посту

**POST** `/api/v1/posts/14/comments/`

**Тело запроса:**

```json
{
    "text": "тест тест"
}
```

**Пример ответа:**

```json
{
    "id": 4,
    "author": "anton",
    "post": 14,
    "text": "тест тест",
    "created": "2021-06-01T10:14:51.388932Z"
}
```

---

### Получение группы

**GET** `/api/v1/groups/2/`

**Пример ответа:**

```json
{
    "id": 2,
    "title": "Математика",
    "slug": "math",
    "description": "Посты на тему математики"
}
```

---

### Подписка на пользователя

**POST** `/api/v1/follow/`

**Тело запроса:**

```json
{
    "user": "root",
    "following": "second_user"
}
```

**Пример ответа:**

```json
{
    "user": "regular_user",
    "following": "second_user"
}
```
