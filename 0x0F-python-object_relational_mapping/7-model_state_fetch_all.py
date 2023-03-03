#!/usr/bin/python3
""" a script that lists all State objects
    from the database hbtn_0e_6_usa
"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("""mysql+mysqldb://{}:{}@localhost/
                              {}""".formtat(sys.argv[1],
                                            sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id)
    for state in states:
        print(state[0]: state[1])
