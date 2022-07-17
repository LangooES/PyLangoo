from pylangoo.clients.xano import CertificationsClient
from pylangoo.protocols.certifications import Certification as CertProto
from pylangoo.protocols.certifications import CertificationLevel as CertLevelProto
from pylangoo.protocols.certifications import Competence as CompetenceProto
from pylangoo.protocols.certifications import Language as LangProto
from pylangoo.protocols.constants import (
    CERTIFICATION_LEVELS,
    CERTIFICATION_COMPETENCES,
    Language,
    LANGUAGE_CERTIFICATIONS,
)


def extract_field_values(ls: list[dict], key: str):
    """Given a key, return the list of values from a list of dicts."""
    return [l[key] for l in ls]


def get_id_from_name(ls: list[dict], name: str):
    "Return the id of a given list of dicts searching for the name."
    for l in ls:
        if l["name"] == name:
            return l["id"]
    raise ValueError(f"Not found {name} in {ls}")


def create_language_if_not_exist(language_name):
    """Creates a language if it doesn't exists in db."""
    db_languages = client.Languages.list()
    db_languages_names = extract_field_values(db_languages, "name")
    if language_name in db_languages_names:
        print("Language already registered: ", language_name)
        return client.Languages.get(
            language_id=get_id_from_name(db_languages, language_name)
        )
    print("Creating language: ", language_name)
    return client.Languages.create(name=language_name)


def create_certification_if_not_exists(cert_name: str):
    """Creates a certification if it doesn't exists in db."""
    db_certs = client.Certifications.list()
    db_certs_names = extract_field_values(db_certs, "name")
    if cert_name in db_certs_names:
        print("Certification already registered: ", cert_name)
        return client.Certifications.get(
            certification_id=get_id_from_name(db_certs, cert_name)
        )
    print("Creating certification: ", cert_name)
    return client.Certifications.create(name=cert_name)


def create_cert_level_if_not_exists(certification_id: int, level: str):
    db_certlevels = client.CertificationLevels.list()

    any = False
    for db_cert_level in db_certlevels:
        if (db_cert_level["certification_id"] == certification_id) and (
            db_cert_level["name"] == level
        ):
            any = True
            cert_name = db_cert_level["certification_id"]
            cert_level_id = db_cert_level["id"]
            break

    if not any:
        print(f"Creating certification-level: {certification.value}-{level}")
        return client.CertificationLevels.create(
            name=cert_level,
            certification_id="cet_id",
        )
    print(f"Certification-level already registered: {cert_name}-{level}")
    return client.CertificationLevels.get(
        certification_level_id=cert_level_id,
    )


def create_competence_if_not_exists(name: str):
    db_competences = client.Competences.list()

    db_competences_names = extract_field_values(db_competences, "name")
    if name in db_competences_names:
        print("Competence already registered: ", name)
        return client.Competences.get(
            competence_id=get_id_from_name(db_competences, name)
        )
    print("Creating competecence: ", name)
    return client.Competences.create(name=name)


client = CertificationsClient()


for language in Language:

    print()
    print("Creating Languages")
    print()
    # Create language if it doesn't exist
    db_lang = LangProto(**create_language_if_not_exist(language.value))

    for certification in LANGUAGE_CERTIFICATIONS[language]:

        print()
        print("Creating Certifications")
        print()
        # Create certification if it doesn't exist
        db_cert = CertProto(**create_certification_if_not_exists(certification.value))

        for cert_level in CERTIFICATION_LEVELS[certification]:

            print()
            print("Creating Levels")
            print()
            # Create certification-level for given certification if it doesn't exist
            db_cert_level = CertLevelProto(
                **create_cert_level_if_not_exists(
                    certification_id=db_cert.id,
                    level=cert_level,
                )
            )

            for compentece in CERTIFICATION_COMPETENCES[certification]:
                print()
                print("Creating Competence")
                print()
                # Create competences for a given certification if they don't exists
                db_cert_competence = CompetenceProto(
                    **create_competence_if_not_exists(name=compentece)
                )


print("Done")
