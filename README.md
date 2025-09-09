# FastAPI with asyncpg (No ORM)

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![asyncpg](https://img.shields.io/badge/asyncpg-000000?style=for-the-badge&logo=postgresql&logoColor=white)](https://magicstack.github.io/asyncpg/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

A demonstration project showing how to build a [FastAPI](https://fastapi.tiangolo.com/) application using [asyncpg](https://magicstack.github.io/asyncpg/) for direct [PostgreSQL](https://www.postgresql.org/) database access without an ORM.

## Why This Approach?

**For the ORM haters who just want to write SQL and be done with it! 😤**

- **Raw SQL Power**: Write queries that actually make sense instead of fighting with ORM magic
- **Speed Demon**: [asyncpg](https://magicstack.github.io/asyncpg/) is stupidly fast - why add layers when you don't need them?
- **What You See Is What You Get**: No hidden queries, no surprise N+1 problems, just pure SQL
- **Debug Like a Pro**: When your query is slow, you know exactly what's happening (no ORM black box)
- **Database Features**: Use all the cool PostgreSQL features without ORM limitations

## How to Run

### Prerequisites

- Python 3.13+
- [UV](https://docs.astral.sh/uv/) package manager

### Setup

1. **Install dependencies:**

   ```bash
   uv sync
   ```

1. **Start PostgreSQL:**

   ```bash
   docker-compose up -d postgres
   ```

1. **Run database migrations:**

   ```bash
   uv run alembic upgrade head
   ```

   (Using [Alembic](https://alembic.sqlalchemy.org/) for database migrations)

1. **Start the application:**

   ```bash
   make run
   ```

The API will be available at `http://localhost:8000`
