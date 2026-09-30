from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .models import Shop
from .schemas import ShopCreate, ShopResponse
import os
import tempfile

from fastapi import UploadFile, File

from .services.medicine_scanner import scan_medicine


# Create database tables
Base.metadata.create_all(bind=engine)


# Create FastAPI application
app = FastAPI(
    title="Shop Location API",
    version="1.0.0"
)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# user
@app.get("/user")
def user_page():
    return FileResponse("user/index.html")
#pharma
@app.get("/pharmacy")
def pharmacy_page():
    return FileResponse("pharmacy/index.html")

# Home
@app.get("/")
def home():
    return {
        "message": "Shop Location API is running"
    }


# Admin page
@app.get("/admin")
def admin_page():
    return FileResponse("admin/index.html")

#scanner
@app.post("/api/medicines/scan")
async def scan_medicine_api(
    file: UploadFile = File(...)
):

    # Create temporary file
    suffix = os.path.splitext(
        file.filename
    )[1] or ".jpg"

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix
    ) as temp:

        temp.write(
            await file.read()
        )

        temp_path = temp.name


    try:

        # Scan image
        text = scan_medicine(
            temp_path
        )

        return {
            "success": True,
            "text": text
        }

    finally:

        if os.path.exists(temp_path):

            os.remove(temp_path)


# Create shop
@app.post("/api/shops", response_model=ShopResponse)
def create_shop(
    shop: ShopCreate,
    db: Session = Depends(get_db)
):

    new_shop = Shop(
        name=shop.name,
        owner=shop.owner,
        category=shop.category,
        phone=shop.phone,
        address=shop.address,
        latitude=shop.latitude,
        longitude=shop.longitude
    )

    db.add(new_shop)
    db.commit()
    db.refresh(new_shop)

    return new_shop


# Get all shops
@app.get("/api/shops", response_model=list[ShopResponse])
def get_shops(
    db: Session = Depends(get_db)
):

    return db.query(Shop).all()


# Get one shop
@app.get("/api/shops/{shop_id}", response_model=ShopResponse)
def get_shop(
    shop_id: int,
    db: Session = Depends(get_db)
):

    shop = db.query(Shop).filter(
        Shop.id == shop_id
    ).first()

    if not shop:
        return {
            "error": "Shop not found"
        }

    return shop


# Delete shop
@app.delete("/api/shops/{shop_id}")
def delete_shop(
    shop_id: int,
    db: Session = Depends(get_db)
):

    shop = db.query(Shop).filter(
        Shop.id == shop_id
    ).first()

    if not shop:
        return {
            "error": "Shop not found"
        }

    db.delete(shop)
    db.commit()

    return {
        "message": "Shop deleted successfully"
    }