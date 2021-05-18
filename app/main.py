import datetime
import uuid
from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import FastAPI
from sqlalchemy import desc
# from fastapi.testclient import TestClient
app = FastAPI()
from app.database import database, engine, products, SessionLocal,Base
Base.metadata.create_all(bind=engine)

from app import model as md

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
async def startup():
    await database.connect()



@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
def read_root():
    return {"Hola": "Mundo"}


@app.get("/Products")
async def register_user():
    query = products.select()
    return await database.fetch_all(query)

@app.post("/Search/title")
async def register_user(search:md.Search):
    title=search.searchKey
    query = products.select().where(products.c.title==title)
    return await database.fetch_all(query)

@app.post("/Search/sku")
async def register_user(search:md.Search):
    sku=search.searchKey
    query = products.select().where(products.c.sku==sku)
    return await database.fetch_all(query)

@app.post("/UpdateProduct",response_model=md.ViewUpdateProduct,tags=["Users"])
async def register_user(UpdateProduct:md.UpdateProduct):
    query = products.update().where(products.c.urlh == UpdateProduct.urlh).values(
        brand=UpdateProduct.brand,
        category=UpdateProduct.category,
        subcategory=UpdateProduct.subcategory,
        product_type=UpdateProduct.product_type,
    )
    await database.execute(query)
    return await find_product_by_id(UpdateProduct.urlh)


@app.get("/Products/{urlh}", response_model=md.ViewUpdateProduct, tags=["Users"])
async def find_product_by_id(urlh: str):
    query = products.select().where(products.c.urlh == urlh)
    return await database.fetch_one(query)

@app.get("/Products/brand/{brand}")
async def find_product_by_brand(brand: str):
    query = products.select().where(products.c.brand == brand)
    return await database.fetch_all(query)

@app.get("/Products/category/{category}")
async def find_product_by_category(category: str):
    query = products.select().where(products.c.category == category)
    return await database.fetch_all(query)

@app.get("/Products/subcategory/{subcategory}")
async def find_product_by_subcategory(subcategory: str):
    print("gh")
    query = products.select().where(products.c.subcategory ==subcategory)
    return await database.fetch_all(query)

@app.get("/Products/source/{source}")
async def find_product_by_source(source: str):
    query = products.select().where(products.c.source == source )
    return await database.fetch_all(query)

@app.post("/FilterProducts")
async def find_product_by_filter(filter:md.ViewFilter):
    print("ajay")


    query = products.select().where(products.c.source == filter.source and products.c.subcategory ==filter.subcategory and products.c.category == filter.category and products.c.brand == filter.brand)
    return await database.fetch_all(query)

@app.get("/ProductDiscounts")
async def find_product_by_discount():

    res=engine.execute('select  count(*) filter (where discount = 0),count(*) filter (where discount > 0 and discount <= 10),count(*) filter (where discount > 10 and discount <= 30),count(*) filter (where discount > 30 and discount <= 50),count(*) filter (where discount > 50 ) from products;').fetchall()
    discount= {
        "0%":res[0][0],
        "0%-10%": res[0][1],
        "10%-30%":res[0][2],
        "30%-50%":res[0][3],
        ">50%":res[0][4]
    }
    json_compatible_item_data = jsonable_encoder(discount)
    return JSONResponse(content=json_compatible_item_data)






