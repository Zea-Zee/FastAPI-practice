from typing import Annotated, Optional
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from contextlib import asynccontextmanager
from database import create_tables, drop_tables
from schemas import TaskAdd
import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    await create_tables()
    print('Create tables')
    yield
    print('Turning off')


app = FastAPI(lifespan=lifespan)
app.include_router(router.router)
