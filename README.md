# Store Sales Data API

## 📌 Project Overview

This is a modular Flask application that connects to a MySQL database and performs basic CRUD operations on store sales data. It supports both GET and POST endpoints and returns query results in JSON, list, and pandas DataFrame formats.

---

## 🚀 Features

- Modular Flask architecture
- MySQL database integration
- REST API with:
  - `GET /sales` — filter data by date range
  - `POST /sales` — insert new sales record
- Data returned as:
  - JSON dictionary
  - List
  - Pandas DataFrame

---

## 🧰 Technologies Used

- Python 3.10
- Flask
- MySQL
- MySQL Connector
- Pandas

---

## 🗃️ Database Setup

**Database:** `StoreData`  
**Table:** `Sales`

```sql
CREATE TABLE IF NOT EXISTS Sales (
  id INT PRIMARY KEY,
  store_id VARCHAR(10),
  total_sales DECIMAL(10,2),
  date DATE
);
```

---

## 🔌 API Usage

### ✅ GET `/sales`

**Parameters:**  
`start_date`, `end_date` (format: YYYY-MM-DD)

**Example:**
```
GET /sales?start_date=2023-01-01&end_date=2023-01-31
```

**Returns:**
```json
{
  "json": [...],
  "list": [...],
  "dataframe": [...]
}
```

---

### ✅ POST `/sales`

**Payload:**
```json
{
  "id": 1001,
  "store_id": "TX001",
  "total_sales": 150.75,
  "date": "2023-01-20"
}
```

**Response:**
```json
{ "message": "New sale record added successfully" }
```

---

## 📦 Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/your-username/store-sales-data-api.git
cd store-sales-data-api
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
python app.py
```

---

## 📧 Contact

For questions or project review, contact:  
**imelendez@cbac.com**

---

