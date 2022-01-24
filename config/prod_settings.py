from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "0.0.0.0"]


STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')