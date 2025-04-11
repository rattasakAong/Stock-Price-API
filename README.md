# Stock-Price-API

Use python3 version 3.13.0

#1. Create env

python3 -m venv venv

#2. Apply env

source venv/bin/activate

#3. Install dependency

pip install -r requirements.txt

#4. Run server

uvicorn main:app --reload

##Example API Request

GET http://localhost:8000/price?ticker=AAPL

##Example API Response


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
            "source": "cache"
        }
    }
}
