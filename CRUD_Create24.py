from fastapi import FastAPI,Depends, HTTPException
from sqlalchemy import create_engine,Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session


app = FastAPI()

# Database URL
DATABASE_URL = "sqlite:///./test.db"

# Engine create (DB connection)
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

# Session (DB operations ke liye)
sessionLocal = sessionmaker(bind=engine)

# Base(model ke liye)
Base = declarative_base()

# Table (Model)
class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(String)

Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create API
@app.post("/todos")
def create_todo(title:str, db: Session = Depends(get_db)):
    # create an object
    todo = Todo(title=title, completed= "False")
    # add into db
    db.add(todo)
    # save into DB
    db.commit()
    # for the latest data fetch file
    db.refresh(todo)
    return{
        "message": "Todo Created",
        "data": todo
    }