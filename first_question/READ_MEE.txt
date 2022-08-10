This is to deploy elasticsearch on kubernetes.
There are two statefulset files in this folder, one for deploying 3 master pods and one for deploying 3 data pods.
Both Statefulset are exactly the same except for the statefulset and contrainer names, both are pointing to a service exposed as a LoadBalancer.
