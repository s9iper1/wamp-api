from main_db import User, engine, Base

Base.metadata.create_all(engine)
