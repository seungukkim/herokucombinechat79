# -*- coding: utf-8 -*-

from flask import Flask
import pandas as pd 
from sqlalchemy import create_engine
engine = create_engine("postgresql://rrymfmuquvllha:3812aa0e630719b0ae32263fe1592d222818850c660c67cb559823299794f8e4@ec2-54-172-175-251.compute-1.amazonaws.com:5432/dbqsobkjgiql18", echo = False)

engine.connect()

## DB 연결 Local
def db_create():
    #로컬 
    #engine = create_engine("postgresql://postgres:12232305@localhost:5432/postgres",echo=False)
    #postgresql://username:password@localhost:5432/Maintenance database
    #Heroku
    
    engine.execute("""
        CREATE TABLE IF NOT EXISTS dreamspon(
            name varchar(90) NOT NULL,
            advantage varchar(10) NOT NULL,
            who varchar(40) NOT NULL,
            age varchar(15) NOT NULL,
            where1 VARCHAR(30) NOT NULL,
            qualification VARCHAR(30) NOT NULL,
            url VARCHAR(70) NOT NULL
        );"""
    )
    data = pd.read_csv('data/dreamspon.csv')
    print(data)
    data.to_sql(name='dreamspon', con=engine, schema = 'public', if_exists='replace', index=False)


def db_select(choice):
    list=[]
    # choice="\'생활비지원'"
    result= engine.execute("SELECT name FROM dreamspon WHERE advantage LIKE {} ".format(choice))
    # result= engine.execute("SELECT name FROM dreamspon WHERE advantage LIKE '생활비지원'")
    
    for r in result: 
        list.append(r)
             
        print(r)
    return list

app = Flask(__name__)

@app.route("/")
def index():
    # db_create()
    return "Hello World!"


if __name__ == "__main__":
    # db_create()
    db_select()
    
    app.run()