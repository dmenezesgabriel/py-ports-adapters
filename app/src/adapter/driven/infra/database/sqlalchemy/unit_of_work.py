from src.core.application.ports.unit_of_work import UnitOfWork


class SQLAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session):
        self.session = session

    def __enter__(self):
        self.session.begin()

    def __exit__(self, type, value, traceback):
        try:
            self.commit()
        except Exception:
            self.rollback()

    def commit(self):
        self.session.flush()
        self.session.commit()
        self.session.close()

    def rollback(self):
        self.session.rollback()
        self.session.close()
