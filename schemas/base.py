from typing import Annotated

from pydantic import BaseModel, Field

ID = Annotated[int, Field(gt=0)]


class Base(BaseModel):
    id: ID
