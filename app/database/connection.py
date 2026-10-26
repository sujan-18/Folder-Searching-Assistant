from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.env.env import password, Server_Port


DATABASE_URL = (
    f"postgresql+psycopg://postgres:{password}"
    f"@localhost:{Server_Port}/myassistant"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)