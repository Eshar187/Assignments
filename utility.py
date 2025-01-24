# from typing import List
# from sqlalchemy import and_
# from fastapi import APIRouter, status ,HTTPException ,Depends
# from database import *
# import models, schema


# def check_user_task_limit(user_id: int, db):
#     active_tasks = db.query(models.Task).filter(and_(models.Task.assigned_to == user_id, models.Task.status != "Completed")).count()
#     if active_tasks >= 5:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User cannot be assigned more than 5 active tasks.")

# def check_project_completion(project_id: int, db):
#     incomplete_tasks = db.query(models.Task).filter(and_(models.Task.project_id == project_id, models.Task.status != "Completed")).count()
#     if incomplete_tasks == 0:
#         project = db.query(models.Project).filter(models.Project.id == project_id).first()
#         if project:
#             project.status = "Completed"
#             db.commit()