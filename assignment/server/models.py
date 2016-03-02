import asyncio
import sqlalchemy as sa
from aiopg.sa import create_engine


metadata = sa.MetaData()

TraitsTbl = sa.Table('traits', metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String(140), nullable=False, index=True)
)

PeopleTbl = sa.Table('people', metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String(140), nullable=False, index=True)
)
