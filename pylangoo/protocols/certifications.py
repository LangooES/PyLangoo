from typing import Literal, Optional

from pydantic import BaseModel


class Language(BaseModel):
    id: Optional[int]
    name: Literal["english", "spanish"]


class Certification(BaseModel):
    id: Optional[int]
    language_id: int
    name: Literal["cambridge", "dele"]


class CertificationLevel(BaseModel):
    id: Optional[int]
    language_id: int
    certification_id: int
    name: str


class Competence(BaseModel):
    id: Optional[int]
    language_id: int
    certification_id: int
    certification_level_id: int
    name: Literal["reading", "writing", "speaking", "listening"]
    display_name: str
