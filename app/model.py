from pydantic import BaseModel, Field

class Search(BaseModel):
  searchKey  : str

class UpdateProduct(BaseModel):
    brand:str
    category:str
    subcategory:str
    product_type:str
    urlh:str

class ViewUpdateProduct(BaseModel):
    urlh:str
    title:str
    brand:str
    category:str
    subcategory:str
    product_type:str
    mrp:float

class ViewFilter(BaseModel):
    brand:str
    category:str
    subcategory:str
    source:str







