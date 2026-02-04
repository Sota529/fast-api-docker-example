from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database import Base, SessionLocal, engine, get_db
from app.models import User
from app.schemas import UserCreate, UserResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables on startup
    Base.metadata.create_all(bind=engine)
    
    # Add sample data if the table is empty
    db = SessionLocal()
    try:
        if db.query(User).count() == 0:
            sample_users = [
                User(name="山田太郎", email="yamada@example.com", age=30),
                User(name="佐藤花子", email="sato@example.com", age=25),
                User(name="鈴木一郎", email="suzuki@example.com", age=35),
            ]
            db.add_all(sample_users)
            db.commit()
    finally:
        db.close()
    
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    """Get all users from database using ORM"""
    users = db.query(User).all()
    return users


@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """Get a specific user by ID"""
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """Create a new user"""
    db_user = User(**user.model_dump())
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409, detail="User with this email already exists"
        )
    return db_user

