import requests
import urllib
import bs4
import psycopg2

def get_show_titles():
    url = "https://www.imdb.com/chart/toptv/"
    resp = urllib.request.urlopen(url)
    data = resp.read()
    soup = bs4.BeautifulSoup(data, features="html.parser")
    titles = soup.find_all("td", attrs={"class":"titleColumn"})
    title_list = []
    for title in titles:
        title_list.append(title.text.strip().split("\n")[1].strip())
    return title_list

def create_table():
    dbconn = psycopg2.connect(dbname = "show")
    cursor = dbconn.cursor()
    f = open("sqlcode.sql")
    sql_code = f.read()
    cursor.execute(sql_code)
    cursor.close()
    dbconn.commit()

def insert():
    dbconn = psycopg2.connect(dbname = "show")
    cursor = dbconn.cursor()
    titles = get_show_titles()
    for title in titles:
        cursor.execute("INSERT INTO shows(title) VALUES (%s)", (title,))
    cursor.close()
    dbconn.commit()

if __name__ == "__main__":
    create_table()
    insert()
