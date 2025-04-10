from app import models, note
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from dotenv import load_dotenv
import os
import requests

models.Base.metadata.create_all(bind=engine)

load_dotenv()

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(note.router, tags=['Notes'], prefix='/api/notes')


@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI with SQLAlchemy"}

@app.get("/posts/{post_id}")
async def get_post(post_id: int):
    try:
        #Make a GET request to the JSONPlaceholder API
        response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
        #Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail="API call failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    

@app.get('/crypto-price-ethereum2')
async def get_crypto_price():
    try:
        api_key = os.getenv("api_key")
        if not api_key:
            raise HTTPException(status_code=500, detail="API key not configured")

        url = (
            "https://api.coingecko.com/api/v3/simple/token_price/ethereum"
            "?contract_addresses=0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"
            f"&vs_currencies=usd&x_cg_demo_api_key={api_key}"
        )
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail="API call failed")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    

@app.get('/crypto-price-ethereum')
async def get_crypto_price():
    try:
        #Make a GET request to the API
        response = requests.get(f"https://api.coingecko.com/api/v3/simple/token_price/ethereum?contract_addresses=0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48&vs_currencies=usd&x_cg_demo_api_key=CG-2DiDAMj5CMnutZkqo3r1jxBJ")
        #Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail="API call failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    




    # url = "https://api.coingecko.com/api/v3/simple/token_price/ethereum?contract_addresses=0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48&vs_currencies=usd&x_cg_demo_api_key=CG-2DiDAMj5CMnutZkqo3r1jxBJ"
    
    # params = {
    #     "contract_addresses": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
    #     "vs_currencies": "usd",
    #     "x_cg_demo_api_key": "CG-2DiDAMj5CMnutZkqo3r1jxBJ"  # <- Move it here
    # }
    
    # try:
    #     response = requests.get(url, params=params, timeout=10)  # <- No headers needed
    #     response.raise_for_status()
    #     data = response.json()
    #     return JSONResponse(content={"status": "success", "data": data})
    # except requests.exceptions.RequestException as e:
    #     raise HTTPException(
    #         status_code=500,
    #         detail=f"Error fetching crypto price: {str(e)}. URL: {url}"
    #     )