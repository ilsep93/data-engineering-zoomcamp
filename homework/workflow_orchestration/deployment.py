from etl_web_to_gcs import etl_parent_flow
from prefect.deployments import Deployment

deployment = Deployment.build_from_flow(
    flow=etl_parent_flow,
    name="multi_green_taxi_flow",
    parameters={"color": "green", "year": 2020, "months": [1,2,3]},
    infra_overrides={"env": {"PREFECT_LOGGING_LEVEL": "DEBUG"}},
    work_queue_name="default",
)

if __name__ == "__main__":
    deployment.apply()