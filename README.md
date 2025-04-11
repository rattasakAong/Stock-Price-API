# Stock-Price-API

Use python 3 version 3.13.0

#create env

python3 -m venv venv

#apply env

source venv/bin/activate

#install dependency

pip install -r requirements.txt

#run server

uvicorn main:app --reload

##Example API Request

GET http://localhost:8000/price?ticker=AAPL

##Example API Response

{
  "ticker": "AAPL",
  "price": 172.24,
  "source": "api"
}
