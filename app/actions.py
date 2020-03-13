import time
import json
from datetime import datetime, date, timedelta
from config import get_env
from app.utils.awshelper import AWSHelper
from constants import backticks, instance_title, summary_title, single_border_unbroken, new_line, region, instances_running_per_region, instance_id, instance_name, instance_type, status, INSTANCES_PATH, SUMMARY_PATH


class Actions:
    def __init__(self, slackhelper, user_info=None):
        self.user_info = user_info
        self.slackhelper = slackhelper

    def get_instances_details(self):
        aws_operations = AWSHelper()
        return aws_operations

    def notify_user(self):
        pass
        # print("USER_INFO", self.user_info)
        # email = self.user_info['user']['profile']['email']
        # recipient = self.user_info['user']['id']
        #
        # aws_operations = self.get_instances_details()
        # instances = aws_operations.result
        # print("instances", instances)
        # print("blocks", blocks)
        # response = self.slackhelper.post_ephemeral_message_to_channel(blocks)
        # return response

    @staticmethod
    def build_blocks(instances_list, summary_list):
        # instance_text = f"``` {single_border} {new_line} {header_instances} {new_line} {double_border} {new_line}"
        instance_text = summary_title
        instance_text += backticks
        for each_region in summary_list:
            body_row = f"{region}{each_region['region']} | {instances_running_per_region}{each_region['total_running']}   ||{new_line} {single_border_unbroken}"
            instance_text = instance_text + body_row

        instance_text += backticks
        instance_text += new_line

        instance_text += instance_title
        instance_text += backticks

        for each_instance in instances_list:
            body_row = f"{region}{each_instance['region']} | {instance_id}{each_instance['id']}   | {instance_name}{each_instance['name']}  | {instance_type}{each_instance['type']}  | {status}{each_instance['status']}  |{new_line} {single_border_unbroken}"
            instance_text = instance_text + body_row

        instance_text += backticks

        print("instance_text", instance_text)
        blocks = [{"type": "section", "text": {"type": "mrkdwn", "text": instance_text}}]

        return blocks

    @staticmethod
    def read_from_file(file_path):
        with open(file_path, 'r') as f:
            instances_list = json.load(f)
            return instances_list

    def notify_channel(self):
        # while True:
        print(datetime.now())

        # aws_operations = self.get_instances_details()
        # instances_list = aws_operations.result
        instances_list = self.read_from_file(INSTANCES_PATH)
        summary_list = self.read_from_file(SUMMARY_PATH)
        print("instances", instances_list)
        print("summary_list", summary_list)

        blocks = self.build_blocks(instances_list, summary_list)

        # text = "Hello World"
        response = self.slackhelper.post_message_to_channel(blocks)
        return None


            # curent_time = datetime.now()
            # current_hour = curent_time.hour
            # current_minute = curent_time.minute
            #
            # if current_hour - 8 > 0:
            #     sleep_time = 24 - current_hour + 8 - (current_minute / 60)
            # elif current_hour - 8 < 0:
            #     sleep_time = 8 - current_hour - (current_minute / 60)
            # elif current_hour == 8:
            #     if current_minute == 0:
            #         sleep_time = 0
            #     else:
            #         sleep_time = 24 - current_hour + 8 - (current_minute / 60)
            #
            # for index, row in enumerate(self.sheet):
            #     check_date = datetime.strptime(self._num_suffix(row['Next Check-In']), '%d %B %Y').date()
            #     todays_date = datetime.now().date()
            #     send_notif_date = check_date - todays_date
            #
            #     if send_notif_date.days == 0:
            #         ## TODO change below
            #         text_detail = (
            #             '*Task #{} for {}:* \n\n'
            #             '*Hey {},* Today is the check-in day for your writeup titled\n'
            #             '`{}`.\n\n'
            #             'Whats the status of the article?\n'
            #             'PS: Please reply to this thread, the managers will review and reply you ASAP').format(
            #             str(index + 1), row['Next Check-In'], row['Name'],
            #             row['Most Recent Learning Experience you\'d like to write about'])
            #         self.slackhelper.post_message_to_channel(text_detail)
            # time.sleep(sleep_time * 3600)
            # time.sleep(2)

