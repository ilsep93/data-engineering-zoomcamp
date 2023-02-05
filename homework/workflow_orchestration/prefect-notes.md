* Author: @ilsep93

# Configuring the Prefect UI

```bash
prefect orion start
```
The dashboard can be accessed at: http://127.0.0.1:4200

Try specifying the Prefect API if there are issues with the UI connection:

```bash
prefect config set PREFECT_API_URL="http://127.0.0.1:4200/api"
```

To unset the Prefect API:

```bash
prefect config unset PREFECT_API_URL
```

# Blocks

To register blocks created by the UI, type:

```bash
prefect block register -m prefect_gcp
```

Documentation: https://docs.prefect.io/concepts/blocks/

# Deployments

Documentation: https://docs.prefect.io/tutorials/deployments/

Create a .yaml file to specify deployment for loading the green taxi data to GCS.

* prefect deployment build: Generate a deployment YAML from /path/to/file.py:flow_function
* Name of file to deploy: homework/workflow_orchestration/etl_web_to_gcs.py
* Entrypoint (flow to run): etl_parent_flow
* Name of deployment: green_taxi_flow

```bash
prefect deployment build homework/workflow_orchestration/etl_web_to_gcs.py:etl_parent_flow -n multi-green_taxi_flow
```

Apply the deployment for it to appear on the UI.
```bash
prefect deployment apply etl_web_to_gcs-deployment.yaml
```

We could also deploy with Python using the `deployment.py` file

```bash
python deployment.py
```

# Run deployment locally

First, we need to add an agent to manage our work queues.

```bash
prefect agent start -q default
```

```bash
prefect deployment run etl-web-to-gcs/multi_green_taxi_flow
```
Note that deployment runs will fail if the specified buckets do not exist.

# Launch Code From Github

First, we create a Github credentials block using the UI.

```python
from prefect.filesystems import GitHub

github_block = GitHub.load("github-repo")
```

Once the block is created, we update our deployment to pull code from Github (rather than locally)

* -sb: storage-block. The slug of a remote storage block. Use the syntax 'block_type/block_name'
* github/github-repo: Github storage block, followed by Github block name created earlier
* Name of file to deploy: homework/workflow_orchestration/etl_web_to_gcs.py
* Entrypoint (flow to run): etl_parent_flow

```bash
prefect deployment build -n etl_github -sb github/github-repo homework/workflow_orchestration/etl_web_to_gcs.py:etl_parent_flow
```

The same can be done using the `deployment.py` script by specifying a `storage` parameter.