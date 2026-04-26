from fastapi import FastAPI
import uvicorn

app = FastAPI(title="AKIMBOT - Serveur Arbitre")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Le Serveur Arbitre AKIMBOT est prêt !"}

if __name__ == "__main__":
    uvicorn.run("server.serveur_arbitre:app", host="0.0.0.0", port=8000, reload=True)