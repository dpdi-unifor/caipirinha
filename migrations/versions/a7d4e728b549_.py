"""empty message

Revision ID: a7d4e728b549
Revises: 63df7f61d072
Create Date: 2017-08-09 12:31:42.628620

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
from sqlalchemy.dialects import mysql

revision = 'a7d4e728b549'
down_revision = '63df7f61d072'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('visualization',
                  sa.Column('data', mysql.LONGTEXT(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('visualization', 'data')
    # ### end Alembic commands ###
