from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "My first own project"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"hello": name}
    print("Hi Lokesh")