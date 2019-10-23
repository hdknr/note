# ArangDB プログラム

- https://www.arangodb.com/docs/stable/programs.html

| Binary name     | Brief description |
|-----------------|-------------------|
| `arangod`       | [ArangoDB サーバー](arangodb.arangod.md). [WEBインターフェース](arangodb.web-ui.md)
| `arangosh`      | [ArangoDB シェル](arangodb.arangosh.md). REPLとサーバー管理
| `arangodb`      | [ArangoDB Starter](programs-starter.html) for easy deployment of ArangoDB instances.
| `arangodump`    | Tool to [create backups](programs-arangodump.html) of an ArangoDB database.
| `arangorestore` | Tool to [load backups](programs-arangorestore.html) back into an ArangoDB database.
| `arangobackup`  | Tool to [perform hot backup operations](programs-arangobackup.html) on an ArangoDB installation.
| `arangoimport`  | [Bulk importer](programs-arangoimport.html) for the ArangoDB server. It supports JSON and CSV.
| `arangoexport`  | [Bulk exporter](programs-arangoexport.html) for the ArangoDB server. It supports JSON, CSV and XML.
| `arango-dfdb`   | [Datafile debugger](programs-arango-dfdb.html) for ArangoDB (MMFiles storage engine only).
| `arangobench`   | [Benchmark and test tool](programs-arangobench.html). It can be used for performance and server function testing.
| `arangoinspect` | [Inspection tool](programs-arangoinspect.html) that gathers server setup information.
| `arangovpack`   | Utility to convert [VelocyPack](https://github.com/arangodb/velocypack){:target="_blank"} data to JSON.

The client package comes with a subset of programs and tools:

- arangosh
- arangoimport
- arangoexport
- arangodump
- arangorestore
- arangobackup
- arangobench
- arangoinspect
- arangovpack

Additional tools which are available separately:

| Name            | Brief description |
|-----------------|-------------------|
| [Foxx CLI](programs-foxx-cli.html) | Command line tool for managing and developing Foxx services
| [kube-arangodb](deployment-kubernetes.html) | Operators to manage Kubernetes deployments
