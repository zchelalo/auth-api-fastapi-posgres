from pydantic import BaseModel, Field, constr
from typing import Optional

class User(BaseModel):
  id: Optional[int] = None
  name: str = Field(min_length=1, max_length=100)
  email: str = Field(min_length=1, max_length=100)
  password: str = Field(min_length=1, max_length=150)

  model_config = {
    "json_schema_extra" : {
      "example": {
          "name": "Panchito",
          "email": "panchito@email.com",
          "password": "Panchito_1928"
      }
    }
  }

class UserAuth(BaseModel):
  email: str = Field(min_length=1, max_length=100)
  password: str = Field(min_length=1, max_length=150)

  model_config = {
    "json_schema_extra" : {
      "example": {
          "email": "panchito@email.com",
          "password": "Panchito_1928"
      }
    }
  }

class UserUpdate(BaseModel):
  name: Optional[constr(min_length=1, max_length=100)] = None
  email: Optional[constr(min_length=1, max_length=100)] = None
  password: Optional[constr(min_length=1, max_length=150)] = None

  model_config = {
    "json_schema_extra" : {
      "example": {
          "name": "Panchito",
          "email": "panchito@email.com",
          "password": "Panchito_1928"
      }
    }
  }