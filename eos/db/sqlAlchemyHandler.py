from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from eos import config

"""
How sql transactions are supposed to happen:

engine = create_engine(db_url, convert_unicode=True)
connection = engine.connect()
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=True, bind=engine))
# DO STUFF
db_session.remove()
connection.close()
"""


def session_engine_factory(path):
    if callable(path):
        engine = create_engine("sqlite://", creator=path, echo=config.debug)
    else:
        engine = create_engine(path, echo=config.debug)

    connection = engine.connect()

    session_factory = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
    return {
        'Engine'        : engine,
        'Connnection'   : connection,
        'Session'       : scoped_session(session_factory)(),
        'SessionFactory': session_factory,
    }


def new_session(session_factory):
    return {
        'Session': scoped_session(session_factory)()
    }
