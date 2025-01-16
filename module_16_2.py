from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/user/{user_id}")
def get_user_by_id(user_id: Annotated[int, Path(
    title="Enter User ID",
    description="User ID должен быть целым числом от 1 до 100.",
    ge=1, le=100,
    example=1
)]):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{username}/{age}")
def get_user_info(
    username: Annotated[str, Path(
        title="Enter Username",
        description="Имя пользователя должно содержать от 5 до 20 символов.",
        min_length=5, max_length=20,
        example="UrbanUser"
    )],
    age: Annotated[int, Path(
        title="Enter Age",
        description="Возраст должен быть целым числом от 18 до 120.",
        ge=18, le=120,
        example=24
    )]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
