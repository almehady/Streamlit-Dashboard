# import mysql.connector
# import streamlit as st

# #connection

# conn=mysql.connector.connect(
#     host="localhost",
#     port="3306",
#     user="root",
#     passwd="",
#     db="myDb"
# )
# c=conn.cursor()

#fetch

import pandas as pd
all_data = pd.read_csv('/Users/faisalsalam/dev/data_analytics/streamlit_dashboard/resources/excel.csv')
def view_all_data():
#  c.execute('select * from insurance order by id asc')
 data=all_data
 return data