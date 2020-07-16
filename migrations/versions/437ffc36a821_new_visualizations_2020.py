""" new visualizations 2020  

Revision ID: 437ffc36a821
Revises: d73f1a3bccf3
Create Date: 2020-07-16 19:48:01.228630

"""
from alembic import op
from sqlalchemy import String, Integer
from sqlalchemy.sql import table, column, text


# revision identifiers, used by Alembic.
revision = '437ffc36a821'
down_revision = 'd73f1a3bccf3'
branch_labels = None
depends_on = None


def insert_visualization_type():
    tb = table(
        'visualization_type',
        column('id', Integer),
        column('name', String),
        column('help', String),
        column('icon', String))

    all_ops = [
        (130, 'indicator', 'Gauge', 'fa-chart'),                              
        (131, 'markdown', 'Markdown text', 'fa-chart'),                       
        (132, 'word-cloud', 'Word cloud', 'fa-chart'),                        
        (133, 'heatmap', 'Heatmap', 'fa-chart'),                              
        (134, 'bubble-chart', 'Bubble chart', 'fa-chart'),                    
        (135, 'force-direct', 'Network graphs', 'fa-chart'),                  
        (136, 'iframe', 'HTML iframe', 'fa-chart'),                           
        (137, 'treemap', 'Treemap', 'fa-chart'),
    ]
    rows = [dict(zip([c.name for c in tb.columns], operation)) for operation in
            all_ops]

    op.bulk_insert(tb, rows)


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    try:
        op.execute(text('START TRANSACTION'))
        insert_visualization_type()
        op.execute(text('COMMIT'))
    except:
        op.execute(text('ROLLBACK'))
        raise


# noinspection PyBroadException
def downgrade():
    try:
        op.execute(text('START TRANSACTION'))
        op.execute(text('SET FOREIGN_KEY_CHECKS=0;'))
        op.execute(
            text("DELETE FROM visualization_type WHERE id IN (123, 124)"))
        op.execute(text('SET FOREIGN_KEY_CHECKS=1;'))
        op.execute(text('COMMIT'))
    except:
        op.execute(text('ROLLBACK'))
        raise
