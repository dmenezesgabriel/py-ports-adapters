import uvicorn
from src.adapter.driven.infra.database.sqlalchemy.orm import (
    engine, Base
)
from src.adapter.driven.infra.database.sqlalchemy.models import user


if __name__ == "__main__":
    Base.metadata.create_all(engine)

    uvicorn.run(
        "src.adapter.driver.api.app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
