from slackclient import SlackClient
from config import get_env


class SlackHelper:

    def __init__(self, user_id=None, slack_channel=get_env('SLACK_CHANNEL')):
        self.slack_token = get_env('SLACK_TOKEN')
        self.slack_client = SlackClient(self.slack_token)
        self.slack_channel = slack_channel
        self.text = "You can checkout the list of currently running EC2 instances in the channel #aws_botmon"
        self.user_id = user_id

    def post_message(self, blocks):
        print("Before posting message")
        print("blocks_in", blocks)
        return self.slack_client.api_call(
            "chat.postMessage",
            channel=self.slack_channel,
            username='aws_botmon',
            text=self.text,
            blocks=blocks,
            as_user=True,
        )

    def post_message_to_channel(self, blocks):
        print("slack_token", self.slack_token)
        print("Before posting message to channel")
        return self.slack_client.api_call(
            "chat.postMessage",
            channel=self.slack_channel,
            text=self.text,
            username='aws_botmon',
            blocks=blocks,
            # parse='full',
            as_user=True,
        )

    def post_ephemeral_message_to_channel(self, blocks):
        print("slack_token", self.slack_token)
        print("Before posting message to channel")
        return self.slack_client.api_call(
            "chat.postEphemeral",
            channel=self.slack_channel,
            text=self.text,
            username='aws_botmon',
            blocks=blocks,
            # parse='full',
            as_user=True,
        )

    # def file_upload(self, file_content, file_name, file_type, title=None, ):
    #     return self.slack_client.api_call(
    #         "files.upload",
    #         channels=self.slack_channel,
    #         content=file_content,
    #         filename=file_name,
    #         filetype=file_type,
    #         initial_comment='{} Log File'.format(file_name),
    #         title=title
    #     )

    def set_user_info(self):
        return self.slack_client.api_call(
            "users.info",
            user=self.user_id,
            token=self.slack_token
        )
