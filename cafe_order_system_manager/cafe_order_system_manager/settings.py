import os

# Определяем базовую директорию проекта. Это полезно для построения путей к другим файлам и директориям.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Секретный ключ для проекта. Он используется для шифрования данных. В реальном проекте его следует хранить в переменной окружения.
SECRET_KEY = 'your-secret-key'

# Режим отладки. Включает подробные сообщения об ошибках и другие функции, полезные при разработке.
DEBUG = True

# Список разрешенных хостов. В режиме отладки обычно пустой, но в продакшене должен содержать домены, с которых разрешено обращаться к приложению.
ALLOWED_HOSTS = []

# Список установленных приложений. Включает как встроенные приложения Django, так и пользовательские.
INSTALLED_APPS = [
    'django.contrib.admin',         # Административный интерфейс
    'django.contrib.auth',          # Система аутентификации
    'django.contrib.contenttypes',  # Работа с типами контента
    'django.contrib.sessions',      # Поддержка сессий
    'django.contrib.messages',      # Сообщения для пользователей
    'django.contrib.staticfiles',   # Обработка статических файлов
    'orders',                       # Пользовательское приложение для управления заказами
    'rest_framework',               # Django REST Framework для создания API
]

# Список промежуточного ПО (middleware), которое обрабатывает запросы.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',          # Обеспечение безопасности
    'django.contrib.sessions.middleware.SessionMiddleware',  # Поддержка сессий
    'django.middleware.common.CommonMiddleware',             # Общие задачи
    'django.middleware.csrf.CsrfViewMiddleware',             # Защита от CSRF атак
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Аутентификация
    'django.contrib.messages.middleware.MessageMiddleware',   # Сообщения
    'django.middleware.clickjacking.XFrameOptionsMiddleware',# Защита от clickjacking
]

# Основной файл конфигурации URL.
ROOT_URLCONF = 'cafe_order_system_manager.urls'

# Настройки шаблонов.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Используемый движок шаблонов
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Директории с шаблонами
        'APP_DIRS': True,  # Включать ли директории приложений в поиск шаблонов
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Переменные контекста для отладки
                'django.template.context_processors.request', # Переменные контекста запроса
                'django.contrib.auth.context_processors.auth', # Переменные контекста аутентификации
                'django.contrib.messages.context_processors.messages', # Переменные контекста сообщений
            ],
        },
    },
]

# Настройка WSGI приложения.
WSGI_APPLICATION = 'cafe_order_system_manager.wsgi.application'

# Настройки базы данных. Используется SQLite по умолчанию.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Валидаторы паролей.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Языковые настройки.
LANGUAGE_CODE = 'ru-ru'

# Часовой пояс.
TIME_ZONE = 'UTC'

# Настройки интернационализации.
USE_I18N = True
USE_L10N = True
USE_TZ = True

# URL для статических файлов.
STATIC_URL = '/static/'