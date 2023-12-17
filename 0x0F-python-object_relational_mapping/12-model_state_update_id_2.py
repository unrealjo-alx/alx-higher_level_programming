#!/usr/bin/python3
"""
Script changes the name of a State object in the database hbtn_0e_6_usa
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

    state_id = 2
    new_name = "New Mexico"

    state = session.query(State).filter(State.id == state_id).first()

    if state:
        state.name = new_name
        session.commit()
        print("State name changed successfully.")
    else:
        print("State not found.")

    session.close()
