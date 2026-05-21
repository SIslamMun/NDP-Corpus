# ndp-ep-helm

> NDP-Endpoint Helm chart 

## Documentation Files

### README.md (882 bytes)

# NDP-EP Helm Chart

Register an endpoint on https://nationaldataplatform.org/endpoints/create (click `Generate Script` and ignore generated script) to register your ndp-endpoint on `Federation`.<br>
Or https://federation.ndp.utah.edu/docs, query `/ep/simple` to directly register your endpoint on `Federation`. Copy the `config-id`. 

One-liner install:
```
bash <(curl -sL https://raw.githubusercontent.com/sci-ndp/ndp-ep-helm/main/helm.sh) \
    --config-id <xxxxxxxxxxxxxx> \
    --host <your-host> \
    --storage-class <your-storage-class> \
    --ingress-class <your-ingress-class>
```

Access:
- **NDP EP UI:** `https://<ingress-host>/ep/ui`
- **NDP EP API Docs:** `https://<ingress-host>/ep/api/docs`
- **CKAN:** `https://<ingress-host>/ckan`
- **NDP JHub:** `https://<ingress-host>/jupyter` if it's enabled
- **Kafka:** `kcat -L -b <ingress-host>:31090` if it's enabled

---

### helm/ckan/templates/NOTES.txt (1,906 bytes)

1. Get the application URL by running these commands:
{{- if .Values.ingress.enabled }}
{{- range $host := .Values.ingress.hosts }}
  {{- range .paths }}
  http{{ if $.Values.ingress.tls }}s{{ end }}://{{ $host.host }}{{ . }}
  {{- end }}
{{- end }}
{{- else if contains "NodePort" .Values.service.type }}
  export NODE_PORT=$(kubectl get --namespace {{ .Release.Namespace }} -o jsonpath="{.spec.ports[0].nodePort}" services {{ include "ckan-chart.fullname" . }})
  export NODE_IP=$(kubectl get nodes --namespace {{ .Release.Namespace }} -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT
{{- else if contains "LoadBalancer" .Values.service.type }}
     NOTE: It may take a few minutes for the LoadBalancer IP to be available.
           You can watch the status of by running 'kubectl get --namespace {{ .Release.Namespace }} svc -w {{ include "ckan-chart.fullname" . }}'
  export SERVICE_IP=$(kubectl get svc --namespace {{ .Release.Namespace }} {{ include "ckan-chart.fullname" . }} --template "{{"{{ range (index .status.loadBalancer.ingress 0) }}{{.}}{{ end }}"}}")
  echo http://$SERVICE_IP:{{ .Values.service.port }}
{{- else if contains "ClusterIP" .Values.service.type }}
  export POD_NAME=$(kubectl get pods --namespace {{ .Release.Namespace }} -l "app.kubernetes.io/name={{ include "ckan-chart.name" . }},app.kubernetes.io/instance={{ .Release.Name }}" -o jsonpath="{.items[0].metadata.name}")
  kubectl --namespace {{ .Release.Namespace }} port-forward $POD_NAME 5000:5000
  echo "Visit http://127.0.0.1:5000 to use CKAN"
{{- end }}
2. Generate an API Token for the sysadmin user using the CKAN UI, replace it in your values file and replace the secret with the new value at runtime
  kubectl -n {namespace} create secret generic ckansysadminapitoken --from-literal=sysadminApiToken={insert_generated_api_token_here} --dry-run -o yaml | kubectl apply -f -

---

## Source Files

Source code files are processed separately by the processor.
File list:

- `.gitignore` (3,354 bytes)
- `helm.local.sh` (3,711 bytes)
- `helm.sh` (3,776 bytes)
- `helm/Chart.yaml` (1,224 bytes)
- `helm/ckan/Chart.yaml` (488 bytes)
- `helm/ckan/solr-init/solr-configset/solrconfig.xml` (42,558 bytes)
- `helm/ckan/solr-init/solr-init.py` (9,118 bytes)
- `helm/ckan/templates/beaker_sessions.yaml` (263 bytes)
- `helm/ckan/templates/ckan_workers.yaml` (8,907 bytes)
- `helm/ckan/templates/ckancredentials.yaml` (1,788 bytes)
- `helm/ckan/templates/ckansysadminapitoken.yaml` (148 bytes)
- `helm/ckan/templates/cronjob.yaml` (3,429 bytes)
- `helm/ckan/templates/deployment.yaml` (8,760 bytes)
- `helm/ckan/templates/hpa.yaml` (728 bytes)
- `helm/ckan/templates/ingress.yaml` (2,964 bytes)
- `helm/ckan/templates/ingressroute.yaml` (396 bytes)
- `helm/ckan/templates/postgrescredentials.yaml` (209 bytes)
- `helm/ckan/templates/psql-init-job.yaml` (1,560 bytes)
- `helm/ckan/templates/pvc.yaml` (380 bytes)
- `helm/ckan/templates/service.yaml` (370 bytes)
- `helm/ckan/templates/serviceaccount.yaml` (327 bytes)
- `helm/ckan/templates/solr-configset-configmap.yaml` (203 bytes)
- `helm/ckan/templates/solr-init-configmap.yaml` (200 bytes)
- `helm/ckan/templates/solr-init-job.yaml` (1,856 bytes)
- `helm/ckan/templates/tests/test-connection.yaml` (473 bytes)
- `helm/ckan/values.yaml` (16,027 bytes)
- `helm/kafka-kraft/Chart.yaml` (324 bytes)
- `helm/kafka-kraft/templates/kafka-cluster.yaml` (1,886 bytes)
- `helm/kafka-kraft/values.yaml` (908 bytes)
- `helm/ndp-ep-api/Chart.yaml` (136 bytes)
- `helm/ndp-ep-api/templates/deployment.yaml` (2,100 bytes)
- `helm/ndp-ep-api/templates/env-secret.yaml` (1,396 bytes)
- `helm/ndp-ep-api/templates/hpa.yaml` (801 bytes)
- `helm/ndp-ep-api/templates/ingress.yaml` (1,916 bytes)
- `helm/ndp-ep-api/templates/namespace.yaml` (183 bytes)
- `helm/ndp-ep-api/templates/root-path-configmap.yaml` (290 bytes)
- `helm/ndp-ep-api/templates/service.yaml` (473 bytes)
- `helm/ndp-ep-api/values.yaml` (1,160 bytes)
- `helm/ndp-jupyterhub/Chart.yaml` (241 bytes)
- `helm/ndp-jupyterhub/spawner.py` (25,705 bytes)
- `helm/ndp-jupyterhub/templates/hub-cluster-config.yaml` (863 bytes)
- `helm/ndp-jupyterhub/templates/ingress.yaml` (801 bytes)
- `helm/ndp-jupyterhub/templates/spawner-configmap.yaml` (405 bytes)
- `helm/ndp-jupyterhub/values.yaml` (5,674 bytes)
- `helm/templates/ckan-bootstrap-job.yaml` (5,803 bytes)
- `helm/templates/ckan-bootstrap-rbac.yaml` (1,846 bytes)
- `helm/templates/federation-fetch-job.yaml` (11,704 bytes)
- `helm/templates/federation-fetch-rbac.yaml` (1,624 bytes)
- `helm/values.yaml` (3,266 bytes)
