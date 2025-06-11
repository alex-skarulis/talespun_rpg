from pydantic import BaseModel, Field
from typing import Optional, List, Dict

class AttributeSet(BaseModel):
    strength: int = 10
    dexterity: int = 10
    constitution: int = 10
    intelligence: int = 10
    wisdom: int = 10
    charisma: int = 10

class Character(BaseModel):
    player_name: str
    character_name: str
    character_class: str
    ancestry: str
    attributes: AttributeSet
    key_attribute: Optional[str]
    secondary_attributes: List[str] = []