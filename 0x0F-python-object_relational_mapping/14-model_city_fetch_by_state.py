#!/usr/bin/python3
"""
Script fetches and prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    """
    Main entry point of the script.
    """
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{database}",
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    session = Session(engine)

    results = (
        session.query(State.name, City.id, City.name)
        .join(City, City.state_id == State.id)
        .order_by(City.id)
    )

    for state_name, city_id, city_name in results:
        print(f"{state_name}: ({city_id}) {city_name}")

    session.close()
