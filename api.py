from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Dummy data for 100 students, example:
marks_db = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 78,
    # ... add up to 100
}

@app.get("/api")
async def get_marks(name: list[str] = Query(...)):
    result = [marks_db.get(n, 0) for n in name]
    return {"marks": result}
