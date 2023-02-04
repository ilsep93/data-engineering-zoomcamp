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




#Schedule a deployment: https://docs.prefect.io/tutorials/deployments/
prefect deployment build homework/workflow_orchestration/etl_web_to_gcs.py:etl_web_to_gcs -n green_taxi_flow

# Found flow 'etl-web-to-gcs'
# Default '.prefectignore' file written to 
# /Users/ilsepaniagua/Documents/GitHub/data-engineering-zoomcamp/.prefectignore
# Deployment YAML created at 
# '/Users/ilsepaniagua/Documents/GitHub/data-engineering-zoomcamp/etl_web_to_gcs-deploy
# ment.yaml'.
# Deployment storage None does not have upload capabilities; no files uploaded.  Pass 
# --skip-upload to suppress this warning.