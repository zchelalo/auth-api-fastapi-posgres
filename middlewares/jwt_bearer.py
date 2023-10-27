from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from starlette.status import HTTP_401_UNAUTHORIZED
from utils.jwt_manager import validate_token
from services.users import UserService
from config.database import Session

class JWTBearer(HTTPBearer):
  async def __call__(self, request: Request):
    auth = await super().__call__(request)
    data = validate_token(auth.credentials)

    db = Session()
    result = UserService(db).get_user_by_email(data['email'])

    if not result:
      raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail={'message': 'Credenciales incorrectas'})