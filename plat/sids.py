import uuid

from pydantic import constr

# A repo that maps all sid_name => sid_prefix
ALL_SIDS = {}


def sid_factory(sid_name, prefix=None):
    """
    Create a new Sid class.

    Args:
        sid_name (str): Name of the Sid to create
        prefix (str): Prefix of the Sid to create. Will raise a ValueError if
            the prefix is passed in and is not of length 2. If not passed in,
            will create a "prefix-less" sid, i.e., one that can be constructed
            from any sid.

    Returns:
        type: Returns a new type / class defining the new Sid.

    """
    if prefix and len(prefix) != 2:
        raise ValueError("Prefixes must be of length 2")
    sid_requirement = constr(regex="^" + (prefix or "[A-Z]{2}") + "[a-fA-F0-9]{32}$")

    class BaseSid(sid_requirement):

        PREFIX = None

        def __init__(self, value):
            self.validate(value)
            super().__init__()

        @classmethod
        def looks_like(cls, sid):
            try:
                return str(sid) == str(cls(sid))
            except Exception:
                return False

        @classmethod
        def random(cls):
            """Create a random Sid object"""
            if not cls.PREFIX:
                raise TypeError("Cannot create random sid without a prefix.")
            return cls(f"{cls.PREFIX}{uuid.uuid4().hex}")

    sid_type = type(sid_name, (BaseSid,), {"PREFIX": prefix})
    if prefix:
        ALL_SIDS.update({sid_name: prefix})
    return sid_type


def _create(name, prefix):
    """Pass through to the sid_factory to be able to also add to ALL_SIDS."""
    if prefix:
        ALL_SIDS.update({name: prefix})
    return sid_factory(name, prefix)


# How to construct Sids
AnySid = sid_factory("AnySid")
