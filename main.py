from dotenv import load_dotenv
import os
import json
from fastapi import FastAPI
from fastapi import APIRouter
from fastapi.responses import FileResponse, RedirectResponse

from database import Outlet

load_dotenv()
MAPS_API_KEY = os.getenv("MAPS_API_KEY")

app = FastAPI()
api = APIRouter(prefix="/api")

@app.get("/")
def index():
    return FileResponse("index.html")

@api.get("/outlets")
def list_outlet():
    outlets = []
    rows = Outlet.select().dicts()
    for row in rows:
        row['operating_hours'] = json.loads(row['operating_hours'])
        outlets.append(row)
    return outlets

@api.get("/google/maps")
def google_maps():
    return RedirectResponse(f"https://maps.googleapis.com/maps/api/js?key={MAPS_API_KEY}")

app.include_router(api)