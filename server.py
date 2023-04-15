from flaskr import app, db

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=54088, ssl_context='adhoc', debug = True)