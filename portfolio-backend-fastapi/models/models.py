from datetime import datetime, UTC

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP

metadata = MetaData()

video_files = Table(
    "video_files",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("created_at", TIMESTAMP, default=datetime.now(UTC))
)
