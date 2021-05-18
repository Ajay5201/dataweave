from typing import Generator
import asyncio
import pytest
from fastapi.testclient import TestClient
from main import get_db
from database import Base
from main import app
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker

Db_URL="postgresql://postgres:swethA@127.0.0.1:5432/postgres"
engine = create_engine(Db_URL, pool_pre_ping=True)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
print("ajay")
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
@pytest.fixture(scope="session")
def db() -> Generator:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    yield TestingSessionLocal()
@pytest.fixture(scope="module")
def client() -> Generator:

    with TestClient(app) as c:
        yield c
def test_create_user(client: TestClient):
    response = client.get("/ProductDiscounts")
    assert response.status_code == 200