#!/usr/bin/python3
""" a script that deletes all states their
    name contains the letter 'a'
"""

import sys
from model_state import State, Base
from model_city import City
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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
 
    results = session.query(State, City).join(City, State.id == City.state_id).order_by(City.id)
    for result in results:
        print ("{}: ({}) {}".format(result.State.name, result.City.id, result.City.name))
    session.close()
