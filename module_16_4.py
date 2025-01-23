from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import List, Annotated

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users")
def get_users():
    return users


@app.post("/user/{username}/{age}")
def create_user(
    username: Annotated[str, Path(
        title="Enter Username", description="Имя пользователя", min_length=5, max_length=20, example="UrbanUser"
    )],
    age: Annotated[int, Path(
        title="Enter Age", description="Возраст пользователя", ge=18, le=120, example=24
    )]
):

    user_id = users[-1].id + 1 if users else 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}")
def update_user(
    user_id: Annotated[int, Path(title="Enter User ID", description="ID пользователя", ge=1, example=1)],
    username: Annotated[str, Path(
        title="Enter Username", description="Имя пользователя", min_length=5, max_length=20, example="UrbanProfi"
    )],
    age: Annotated[int, Path(
        title="Enter Age", description="Возраст пользователя", ge=18, le=120, example=28
    )]
):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
def delete_user(
    user_id: Annotated[int, Path(title="Enter User ID", description="ID пользователя", ge=1, example=1)]
):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")

