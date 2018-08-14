# kubectl create: リソースの作成

~~~bash
$ kubectl create  --help
Create a resource from a file or from stdin.

JSON and YAML formats are accepted.

Examples:
  # Create a pod using the data in pod.json.
  kubectl create -f ./pod.json

  # Create a pod based on the JSON passed into stdin.
  cat pod.json | kubectl create -f -

  # Edit the data in docker-registry.yaml in JSON using the v1 API format then create the resource using the edited
data.
  kubectl create -f docker-registry.yaml --edit --output-version=v1 -o json

Available Commands:
  clusterrole         Create a ClusterRole.
  clusterrolebinding  Create a ClusterRoleBinding for a particular ClusterRole
  configmap           Create a configmap from a local file, directory or literal value
  deployment          Create a deployment with the specified name.
  job                 Create a job with the specified name.
  namespace           Create a namespace with the specified name
  poddisruptionbudget Create a pod disruption budget with the specified name.
  priorityclass       Create a priorityclass with the specified name.
  quota               Create a quota with the specified name.
  role                Create a role with single rule.
  rolebinding         Create a RoleBinding for a particular Role or ClusterRole
  secret              Create a secret using specified subcommand
  service             Create a service using specified subcommand.
  serviceaccount      Create a service account with the specified name

Options:
      --allow-missing-template-keys=true: If true, ignore any errors in templates when a field or map key is missing in
the template. Only applies to golang and jsonpath output formats.
      --dry-run=false: If true, only print the object that would be sent, without sending it.
      --edit=false: Edit the API resource before creating
  -f, --filename=[]: Filename, directory, or URL to files to use to create the resource
      --include-extended-apis=true: If true, include definitions of new APIs via calls to the API server. [default true]
      --no-headers=false: When using the default or custom-column output format, don't print headers (default print
headers).
  -o, --output='': Output format. One of:
