#Configure the prefect UI

#Launch the UI
prefect orion start

#Check out the dashboard at http://127.0.0.1:4200

#Set up prefect blocks
prefect block register -m prefect_gcp

#To configure the newly registered blocks, go to the Blocks page in the Prefect UI: 
#http://127.0.0.1:4200/blocks/catalog

#prefect config set PREFECT_API_URL="http://127.0.0.1:4200/api"
#prefect config unset PREFECT_API_URL