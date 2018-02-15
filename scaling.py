import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client('ecs')

def scale_service(event, context):
    # Process own expected event
    cluster = event["cluster"]
    service_name = event["service_name"]
    service_desired_count = int(event["service_desired_count"])

    response = client.update_service(
		    cluster=cluster,
		    service=service_name,
		    desiredCount=service_desired_count
		)

    logger.info("Updated {0} service in {1} cluster with desire count set to {2} tasks".format(service_name, cluster, service_desired_count))