from prefect_gcp import GcpCredentials
from prefect_gcp.cloud_storage import GcsBucket

gcp_credentials_block = GcpCredentials.load("zoom-gcp-creds")
gcp_cloud_storage_bucket_block = GcsBucket.load("green-taxi-bucket")

#gcp_cloud_storage_bucket_block.save("zoom-gcs", overwrite=True)