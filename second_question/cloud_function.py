import base64
import json
import stat
import os


def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')

    from google.cloud import storage
    storage_client = storage.Client()
    bucket_name = "husambucket"

    final = json.loads(pubsub_message)
    inst_id = final['resource']['labels']['instance_id']
    inst_nameFull = final['protoPayload']['resourceName']
    inst_name= inst_nameFull.replace('projects/cool-framing-358912/zones/us-west4-b/instances/','')
    starttime= final['timestamp']
    endtime = final['receiveTimestamp']


    path = '/tmp/husam-assignemnt.txt'
    with open(path, 'w') as f:
      f.write(" VM ID is->" + inst_id)
      f.write(" VM Instance name is->" + inst_name)
      f.write(" starttime is->" + starttime)
      f.write(" endtime is->" + endtime)
    st = os.stat(path)
    os.chmod(path, st.st_mode | stat.S_IWOTH)
    
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(path)
    blob.upload_from_filename(path)
  


