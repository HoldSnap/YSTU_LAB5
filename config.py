import os

DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "layered_lab")
DB_USER = os.getenv("POSTGRES_USER", "lab_user")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "secure_password")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
