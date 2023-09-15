from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import createHtml
app = FastAPI()

origins = ['http://localhost:3000', 'https://localhost:3000','*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/image/")
async def getImg():
    html,data = createHtml.html_to_text()
    a = {"html":html,"full_address":data}
    return a

@app.get("/")
async def root():
    return {"message": "Hello World"}

