class Config:
    PG_USER = "cursor"
    PG_PASSWORD = "very_secret_password"
    PG_HOST = "psql"
    PG_PORT = 5432
    DB_NAME = "docker_flask_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEGUB = True
    HOST = '0.0.0.0'
    PORT = 5001
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"