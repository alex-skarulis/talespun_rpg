from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from talespun.data_loader import get_ancestry_by_name

class ModifierChange(BaseModel):
    source: str
    reason: Optional[str] = None
    delta: int = 0

class AbilityModifier(BaseModel):
    base: int = 0
    changes: List[ModifierChange] = []

    @property
    def total(self) -> int:
        return self.base + sum(change.delta for change in self.changes)

    def apply(self, delta: int, source: str, reason: Optional[str] = None):
        self.changes.append(ModifierChange(source=source, reason=reason, delta=delta))

class AbilityScores(BaseModel):
    STR: AbilityModifier = Field(default_factory=AbilityModifier)
    DEX: AbilityModifier = Field(default_factory=AbilityModifier)
    CON: AbilityModifier = Field(default_factory=AbilityModifier)
    INT: AbilityModifier = Field(default_factory=AbilityModifier)
    WIS: AbilityModifier = Field(default_factory=AbilityModifier)
    CHA: AbilityModifier = Field(default_factory=AbilityModifier)

    def adjust_modifier(self, ability: str, delta: int, source: str, reason: Optional[str] = None):
        getattr(self, ability.upper()).apply(delta=delta, source=source, reason=reason)

    def summary(self) -> Dict[str, int]:
        return {stat: getattr(self, stat).total for stat in self.__fields__}

class Character(BaseModel):
    player_name: str
    character_name: str
    character_class: str
    ancestry: str
    key_attribute: Optional[str] = None
    ability_scores: AbilityScores = Field(default_factory=AbilityScores)
    ancestry_applied: bool = False

    def apply_ancestry(self):
        ancestry_data = get_ancestry_by_name(self.ancestry)
        source = f"Ancestry ({self.ancestry})"
        for mod in ancestry_data.get("ability_modifiers", []):
            delta = mod["value"]
            if mod["type"] == "fixed":
                self.ability_scores.adjust_modifier(mod["options"], delta, source=source)
            elif mod["type"] == "choice":
                options = mod["options"]
                # For now, just pick the first option (later: prompt user or CLI)
                chosen = options[0]
                self.ability_scores.adjust_modifier(chosen, delta, source=source + " (choice)")

        self.ancestry_applied = True

    def print_ability_summary(self):
        print("Ability Modifier Summary:")
        for stat, value in self.ability_scores.summary().items():
            print(f"  {stat}: {value}")
