from pydantic import BaseModel # jak przekazywane dane maja wygladac
from typing import Optional

# WALIDACJA
class Author(BaseModel):
    id: Optional[int] = None # Pole opcjonalne
    first_name: str # pole obowiazkowe
    last_name: str # pole obowiazkowe
