from fastapi.responses import JSONResponse
from fastapi import FastAPI, status
from routes import user
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app = FastAPI()

app.include_router(user.router, prefix='/user')

@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    return JSONResponse(content={"message": "Hello Bigger Applications!"},
                        status_code=status.HTTP_200_OK)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)