from pydantic import BaseModel
from typing import Optional

class TarefaCreate(BaseModel):
    titulo: str

class TarefaUpdate(BaseModel):
    titulo: Optional[str] = None
    concluida: Optional[bool] = None

class TarefaResponse(BaseModel):
    id: int
    titulo: str
    concluida: bool

    class Config:
        from_attributes = True  # era orm_mode no Pydantic v1