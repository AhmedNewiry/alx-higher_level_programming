#!/usr/bin/python3
""" a script that Changes the name of state
    object from the database
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
    name = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(user,
                                                                   passwd,
                                                                   host, port,
                                                                   db))
    Base.metadata.create_ all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
 
    state = session.query(State).filter(State.id == 2).one_or_none()
    if state:
            state.name = "New Mexico"
            session.commit()
    session.close()