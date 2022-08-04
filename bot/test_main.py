import pytest

from main import load_conf

def test_load_conf():
    config = load_conf()
    assert(config["database_port"] != None)