from fastapi import APIRouter, Response, status, HTTPException, Depends, Query
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_200_OK
from typing import List
from middlewares.jwt_bearer import JWTBearer
from config.database import Session, engine, Base
from services.users import UserService
from schemas.users import User as UserSchema, UserUpdate as UserUpdateSchema
from passlib.hash import sha256_crypt

user_router = APIRouter()

Base.metadata.create_all(bind=engine)

############################################################################
# Obtener todos los registros
############################################################################
@user_router.get(
    path='/users', 
    tags=['users'], 
    status_code=status.HTTP_200_OK,
    response_model=List[UserSchema],
    dependencies=[Depends(JWTBearer())]
  )
def get_users() -> List[UserSchema]:
  db = Session()
  result = UserService(db).get_users()
  if not result:
      raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontraron usuarios'})
  return result

############################################################################
# Obtener un registro en base al ID
############################################################################
@user_router.get(
    path='/users/{id}', 
    tags=['users'], 
    status_code=status.HTTP_200_OK,
    response_model=UserSchema,
    dependencies=[Depends(JWTBearer())]
  )
def get_user(id: int) -> UserSchema:
  db = Session()
  result = UserService(db).get_user(id)
  if not result:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró el usuario'})
  return result

############################################################################
# Insertar un registro
############################################################################
@user_router.post(
    path='/users', 
    tags=['users'], 
    status_code=status.HTTP_200_OK,
    response_model=UserSchema,
    dependencies=[Depends(JWTBearer())]
  )
def create_user(user: UserSchema) -> UserSchema:
  if user.id:
    user.id = None
    
  password = sha256_crypt.hash(user.password)
  user.password = password
  db = Session()
  new_user = UserService(db).create_user(user)
  return new_user

############################################################################
# Actualizar un registro
############################################################################
@user_router.put(
    path='/users/{id}', 
    tags=['users'], 
    status_code=status.HTTP_200_OK,
    response_model=UserSchema,
    dependencies=[Depends(JWTBearer())]
  )
def update_user(id: int, user_update: UserUpdateSchema) -> UserSchema:
  db = Session()
  user = UserService(db).get_user(id)
  if not user:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró el usuario'})
  
  if user_update.password:
    password = sha256_crypt.hash(user_update.password)
    user_update.password = password
  
  result = UserService(db).update_user(user, user_update)

  return result

############################################################################
# Borrar un registro
############################################################################
@user_router.delete(
    path='/users/{id}', 
    tags=['users'], 
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(JWTBearer())]
  )
def delete_user(id: int):
  db = Session()
  user = UserService(db).get_user(id)
  if not user:
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail={'message': 'No se encontró el usuario'})
  
  UserService(db).delete_user(user)

  return Response(status_code=HTTP_204_NO_CONTENT)