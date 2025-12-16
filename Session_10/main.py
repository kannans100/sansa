from fastapi import FastAPI
app = FastAPI(title='Simple Fast API App')
@app.get("/")
def read_root():
    return{"message":"Hello Welcome to my Kannan App"}
@app.get("/check_status")
def check_status():
    return{"Status: OK"}

