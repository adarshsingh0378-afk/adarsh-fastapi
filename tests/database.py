import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.schemas import UserOut
from app.config import settings
from app.database import Base, get_db


SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{settings.database_username}:"
    f"{settings.database_password}@{settings.database_hostname}:"
    f"{settings.database_port}/{settings.database_name}_test"
)

# Create test engine + session
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Pytest fixture for client
@pytest.fixture(scope="module")
def client(session):
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def client(session):
    def override_get_db():
        db = TestingSessionLocal()
        try:
                yield session
        finally:
             session.clode()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)