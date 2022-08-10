This is to setup an Event driven architecture where in, whenever a VM instance is Stopped or Started, data such as VM name , VM ID , start time and end time are stored in a text file in Cloud Storage.

 1.)Whenever a VM instance is Stopped or Started, the corresponding logs are exported to a Pub/Sub topic using a Log routing Sink. The filter used by the Sink is as follows:
protoPayload.methodName=("v1.compute.instances.start" OR "v1.compute.instances.stop")

2.)  In Pub/Sub, a Cloud Function trigger is created with its source as the topic created in the first step.
