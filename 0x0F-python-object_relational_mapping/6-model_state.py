#!/usr/bin/python3
"""
starts link class to a table in a database
"""
from sys import argv
from model_state import Base, State


from sqlalchemy import (create_engine)


if __name__ == "__main__":
    arg1 = argv[1], arg2 = argv[2], arg3 = argv[3]
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(arg1, arg2, arg3),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)
