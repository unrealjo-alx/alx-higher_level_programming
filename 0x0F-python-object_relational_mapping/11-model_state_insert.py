#!/usr/bin/python3
"""
Script adds the State object "Louisiana" to the database hbtn_0e_6_usa
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

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
