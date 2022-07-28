from pylangoo.clients.xano import CertificationsClient
from pylangoo.protocols.certifications import (
    Certification,
    CertificationLevel,
    Competence,
    Language,
)
from pylangoo.protocols.constants import (
    CERTIFICATION_LEVELS,
    CERTIFICATION_COMPETENCES,
    COMPETENECES_DISPLAY_NAME,
    LANGUAGE_CERTIFICATIONS,
)
from pylangoo.protocols.constants import Language as LanguageEnum


def extract_field_values(ls: list[dict], key: str):
    """Given a key, return the list of values from a list of dicts."""
    return [l[key] for l in ls]


def get_id_from_name(ls: list[dict], name: str):
    "Return the id of a given list of dicts searching for the name."
    for l in ls:
        if l["name"] == name:
            return l["id"]
    raise ValueError(f"Not found {name} in {ls}")


def create_language_if_not_exist(language_name) -> Language:
    """Creates a language if it doesn't exists in db."""
    db_languages = client.Languages.list()
    db_languages_names = extract_field_values(db_languages, "name")
    if language_name in db_languages_names:
        print("Language already exist: ")
        return Language(
            **client.Languages.get(
                language_id=get_id_from_name(db_languages, language_name)
            )
        )
    new_lang = client.Languages.create(name=language_name)
    print("===> Created")
    return Language(**new_lang)


def create_certification_if_not_exists(
    language_id: int, cert_name: str
) -> Certification:
    """Creates a certification if it doesn't exists in db."""
    db_certs = client.Certifications.list()
    db_certs_names = extract_field_values(db_certs, "name")
    if cert_name in db_certs_names:
        print("===> Certification already exists")
        return Certification(
            **client.Certifications.get(
                certification_id=get_id_from_name(db_certs, cert_name)
            )
        )
    new_cert = client.Certifications.create(language_id=language_id, name=cert_name)
    print("===> Created")
    return Certification(**new_cert)


def create_cert_level_if_not_exists(
    language_id: int, certification_id: int, name: str
) -> CertificationLevel:
    db_certlevels = client.CertificationLevels.list()

    any = False
    for db_cert_level in db_certlevels:
        if (db_cert_level["certification_id"] == certification_id) and (
            db_cert_level["name"] == name
        ):
            any = True
            cert_level_id = db_cert_level["id"]
            break

    if not any:
        new_cert_level = client.CertificationLevels.create(
            language_id=language_id,
            certification_id=certification_id,
            name=cert_level,
        )
        print("===> Created")
        return CertificationLevel(**new_cert_level)

    print("===> Certification-level already exists")
    return CertificationLevel(
        **client.CertificationLevels.get(
            certification_level_id=cert_level_id,
        )
    )


def create_competence_if_not_exists(
    language_id: int,
    certification_id: int,
    certification_level_id: int,
    name: str,
    display_name: str,
):
    db_competences = client.Competences.list()

    any = False
    for db_competence in db_competences:
        if (db_competence["certification_level_id"] == certification_level_id) and (
            db_competence["name"] == name
        ):
            any = True
            competence_id = db_competence["id"]
            break

    if not any:
        new_competence = client.Competences.create(
            language_id=language_id,
            certification_id=certification_id,
            certification_level_id=certification_level_id,
            name=name,
            display_name=display_name,
        )
        print("===> Created")
        return CertificationLevel(**new_competence)

    print("===> Competecence already exists")
    new_competence = client.Competences.get(competence_id=competence_id)
    return Competence(**new_competence)


client = CertificationsClient()


for language in LanguageEnum:

    print()
    print(f"Creating Language {language}")
    print()
    # Create language if it doesn't exist
    db_lang = create_language_if_not_exist(language.value)

    for certification in LANGUAGE_CERTIFICATIONS[language]:

        print()
        print(f"Creating Certification: {certification}")
        print()
        # Create certification if it doesn't exist
        db_cert = create_certification_if_not_exists(
            language_id=db_lang.id, cert_name=certification.value
        )

        for cert_level in CERTIFICATION_LEVELS[certification]:

            print()
            print(f"Creating Level {db_cert.name}-{cert_level}")
            print()
            # Create certification-level for given certification if it doesn't exist
            db_cert_level = create_cert_level_if_not_exists(
                language_id=db_lang.id,
                certification_id=db_cert.id,
                name=cert_level,
            )

            for compentece in CERTIFICATION_COMPETENCES[certification]:
                print()
                print(
                    "Creating Competence "
                    f"{db_cert.name}-{db_cert_level.name}-{compentece}"
                )
                print()
                # Create competences for a given certification if they don't exists
                db_cert_competence = create_competence_if_not_exists(
                    language_id=db_lang.id,
                    certification_id=db_cert.id,
                    certification_level_id=db_cert_level.id,
                    name=compentece,
                    display_name=COMPETENECES_DISPLAY_NAME[certification][compentece],
                )


print("Done")
