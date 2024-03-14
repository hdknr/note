# イメージ管理


## 一覧(ls)

~~~bash
$ docker image ls
REPOSITORY                                 TAG                 IMAGE ID            CREATED             SIZE
django-history                             latest              ce0df70629a6        14 minutes ago      1.08GB
docker/kube-compose-controller             v0.3.9              16260a912a7b        8 weeks ago         29.9MB
docker/kube-compose-api-server             v0.3.9              8757267f7b06        8 weeks ago         42.5MB
k8s.gcr.io/kube-proxy-amd64                v1.10.3             4261d315109d        2 months ago        97.1MB
k8s.gcr.io/kube-scheduler-amd64            v1.10.3             353b8f1d102e        2 months ago        50.4MB
k8s.gcr.io/kube-controller-manager-amd64   v1.10.3             40c8d10b2d11        2 months ago        148MB
k8s.gcr.io/kube-apiserver-amd64            v1.10.3             e03746fe22c3        2 months ago        225MB
k8s.gcr.io/etcd-amd64                      3.1.12              52920ad46f5b        5 months ago        193MB
k8s.gcr.io/k8s-dns-dnsmasq-nanny-amd64     1.14.8              c2ce1ffb51ed        7 months ago        41MB
k8s.gcr.io/k8s-dns-sidecar-amd64           1.14.8              6f7f2dc7fab5        7 months ago        42.2MB
k8s.gcr.io/k8s-dns-kube-dns-amd64          1.14.8              80cc5ea4b547        7 months ago        50.5MB
k8s.gcr.io/pause-amd64                     3.1                 da86e6ba6ca1        7 months ago        742k
~~~


## イメージの削除(rm)

~~~bash
$ docker image rm ce0df70629a6
Error response from daemon: conflict: unable to delete ce0df70629a6 (must be forced) - image is being used by stopped container 33c5663efe9d
~~~

### <none> を一括して削除

古いコマンド:

~~~bash
$ docker rmi -f $(docker images -f "dangling=true" -q)
~~~

新しいコマンド：

~~~bash
$ docker image rm -f $(docker image ls -f "dangling=true" -q)
~~~

## 全削除

~~~bash
docker images -aq | xargs docker rmi
~~~

## `down` して全削除

~~~bash
docker-compose down --rmi all --volumes --remove-orphans
~~~

## 記事

-[ docker images を全削除する](https://qiita.com/fist0/items/2fb1c7f894b5bdff79f4)
