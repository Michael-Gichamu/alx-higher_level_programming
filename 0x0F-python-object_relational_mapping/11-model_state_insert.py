#!/usr/bin/python3
"""
Adds State object "Louisiana" to the database hbtn_0e_6_usa
Usage: ./11-model_state_insert.py <mysql username> \
                                  <mysql password> \
                                  <mysql database name> \
"""

import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}",
        pool_pre_ping=True
        )

    Session = sessionmaker(bind=engine)
    session = Session()

    louisiana = State(name="Louisiana")

    session.add(louisiana)
    session.commit()

    print(louisiana.id)
