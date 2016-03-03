"""extensions

Revision ID: 22c911d2bf6d
Revises: d6ae559902f7
Create Date: 2016-03-03 04:07:11.708067

"""

# revision identifiers, used by Alembic.
revision = '22c911d2bf6d'
down_revision = 'd6ae559902f7'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.execute('CREATE EXTENSION btree_gist;')
    op.execute('CREATE EXTENSION btree_gin;')
    op.execute('CREATE EXTENSION intarray;')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###
