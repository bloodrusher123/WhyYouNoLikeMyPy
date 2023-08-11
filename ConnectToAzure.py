from datetime import datetime, timedelta
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
import pandas as pd
import requests
import urllib.request as request

account_name = 'sadev01'
account_key = ''
container_name = 'released'

connect_str = 'DefaultEndpointsProtocol=https;AccountName=' + account_name + ';AccountKey=' + account_key + ';EndpointSuffix=core.windows.net'
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

container_client = blob_service_client.get_container_client(container_name)
blob_list = []
for blob_i in container_client.list_blobs():
    if '20210205' in blob_i.name:
        blob_list.append(blob_i.name)
        print (blob_i.name)
    
#df_list = []

for blob_i in blob_list:
    sas_i = generate_blob_sas(account_name = account_name,
                                container_name = container_name,
                                blob_name = blob_i,
                                account_key=account_key,
                                permission=BlobSasPermissions(read=True),
                                expiry=datetime.utcnow() + timedelta(hours=1))
    #blob_name = '20210205/LV21111111/Test MCP.docx'
    sas_url = 'https://' + account_name+'.blob.core.windows.net/' + container_name + '/' + blob_i + '?' + sas_i

    r = requests.get(sas_url)
    open(blob_i.rsplit('/', 1)[-1], 'wb').write(r.content)

