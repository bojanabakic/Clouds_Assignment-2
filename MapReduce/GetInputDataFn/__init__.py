# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import itertools
from azure.storage.blob import BlobServiceClient


def main(text: str) -> list:
    blob_service_client = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=assignment2task5app;AccountKey=qZr0dCl8G0kMNy1sYgKbNNN193bxO5zWG8ngnhjestRcxMA1sqx7ysSTk+K/l9wQxKaZTfKfH108+AStx33JPw==;EndpointSuffix=core.windows.net")
    container_client = blob_service_client.get_container_client(container = text) 
    
    blob_list = container_client.list_blobs()
    lines_plus_offset = []
    
    for blob in blob_list:
        text = container_client.download_blob(blob.name).readall()
        lines = text.splitlines()
        
        pair = []
        offset = 0

        for i in lines:
            offset += 1
            line = str(i)
            pair.append((offset, line))

        lines_plus_offset.extend(pair)
        
    return lines_plus_offset
