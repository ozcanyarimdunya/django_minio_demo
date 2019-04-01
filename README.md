# Django Mini Storage Demo

> **django-minio-storage** enables using minio as django static and media file storages.

We are using minio for storing media files only.

| |In-Local-Development|In-Production|
|----------|--------------------|-------------|
|statics   |Saved in django files and served by django|Saved in django files and served by WhiteNoise  |
|medias    |Saved in django files and served by django|Saved in minio and served by minio(not finished)|


Quick look
==========

```bash
config/base.py
config/production.py
```

Installation
============

You need to run at least 4 minio instances. 

```bash
docker-compose -f docker-compose-minio.yml -f docker-compose.yml up -d --build
```

Development
===========

Install all requirements

```bash
make
```

You need a superuser to access admin pages( /admin/ ). To create a superuser,

```bash
make superuser
```

Run the application

```bash
make run
```

TODO
=====

- [ ] Provide direct download link

- [ ] Provide `Serve by minio as public`
