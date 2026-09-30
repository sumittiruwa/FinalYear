# 💊 MediCare Pharma

**MediCare Pharma** is a smart pharmacy and medicine availability platform that helps users **identify medicines, find nearby pharmacies, check medicine availability, compare information, and locate pharmacies on an interactive map**.

The system connects users with nearby pharmacies and allows pharmacy owners to manage their medicines and stock through a dedicated dashboard.

---

## 🚀 Main Features

### 👤 User

* Scan medicine using camera/image
* Detect medicine name using **OpenCV + OCR**
* Search medicines
* Find nearby pharmacies
* View pharmacies on an interactive map
* Calculate distance from the user
* View pharmacy details
* View available medicines
* Check medicine price and stock
* View generic medicine information
* Find alternative medicines
* Reserve/request medicine

### 🏥 Pharmacy

Pharmacy owners can:

* Manage pharmacy profile
* Add pharmacy location
* Add medicines
* Update medicine price
* Update stock quantity
* Set medicine availability
* View their medicine inventory
* Scan medicine packages
* Manage medicine information

### 👨‍💼 Admin

Admin can:

* Manage pharmacies
* View pharmacy locations
* Manage users
* Manage medicines
* Monitor pharmacy information
* Manage system data

---

# 🧠 Medicine Scanning

The system provides an image-based medicine scanning feature.

```text
📷 Medicine Image
       ↓
   OpenCV
       ↓
 Image Processing
       ↓
      OCR
       ↓
 Medicine Name
       ↓
 Medicine Database
       ↓
 Medicine Information
```

The scanner can process an image of a medicine package and extract text from it.

---

# 🗺️ Pharmacy Location System

Pharmacies store:

* Pharmacy name
* Owner
* Phone
* Address
* Latitude
* Longitude

Users can see pharmacies on the map.

```text
              USER
                │
                ↓
        Get User Location
                │
                ↓
       Find Nearby Pharmacies
                │
                ↓
        Display on Map
                │
                ↓
       Calculate Distance
                │
                ↓
       Pharmacy Information
```

---

# 🏗️ System Architecture

```text
                         MediCare Pharma
                                │
             ┌──────────────────┼──────────────────┐
             │                  │                  │
           USER              PHARMACY            ADMIN
             │                  │                  │
       Scan Medicine      Manage Medicines    Manage System
       Search Medicine    Manage Stock        Manage Pharmacy
       Find Pharmacy      Update Price         Manage Users
       View Map           Pharmacy Location    Monitor Data
             │                  │                  │
             └──────────────────┼──────────────────┘
                                │
                           REST API
                                │
                           FastAPI
                                │
                           Database
```

---

# 🛠️ Technology Stack

## Frontend

* **HTML5**
* **CSS3**
* **JavaScript**
* **React.js** *(planned/optional for advanced frontend)*
* **Bootstrap / Tailwind CSS** *(UI styling where required)*

## Backend

* **Python**
* **FastAPI**
* **Uvicorn**
* **REST API**

## Database

* **PostgreSQL** / **MySQL**
* **SQLAlchemy ORM**

## AI / Image Processing

* **OpenCV**
* **Tesseract OCR**
* **Python**
* **Pillow**

## Maps & Location

* **Map API**
* **JavaScript Maps**
* **Geolocation API**
* Latitude & Longitude
* Distance calculation

## Development Tools

* **VS Code**
* **Git**
* **GitHub**
* **Postman**
* **Python Virtual Environment**

---

# 📁 Project Structure

```text
MediCare-Pharma/
│
├── app/
│   │
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   │
│   ├── routes/
│   │   ├── shops.py
│   │   ├── medicines.py
│   │   ├── users.py
│   │   └── admin.py
│   │
│   └── services/
│       └── medicine_scanner.py
│
├── pharmacy/
│   └── index.html
│
├── admin/
│   └── index.html
│
├── user/
│   └── index.html
│
├── uploads/
│
├── requirements.txt
│
├── .env
│
└── README.md
```

---

# 🔌 Important APIs

### Pharmacy

```text
POST /api/shops
GET  /api/shops
GET  /api/shops/{id}
```

### Medicines

```text
POST /api/medicines
GET  /api/medicines
GET  /api/medicines/pharmacy/{pharmacy_id}
```

### Medicine Scanner

```text
POST /api/medicines/scan
```

### User

```text
GET /api/nearby-pharmacies
GET /api/medicines/search
```

---

# 📦 Installation

Clone the project:

```bash
git clone <your-github-repository>
```

Go to the project:

```bash
cd MediCare-Pharma
```

Create virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Backend

Start FastAPI:

```bash
python -m uvicorn app.main:app --reload
```

Backend will run at:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

Pharmacy dashboard:

```text
http://127.0.0.1:8000/pharmacy
```

---

# 📷 Medicine Scanner Setup

Install required packages:

```bash
pip install opencv-python
pip install pytesseract
pip install pillow
pip install python-multipart
```

The scanner uses:

```text
OpenCV → Image Processing
Tesseract → Text Recognition
FastAPI → Scanner API
```

---

# 🔐 Security

The final system can include:

* User authentication
* Pharmacy authentication
* Admin authentication
* Password hashing
* JWT authentication
* Role-based access control
* API validation
* Environment variables for secrets
* Secure database access

---

# 📊 Example Pharmacy Data

```json
{
    "name": "ABC Pharmacy",
    "owner": "Sumit",
    "category": "Pharmacy",
    "phone": "9800000000",
    "address": "New Baneshwor, Kathmandu",
    "latitude": 27.6915,
    "longitude": 85.3420
}
```

---

# 💊 Example Medicine Data

```json
{
    "name": "Paracetamol 500mg",
    "generic_name": "Paracetamol",
    "category": "Pain Relief",
    "price": 25,
    "quantity": 100,
    "available": true,
    "description": "Used for pain and fever."
}
```

---

# 🎯 Project Goal

The main goal of **MediCare Pharma** is to make it easier for users to find medicines when they need them.

Instead of visiting multiple pharmacies manually, a user can:

```text
Scan Medicine
      ↓
Identify Medicine
      ↓
Find Nearby Pharmacies
      ↓
Check Availability
      ↓
Check Price
      ↓
View Distance
      ↓
Contact / Reserve Medicine
```

---

# 🔮 Future Scope

Future versions can include:

* AI-based medicine recognition
* Better OCR accuracy
* Prescription OCR
* Drug interaction warnings
* Medicine alternative recommendations
* Medicine price comparison
* Online medicine reservation
* Pharmacy-to-user notifications
* Real-time inventory updates
* Delivery integration
* Payment integration
* Advanced recommendation system
* Mobile application
* AI medical assistant

---

# 👨‍💻 Development Status

### Completed

* FastAPI backend setup
* Pharmacy/shop model
* Pharmacy location storage
* Map integration foundation
* Admin pharmacy management
* Pharmacy dashboard
* Medicine management
* Medicine stock management
* OpenCV/OCR scanner foundation

### In Progress

* Medicine recognition improvement
* Medicine database matching
* Nearby pharmacy search
* Distance calculation
* User medicine search

### Planned

* Authentication
* Prescription scanning
* Alternative medicine recommendation
* Reservation system
* Real-time inventory
* AI-based features

---

# 📜 License

This project is developed for **academic/final-year project purposes**.

---

# 👨‍💻 Author

**Sumit Tiruwa**

BCA Final Year Project

**MediCare Pharma — Smart Medicine & Pharmacy Finder**
