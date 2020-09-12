import pandas as pd
from sqlalchemy import create_engine
engine_person = create_engine('postgresql+psycopg2://postgres:aitibame@postgres-aiot.c9nuu9lbcvlx.ap-northeast-1.rds.amazonaws.com/PERSON')
engine_face = create_engine('postgresql+psycopg2://postgres:aitibame@postgres-aiot.c9nuu9lbcvlx.ap-northeast-1.rds.amazonaws.com/FACE')

persons = pd.read_sql('select * from app_person', engine_person)
faces = pd.read_sql('select * from app_face', engine_face)
# posts_companies = pd.merge(companies, posts, left_on='id', right_on='company_id')
# posts_companies

print(persons)