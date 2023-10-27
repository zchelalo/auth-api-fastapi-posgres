from fastapi import APIRouter, HTTPException, status
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
from utils.jwt_manager import create_token
from schemas.users import User as UserSchema
from services.users import UserService
from config.database import Session
from passlib.hash import sha256_crypt

auth_router = APIRouter()

@auth_router.post(
  path='/login',
  status_code=status.HTTP_200_OK,
  tags=['auth']
)
def login(user: UserSchema) -> dict:
  email = user.email
  password = user.password

  db = Session()
  result = UserService(db).get_user_by_email(email)

  if not result:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró el usuario'})

  if sha256_crypt.verify(password, result.password):
    token: str = create_token(user.model_dump())
    return {'token': token}
  else:
    raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail={'message': 'Credenciales incorrectas'})