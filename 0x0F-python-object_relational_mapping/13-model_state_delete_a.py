#!/usr/bin/python3
"""
Script deletes all State objects with a name
containing the letter 'a' from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    """
    Main entry point of the script.
    """
    if len(sys.argv) != 4:
        exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{database}",
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    session = Session(engine)

    results = session.query(State).filter(State.name.like("%a%")).all()

    if results:
        for state in results:
            session.delete(state)
        session.commit()

    session.close()
