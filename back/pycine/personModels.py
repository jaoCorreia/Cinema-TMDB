from typing import Optional
from pydantic import BaseModel
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator
PyObjectId = Annotated[str, BeforeValidator(str)]
from pydantic import ConfigDict, BaseModel, Field
from bson import ObjectId


class Person(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str
    popularity: Optional[float] = None
    known_for_department: Optional[str] = None
    profile_path: Optional[str] = None
    is_fav: Optional[bool] = False
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
    )

class PersonCollection(BaseModel):
    persons: list[Person]

class PersonResults(BaseModel):
    results: list[Person]
    page: int
    total_pages: int
    total_results: int