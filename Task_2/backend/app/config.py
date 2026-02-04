import os


class Config:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVER_NAME = None

    # MySQL
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('MYSQL_USER')}:"
        f"{os.getenv('MYSQL_PASSWORD')}@"
        f"{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DB')}"
    )

    # Redis cache
    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_HOST = os.getenv("REDIS_HOST", "redis")
    CACHE_REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    CACHE_DEFAULT_TIMEOUT = 60

    # CORS
    FE_HOST = os.getenv("FE_HOST")
