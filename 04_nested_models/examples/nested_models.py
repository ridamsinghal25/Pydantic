from pydantic import BaseModel #type: ignore
from typing import List, Optional


class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address



class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List["Comment"]] = None # also known as forward referencing

Comment.model_rebuild() # important


address = Address(
    street= "123 something",
    city = "Saharanpur",
    postal_code = "243244",
)

user = User(
    id = 1,
    name = "Ridam",
    address=address
)

comment = Comment(
    id=1,
    content= "Hello",
    replies = [
        Comment(
            id = 2,
            content = "reply 1",
        ),
        Comment(
            id = 3,
            content = "reply 2",
        )
    ]
)