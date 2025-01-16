from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def main_page():
    return JSONResponse(content={"message": "Главная страница"}, media_type="application/json; charset=utf-8")

@app.get("/user/admin")
def admin_page():
    return JSONResponse(content={"message": "Вы вошли как администратор"}, media_type="application/json; charset=utf-8")

@app.get("/user/{user_id}")
def user_page(user_id: int):
    return JSONResponse(content={"message": f"Вы вошли как пользователь № {user_id}"}, media_type="application/json; charset=utf-8")

@app.get("/user")
def user_info(username: str, age: int):
    return JSONResponse(content={"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}, media_type="application/json; charset=utf-8")