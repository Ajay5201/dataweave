import databases, sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Db_URL="postgresql://username:password@db:5432/nudges"
database=databases.Database(Db_URL)
metadata=sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    Db_URL
)
products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("urlh",sqlalchemy.String),
    sqlalchemy.Column("status",sqlalchemy.Integer),
    sqlalchemy.Column("brand",sqlalchemy.String),
    sqlalchemy.Column("category",sqlalchemy.String),
    sqlalchemy.Column("subcategory",sqlalchemy.String),
    sqlalchemy.Column("product_type",sqlalchemy.String),
    sqlalchemy.Column("sku",sqlalchemy.String),
    sqlalchemy.Column("title",sqlalchemy.String),
    sqlalchemy.Column("thumbnail",sqlalchemy.String),
    sqlalchemy.Column("url",sqlalchemy.String),
    sqlalchemy.Column("source",sqlalchemy.String),
    sqlalchemy.Column("seller",sqlalchemy.String),
    sqlalchemy.Column("crawl_date",sqlalchemy.Date),
    sqlalchemy.Column("crawl_time",sqlalchemy.DateTime),
    sqlalchemy.Column("mrp",sqlalchemy.Float),
    sqlalchemy.Column("available_price",sqlalchemy.Float),
    sqlalchemy.Column("discount",sqlalchemy.Float),
    sqlalchemy.Column("stock",sqlalchemy.String),

)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata.create_all(engine)
Base = declarative_base()