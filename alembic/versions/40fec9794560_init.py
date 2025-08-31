"""init

Revision ID: 40fec9794560
Revises:
Create Date: 2025-08-30 09:54:43.741314

"""

from collections.abc import Sequence

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "40fec9794560"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.execute("""
        create table if not exists operation (
            id bigint generated always as identity primary key,
            description text,
            created_at timestamptz default now()
        )
    """)

    op.execute("""
        insert into operation (description, created_at)
        select
            (array[
                'User login', 'Data export', 'Report generation', 'Backup creation',
                'System maintenance', 'User registration', 'Password reset', 'Data import',
                'Log analysis', 'Performance monitoring', 'Security scan', 'Update deployment',
                'Database cleanup', 'Cache refresh', 'API request', 'File upload',
                'Email sending', 'Notification dispatch', 'Audit logging', 'Health check'
            ])[floor(random() * 20 + 1)] as description,
            (now() - (random() * interval '30 days')) as created_at
        FROM generate_series(1, 1000)
    """)


def downgrade() -> None:
    op.execute("drop table if exists operation")
