from pydantic import BaseModel # type: ignore

class User(BaseModel):
    id: int
    name: str
    is_active: bool


input_data = {
    "id": 101,
    "name": "chaicode",
    "is_active": "True"
}

user = User(**input_data)
print(user)
print("input_data::",input_data)
print("expansion:: ", {**input_data})