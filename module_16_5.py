from fastapi import FastAPI, HTTPException, Path, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Annotated

app = FastAPI()

templates = Jinja2Templates(directory="templates")

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/", response_class=HTMLResponse)
def home_page(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users, "user": None})


@app.get("/user/{user_id}", response_class=HTMLResponse)
def get_user_by_id(request: Request, user_id: Annotated[int, Path(title="Enter User ID", ge=1)]):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user, "users": None})
    raise HTTPException(status_code=404, detail="User was not found")


@app.post("/user/{username}/{age}")
def create_user(
    username: Annotated[str, Path(
        title="Enter Username",
        description="Имя пользователя",
        min_length=5, max_length=20,
        examples={"example_username": {"summary": "Example username", "value": "UrbanUser"}}
    )],
    age: Annotated[int, Path(
        title="Enter Age",
        description="Возраст пользователя", 
        ge=18, le=120,
        examples={"example_age": {"summary": "Example age", "value": 24}}
    )]
):
    user_id = users[-1].id + 1 if users else 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user

