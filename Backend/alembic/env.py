import asyncio
import os
from logging.config import fileConfig
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import pool
from alembic import context
from models import Base  # Import your models
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read the DATABASE_URL from the .env file
DATABASE_URL = os.getenv("DATABASE_URL")

# Convert async URL to sync URL for Alembic
SYNC_DATABASE_URL = DATABASE_URL.replace("asyncpg", "psycopg2")

# Alembic Config object
config = context.config
config.set_main_option("sqlalchemy.url", SYNC_DATABASE_URL)

# Configure logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata for autogenerate support
target_metadata = Base.metadata

def run_migrations_offline():
    """Run migrations in offline mode."""
    context.configure(
        url=SYNC_DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

async def do_migrations():
    """Perform migrations asynchronously."""
    connectable = create_async_engine(DATABASE_URL, poolclass=pool.NullPool)

    async with connectable.connect() as connection:
        await connection.run_sync(sync_migrations)

def sync_migrations(connection):
    """Synchronous migration execution."""
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in online mode."""
    loop = asyncio.get_event_loop()
    loop.run_until_complete(do_migrations())

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
