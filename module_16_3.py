from fastapi import FastAPI


app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
def get_users():
    return users


@app.post('/user/{username}/{age}')
def create_user(username: str, age: int):
    user_id = str(max(map(int, users.keys()), default=0) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
def update_user(user_id: str, username: str, age: int):
    if user_id not in users:
        raise f'User {user_id} not found'
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} has been updated'


@app.delete('/user/{user_id}')
def delete_user(user_id: str):
    if user_id not in users:
        raise f'User {user_id} not found'
    del users[user_id]
    return f'User {user_id} has been deleted'

