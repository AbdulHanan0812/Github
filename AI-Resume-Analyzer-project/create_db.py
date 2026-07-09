from app.db import Base, engine
from app.models import Report, User  


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")
