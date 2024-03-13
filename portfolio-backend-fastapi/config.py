import os

DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_NAME = os.environ.get("DB_NAME", "portfolio")
DB_USER = os.environ.get("DB_USER", "portfolio")
DB_PASS = os.environ.get("DB_PASS", "portfolio")
