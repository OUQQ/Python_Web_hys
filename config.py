class DbConfig(object):
    USERNAME='root'
    PASSWORD='d1a241f666'
    HOST='127.0.0.1'
    PORT='3306'
    DATABASE='db_demo1'
    DB_URI='mysql+pymysql://root:d1a241f666@127.0.0.1:3306/db_demo1?charset=utf8'
    SQLALCHEMY_DATABASE_URI=DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO=True