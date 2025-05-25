from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load marks from JSON file at startup
with open("q-vercel-python.json") as f:
    marks_db = json.load(f)

@app.get("/api")
async def get_marks(name: list[str] = Query(...)):
    # For each requested name, get the marks or 0 if not found
    result = [marks_db.get(n, 0) for n in name]
    return {"marks": result}
