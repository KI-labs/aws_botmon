import time
from datetime import datetime, date, timedelta
from config import get_env
from app.utils.awshelper import AWSHelper


class Actions:
    def __init__(self, slackhelper, user_info=None):
        self.user_info = user_info
        self.slackhelper = slackhelper

    def notify_channel(self):
        while True:
            print(datetime.now())

            aws_operations = AWSHelper()
            print("aws_operations", aws_operations.result)

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
            time.sleep(2)

