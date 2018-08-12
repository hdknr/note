#  ビルド/リリース/実行

- https://12factor.net/build-release-run
- `Strictly separate build and run stages`


Dockerビルド:

- docker build

K8s リリース:

- kubctrl apply -f ....
- kubctrl create -f ....

Helm実行:

- helm install
- helm update