json|yaml|wide|name|custom-columns=...|custom-columns-file=...|go-template=...|go-template-file=...|jsonpath=...|jsonpath-file=...
See custom columns [http://kubernetes.io/docs/user-guide/kubectl-overview/#custom-columns], golang template
[http://golang.org/pkg/text/template/#pkg-overview] and jsonpath template
[http://kubernetes.io/docs/user-guide/jsonpath].
      --raw='': Raw URI to POST to the server.  Uses the transport specified by the kubeconfig file.
      --record=false: Record current kubectl command in the resource annotation. If set to false, do not record the
command. If set to true, record the command. If not set, default to updating the existing annotation value only if one
already exists.
  -R, --recursive=false: Process the directory used in -f, --filename recursively. Useful when you want to manage
related manifests organized within the same directory.
      --save-config=false: If true, the configuration of current object will be saved in its annotation. Otherwise, the
annotation will be unchanged. This flag is useful when you want to perform kubectl apply on this object in the future.
  -l, --selector='': Selector (label query) to filter on, supports '=', '==', and '!='.(e.g. -l key1=value1,key2=value2)
  -a, --show-all=true: When printing, show all resources (default show all pods including terminated one.)
      --show-labels=false: When printing, show all labels as the last column (default hide labels column)
      --sort-by='': If non-empty, sort list types using this field specification.  The field specification is expressed
as a JSONPath expression (e.g. '{.metadata.name}'). The field in the API resource specified by this JSONPath expression
must be an integer or a string.
      --template='': Template string or path to template file to use when -o=go-template, -o=go-template-file. The
template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].
      --validate=true: If true, use a schema to validate the input before sending it
      --windows-line-endings=false: Only relevant if --edit=true. Defaults to the line ending native to your platform.

Usage:
  kubectl create -f FILENAME [options]

Use "kubectl <command> --help" for more information about a given command.
Use "kubectl options" for a list of global command-line options (applies to all commands).
~~~

[kubectl Cheat Sheet - Kubernetes](https://kubernetes.io/docs/reference/kubectl/cheatsheet/) より:

~~~bash 
kubectl create -f ./my-manifest.yaml           # create resource(s)
kubectl create -f ./my1.yaml -f ./my2.yaml     # create from multiple files
kubectl create -f ./dir                        # create resource(s) in all manifest files in dir
kubectl create -f https://git.io/vPieo         # create resource(s) from url
kubectl run nginx --image=nginx                # start a single instance of nginx
kubectl explain pods,svc                       # get the documentation for pod and svc manifests

# Create multiple YAML objects from stdin
cat <<EOF | kubectl create -f -
apiVersion: v1
kind: Pod
metadata:
  name: busybox-sleep
spec:
  containers:
  - name: busybox
    image: busybox
    args:
    - sleep
    - "1000000"
---
apiVersion: v1
kind: Pod
metadata:
  name: busybox-sleep-less
spec:
  containers:
  - name: busybox
    image: busybox
    args:
    - sleep
    - "1000"
EOF

# Create a secret with several keys
cat <<EOF | kubectl create -f -
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: Opaque
data:
  password: $(echo -n "s33msi4" | base64)
  username: $(echo -n "jane" | base64)
EOF
~~~


## 例

[Kubernetes の学習 (2) ～ Pod の作成 - Qiita](https://qiita.com/Arturias/items/62499b961b5d7375f608)

~~~bash 
$ kubectl get pod
No resources found.
~~~

~~~bash 
$ cat <<EOF | kubectl create -f -
> apiVersion: v1
> kind: Pod
> metadata:
>   name: nginx-pod
> spec:
>   containers:
>     - name: nginx-container
>       image: nginx
>       ports:
>       - containerPort: 80
> EOF
pod "nginx-pod" created
~~~

~~~bash
$ kubectl get pod
NAME        READY     STATUS              RESTARTS   AGE
nginx-pod   0/1       ContainerCreating   0          20s
~~~


~~~bash 
$ kubectl describe pods nginx-pod
Name:         nginx-pod
Namespace:    default
Node:         docker-for-desktop/192.168.65.3
Start Time:   Sun, 12 Aug 2018 11:34:07 +0900
Labels:       <none>
Annotations:  <none>
Status:       Running
IP:           10.1.0.10
Containers:
  nginx-container:
    Container ID:   docker://2a71f6d7d45acf9ef5a6c4ba743f726bd8a047b7e188a3a0d537036da736b3ad
    Image:          nginx
    Image ID:       docker-pullable://nginx@sha256:d85914d547a6c92faa39ce7058bd7529baacab7e0cd4255442b04577c4d1f424
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Sun, 12 Aug 2018 11:35:09 +0900
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-kzjfw (ro)
Conditions:
  Type           Status
  Initialized    True
  Ready          True
  PodScheduled   True
Volumes:
  default-token-kzjfw:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-kzjfw
    Optional:    false
QoS Class:       BestEffort
Node-Selectors:  <none>
Tolerations:     node.kubernetes.io/not-ready:NoExecute for 300s
                 node.kubernetes.io/unreachable:NoExecute for 300s
Events:
  Type    Reason                 Age   From                         Message
  ----    ------                 ----  ----                         -------
  Normal  Scheduled              1m    default-scheduler            Successfully assigned nginx-pod to docker-for-desktop
  Normal  SuccessfulMountVolume  1m    kubelet, docker-for-desktop  MountVolume.SetUp succeeded for volume "default-token-kzjfw"
  Normal  Pulling                1m    kubelet, docker-for-desktop  pulling image "nginx"
  Normal  Pulled                 2s    kubelet, docker-for-desktop  Successfully pulled image "nginx"
  Normal  Created                2s    kubelet, docker-for-desktop  Created container
  Normal  Started                2s    kubelet, docker-for-desktop  Started container
~~~


~~~bash 
$ kubectl exec nginx-pod cat /proc/version
Linux version 4.9.93-linuxkit-aufs (root@856d34d1168e) (gcc version 6.4.0 (Alpine 6.4.0) ) #1 SMP Wed Jun 6 16:55:56 UTC 2018
~~~

~~~bash
$ kubectl get pod
NAME        READY     STATUS    RESTARTS   AGE
nginx-pod   1/1       Running   0          14m
~~~

~~~bash
$ kubectl get svc
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   16d
~~~~


~~~bash 
$ kubectl delete pod nginx-pod
pod "nginx-pod" deleted
~~~

~~~bash 
$ kubectl get pod
No resources found.
~~~