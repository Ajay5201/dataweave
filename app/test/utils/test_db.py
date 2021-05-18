from pydantic import PostgresDsn
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker




Db_URL="postgresql://postgres:swethA@127.0.0.1:5432/postgres"
engine = create_engine(Db_URL, pool_pre_ping=True)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)