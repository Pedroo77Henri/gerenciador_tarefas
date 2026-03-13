from pydantic import BaseModel

class TarefaCreate(BaseModel):
    titulo: str

class TarefaResponse(BaseModel):
    id: int
    titulo: str
    concluida: bool

    class Config:
        orm_mode = True