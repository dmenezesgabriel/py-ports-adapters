import uvicorn
from src.adapter.driven.infra.database.sqlalchemy.db import create_db_and_tables
from src.adapter.driven.infra.database.sqlalchemy.models.user import user

if __name__ == "__main__":
    create_db_and_tables()

    uvicorn.run(
        "src.adapter.driver.api.app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
