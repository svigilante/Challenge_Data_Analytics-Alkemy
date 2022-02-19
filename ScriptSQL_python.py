import psycopg2


conn = psycopg2.connect(host="localhost", user="santi", password="admin", database="alkemy_db", port="5432")

with conn.cursor() as cursor:
    cursor.execute(open("Script.sql", "r").read())
