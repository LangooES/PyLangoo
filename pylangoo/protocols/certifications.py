from typing import Literal

from pydantic import BaseModel


class Language(BaseModel):
    id: int
    name: Literal["english", "spanish"]


class Certification(BaseModel):
    id: int
    language_id: int
    name: Literal["cambridge", "dele"]


class CertificationLevel(BaseModel):
    id: int
    certification_id: str
    name: str


class Competence(BaseModel):
    id: int
    name: Literal["reading", "writing", "speaking", "listening"]
