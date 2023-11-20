#!/usr/bin/python3
"""
Lists all state obojects using sqlalchemy
"""


from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    user_name = argv[1]
    password = argv[2]
    data_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(user_name, password, data_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = session(bind=engine)
    session = Session()

    new_state = State(name='California')
    new_city = City(name='San Francisco', state=new_state)
    new_state.cities.append(new_city)

    session.add(new_state)
    session.add(new_city)
    session.commit()
