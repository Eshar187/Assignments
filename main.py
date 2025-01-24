from fastapi import FastAPI
from routes import project,task,user
from database import engine
import models


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
def root():
    return {'message':'Hello World'}

app.include_router(project.project_route)

app.include_router(task.task_route)

app.include_router(user.user_route)