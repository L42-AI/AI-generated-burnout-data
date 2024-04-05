from sqlmodel import create_engine, Session, select, SQLModel

from repr import MonologicalData

class SQLWorker:
    def __init__(self):
        self.engine = create_engine("sqlite:///database.db")
        SQLModel.metadata.create_all(self.engine)

    def add(self, data: MonologicalData):
        with Session(self.engine) as session:
            session.add(data)
            session.commit()

    def get(self, prompt: str) -> MonologicalData:
        with Session(self.engine) as session:
            statement = select(MonologicalData).where(MonologicalData.prompt == prompt)
            result = session.exec(statement)
            return result.one()
        
    def get_all(self) -> list[MonologicalData]:
        with Session(self.engine) as session:
            statement = select(MonologicalData)
            result = session.exec(statement)
            return result.all()
        
    def delete(self, data: MonologicalData):
        with Session(self.engine) as session:
            session.delete(data)
            session.commit()
    
    def in_db(self, prompt: str) -> bool:
        with Session(self.engine) as session:
            statement = select(MonologicalData).where(MonologicalData.prompt == prompt)
            result = session.exec(statement)
            return bool(result.one_or_none())