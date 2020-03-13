import subprocess as sp
import json


class AWSHelper:

    def __init__(self):
        self.regions = []
        self.reservations_in_regions = []
        self.instances_per_region = []
        self.total_instances = []
        self.result = self.run()

    def run(self):
        self.__get_regions()
        self.__find_reservations_for_regions()
        self.__find_running_ec2_instances()
        return self.total_instances, self.instances_per_region

    def __get_regions(self):
        data = sp.check_output("aws ec2 describe-regions --output text | cut -f4", shell=True)
        regions = data.decode("utf-8")
        self.regions = regions.splitlines()

    def __find_reservations_for_regions(self):
        for region in self.regions:
            log_file_path = f"/Users/s.sathyakumari/Downloads/projects/aws-ec2-slackbot/{region}_instances.json"
            sp.call("aws ec2 describe-instances --region {} > {}".format(region, log_file_path), shell=True)
            data = json.load(open(log_file_path))
            reservations = data["Reservations"]
            if reservations:
                reservations_in_regions = {region: reservations}
                self.reservations_in_regions.append(reservations_in_regions)

    def __find_running_ec2_instances(self):
        for each in self.reservations_in_regions:
            for region, reservationsList in each.items():
                instances = [instance for instance_list in
                             [reservationsList.get("Instances") for reservationsList in reservationsList] for instance
                             in instance_list]
                if instances:
                    running_instances = [(instance.get("InstanceId"), instance.get("KeyName"),
                                          instance.get("InstanceType"), instance.get("State").get("Name")) for instance
                                         in instances if instance.get("State").get("Name") == "running"]
                    machines = [
                        {"region": region, "id": instance_id[0], "name": instance_id[1], "type": instance_id[2],
                         "status": instance_id[3]}
                        for instance_id in running_instances]

                    no_of_running_instances = len(running_instances)

                    instance_summary = {"region": region, "total_running": no_of_running_instances}

                    self.instances_per_region.append(instance_summary)

                    self.total_instances = self.total_instances + machines
