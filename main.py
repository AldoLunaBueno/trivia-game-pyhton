from fastapi import FastAPI
import databases

DATABASE_URL = "postgresql://user:123@db:5432/triviadb"

db = databases.Database(DATABASE_URL)
app = FastAPI()

@app.on_event("startup")
async def startup():
    await db.connect()
    print("Conected to postgresql")


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()
    print("Disconnected from postgresql")

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}
