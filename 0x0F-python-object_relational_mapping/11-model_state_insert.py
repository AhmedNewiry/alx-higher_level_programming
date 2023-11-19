#!/usr/bin/python3
""" a script that adds the state object 
    'Louisiana' to the database
"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    host = 'localhost'
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(user,
                                                                   passwd,
                                                                   host, port,
                                                                   db))
    Base.metadata.create_ all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    louisiana = State(name="Louisiana")
    session.commit()
    state = session.add(louisiana)
    get_louisiana = session.query(State).filter(State.name == "Louisiana").one_or_none()
    if get_louisiana:
        print(get_louisiana.id)
    session.close()