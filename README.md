# Where to go

Сайт аналог Яндекс.Афишы. Представляет собой интерактивную карту Москвы с указанием интересных мест с их подробным описанием, фотографиями и комментариями. Можно посмотреть [демо версию сайта](https://permsky.pythonanywhere.com/).

## Запуск

Для запуска в системе должен быть установлен Python 3.7+.

- Скачайте код
- Создайте и активируйте виртуальное окружение командой:
```bash
python -m venv env && source env/bin/activate
```
- Установите зависимости командой:
```bash
pip install -r requirements.txt
```
- Создайте в корне проекта файл `.env` с переменными окружения:

  SECRET_KEY=*секретный ключ проекта, например `erofheronoirenfoernfx49389f43xf3984xf9384`*

  Для более детальной настройки django-проекта, в том числе при деплое, можно использовать следующие переменные окружения:

  DEBUG=*дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки. Выключается значением `False`*

  ALLOWED_HOSTS=*список разрешенных имен хостов, например `example.com`*

  DATABASE=*URL для конфигурирования базы данных. Подробнее в [README](https://github.com/kennethreitz/dj-database-url)*

  STATIC_URL=*URL статики*

  STATIC_ROOT=*директория для сбора файлов статики*

  MEDIA_URL=*URL для медиа файлов*

  MEDIA_ROOT=*директория для сохранения загружаемых медиа-файлов*

  SESSION_COOKIE_SECURE=*Установить в значение `True` для предотвращения передачи куки сессии с помощью HTTP протокола*

  CSRF_COOKIE_SECURE=*Установить в значение `True` для предотвращения передачи CSRF-куки с помощью HTTP протокола*

  SECURE_SSL_REDIRECT=*Установить в значение `True` для перенаправления не-HTTPS запросов на HTTPS*

- Создайте базу данных и примените миграции командами:
```bash
python manage.py migrate
python manage.py makemigrations places
python manage.py migrate
```
- Создайте учётную запись администратора командой:
```bash
python manage.py createsuperuser
```
- Загрузите данные об интересных местах в базу данных командой:
```bash
python manage.py load_places
```
Загрузка данных выполняется из json-файлов следующего вида:
```{
    "title": "Антикафе Bizone",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/be067a44fb19342c562e9ffd815c4215.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/f6148bf3acf5328347f2762a1a674620.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b896253e3b4f092cff47a02885450b5c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/605da4a5bc8fd9a748526bef3b02120f.jpg"
    ],
    "description_short": "Настольные и компьютерные игры, виртуальная реальность и насыщенная программа мероприятий — новое антикафе Bizone предлагает два уровня удовольствий для вашего уединённого отдыха или радостных встреч с родными, друзьями, коллегами.",
    "description_long": "<p>Рядом со станцией метро «Войковская» открылось антикафе Bizone, в котором создание качественного отдыха стало делом жизни для всей команды. Создатели разделили пространство на две зоны, одна из которых доступна для всех посетителей, вторая — только для совершеннолетних гостей.</p><p>В Bizone вы платите исключительно за время посещения. В стоимость уже включены напитки, сладкие угощения, библиотека комиксов, большая коллекция популярных настольных и видеоигр. Также вы можете арендовать ВИП-зал для большой компании и погрузиться в мир виртуальной реальности с помощью специальных очков от топового производителя.</p><p>В течение недели организаторы проводят разнообразные встречи для меломанов и киноманов. Также можно присоединиться к английскому разговорному клубу или посетить образовательные лекции и мастер-классы. Летом организаторы запускают марафон настольных игр. Каждый день единомышленники собираются, чтобы порубиться в «Мафию», «Имаджинариум», Codenames, «Манчкин», Ticket to ride, «БЭНГ!» или «Колонизаторов». Точное расписание игр ищите в группе антикафе <a class=\"external-link\" href=\"https://vk.com/anticafebizone\" target=\"_blank\">«ВКонтакте»</a>.</p><p>Узнать больше об антикафе Bizone и забронировать стол вы можете <a class=\"external-link\" href=\"http://vbizone.ru/\" target=\"_blank\">на сайте</a> и <a class=\"external-link\" href=\"https://www.instagram.com/anticafe.bi.zone/\" target=\"_blank\">в Instagram</a>.</p>",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```
- Запустите сервер командой:
```bash
python manage.py runserver
```

После этого главная страница будет доступна по адресу [127.0.0.1:8000](http://127.0.0.1:8000), админка — [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).