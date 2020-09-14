import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://postgres:aitibame@postgres-aiot.c9nuu9lbcvlx.ap-northeast-1.rds.amazonaws.com/PERSON')

persons = pd.read_sql('select * from app_person', engine)
faces = pd.read_sql('select * from app_face', engine)
# posts_companies = pd.merge(companies, posts, left_on='id', right_on='company_id')
# posts_companies

print(persons)
print('==========================================')
print(faces)