from fastapi import FastAPI

app = FastAPI(
    title="API TCC DevOps",
    version="1.0.0")

@app.get("/")
def home ():
    return {"mensagem": "API do TCC funcionando"}
    
@app.get("/health")
def health():
    return {"status": "ok"}
    
@app.get("/versao")
def versao():
    return {"versao": "1.0.0"}
    
@app.get("/info")
def info():
    return {"projeto": "TCC MBA USP ESALQ",
            "tema": "Implementacao de Pipeline DevOps",
            "autor": "Guilherme Soares dos Santos"}
            
@app.get("/status")
def status():
    return {"API": "Online",
            "Ambiente": "Desenvolvimento"}