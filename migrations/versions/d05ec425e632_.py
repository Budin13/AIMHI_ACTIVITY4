"""empty message

Revision ID: d05ec425e632
Revises: cb035331dd52
Create Date: 2023-09-08 10:30:49.337978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd05ec425e632'
down_revision = 'cb035331dd52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Conversion',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('type', sa.String(length=200), nullable=False),
    sa.Column('unit', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('unit')
    )
    op.create_table('AreaConversion',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('area', sa.String(length=200), nullable=False),
    sa.Column('hectare', sa.Numeric(), nullable=False),
    sa.Column('square_meter', sa.Numeric(), nullable=False),
    sa.Column('square_kilometer', sa.Numeric(), nullable=False),
    sa.Column('square_centimeter', sa.Numeric(), nullable=False),
    sa.Column('square_millimeter', sa.Numeric(), nullable=False),
    sa.Column('square_mile', sa.Numeric(), nullable=False),
    sa.Column('square_yard', sa.Numeric(), nullable=False),
    sa.Column('square_foot', sa.Numeric(), nullable=False),
    sa.Column('square_inch', sa.Numeric(), nullable=False),
    sa.ForeignKeyConstraint(['area'], ['Conversion.unit'], onupdate='cascade', ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('FuelConversion',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('fuel', sa.String(length=200), nullable=False),
    sa.Column('gallon', sa.Numeric(), nullable=False),
    sa.Column('liter', sa.Numeric(), nullable=False),
    sa.Column('milliliter', sa.Numeric(), nullable=False),
    sa.Column('quart', sa.Numeric(), nullable=False),
    sa.ForeignKeyConstraint(['fuel'], ['Conversion.unit'], onupdate='cascade', ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('LengthConversion',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('length', sa.String(length=200), nullable=False),
    sa.Column('meter', sa.Numeric(), nullable=False),
    sa.Column('centimeter', sa.Numeric(), nullable=False),
    sa.Column('millimeter', sa.Numeric(), nullable=False),
    sa.Column('foot', sa.Numeric(), nullable=False),
    sa.Column('inch', sa.Numeric(), nullable=False),
    sa.Column('yard', sa.Numeric(), nullable=False),
    sa.ForeignKeyConstraint(['length'], ['Conversion.unit'], onupdate='cascade', ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('LumberConversion',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('lumber', sa.String(length=200), nullable=False),
    sa.Column('board_foot', sa.Numeric(), nullable=False),
    sa.Column('cubic_foot', sa.Numeric(), nullable=False),
    sa.Column('cubic_inch', sa.Numeric(), nullable=False),
    sa.ForeignKeyConstraint(['lumber'], ['Conversion.unit'], onupdate='cascade', ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('MassWeightConversion',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('mass_weight', sa.String(length=200), nullable=False),
    sa.Column('kilogram', sa.Float(), nullable=True),
    sa.Column('gram', sa.Float(), nullable=True),
    sa.Column('milligram', sa.Float(), nullable=True),
    sa.Column('metric_ton', sa.Float(), nullable=True),
    sa.Column('long_ton', sa.Float(), nullable=True),
    sa.Column('short_ton', sa.Float(), nullable=True),
    sa.Column('pound', sa.Float(), nullable=True),
    sa.Column('ounce', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['mass_weight'], ['Conversion.unit'], onupdate='cascade', ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('VolumeConversion',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('volume', sa.String(length=200), nullable=False),
    sa.Column('liter', sa.Numeric(), nullable=False),
    sa.Column('milliliter', sa.Numeric(), nullable=False),
    sa.Column('cubic_meter', sa.Numeric(), nullable=False),
    sa.Column('cubic_kilometer', sa.Numeric(), nullable=False),
    sa.Column('cubic_centimeter', sa.Numeric(), nullable=False),
    sa.Column('cubic_millimeter', sa.Numeric(), nullable=False),
    sa.Column('cubic_mile', sa.Numeric(), nullable=False),
    sa.Column('cubic_yard', sa.Numeric(), nullable=False),
    sa.Column('cubic_foot', sa.Numeric(), nullable=False),
    sa.Column('cubic_inch', sa.Numeric(), nullable=False),
    sa.ForeignKeyConstraint(['volume'], ['Conversion.unit'], onupdate='cascade', ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('VolumeConversion')
    op.drop_table('MassWeightConversion')
    op.drop_table('LumberConversion')
    op.drop_table('LengthConversion')
    op.drop_table('FuelConversion')
    op.drop_table('AreaConversion')
    op.drop_table('Conversion')
    # ### end Alembic commands ###
