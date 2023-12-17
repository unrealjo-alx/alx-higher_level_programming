#!/usr/bin/python3
"""
Script prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    """
    Main entry point of the script.
    """
    if len(sys.argv) != 5:
        exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{database}",
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    session = Session(engine)

    result = session.query(State).filter(State.name == state_name).first()

    if result:
        print(result.id)
    else:
        print("Not found")

    session.close()
