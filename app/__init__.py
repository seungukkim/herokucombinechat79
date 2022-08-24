import os 
from cgi import parse_multipart
from flask import Flask, render_template,request


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'development'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello():
        return render_template('index.jinja2', title='index page')

    @app.route('/api/sayHello', methods=['POST'])
    def sayHello():
        body = request.get_json() # 사용자가 입력한 데이터
        print(body)
        print(body['userRequest']['utterance'])

        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "안녕 hello I'm Ryan"
                        }
                    }   
                ]
            }
        }

        return responseBody


    ## 카카오톡 이미지형 응답
    @app.route('/api/showHello', methods=['POST'])
    def showHello():
        body = request.get_json()
        print(body)
        print(body['userRequest']['utterance'])

        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleImage": {
                            "imageUrl": "https://t1.daumcdn.net/friends/prod/category/M001_friends_ryan2.jpg",
                            "altText": "hello I'm Ryan"
                        }
                    }
                ]
            }
        }

        return responseBody

    from .main import main
    # from .dashapp1 import dashapp1
    from .dashapp1 import bp as bp_dashapp1
    from .dashapp1.dashapp1 import add_dash
    from .dashapp2 import dashapp2


    app.register_blueprint(main.bp)
    app.register_blueprint(bp_dashapp1)
    app.register_blueprint(dashapp2.bp)

    app = add_dash(app)

    return app
