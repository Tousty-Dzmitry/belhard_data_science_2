# Drone Detection API (FastAPI)

Проект на **FastAPI** для загрузки видео, детекции дронов (YOLOv8), обводки их красной рамкой и подписи меткой **"Drone!"** при уверенности ≥ 0.82.

Если необходимо готовое виртуальное окружение для тестирования, **не рекомендуем** коммитить `venv/` (\~6 ГБ) в репозиторий:

* Используйте `requirements.txt`: `pip install -r requirements.txt`.
* Или создайте архив `venv.tar.gz` и поделитесь им извне Git.

---

##  Структура проекта

```bash
drone-detection-api/
├── app/
│   ├── main.py             # FastAPI-приложение
│   ├── routes/
│   │   └── video.py        # Эндпоинты API для загрузки и обработки видео
│   ├── services/
│   │   └── detector.py     # Бизнес-логика обработки видео
│   └── models/
│       └── yolo_wrapper.py # Загрузка YOLO, детекция и аннотации
├── uploads/                # Временное хранение исходных видео
├── processed_videos/       # Выходные видео с рамками и метками
├── requirements.txt        # Список зависимостей
├── .gitignore              # Исключения Git (включает venv/)
└── README.md               # Инструкция по установке и использованию
```

## ⚙️ Установка и запуск

1. **Клонировать репозиторий**:

   ```bash
   ```

git clone \<repo\_url> drone-detection-api
cd drone-detection-api

````
2. **Создать и активировать виртуальное окружение**:
```bash
python3 -m venv venv
source venv/bin/activate
````

3. **Установить зависимости**:

   ```bash
   ```

pip install -r requirements.txt

````
4. **Запустить сервер**:
```bash
uvicorn app.main:app --reload
````

Откройте: `http://127.0.0.1:8000/docs`

---

##  Тестирование API

### Swagger UI

1. Перейдите в браузере по адресу:

   ```
   ```

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

````
2. В разделе **video** выберите **POST /video/detect**.
3. Нажмите **Try it out**, загрузите `.mp4` и нажмите **Execute**.
4. После обработки появится ссылка **Download file**. Видео сохранится в `processed_videos/`.

### `curl`
```bash
curl -X POST "http://127.0.0.1:8000/video/detect" \
  -F "file=@/path/to/video.mp4" \
  --output result.mp4
````

---

##  Параметры и настройки

* **Порог уверенности** изменяется в `app/models/yolo_wrapper.py`:

  ```python
  if cls_id == 0 and conf >= 0.82:
      # рисуем рамку
  ```
* **Путь к весам** в `load_model()`:

  ```python
  model = YOLO("app/models/best.pt")
  ```

---

##  Очистка

```bash
rm -rf uploads/* processed_videos/*
```

---

##  Устранение неполадок

* **404 Not Found**: обращайтесь к `/docs` или `/video/detect`.
* **Port in use**: `pkill -f uvicorn`.
* **Ошибки зависимостей**: проверьте `requirements.txt` и переустановите пакеты.

---

Результаты можно посмотреть в папке "processed_videos"

*Приятного использования!*

