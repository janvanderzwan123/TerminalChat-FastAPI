from pydantic import BaseModel

# Response schema
class RoleRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

# Input schema (for creating a new role)
class RoleCreate(BaseModel):
    name: str
