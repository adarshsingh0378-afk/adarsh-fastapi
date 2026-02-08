from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# 1. Database URL setup
# Sabse pehle Render ka environment variable check karein
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Agar DATABASE_URL nahi milta (local testing ke liye), tab purana settings wala use karein
if not SQLALCHEMY_DATABASE_URL:
    from .config import settings
    SQLALCHEMY_DATABASE_URL = (
        f"postgresql://{settings.database_username}:{settings.database_password}@"
        f"{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
    )

# 2. Create the engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 3. Create SessionLocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Define Base
Base = declarative_base()

# 5. Dependency for routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()