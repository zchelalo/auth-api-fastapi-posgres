from models.users import User as UserModel
from schemas.users import User as UserSchema

class UserService():
  def __init__(self, db) -> None:
    self.db = db

  def get_users(self):
    result = self.db.query(UserModel).all()
    return result
  
  def get_user(self, id):
    result = self.db.query(UserModel).where(UserModel.id == id).one_or_none()
    return result
  
  def get_user_by_email(self, email):
    result = self.db.query(UserModel).where(UserModel.email == email).one_or_none()
    return result
  
  def create_user(self, user: UserSchema):
    new_user = UserModel(**user.model_dump())
    self.db.add(new_user)
    self.db.commit()
    self.db.refresh(new_user)
    return new_user
  
  def update_user(self, user: UserSchema, user_update: UserSchema):
    for field, value in user_update.model_dump(exclude_unset=True).items():
      setattr(user, field, value)

    self.db.commit()
    self.db.refresh(user)
    return user
  
  def delete_user(self, user):
    self.db.delete(user)
    self.db.commit()
    return