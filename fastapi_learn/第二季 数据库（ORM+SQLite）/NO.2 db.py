from pydantic import BaseModel
from fastapi import Depends, FastAPI, HTTPException

import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import Boolean, Column, Integer, String

pymysql.install_as_MySQLdb()
SQLALCHEMY_DATABASE_URL = 'mysql://root:@127.0.0.1/pysqltest'

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class M_User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50))
    hashed_password = Column(String(50))
    is_active = Column(Boolean, default=True)


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
        print("数据库已关闭")


def get_user(db: Session, user_id: int):
    CCCCC = db.query(M_User).filter(M_User.id == user_id).first()
    print('CCCCC : ', CCCCC)
    return CCCCC


def db_create_user(db: Session, user: UserCreate):
    password = user.password + "_fake"
    db_user = M_User(email=user.email, hashed_password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return db_create_user(db=db, user=user)


@ app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    print(db_user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User Not found")
    return db_user


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
