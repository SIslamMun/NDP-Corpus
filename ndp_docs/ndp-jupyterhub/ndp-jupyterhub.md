# ndp-jupyterhub


### JupyterHub_Docker/README.md (3,600 bytes)

# NDP JupyterHub Docker
## Core Documentation
- JupyterHub Docker Deployment Guide and Examples: https://github.com/jupyterhub/jupyterhub-deploy-docker 

## Setup
1. Install Docker
2. Copy `.env.example` as `.env` file:
```
cp .env.example .env
```
And add missing Keycloak secret `JUPYTERHUB_KEYCLOAK_CLIENT_SECRET= !!! CHANGE ME !!!`

## Deploy:

```docker compose -f docker-compose.yaml up --build -d```
Go to http://localhost:8002/hub/spawn to use JupyterHub.

## Undeploy:
```docker compose -f docker-compose.yaml down```

   
### Important Notes
1. The hub is customized using these guides:
https://jupyterhub.readthedocs.io/en/stable/howto/templates.html#extending-templates
https://github.com/jupyterhub/jupyterhub/tree/886ce6cbdfc00b66b45ac769e5ab2270abca3ef1/share/jupyterhub/templates
`hub_docker_image` folder contains Dockerfile for hub image + templates and pics.

2. `jupyterhub_config.py` is the main JupyterHub configuration, it is mounted in docker compose file (`docker-compose.dev.yaml`). 
3. All needed customization changes and logic can be done in `jupyterhub_config.py`. Mainly, they will be applied to classes:
   - DockerSpawner (https://github.com/jupyterhub/dockerspawner/tree/main/examples/image_form, https://jupyterhub-dockerspawner.readthedocs.io/en/latest/api/index.html)
   - GenericOAuthenticator (https://oauthenticator.readthedocs.io/en/latest/reference/api/gen/oauthenticator.generic.html#)

4. There are few other Jupyter dependencies in the following GIT repos:
 - https://github.com/national-data-platform/ndp-jupyterlab-extension - NDP extension for JupyterLab. It is being installed on single-user server container.
 - https://github.com/national-data-platform/jupyterlab-git - Special version of JupyterLab GIT extension. It was created to allow passing GIT link into GIT Clone dialog for NDP needs. It is being installed on single-user server container.

5. A number of environment variables has to be set in `.env` file, passed to `docker-compose.yaml` file and processed in `jupyterhub_config.py` in order the overall deployment to work.
6. All NDP docker images and Python packages(PyPi) are stored in NRP Gitlab (https://gitlab.nrp-nautilus.io/).
- **Gitlab Container Registry (for Docker images)**. Enter your Gitlab username and personal access token:
``
docker login gitlab-registry.nrp-nautilus.io
``
Now, you should be able to push images to our Gitlab registry. For example: 
```
docker push gitlab-registry.nrp-nautilus.io/ndp/ndp-docker-images/jh:2.0.10
```
Our images are located at: https://gitlab.nrp-nautilus.io/ndp/ndp-docker-images/container_registry

- **GitLab Package Registry (for PyPi packages)**.
To be able to push or pull private Python packages, the local machine should be set up according to the instructions at https://gitlab.nrp-nautilus.io/help/user/packages/package_registry/index.
Add authentication (https://gitlab.nrp-nautilus.io/help/user/packages/pypi_repository/index.md#authenticate-with-a-deploy-token).

Create file: ~/.pypirc
```
[distutils]
index-servers =
    gitlab

[gitlab]
repository = https://gitlab.nrp-nautilus.io/api/v4/projects/ndp%2Fndp-docker-images/packages/pypi
username = <your_personal_access_token_name>
password = <your_personal_access_token>
```
After that, you'll be able to push PyPi packages, so they can be installed later by standard pip command:
```
pip install jupyterlab-git ndp-jupyterlab-extension --index-url https://gitlab.nrp-nautilus.io/api/v4/projects/3930/packages/pypi/simple
```
Our packages are located at: https://gitlab.nrp-nautilus.io/ndp/ndp-docker-images/-/packages


### README.md (6,777 bytes)

# NDP JupyterHub
## Core Documentation
- JupyterHub Deployment documentation on [Nautilus](https://docs.nationalresearchplatform.org/userdocs/jupyter/jupyterhub/)
- JupyterHub with z2jh can be found at https://z2jh.jupyter.org/

## Basic Set Up for NDP JupyterHub Customization

### Prepare Nautilus Namespace and Local Configuration

Use this [documentation](https://docs.nationalresearchplatform.org/) for comprehensive Nautilus setup:

1. Create a namespace using the Nautilus portal or use one of the NDP official namespaces (`ndp` / `ndp-staging` / `ndp-test`).
2. Ask NRP support to make you an admin in that namespace
3. Download `kubeconfig` file from the Nautilus portal

### Set up helm in your namespace

1. Download and install [`helm`](https://helm.sh/) locally:
   (source: https://z2jh.jupyter.org/en/stable/kubernetes/setup-helm.html)
   
   ```bash
   curl https://raw.githubusercontent.com/helm/helm/HEAD/scripts/get-helm-3 | bash
   helm version
   ```
   
   You can use [other installation methods](https://github.com/kubernetes/helm/blob/master/docs/install.md)
   if curling into bash bothers you.

### Install JupyterHub
1. Make Helm aware of the JupyterHub Helm chart repository so you can install the JupyterHub chart from it without having to use a long URL name.
   (source: https://z2jh.jupyter.org/en/stable/jupyterhub/installation.html#install-jupyterhub)
    ```bash
    helm repo add jupyterhub https://hub.jupyter.org/helm-chart/
    helm repo update
    ```
2. Fetch the version of JupyterHub chart mentioned in `helm/ndp-hub/requirements.yaml`.

   ```bash
   cd helm/ndp-hub
   helm dependency build
   helm dep up
   cd ..
   ```

3. Add random bytes for proxy:

   ```bash
   openssl rand -hex 32
   ```
   
   Add/replace output to `ndp-hub/values_<env>.yaml`:
  
   ```
   jupyterhub:
     proxy:
       secretToken: "..."
   ```

4. Create kubernetes secret
- In `jhub/helm/ndp-hub/jupyterhub_secret.yaml`, insert the client/secret values obtained from NDP admins
- Execute:
   ```bash
   kubectl create secret generic jupyterhub-secret --from-file=values.yaml=jhub/helm/ndp-hub/jupyterhub_secret.yaml --namespace <namespace>
   ```

5. Install the hub
- TEST
   ```bash
   make deploy-test
   ```
- STAGING
   ```bash
   make deploy-staging
   ```
- PRODUCTION
   ```bash
   make deploy-prod
   ```

6. Wait for the pods to be ready, and go to the URL specified in `jhub/helm/ndp-hub/values_env.yaml`:
   - https://ndp-test-jupyterhub.nrp-nautilus.io/
   - https://ndp-staging-jupyterhub.nrp-nautilus.io/
   - https://ndp-jupyterhub.nrp-nautilus.io/

7. To uninstall the deployment:
   
   ```bash
   helm uninstall ndp-hub --kube-context nautilus --namespace <namespace>
   ```
   
### Important Notes
1. Before making deployment to any environment, make sure to deploy the `helm/ndp-hub/jupyterhub_secret.yaml` with Keycloak secrets.

2.
- `helm/ndp-hub` folder contains 3 `values_env.yaml` Helm configuration files, corresponding to different environments:
   - `values_test.yaml`
   - `values_staging.yaml`
   - `values_prod.yaml`

- `helm/ndp-hub` folder contains 3 `spawner_env.py` complimentary configuration files, such that values_env.yaml references spawner_env.py:
  - `spawner_test.py`
  - `spawner_staging.py`
  - `spawner_prod.py`

   For example, values_test.yaml file has reference to spawner_test.py. This has been done in order to decouple YAML values from Python and HTML code.
   Each pair of files create unique customized deployment of NDP JupyterHub per each environment.
3. The pre-built images that appear in spawner_env.py files can be modified and built using Dockerfiles inside `images` folder. Each image corresponds to NDP use case such as:
   - NAIRR
   - PGML
   - Earthscope
   - Others

   Note: the content notebooks and other files inside the image typically is downloaded from separate repo:
   - https://github.com/national-data-platform/jupyter-notebooks
4. There are few other Jupyter dependencies in the following GIT repos:
 - ~~https://github.com/national-data-platform/jupyter-templates - this is to override few UI web pages, based on this guide: https://jupyterhub.readthedocs.io/en/stable/howto/templates.html#extending-templates.~~ Note: this is not needed anymore as pics and templates are hardcoded into hub image (helm/k8s_hub_docker_image/Dockerfile).
 - https://github.com/national-data-platform/ndp-jupyterlab-extension - NDP extension for JupyterLab. It is being installed on single-user server instance each time while spawning. Defined in `spawner_env.py` files.
 - https://github.com/national-data-platform/jupyterlab-git - Special version of JupyterLab GIT extension. It was created to allow passing GIT link into GIT Clone dialog for NDP needs. It is being installed on single-user server instance each time while spawning. Defined in `spawner_env.py` files.
5. The main JupyterHub image is customized as well to be able to serve NDP logo images. It can be modified and built from `helm/k8s_hub_docker_image/Dockerfile`. In case of creating new image version, it has to be modified inside `helm/ndp-hub/values_<env>.yaml` files:
   ```
   hub:
     image:
       name: gitlab-registry.nrp-nautilus.io/ndp/ndp-docker-images/jh
       tag: "2.0.9"
   ```
   
6. All NDP docker images and Python packages(PyPi) are stored in NRP Gitlab (https://gitlab.nrp-nautilus.io/).
- **Gitlab Container Registry (for Docker images)**. Enter your Gitlab username and personal access token:
``
docker login gitlab-registry.nrp-nautilus.io
``
Now, you should be able to push images to our Gitlab registry. For example: 
```
docker push gitlab-registry.nrp-nautilus.io/ndp/ndp-docker-images/jh:2.0.10
```

Our images are located at: https://gitlab.nrp-nautilus.io/ndp/ndp-docker-images/container_registry

- **GitLab Package Registry (for PyPi packages)**.
To be able to push or pull private Python packages, the local machine should be set up according to the instructions at https://gitlab.nrp-nautilus.io/help/user/packages/package_registry/index.
Add authentication (https://gitlab.nrp-nautilus.io/help/user/packages/pypi_repository/index.md#authenticate-with-a-deploy-token).

Create file: ~/.pypirc
```
[distutils]
index-servers =
    gitlab

[gitlab]
repository = https://gitlab.nrp-nautilus.io/api/v4/projects/ndp%2Fndp-docker-images/packages/pypi
username = <your_personal_access_token_name>
password = <your_personal_access_token>
```
After that, you'll be able to push PyPi packages, so they can be installed later by standard pip command:
```
pip install jupyterlab-git ndp-jupyterlab-extension --index-url https://gitlab.nrp-nautilus.io/api/v4/projects/3930/packages/pypi/simple
```

Our packages are located at: https://gitlab.nrp-nautilus.io/ndp/ndp-docker-images/-/packages


### helm-generic/README.md (7,728 bytes)

# Generic NDP JupyterHub Kubernetes Deployment Documentation

This guide provides instruction for deploying the generic NDP JupyterHub Helm chart.

## Prerequisites

Ensure you have `kubectl` and `helm` installed and configured to interact with your Kubernetes cluster.

Nginx ingress controller is installed on your cluster; if not, you can follow [installation guide](https://docs.nginx.com/nginx-ingress-controller/installation/installing-nic/).

## Additional Resources

For more information on `kubectl` and `helm`, refer to the following resources:

- [kubectl Installation Guide](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- [Helm Installation Guide](https://helm.sh/docs/intro/install/)
- [Helm Documentation](https://helm.sh/docs/intro/using_helm/)

## **Installation**

1. #### **Copy and edit the example once so all targets share the same settings:**

    ```bash
    cp config.example.mk config.mk
    ```
    Then open ./config.mk and set values<br>
    ```bash
    vi config.mk
    ```
    [Optional: Click to see example `config.mk`](#configmk-settings)

2. #### **Setting Up Keycloak Client Credentials**

    Create a local secret file from the template (kept out of git):

    ```bash
    cp ./ndp-hub/jupyterhub_secret.yaml.template ./ndp-hub/jupyterhub_secret.yaml
    ```

    Then open ./ndp-hub/jupyterhub_secret.yaml and fill in the **`client_id`** and **`client_secret`** values provided by your NDP administrators: [support@nationaldataplatform.org](mailto:support@nationaldataplatform.org)
    ```bash
    vi ./ndp-hub/jupyterhub_secret.yaml
    ```

    Once the file is ready, apply the secret to your cluster: 
    >Quick heads-up: This command will create a Kubernetes secret containing your Keycloak client credentials you provided in `./ndp-hub/jupyterhub_secret.yaml`, which JupyterHub will use for authentication. Further details are in the [JupyterHub Secret Explanation](#jupyterhub-secret-explaination) section below.

    ```bash
    make create-jhub-secret
    ```

3. #### **Centralize Site Overrides**

    Copy the example file and fill in the fields that matter for your site:

    ```bash
    cp ./ndp-hub/site-values.example.yaml ./ndp-hub/site-values.yaml
    ```
    Then open ./ndp-hub/site-values.yaml and set values<br>
    ```bash
    vi ./ndp-hub/site-values.yaml
    ```
    For details and examples, [click to see the `Custom Site Values` section below](#custom-site-values)

4. #### **Update Helm Chart Dependencies:** Fetch and update Helm chart dependencies listed in `Chart.yaml`

   ```bash
   make update
   ```

5. #### **Deploy JupyterHub:** Install/upgrade the generic NDP JupyterHub in the target namespace using Helm
    
    >Quick heads-up: This Make target automatically layers `ndp-hub/site-values.yaml` (when present) on top of the defaults(`values.yaml`) and injects `spawner.py` via `--set-file`.

   ```bash
   make deploy
   ```

## **Access your JupyterHub**
`http://<ingress-host>/jupyter/`

## **Optional follow-up**: verify and cleanup

`make status`: Run to confirm helm release is healthy.<br>
`make get-ingress`: Grab the ingress endpoint when you need the URL.<br>
`make uninstall`: Remove the helm release.<br>
`make delete-jhub-secret`: Delete the jupyterhub-secret from the cluster.

## Next Steps
Go back to [**SciDx Kubernetes Document**](https://github.com/sci-ndp/scidx-k8s/tree/main#deploy-jupyterhub) for more details about the overall Kubernetes setup for SciDx service.

<br>

## config.mk Settings
`KUBE_CONTEXT`: kubernetes cluster context (defaults to **kubectl config current-context** if leaves empty, or **"microk8s"** if none).

`NAMESPACE`: namespace to deploy generic NDP Jupyterhub into (default: **ndp-jhub**).

`RELEASE_NAME`: Helm release name for generic NDP JupyterHub deployment (default: **ndp-jhub**).

Example:
```mk
KUBE_CONTEXT = arn:aws:eks:us-west-2:xxxxxxxxxxxx:cluster/cluster-name
HELM_RELEASE = ndp-jhub
NAMESPACE = ndp-jhub
```
[Back to `Installation`](#copy-and-edit-the-example-once-so-all-targets-share-the-same-settings)

## Custom Site Values

Goal: fill in `ndp-hub/site-values.yaml`. <br>
Gather these first:
   1. `Namespace`, it should be the same defined in config.mk → NAMESPACE;
   2. `DNS hostname` of your ingress controller users will hit (e.g., ndp-dev-202.chpc.utah.edu);
   3. `Client ID` from NDP admins, same as in jupyterhub_secret.yaml;
   4. `Group name` from NDP admins, to allow users in that group to login (e.g., jhub_user);
   5. `Admin user email`, at least one;
   6. `StorageClass names` to use for PVCs; run `kubectl get storageclass` if unsure.
   7. `Ingress class name` of your cluster ingress controller; run `kubectl get ingressclass` if unsure.


<br>Then open ndp-hub/site-values.yaml and replace every `<...>` in the template below.

>Caveats:
>1. Replace every `<...>` before deploying. `client_id` here must match the one in `ndp-hub/jupyterhub_secret.yaml`. 
>2. Make sure the keycloak url(`https://idp.nationaldataplatform.org`) in logout_redirect_url matches the NDP_KEYCLOAK_URL in extraEnv, consult NDP admins if unsure: [support@nationaldataplatform.org](mailto:support@nationaldataplatform.org).
>3. The namespace in extraEnv(`NDP_JUPYTERHUB_NAMESPACE`) must match the `NAMESPACE` in config.mk.

```yaml
# ndp-hub/site-values.yaml
jupyterhub:
  ingress:
    ingressClassName: <nginx>               # change if your ingress class is different
    hosts:
      - <hub.example.com>                   # REQUIRED: your DNS hostname
  hub:
    config:
      GenericOAuthenticator:
        oauth_callback_url: https://<hub.example.com>/jupyter/hub/oauth_callback   # same host as above
        logout_redirect_url: https://idp.nationaldataplatform.org/realms/NDP/protocol/openid-connect/logout?post_logout_redirect_uri=https://<hub.example.com>/jupyter/&client_id=<your-client-id>
        allowed_groups:
          - <your-keycloak-group>           # e.g., jhub_user
        admin_users:
          - <admin@example.com>             # admin user email 
    extraEnv:
      NDP_JUPYTERHUB_NAMESPACE: <ndp-jhub>  # must match config.mk NAMESPACE
      NDP_KEYCLOAK_URL: https://idp.nationaldataplatform.org
      NDP_KEYCLOAK_REALM: NDP
      PVC_STORAGE_CLASS: <storage-class>    # group shared PVCs; e.g., microk8s-hostpath, gp2, etc.
    db:
      pvc:
        storageClassName: <storage-class>   # hub DB PVC
  singleuser:
    storage:
      dynamic:
        storageClass: <storage-class>       # per-user PVC
```

### What you just configured
- **Auth**: Callback/logout URLs, which Keycloak groups can log in, and who gets JupyterHub admin.
- **Spawner env**: Namespace (`NDP_JUPYTERHUB_NAMESPACE`) and storage class the spawner uses; `spawner.py` reads these from `jupyterhub.hub.extraEnv`.
- **Storage**: StorageClass for the hub database PVC and for each user’s PVC.
- **Ingress**: Which ingress controller/class to bind to and which hostnames your DNS/TLS should cover.

[Back to `Installation`](#centralize-site-overrides)

## JupyterHub Secret Explaination

By executing `make create-jhub-secret`, you basically run:

```sh
kubectl create secret generic jupyterhub-secret \
  --from-file=values.yaml=jupyterhub_secret.yaml \
  -n jupyterhub
```

- The `--from-file=values.yaml=jupyterhub_secret.yaml` flag loads the contents of `jupyterhub_secret.yaml` into the secret under the key `values.yaml`.
- The resulting secret will look like:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: jupyterhub-secret
data:
  values.yaml: <base64-encoded contents of jupyterhub_secret.yaml>
```

[Back to `Installation`](#setting-up-keycloak-client-credentials)
