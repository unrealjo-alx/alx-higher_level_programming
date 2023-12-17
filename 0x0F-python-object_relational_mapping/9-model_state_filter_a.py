#!/usr/bin/python3
"""
    Script lists all State objects that contain the letter 'a'
	from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Main entry point of the script.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{database}",
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(State.name.like("%a%")).order_by(State.id)
    for state in result:
        print("{}: {}".format(state.id, state.name))
    session.close()
