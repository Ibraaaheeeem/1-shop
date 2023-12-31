"""empty message

Revision ID: c1a19cf2a1de
Revises: 
Create Date: 2023-10-25 21:07:54.529415

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1a19cf2a1de'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('level1',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('description', sa.String(length=1024), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('item_count', sa.Integer(), nullable=True),
    sa.Column('image_url', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('property',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('values', sa.String(length=1024), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('level2',
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('description', sa.String(length=1024), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('item_count', sa.Integer(), nullable=True),
    sa.Column('image_url', sa.String(length=200), nullable=False),
    sa.ForeignKeyConstraint(['parent_id'], ['level1.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('level3',
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('description', sa.String(length=1024), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('item_count', sa.Integer(), nullable=True),
    sa.Column('image_url', sa.String(length=200), nullable=False),
    sa.ForeignKeyConstraint(['parent_id'], ['level2.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('level4',
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('description', sa.String(length=1024), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('item_count', sa.Integer(), nullable=True),
    sa.Column('image_url', sa.String(length=200), nullable=False),
    sa.ForeignKeyConstraint(['parent_id'], ['level3.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('level5',
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('description', sa.String(length=1024), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('item_count', sa.Integer(), nullable=True),
    sa.Column('image_url', sa.String(length=200), nullable=False),
    sa.ForeignKeyConstraint(['parent_id'], ['level4.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=124), nullable=False),
    sa.Column('skuList', sa.String(length=102400), nullable=False),
    sa.Column('defaultSku', sa.String(length=1024), nullable=False),
    sa.Column('defaultImageUrl', sa.String(length=1024), nullable=False),
    sa.Column('otherImagesUrl', sa.String(length=1024), nullable=False),
    sa.Column('productDescriptionUrl', sa.String(), nullable=False),
    sa.Column('appliedProperties', sa.String(), nullable=True),
    sa.Column('level1_id', sa.Integer(), nullable=True),
    sa.Column('level2_id', sa.Integer(), nullable=True),
    sa.Column('level3_id', sa.Integer(), nullable=True),
    sa.Column('level4_id', sa.Integer(), nullable=True),
    sa.Column('level5_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['level1_id'], ['level1.id'], ),
    sa.ForeignKeyConstraint(['level2_id'], ['level2.id'], ),
    sa.ForeignKeyConstraint(['level3_id'], ['level3.id'], ),
    sa.ForeignKeyConstraint(['level4_id'], ['level4.id'], ),
    sa.ForeignKeyConstraint(['level5_id'], ['level5.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    op.drop_table('level5')
    op.drop_table('level4')
    op.drop_table('level3')
    op.drop_table('level2')
    op.drop_table('property')
    op.drop_table('level1')
    # ### end Alembic commands ###
