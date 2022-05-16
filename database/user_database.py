from database.main_db import User, Session, engine

local_session = Session(bind=engine)


def create_new_user(username, email):
    new_user = User(username=username, email=email)
    local_session.add(new_user)
    local_session.commit()
