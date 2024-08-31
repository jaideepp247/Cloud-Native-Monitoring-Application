from kubernetes import client, config
from kubernetes import client, config

config.load_kube_config()

# create a kubernetes api client
api_client = client.ApiClient()

# define the deployment
deployment = client.V1Deployment()
deployment.metadata = client.V1ObjectMeta(name="my-deployment")
deployment.spec = client.V1DeploymentSpec(
    replicas=1,
    selector=client.V1LabelSelector(
        match_labels={"app": "my-app"}
    ),
    template=client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(
            labels={"app": "my-app"}
        ),
        spec=client.V1PodSpec(
            containers=[
                client.V1Container(
                    name="my-container",
                    image="624822943522.dkr.ecr.us-east-1.amazonaws.com/resource_monitoring_app_cloud_native:latest",
                    ports=[
                        client.V1ContainerPort(container_port=5000)
                    ]
                )
            ] 
        )
    )
)

# create the deployment
api_instance = client.AppsV1Api(api_client)
api_instance.create_namespaced_deployment(
    namespace="default",
    body=deployment
)

# define the service
service = client.V1Service()
service.metadata = client.V1ObjectMeta(name="my-service")
service.spec = client.V1ServiceSpec(
    selector={"app": "my-app"},
    ports=[client.V1ServicePort(port=5000)]
)

# create the service
api_instance = client.CoreV1Api(api_client)

api_instance.create_namespaced_service(
    namespace="default",
    body=service
)

