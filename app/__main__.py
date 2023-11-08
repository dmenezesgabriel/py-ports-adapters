import uvicorn
from src.adapter.driven.infra.database.sqlalchemy.orm import (
    metadata, engine
)
from src.adapter.driven.infra.database.sqlalchemy.models.user import (
    start_mapper
)


if __name__ == "__main__":
    metadata.create_all(engine)
    start_mapper()

    uvicorn.run(
        "src.adapter.driver.api.app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
