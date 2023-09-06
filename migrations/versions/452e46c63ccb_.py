"""empty message

Revision ID: 452e46c63ccb
Revises: 077ae7254874
Create Date: 2023-09-06 15:12:40.023787

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '452e46c63ccb'
down_revision = '077ae7254874'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Conversion', 'meter',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.Numeric(),
               existing_nullable=True)
    op.alter_column('Conversion', 'centimeter',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.Numeric(),
               existing_nullable=True)
    op.alter_column('Conversion', 'millimeter',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.Numeric(),
               existing_nullable=True)
    op.alter_column('Conversion', 'foot',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.Numeric(),
               existing_nullable=True)
    op.alter_column('Conversion', 'inch',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.Numeric(),
               existing_nullable=True)
    op.alter_column('Conversion', 'kilometer',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.Numeric(),
               existing_nullable=True)
    op.alter_column('Conversion', 'mile',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.Numeric(),
               existing_nullable=True)
    op.alter_column('Conversion', 'yard',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.Numeric(),
               existing_nullable=True)
    op.alter_column('Conversion', 'hectare',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.Numeric(),
               existing_nullable=True)
    op.alter_column('Conversion', 'liter',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.Numeric(),
               existing_nullable=True)
    op.alter_column('Conversion', 'milliliter',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.Numeric(),
               existing_nullable=True)
    op.alter_column('Conversion', 'gallon',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.Numeric(),
               existing_nullable=True)
    op.alter_column('Conversion', 'quart',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.Numeric(),
               existing_nullable=True)
    op.alter_column('Conversion', 'board_foot',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.Numeric(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Conversion', 'board_foot',
               existing_type=sa.Numeric(),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
    op.alter_column('Conversion', 'quart',
               existing_type=sa.Numeric(),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
    op.alter_column('Conversion', 'gallon',
               existing_type=sa.Numeric(),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
    op.alter_column('Conversion', 'milliliter',
               existing_type=sa.Numeric(),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
    op.alter_column('Conversion', 'liter',
               existing_type=sa.Numeric(),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
    op.alter_column('Conversion', 'hectare',
               existing_type=sa.Numeric(),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
    op.alter_column('Conversion', 'yard',
               existing_type=sa.Numeric(),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
    op.alter_column('Conversion', 'mile',
               existing_type=sa.Numeric(),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
    op.alter_column('Conversion', 'kilometer',
               existing_type=sa.Numeric(),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
    op.alter_column('Conversion', 'inch',
               existing_type=sa.Numeric(),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
    op.alter_column('Conversion', 'foot',
               existing_type=sa.Numeric(),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
    op.alter_column('Conversion', 'millimeter',
               existing_type=sa.Numeric(),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
    op.alter_column('Conversion', 'centimeter',
               existing_type=sa.Numeric(),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
    op.alter_column('Conversion', 'meter',
               existing_type=sa.Numeric(),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
    # ### end Alembic commands ###
