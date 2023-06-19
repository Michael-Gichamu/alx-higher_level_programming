#!/usr/bin/python3
"""
Prints all city Objects from database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from model_city import City
from enum import unique

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

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state_name = city.state.name
        city_id = city.id
        city_name = city.name
        print("{}: ({}) {}".format(state_name, city_id, city_name))

    session.close()
