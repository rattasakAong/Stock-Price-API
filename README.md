# 📈 Stock Price API

A FastAPI service to fetch real-time stock prices using Yahoo Finance (`yfinance`).

---

## ✅ Requirements

- Python 3.13.0 (or compatible with 3.10+)
- Dependencies listed in `requirements.txt`

---

## ⚙️ Setup Instructions

### 1. Create a virtual environment

```bash
python3 -m venv venv
```

### 2. Activate the virtual environment

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn main:app --reload
```

---

## 🚀 API Usage

### Example Request

```bash
GET http://localhost:8000/price?ticker=AAPL
```

### Example Response (Success)

```bash
{
    "detail": {
        "code": "0000I",
        "msg": {
            "th": "สำเร็จ",
            "en": "SUCCESS"
        },
        "data": {
            "ticker": "AAPL",
            "price": 190.42,
            "currency": "USD",
            "source": "api"
        }
    }
}
```

