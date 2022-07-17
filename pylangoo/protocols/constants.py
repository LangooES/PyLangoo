from pylangoo.core.enum import ExtendedEnum


class Language(ExtendedEnum):
    ENGLISH = "english"
    SPANISH = "spanish"


class Certification(ExtendedEnum):
    CAMBRIDGE = "cambridge"
    DELE = "dele"


class Competence(ExtendedEnum):
    READING = "reading"
    WRITING = "writing"
    SPEAKING = "speaking"
    LISTENING = "listening"


LANGUAGE_CERTIFICATIONS = {
    Language.ENGLISH: [Certification.CAMBRIDGE],
    Language.SPANISH: [Certification.DELE],
}


CERTIFICATION_LEVELS = {
    Certification.CAMBRIDGE: ["A1", "A2", "B1", "B2", "C1", "C2"],
    Certification.DELE: ["A1", "A2", "B1", "B2", "C1", "C2"],
}


COMMON_COMPENTENCES = [
    Competence.READING.value,
    Competence.WRITING.value,
    Competence.SPEAKING.value,
    Competence.LISTENING.value,
]

CERTIFICATION_COMPETENCES = {
    Certification.CAMBRIDGE: COMMON_COMPENTENCES,
    Certification.DELE: COMMON_COMPENTENCES,
}


# How many tasks are there for every competence-level
COMPETENCE_LEVEL_TYPES = {
    Competence.READING: {"any-level": 7},
    Competence.WRITING: {"any-level": 2},
    Competence.SPEAKING: {"any-level": 4},
    Competence.LISTENING: {"any-level": 5},
}
