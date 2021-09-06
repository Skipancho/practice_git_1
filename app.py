import sqlite3
from flask import Flask, redirect, request

app = Flask(__name__)

@app.route("/create_process",methods=['POST'])
def create_process():
    title = request.form['title']
    body = request.form['body']
    con = sqlite3.connect('topic_m.db')
    sql = "INSERT INTO TOPIC(title, body) VALUES('"+title+"','"+body+"')"

    result = con.execute(sql)
    con.commit()

    return  redirect("/read/"+str(result.lastrowid))

    


@app.route("/read/<topicid>")
def read(topicid): 
    con = sqlite3.connect('topic_m.db')
    result = con.execute('SELECT * FROM TOPIC')
    topics = result.fetchall()
    
    print(topics)
    nav = '<ol>'
    for topic in topics:
        nav += '<li><a href="/read/'+str(topic[0])+'">'+topic[1]+'</a></li>'
    nav += '</ol>'

    result = con.execute('SELECT * FROM topic WHERE id='+topicid)
    topic = result.fetchone()
    print(topic)

    content = '<h2>'+topic[1]+'</h>'+topic[2]
        
    html = '''
        <!DOCTYPE html>
        <html>
            <body>
                <h1><a href="/">WEB</a></h1>
                '''+nav+content+'''

                <h2>Welcome</h2>
                <p><a href="/create">create</a></p>
                Hello, WEB!
            </body>
        </html>
    '''
    return html

@app.route("/create")
def create():    
    con = sqlite3.connect('topic_m.db')
    result = con.execute('SELECT * FROM TOPIC')
    topics = result.fetchall()
    print('topics', topics)

    nav = '<ol>'
    for topic in topics:
        nav = nav + '<li><a href="/read/'+str(topic[0])+'">'+topic[1]+'</a></li>'
    nav = nav + '</ol>'
    
    html = '''
        <!DOCTYPE html>
        <html>
            <body>
                <h1><a href="/">WEB</a></h1>
                '''+nav+'''
                <h2>Welcome</h2>
                <p><a href="/create">create</a></p>
                Hello, WEB!
                <form action="/create_process" method="POST">
                    <p><input type="text" name ="title" placeholder="title"></p>
                    <p><textarea name = "body" placeholder="body"></textarea></p>
                    <p><input type="submit" value="create"></p>
                </form>
            </body>
        </html>
    '''
    return html


@app.route("/")
def home():
    con = sqlite3.connect('topic_m.db')
    result = con.execute('SELECT * FROM TOPIC')
    topics = result.fetchall()
    print('topics', topics)

    nav = '<ol>'
    for topic in topics:
        nav = nav + '<li><a href="/read/'+str(topic[0])+'">'+topic[1]+'</a></li>'
    nav = nav + '</ol>'
    
    html = '''
        <!DOCTYPE html>
        <html>
            <body>
                <h1><a href="/">WEB</a></h1>
                '''+nav+'''
                <h2>Welcome</h2>
                <p><a href="/create">create</a></p>
                Hello, WEB!
            </body>
        </html>
    '''
    return html


app.run(debug=True)
