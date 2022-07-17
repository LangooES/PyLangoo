from pylangoo.clients.base_http_client import BaseHTTPClient, HTTPClientException


class XanoAPIException(HTTPClientException):
    pass


class AccountsClient(BaseHTTPClient):

    BASE_URI = "https://x8ki-letl-twmt.n7.xano.io/api:ACPYJZHj"
    PROFILES_URI = f"{BASE_URI}/profile"
    USERS_URI = f"{BASE_URI}/user"
    STUDENTS_URI = f"{BASE_URI}/student"
    TEACHERS_URI = f"{BASE_URI}/student"
    ORGANIZATIONS_URI = f"{BASE_URI}/organization"

    def __init__(self, host=BASE_URI, port=80):
        super().__init__(host, port)


class CertificationsClient(BaseHTTPClient):

    BASE_URI = "https://x8ki-letl-twmt.n7.xano.io/api:qxYWdwtk"
    LANGUAGES_URI = f"{BASE_URI}/language"
    CERTIFICATIONS_URI = f"{BASE_URI}/certification"
    CERTIFICATION_LEVELS_URI = f"{BASE_URI}/certification_level"
    COMPETENCE_URI = f"{BASE_URI}/competence"

    def __init__(self, host=BASE_URI, port=80):
        super().__init__(host, port)

    class Languages:
        @staticmethod
        def list():
            """Admin API - Get list of languages"""
            url = CertificationsClient.LANGUAGES_URI
            return CertificationsClient().do_request(
                method="GET",
                url=url,
                operation_name="list-languages",
            )

        @staticmethod
        def create(name: str):
            """Admin API - Create language"""
            url = CertificationsClient.LANGUAGES_URI
            params = {"name": name}
            return CertificationsClient().do_request(
                method="POST",
                url=url,
                operation_name="create-language",
                params=params,
            )

        @staticmethod
        def get(language_id: int):
            """Admin API - Get language by id"""
            url = CertificationsClient.LANGUAGES_URI + f"/{language_id}"
            return CertificationsClient().do_request(
                method="GET",
                url=url,
                operation_name="get-language",
            )

    class Certifications:
        @staticmethod
        def list():
            """Admin API - Get list of certifications"""
            url = CertificationsClient.CERTIFICATIONS_URI
            return CertificationsClient().do_request(
                method="GET",
                url=url,
                operation_name="list-certifications",
            )

        def create(name: str, language_id: int):
            """Admin API - Create certification"""
            url = CertificationsClient.CERTIFICATIONS_URI
            params = {"name": name, "language_id": language_id}
            return CertificationsClient().do_request(
                method="POST",
                url=url,
                operation_name="create-certification",
                params=params,
            )

        def get(
            certification_id: int,
        ):
            """Admin API - Get certification by id"""
            url = CertificationsClient.CERTIFICATIONS_URI + f"/{certification_id}"
            return CertificationsClient().do_request(
                method="GET",
                url=url,
                operation_name="get-certification",
            )

    class CertificationLevels:
        @staticmethod
        def list():
            """Admin API - Get list of certification_levels"""
            url = CertificationsClient.CERTIFICATION_LEVELS_URI
            return CertificationsClient().do_request(
                method="GET",
                url=url,
                operation_name="list-certification_levels",
            )

        @staticmethod
        def create(
            name: str,
            certification_id: int,
        ):
            """Admin API - Create certification_level"""
            url = CertificationsClient.CERTIFICATION_LEVELS_URI
            params = {"name": name, "certification_id": certification_id}
            return CertificationsClient().do_request(
                method="POST",
                url=url,
                operation_name="create-certification_level",
                params=params,
            )

        @staticmethod
        def get(
            certification_level_id: int,
        ):
            """Admin API - Get certification_level by id"""
            url = (
                CertificationsClient.CERTIFICATION_LEVELS_URI
                + f"/{certification_level_id}"
            )
            return CertificationsClient().do_request(
                method="GET",
                url=url,
                operation_name="get-certification_level",
            )

    class Competences:
        @staticmethod
        def list():
            """Admin API - Get list of competences"""
            url = CertificationsClient.COMPETENCE_URI
            return CertificationsClient().do_request(
                method="GET",
                url=url,
                operation_name="list-competences",
            )

        @staticmethod
        def create(name: str):
            """Admin API - Create certification_competence"""
            url = CertificationsClient.COMPETENCE_URI
            params = {"name": name}
            return CertificationsClient().do_request(
                method="POST",
                url=url,
                operation_name="create-certification_competence",
                params=params,
            )

        @staticmethod
        def get(
            competence_id: int,
        ):
            """Admin API - Get competence_id by id"""
            url = CertificationsClient.COMPETENCE_URI + f"/{competence_id}"
            return CertificationsClient().do_request(
                method="GET",
                url=url,
                operation_name="get-competence",
            )
