from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "home": "status_code=200","cycle_life": "closed"
    }

@app.post("/cadastro")
def cadastro():
    pessoa = {
        "nome": "Natan","idade": 24,"altura": 1.75
    }
    return {f"pessoa1": {pessoa}}