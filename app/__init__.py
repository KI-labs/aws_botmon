from flask_api import FlaskAPI
from config.env import app_env
from app.utils.slackhelper import SlackHelper
from flask import request, jsonify
from app.actions import Actions

'''
/botmon instances
/botmon inst
/botmon machines
'''
# client secret file


allowed_commands = ['help', 'instances', 'inst', 'machines']


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=False)
    app.config.from_object(app_env[config_name])
    app.config.from_pyfile('../config/env.py')

    def shutdown_server():
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()

    @app.route("/")
    def hello():
        return "Hello World!"

    @app.route('/shutdown', methods=['POST'])
    def shutdown():
        shutdown_server()
        return 'Server shutting down...'

    @app.route('/botmon', methods=['POST'])
    def botmon():
        print("Botmon at your service")
        command_text = request.data.get('text')
        command_text = command_text.split(' ')
        slack_uid = request.data.get('user_id')
        slack_channel = request.data.get('channel_name')

        if slack_channel == "directmessage":
            slack_channel = slack_uid

        slackhelper = SlackHelper(user_id=slack_uid, slack_channel=slack_channel)

        slack_user_info = slackhelper.set_user_info()
        actions = Actions(slackhelper, slack_user_info)

        if command_text[0] not in allowed_commands:
            response_body = {'text': 'Invalid Command Sent - `/botmon help` for available commands'}

        if command_text[0] == 'help':

            response_body = actions.help()

        if command_text[0] in ['instances', 'inst', 'machines']:
            response_body = actions.notify_channel()

        response = jsonify(response_body)
        response.status_code = 200
        return "You can checkout the list of currently running EC2 instances in your direct message from aws_botmon bot"

    return app
