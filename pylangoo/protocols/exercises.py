from pydantic import BaseModel


class Exercise(BaseModel):
    id: int
    competence_id: int
    certification_id: int
    certification_level_id: int
    task: int
