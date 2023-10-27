from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
  id: Optional[int] = None
  name: Optional[str] = None
  email: str = Field(min_length=1, max_length=100)
  password: str = Field(min_length=1, max_length=150)

  model_config = {
    "json_schema_extra" : {
      "example": {
          "id": 1,
          "name": "Panchito",
          "email": "panchito@email.com",
          "password": "Panchito_1928"
      }
    }
  }