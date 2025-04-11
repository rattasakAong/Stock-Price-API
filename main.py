from fastapi import FastAPI, HTTPException, Query
from cachetools import TTLCache
import yfinance as yf

app = FastAPI()
cache = TTLCache(maxsize=100, ttl=60)

def transform_success_response(ticker: str, price_with_currency: dict[str, float | str], source: str) -> dict:
    return {
        "detail": {
            "code": "0000I",
            "msg": {
                "th": "สำเร็จ",
                "en": "SUCCESS"
            },
            "data": {
                "ticker": ticker,
                "price": price_with_currency["price"],
                "currency": price_with_currency["currency"],
                "source": source
            }
        }
    }

def transform_not_found_response(ticker: str) -> dict:
    return {
        "code": "2008E",
        "msg": {
            "th": f"ไม่พบข้อมูลสำหรับ {ticker}",
            "en": f"Data not found for {ticker}."
        }
    }

def transform_exception_response(error_msg: str) -> dict:
    return {
        "code": "5000E",
        "msg": {
            "th": f"{error_msg}",
            "en": f"{error_msg}"
        }
    }

@app.get("/price")
def get_price(ticker: str = Query(..., description="รหัสหุ้น เช่น AAPL")):
    old_ticker = ticker
    ticker = ticker.upper()

    if ticker in cache:
        return transform_success_response(old_ticker, cache[ticker], "cache")

    try:
        stock = yf.Ticker(ticker)

        try:
            info = stock.info
        except:
            info = None

        if not isinstance(info, dict) or ("regularMarketPrice" not in info or "currency" not in info):
            raise HTTPException(status_code=404, detail=transform_not_found_response(old_ticker))

        price = info["regularMarketPrice"]
        currency = info["currency"]
        price_with_currency = {
            "price": price,
            "currency": currency
        }
        cache[ticker] = price_with_currency
        return transform_success_response(old_ticker, price_with_currency, "api")

    except HTTPException as http_err:
        raise http_err

    except Exception as e:
        raise HTTPException(status_code=500, detail=transform_exception_response(str(e)))
