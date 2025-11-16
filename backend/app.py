from fastapi import FastAPI

# Crée l'application (ton QG)
app = FastAPI()

@app.get("/")
def read_root():
    """
    Ceci est l'endpoint racine de ton QG.
    Il sert juste à vérifier que le serveur est démarré.
    """
    return {"Message": "Bienvenue sur le QG (Backend) du Dashboard Média-Scan"}