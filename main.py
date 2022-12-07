import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()
HOST = os.environ.get('DOMAIN')
PORT = int(os.environ.get('PORT'))

app = FastAPI(
    title="Web OpenShift",
    version="1.0.0"
)

@app.get("/", tags=['Root'])
async def root() -> dict:
    """ Test API Endpoint """
    return {
        "message": "Web OpenShift"
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=HOST,
        port=PORT,
        log_level="info",
        reload=True
    )