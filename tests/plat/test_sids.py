import random

import pytest
from pydantic.errors import PydanticValueError

from pylangoo.core import sids
from pylangoo.core.sids import sid_factory


def get_random_sid(exclude=None):
    exclude = exclude or []
    slist = [sid_name for sid_name in sids.ALL_SIDS if sid_name not in exclude]
    return getattr(sids, random.sample(slist, 1)[0])


class TestSid:
    def test_create_sids(self):
        FooBarSid = get_random_sid()
        BimBamSid = get_random_sid(exclude=[FooBarSid.__name__])
        a = FooBarSid.random()
        b = BimBamSid.random()
        assert a != b

        assert a == FooBarSid(a)

    def test_all_sids_in_module(self):
        for sid_name, sid_prefix in sids.ALL_SIDS.items():
            assert hasattr(sids, sid_name)
            sid_cls = getattr(sids, sid_name)
            assert sid_cls.PREFIX == sid_prefix
            _ = sid_cls.random()

    def test_bad_creation(self):
        FooBarSid = get_random_sid()
        BimBamSid = get_random_sid(exclude=[FooBarSid.__name__])

        a = FooBarSid.random()

        with pytest.raises(PydanticValueError):
            _ = BimBamSid(a)

        with pytest.raises(PydanticValueError):
            _ = BimBamSid(BimBamSid.random()[:-1])

        with pytest.raises(PydanticValueError):
            _ = BimBamSid("bimbam")

        with pytest.raises(PydanticValueError):
            _ = BimBamSid("Z" * 32)

        with pytest.raises(ValueError):
            _ = sid_factory("MySid", "TOOLONG")

    def test_idempotent(self):
        FooBarSid = get_random_sid()
        a = FooBarSid.random()
        b = a

        for _ in range(10):
            a = FooBarSid(a)

        for _ in range(10):
            a = FooBarSid(str(a))

        assert b == a
