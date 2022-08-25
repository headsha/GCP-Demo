This repo has two self study scenarios. 

FIRST SCENARIO
This is to deploy elasticsearch on Kubernetes and verify its health when one pod is force deleted.

There are two statefulset files in this folder, one for deploying 3 master pods and one for deploying 3 data pods.
Both Statefulset are exactly the same except for the statefulset and contrainer names, both are pointing to a service exposed as a LoadBalancer.
The health was verified by running <curl -XGET 'ELB:9200/_cluster/health?pretty'>




SECOND SCENARIO
This is to setup an Event driven architecture where in, whenever a VM instance is Stopped or Started, data such as VM name , VM ID , start time and end time are stored in a text file in Cloud Storage.

 1.)Whenever a VM instance is Stopped or Started, the corresponding logs are exported to a Pub/Sub topic using a Log routing Sink. The filter used by the Sink is as follows:
protoPayload.methodName=("v1.compute.instances.start" OR "v1.compute.instances.stop")

2.)  In Pub/Sub, a Cloud Function trigger is created with its source as the topic created in the first step.

3.) Cloud Function then decodes the log data to fetch the required fields, it then adds it to text file and pushes to a Cloud Storage Bucket.
