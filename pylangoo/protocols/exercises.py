from typing import List

from pydantic import BaseModel


class Exercise(BaseModel):
    # Identification
    id: int
    certification_id: int
    certification_level_id: int
    competence_id: int
    # Flag
    visible: bool
    is_open_question: bool  # if the exercise is an open question or a multiple-choice
    level_test: int = 0  # if any, does it belong to a competence test ?
    # Body
    task_type: int
    order: int
    statement: str
    content: str  # -> HTML
    audience: str  # TODO (move to enum) -> types of audiences ?
    registre: str  # TODO (move to enum) -> types of registres ?
    # Particular
    # writting
    min_words: int
    max_words: int
    production_type: str  # TODO (move to enum)
    # listening
    file: List[str]
    ## validator -> competence_id + task_type + order has to be unique


class Question(BaseModel):
    # Identification
    id: int
    exercise_id: int
    # Body
    order: int
    content: str

    ## validator -> exercise_id + order has to be unique


class Solution(BaseModel):
    # Identification
    id: int
    question_id: int
    exercise_id: int
    # Body
    order: int
    content: str  # path to image or answer
    type: str  # TODO (Rober): -> Which types can we have ? (move to Enum)
    #
    option_correct: bool = None  # -> TODO (Rober): -> Why boolean ?
    fill_correct: str = None  # -> If option is to fill a space, which is the solution
    #
