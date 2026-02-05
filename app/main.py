import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.database import Base, SessionLocal, engine
from app.models import User
from app.routers import items, users


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    if os.environ.get("SEED_DATA") == "true":
        db = SessionLocal()
        try:
            if not db.scalars(select(User)).first():
                sample_users = [
                    User(name="Alice", email="alice@example.com", age=28),
                    User(name="Bob", email="bob@example.com", age=35),
                ]
                db.add_all(sample_users)
                db.commit()
        except IntegrityError:
            db.rollback()
        finally:
            db.close()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(items.router, prefix="/items", tags=["Items"])


@app.get("/", tags=["General"])
def read_root():
    return {"Hello": "World"}


@app.get("/health", tags=["General"])
def health_check():
    return {"status": "healthy"}
