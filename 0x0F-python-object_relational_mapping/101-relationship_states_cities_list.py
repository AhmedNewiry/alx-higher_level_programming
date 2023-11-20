#!/usr/bin/python3
"""   lists all State objects, and corresponding City objects,
"""

import sys
from relationship_state import State, Base
from relationship_city import City
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
    results = session.query(
        State,
        City).join(
        State.cities).order_by(
            State.id).all()
    for result in results:
        print("{}: {}".format(result.State.id, result.State.name))
        for city in result.State.cities:
            print("   {}: {}".format(city.id, city.name))

    session.close()
