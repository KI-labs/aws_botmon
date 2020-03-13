from apscheduler.schedulers.blocking import BlockingScheduler
from app.utils.awshelper import AWSHelper
from app.utils.slackhelper import SlackHelper
from app.actions import Actions
from constants import INSTANCES_PATH, SUMMARY_PATH
import json

sched_aws = BlockingScheduler()
sched_bod = BlockingScheduler()


def write_into_file(data_list, save_path):
    with open(save_path, "w") as f:
        json.dump(data_list, f, indent=0)


@sched_aws.scheduled_job('interval', seconds=900)
def perform_aws_operations():
    # Get AWS instances list
    aws_operations = AWSHelper()
    instances_list, instances_summary = aws_operations.result

    write_into_file(instances_list, INSTANCES_PATH)
    write_into_file(instances_summary, SUMMARY_PATH)


@sched_bod.scheduled_job('cron', day_of_week='mon-fri', hour=10)
def send_bod_messages_to_slack():
    slackhelper = SlackHelper()
    actions = Actions(slackhelper)
    actions.notify_channel()

sched_aws.start()
sched_bod.start()
