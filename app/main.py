from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Tarefa, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tarefas/")
def criar_tarefa(titulo: str, db: Session = Depends(get_db)):
    nova_tarefa = Tarefa(titulo=titulo)
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)
    return nova_tarefa

@app.get("/tarefas/")
def listar_tarefas(db: Session = Depends(get_db)):
    return db.query(Tarefa).all()

@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    if tarefa:
        db.delete(tarefa)
        db.commit()
        return {"mensagem": "Tarefa deletada"}
    return {"erro": "Tarefa não encontrada"}