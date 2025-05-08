Status: published
Date: 2022-05-09 23:39:30
Modified: 2025-05-08 15:20:14
Author: Benjamin Du
Slug: tips-on-gcp
Title: Tips on GCP
Category: Computer Science
Tags: Computer Science, programming, Google, cloud, GCP

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

[Google Cloud Free Program](https://cloud.google.com/free/docs/gcp-free-tier)

Notice that lots of services can be used for free (with monthly limits).
For more details,
please refer to
[GCP Free Tier Usage Limits](https://cloud.google.com/free/docs/gcp-free-tier#free-tier-usage-limits)
.

https://cloud.google.com/compute/docs/general-purpose-machines#c3-standard

https://cloud.google.com/compute/docs/general-purpose-machines#c3-highcpu

https://cloud.google.com/compute/docs/general-purpose-machines#c3-highmem

https://cloud.google.com/compute/docs/compute-optimized-machines#c2_machine_types

https://cloud.google.com/compute/docs/compute-optimized-machines#c2d-standard

https://cloud.google.com/compute/docs/compute-optimized-machines#c2d-high-cpu

https://cloud.google.com/compute/docs/compute-optimized-machines#c2d-high-mem

## Google Cloud Shell

- [Using Google Cloud Shell](https://cloud.google.com/shell/docs/using-cloud-shell)

## Install Google Cloud CLI 

Please refer to
[Install the Google Cloud CLI](https://cloud.google.com/sdk/docs/install-sdk#deb)
for instructions.

gcloud init
gcloud auth application-default login

## GitHub Actions & GCP

- [actions-runner-controller](https://github.com/actions/actions-runner-controller)

- [Optimizing Costs with GitHub Actions: Dynamically Starting and Stopping Self-Hosted Runner VMs](https://nakamasato.medium.com/optimizing-costs-with-github-actions-self-hosted-runner-dynamically-starting-and-stopping-gcp-vms-c04acb69bdee)

1. You must allow http and https traffic for it to work.
  For more instructions,
  pelase refer to
  [Setup GitHub Actions self-hosted runners on Google Compute Engine Instance](https://www.youtube.com/watch?v=yfMzNVtQsVw)
  .

## References

- [GCP Compute Engine VM Instances]( https://www.legendu.net/misc/blog/gcp-compute-engine-vm-instances )

- [Tips on BigQuery]( https://www.legendu.net/misc/blog/tips-on-bigquery )

- [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc)
