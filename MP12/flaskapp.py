import kubernetes
from flask import Flask, request, jsonify
import json
import yaml

app = Flask(__name__)

def k8_config():
    print("entered k8_config")
    kubernetes.config.load_kube_config()
    batch_v1 = kubernetes.client.BatchV1Api()
    v1 = kubernetes.client.CoreV1Api()
    ret = v1.list_pod_for_all_namespaces(watch=False)
    result = []
    for i in ret.items:
        result.append({"node":i.spec.node_name, "ip": i.status.pod_ip, "namespace": i.metadata.namespace, "name": i.metadata.name, "status": i.status.phase})
    return result

@app.route('/img-classification/free', methods=['POST'])
def free():
    kubernetes.config.load_kube_config()
    print("entered free")
    with open("mnist-deployment-1.yaml") as f:
        dep = yaml.safe_load(f)
        apps_v1 = kubernetes.client.BatchV1Api()
        api_response = apps_v1.create_namespaced_job(
            body=dep,
            namespace="free-service")
    print("Job created. status='%s'" % str(api_response.status))
    return "success"

@app.route("/img-classification/premium", methods = ["POST"])
def premium():
    kubernetes.config.load_kube_config()
    print("entered premium")
    with open("mnist-deployment-1.yaml") as f:
        dep = yaml.safe_load(f)
        apps_v1 = kubernetes.client.BatchV1Api()
        api_response = apps_v1.create_namespaced_job(
            body=dep,
            namespace="default")
    print("Job created. status='%s'" % str(api_response.status))
    return "success"
    

@app.route('/config', methods=['GET'])
def config():
    print("entered config")
    result = k8_config()
    return json.dumps({"pods": result})

@app.route('/home', methods=['GET'])
def home():
    return "<h1>Hello world</h1>"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)


# I create a EKS Machine -> ec2 instance nano # for set up, open the port for the autograder
# inside the machine, I would save, the job yaml config, and the flaskapp.py
# I create cluster of the AWS K8
# crete namespace free-service
# apply the resourcequota config file to free-service namespace
# run the flaskapp.py on the eks machine
# run the submission file on my laptop

