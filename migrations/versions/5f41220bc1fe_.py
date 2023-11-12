"""empty message

Revision ID: 5f41220bc1fe
Revises: 45fc983aaa22
Create Date: 2023-11-12 20:31:27.958927

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5f41220bc1fe'
down_revision = '45fc983aaa22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('menu',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('path', sa.String(length=50), nullable=True),
    sa.Column('pid', sa.Integer(), nullable=True),
    sa.Column('Menu', sa.NullType(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('pwd',
               existing_type=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=120),
               type_=sa.String(length=50),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('pwd',
               existing_type=sa.String(length=50),
               type_=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=120),
               existing_nullable=False)

    op.drop_table('menu')
    # ### end Alembic commands ###
