---
title: Tips on GCP
created: '2022-05-09T23:39:30-07:00'
date: '2026-11-25T03:20:00-08:00'
authors:
  - bendu
label: tips-on-gcp
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Google
  - cloud
  - GCP
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## GCP Free Tier

The [Google Cloud Free Program](https://cloud.google.com/free/docs/gcp-free-tier) provides an **Always Free** tier for core services (with monthly or daily usage limits) that does not expire after the initial free trial. See [GCP Free Tier Usage Limits](https://cloud.google.com/free/docs/gcp-free-tier#free-tier-usage-limits) for full details.

Notable Always Free limits include:

- **Compute Engine**: 1 non-preemptible `e2-micro` VM instance per month in eligible US regions (`us-west1`, `us-central1`, `us-east1`), plus 30 GB-months of Standard Persistent Disk.
- **Cloud Run**: 2 million requests, 180,000 vCPU-seconds, 360,000 GiB-seconds, and 1 GB of North America outbound data transfer per month.
- **Cloud Storage**: 5 GB-months of Standard Storage in eligible US regions (`us-central1`, `us-east1`, `us-west1`), plus monthly Class A/B operation allowances.
- **BigQuery**: 1 TB of queried data and 10 GB of active storage per month.
- **Cloud Build**: 2,500 build-minutes per month.
- **Cloud Shell**: Free browser-based shell and editor with 5 GB of persistent `$HOME` storage.

```{important}
Always Free compute and storage resources generally require eligible US regions (`us-central1`, `us-east1`, `us-west1`). GCP does not automatically stop services when you exceed free limits, so set up **Billing Budgets and Alerts** to avoid unexpected charges.
```

## Google Cloud Shell

[Google Cloud Shell](https://cloud.google.com/shell/docs/using-cloud-shell) provides a browser-based Linux terminal together with the **Cloud Shell Editor** (a VS Code-based IDE). It comes with `gcloud` and common developer tools preinstalled and includes 5 GB of persistent `$HOME` storage across sessions (reclaimed if unused for 120 days).

## Google Cloud CLI (SDK)

Please refer to [Install the Google Cloud CLI](https://cloud.google.com/sdk/docs/install-sdk#deb) (or the [Cloud SDK overview](https://cloud.google.com/sdk)) for installation instructions.

```bash
gcloud init
gcloud auth application-default login
```

## Core Compute Services

| GCP Service | Workload Model | Deployment Unit | AWS Equivalent | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Compute Engine** | IaaS virtual machines | VM image / OS disk | EC2 | Full OS control; use [Spot VMs](https://cloud.google.com/spot-vms/) for fault-tolerant, lower-cost workloads |
| **Cloud Run** | Serverless containers | Container image (OCI / Dockerfile) | ECS / Fargate | Scales to zero; supports HTTP, gRPC, WebSockets, GPUs, and arbitrary runtimes |
| **Cloud Run functions** *(formerly Cloud Functions)* | Function-as-a-Service (FaaS) | Source code + handler entry point | Lambda | Event/HTTP handlers; Google builds the container via Buildpacks on Cloud Run |
| **App Engine** | Managed PaaS | App source + `app.yaml` | Elastic Beanstalk | Opinionated web app hosting; Cloud Run is preferred for most new workloads |

### Cloud Run vs. Cloud Run functions (formerly Cloud Functions)

Google unified **Cloud Functions** (2nd gen) into **Cloud Run functions**, so both now run on the same underlying Cloud Run container infrastructure:

- **Cloud Run functions**: You supply source code and a function entry point (for lightweight HTTP endpoints, glue code, or event triggers via Pub/Sub and Eventarc), and Google automatically builds and deploys the container using Buildpacks.
- **Cloud Run (Services)**: You supply a custom container image (via `Dockerfile` or custom binaries), giving you full control over system dependencies, multi-route web apps, microservices, and custom runtimes.

## Cloud Storage

[Google Cloud Storage](https://cloud.google.com/storage/pricing) is GCP's managed object storage service (analogous to AWS S3). It offers four main storage classes based on access frequency:

- **Standard**: Frequently accessed ("hot") data.
- **Nearline**: Data accessed less than once a month (30-day minimum storage duration).
- **Coldline**: Data accessed less than once a quarter (90-day minimum storage duration).
- **Archive**: Long-term archival data accessed less than once a year (365-day minimum storage duration).

See [](#cloud-object-storage) for general object storage notes.

## BigQuery

**BigQuery** is GCP's serverless, petabyte-scale data warehouse with built-in SQL analytics, ML integration, and separation of storage and compute. See [](#tips-on-bigquery) for detailed notes.

## Cloud Build

[Google Cloud Build](https://cloud.google.com/build/docs) is GCP's managed CI/CD service (comparable to GitHub Actions for GCP-centric pipelines). It executes builds defined in `cloudbuild.yaml` (or Dockerfiles), integrates tightly with **Artifact Registry** for storing container images and language packages, and deploys directly to Cloud Run, GKE, or App Engine.

## Cloud IAM

**Cloud IAM** (Identity and Access Management) controls who (*principals*: Google accounts, service accounts, Google Groups) has what access (*roles*: sets of permissions) on which GCP resources (*policies*). For CI/CD or external workloads (such as GitHub Actions), prefer **Workload Identity Federation** over long-lived service account JSON keys.

- [Google Cloud IAM Overview (YouTube)](https://www.youtube.com/watch?v=xQClVtAECdg)

## Cloud Observability (formerly Cloud Operations)

[Google Cloud Observability](https://cloud.google.com/products/operations) (formerly Cloud Operations / Stackdriver) is the unified monitoring and telemetry suite on GCP, including:

- **Cloud Logging**: Centralized log ingestion, search, and Log Analytics.
- **Cloud Monitoring**: Infrastructure and application metrics, dashboards, uptime checks, and alerting.
- **Cloud Trace** & **Cloud Profiler**: Distributed request tracing and continuous CPU/memory profiling.

## References

- [](#tips-on-gcp-compute-engine)
- [](#gcp-compute-engine-vm-instances)
- [](#tips-on-bigquery)
- [](#cloud-object-storage)
- [](#comparison-of-popular-cloud-platforms)
- [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc)
