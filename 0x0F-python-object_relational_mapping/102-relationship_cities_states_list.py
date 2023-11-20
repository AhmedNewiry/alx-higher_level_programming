#!/usr/bin/python3
"""   script that lists all City objects from the database
"""

import sys
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine, create_all
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
    results = session.query(State, City).join(State.cities).order_by(City.id).all()
    for result in results:
        print("{}: {} -> {}".format(result.City.id, result.City.name, result.State.name))
    session.close()
