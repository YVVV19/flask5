from app import app
from db import Config, user_create, user_select

if __name__=="__main__":
    try:
        Config.up()
        # migrate()
        user_create(nickname="vasya")
        user_select(nickname="vasya")
        app.run(
            host="localhost",
            port=8080,
            debug=True,
        )
    finally:
        Config.down()