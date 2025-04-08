# server.py
from fastapi import FastAPI, HTTPException, Request
from server.models.Item import Item
from server.models.suppliers import suppliers
from server.models.Order import Order
import json
import os

from pydantic import BaseModel
from typing import Optional, List


app = FastAPI()
JSON_FILE = "orders.json"
SUPPLIERS_FILE = "suppliers.json"
ITEMS_FILE = "items.json"
############################## ORDERS ###########################
class OrderPydantic(BaseModel):
    supplier_id: int
    item: str
    status: str
    
# JSON file helpers
def read_orders():
    if not os.path.exists(JSON_FILE):
        return []
    with open(JSON_FILE, "r") as f:
        return json.load(f)

def write_orders(orders):
    with open(JSON_FILE, "w") as f:
        json.dump(orders, f, indent=4)

# # gets the next order id
# def get_next_order_id(orders):
#     if not orders:
#         return 1
#     last_id = orders[-1] #max(order["id"] for order in orders)
#     return last_id + 1

# Routes
#gets all the orders from the DB
@app.get("/orders")
def get_orders():
    return read_orders()

#gets an order and adds it to the DB
@app.post("/orders")
async def add_order(order: OrderPydantic):
    try:
        new_order = Order(
            supplier_id=order.supplier_id,
            item=order.item,
            status=order.status
        )

        item, status = new_order.add_order()
        return {"message": "order saved", "item": item}, status

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



#gets a supplier id and returns all the orders that have that supplier id
@app.get("/orders/bySupplier/{supplier_id}")
def get_orders_by_supplier(supplier_id: int):
    orders = read_orders()
    filtered_orders = [order for order in orders if order["supplier_id"] == supplier_id]
    return filtered_orders

#updats an orders status to delivered
@app.put("/orders/{order_id}/deliver")
def mark_delivered(order_id: int):
    orders = read_orders()
    updated = False
    for order in orders:
        if int(order["id"]) == order_id:
            order["status"] = "delivered"
            updated = True
            break

    if not updated:
        raise HTTPException(status_code=404, detail="Order not found")

    write_orders(orders)
    return {"message": "Order marked as delivered"}

#updats an orders status to inProgress
@app.put("/orders/{order_id}/inProgress")
def mark_inProgress(order_id: int):
    try: 
        orders = read_orders()
        for order in orders:
            if int(order["id"]) == order_id:
                order["status"] = "in Progress"
                break
        write_orders(orders)
        return {"message": "Order marked as inprogress"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    

########################### SUPPLIERS ###########################


class SupplierPydantic(BaseModel):
    password: str
    name: str
    phone: str
    person: str
    items: Optional[List[str]] = [] 

def read_suppliers():
    if not os.path.exists(SUPPLIERS_FILE):
        return []
    with open(SUPPLIERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def write_suppliers(suppliers_list):
    with open(SUPPLIERS_FILE, "w", encoding="utf-8") as f:
        json.dump(suppliers_list, f, indent=4)

#gets all the suppliers from the DB
@app.get("/suppliers")
def get_suppliers():
    return read_suppliers()

#gets a supplier and adds it to the DB
@app.post("/suppliers")
async def add_supplier_endpoint(supplier_data: SupplierPydantic):
    try:
        # Create the supplier object using your class
        new_supplier = suppliers(
            password=supplier_data.password,
            name=supplier_data.name,
            phone=supplier_data.phone,
            person=supplier_data.person,
            items=supplier_data.items
        )

        name, id, status = new_supplier.add_supplier()
        return {"message": "Supplier saved", "name": name, "supplier_id":id}, status

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
class LoginData(BaseModel):
    username: str
    password: str

@app.post("/suppliers/login")
async def login_supplier(login_data: LoginData):
    try:
        suppliers_list = read_suppliers()
        for supplier in suppliers_list:
            if supplier["name"] == login_data.username and supplier["password"] == login_data.password:
                return {"message": "Login successful", "supplier_id": supplier["id"], "status": 200}
        return {"message": "Invalid credentials", "status": 401}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

################### ITEMS ###########################
class ItemPydantic(BaseModel):
    name: str
    price: float
    minamount: int
    supplier_id: int

def read_items():
    if not os.path.exists(ITEMS_FILE):
        return []
    with open("items.json", "r") as f:
        return json.load(f)
    
#gets all the items from the DB
@app.get("/items")
def get_items():
    return read_items()

def write_items(items):
    with open(ITEMS_FILE, "w") as f:
        json.dump(items, f, indent=4)

#gets an item and adds it to the DB
@app.post("/items")
async def add_item(item: ItemPydantic):
    try:
        name= item.name
        price= item.price
        minamount= item.minamount
        supplier_id= item.supplier_id

        new_item = Item(name, price, minamount, supplier_id)
        id, name, status = new_item.add_item()
        return {"message": "Item saved", "item_id": id, "name": name, "status":status}, 200
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

