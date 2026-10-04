from fastapi import FastAPI, Depends, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .models import Shop, Medicine
from .schemas import (
    ShopCreate,
    ShopResponse,
    MedicineCreate,
    MedicineResponse
)

import os
import tempfile

from .services.medicine_scanner import scan_medicine


# =====================================
# FASTAPI APP
# =====================================

app = FastAPI(
    title="MediCare Pharma API",
    version="1.0.0"
)


# =====================================
# ADMIN FOLDER
# =====================================

app.mount(
    "/admin",
    StaticFiles(
        directory="admin",
        html=True
    ),
    name="admin"
)


# =====================================
# DATABASE
# =====================================

Base.metadata.create_all(bind=engine)


# =====================================
# CORS
# =====================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =====================================
# HOME
# =====================================

@app.get("/")
def home():
    return {
        "message": "MediCare Pharma API is running"
    }


# =====================================
# USER PAGE
# =====================================

@app.get("/user")
def user_page():
    return FileResponse("user/index.html")


# =====================================
# PHARMACY PAGE
# =====================================

@app.get("/pharmacy")
def pharmacy_page():
    return FileResponse("pharmacy/index.html")


# =====================================
# CREATE PHARMACY
# =====================================

@app.post(
    "/api/shops",
    response_model=ShopResponse
)
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


# =====================================
# GET ALL PHARMACIES
# =====================================

@app.get(
    "/api/shops",
    response_model=list[ShopResponse]
)
def get_shops(
    db: Session = Depends(get_db)
):

    return db.query(Shop).all()


# =====================================
# GET ONE PHARMACY
# =====================================

@app.get(
    "/api/shops/{shop_id}",
    response_model=ShopResponse
)
def get_shop(
    shop_id: int,
    db: Session = Depends(get_db)
):

    shop = db.query(Shop).filter(
        Shop.id == shop_id
    ).first()

    if not shop:
        return {
            "error": "Pharmacy not found"
        }

    return shop


# =====================================
# DELETE PHARMACY
# =====================================

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
            "error": "Pharmacy not found"
        }

    db.delete(shop)
    db.commit()

    return {
        "message": "Pharmacy deleted successfully"
    }


# =====================================
# ADD MEDICINE
# =====================================

@app.post(
    "/api/medicines",
    response_model=MedicineResponse
)
def add_medicine(
    medicine: MedicineCreate,
    db: Session = Depends(get_db)
):

    shop = db.query(Shop).filter(
        Shop.id == medicine.shop_id
    ).first()

    if not shop:
        return {
            "error": "Pharmacy not found"
        }

    new_medicine = Medicine(
        shop_id=medicine.shop_id,
        name=medicine.name,
        generic_name=medicine.generic_name,
        strength=medicine.strength,
        price=medicine.price,
        stock=medicine.stock
    )

    db.add(new_medicine)
    db.commit()
    db.refresh(new_medicine)

    return new_medicine


# =====================================
# GET PHARMACY MEDICINES
# =====================================

@app.get(
    "/api/medicines/shop/{shop_id}",
    response_model=list[MedicineResponse]
)
def get_shop_medicines(
    shop_id: int,
    db: Session = Depends(get_db)
):

    return db.query(Medicine).filter(
        Medicine.shop_id == shop_id
    ).all()


# =====================================
# DELETE MEDICINE
# =====================================

@app.delete("/api/medicines/{medicine_id}")
def delete_medicine(
    medicine_id: int,
    db: Session = Depends(get_db)
):

    medicine = db.query(Medicine).filter(
        Medicine.id == medicine_id
    ).first()

    if not medicine:
        return {
            "error": "Medicine not found"
        }

    db.delete(medicine)
    db.commit()

    return {
        "message": "Medicine deleted successfully"
    }


# =====================================
# MEDICINE SCANNER
# =====================================

@app.post("/api/medicines/scan")
async def scan_medicine_api(
    file: UploadFile = File(...)
):

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