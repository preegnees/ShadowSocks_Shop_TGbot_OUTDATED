import pytest

from client_mongo import get_dbclient

def test_get_dbclient():
    config = {"database_name":"ss-shop", "database_port":"27017", "database_server":"localhost"}
    client = get_dbclient(config=config)
    assert(client != None)
    try:
        client.admin.command("ping")
    except Exception:
        assert(False)
