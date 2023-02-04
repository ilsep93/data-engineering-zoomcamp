from prefect_gcp import GcpCredentials
from prefect_gcp.cloud_storage import GcsBucket

gcp_credentials_block = GcpCredentials.load("zoom-gcp-creds")
gcp_bucket = GcsBucket.load("green-taxi-rides")

#gcp_cloud_storage_bucket_block.save("zoom-gcs", overwrite=True)