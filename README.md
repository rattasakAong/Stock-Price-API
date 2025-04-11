# Stock-Price-API

Use python 3 version 3.13.0

#1. create env

python3 -m venv venv

#2. apply env

source venv/bin/activate

#3. install dependency

pip install -r requirements.txt

#4. run server

uvicorn main:app --reload

##Example API Request

GET http://localhost:8000/price?ticker=AAPL

##Example API Response

{
  "ticker": "AAPL",
  "price": 172.24,
  "source": "api"
}
