"""initial

Revision ID: 44bf45005346
Revises: 
Create Date: 2016-03-03 00:21:38.966888

"""

# revision identifiers, used by Alembic.
revision = '44bf45005346'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=140), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_people_name'), 'people', ['name'], unique=False)
    op.create_table('traits',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=140), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_traits_name'), 'traits', ['name'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_traits_name'), table_name='traits')
    op.drop_table('traits')
    op.drop_index(op.f('ix_people_name'), table_name='people')
    op.drop_table('people')
    ### end Alembic commands ###
