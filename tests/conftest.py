import pytest

from lib.db_conn import DatabaseConnection


@pytest.fixture
def db_connection():
    conn = DatabaseConnection()
    conn.connect()
    return conn
