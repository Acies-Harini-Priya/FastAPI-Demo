import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv('.env')
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(router=interns_info_router)
    
if __name__ == "__main__":
    import uvicorn
    from dotenv import load_dotenv
    import os

    # Load environment variables
    load_dotenv(dotenv_path=f"{os.getcwd()}\\dev\\envs\\.env")

    uvicorn.run("__main__:app", host="0.0.0.0", port=int(os.getenv('API_PORT')), reload=True)

