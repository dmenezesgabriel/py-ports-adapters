from sqlalchemy import create_engine
from sqlalchemy.orm import registry


mapper_registry = registry()
Base = mapper_registry.generate_base()


engine = create_engine(
            'sqlite:///./app.db',
            echo=True,
            connect_args={"check_same_thread": False}
        )
