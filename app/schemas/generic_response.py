from pydantic import BaseModel
from typing import Generic, TypeVar, List, Optional, Union

T = TypeVar('T')

class GenericResponse(BaseModel, Generic[T]):
    success: bool
    message: str
    data: Optional[Union[List[T], T]] = None
    total: Optional[int] = None