Author: Benjamin Du
Date: 2023-07-01 17:57:54
Modified: 2025-05-08 12:15:01
Title: GCP Compute Engine VM Instances
Slug: gcp-compute-engine-vm-instances
Category: Computer Science
Tags: Computer Science, programming, cloud, GCP, VM, compute engine, spot, Google

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## GCP

GCP c2 and c3 VMs are good choices according to performance per price.
It's even cheaper than customized VM types with reduced memories!
GCP c2 VMs are compute optimized and are ideal for CPU intensive workloads.
Note that GCP c2 spot VMs are even cheaper than AWS t2.nano VMs
if you can stand your VM being preempted.

![gcp-c2-price](https://user-images.githubusercontent.com/824507/250313656-891cd99a-c9a0-4004-9158-fd87503c39a6.png)

![gcp-c3-price](https://user-images.githubusercontent.com/824507/250313771-b776b124-5503-4aa9-a457-a55452bfdf67.png)

## Create GCP VMs Using Command Line

```
gcloud compute instances create instance-20240304-20240304-064337 \
    --project=crested-studio-416206 \
    --zone=northamerica-northeast1-c \
    --machine-type=e2-medium \
    --network-interface=network-tier=PREMIUM,stack-type=IPV4_ONLY,subnet=default \
    --maintenance-policy=MIGRATE \
    --provisioning-model=STANDARD \
    --service-account=170261695503-compute@developer.gserviceaccount.com \
    --scopes=https://www.googleapis.com/auth/cloud-platform \
    --tags=https-server,lb-health-check \
    --create-disk=auto-delete=yes,boot=yes,device-name=instance-20240304-062735,image=projects/ubuntu-os-cloud/global/images/ubuntu-2204-jammy-v20240228,mode=rw,size=10,type=projects/crested-studio-416206/zones/northamerica-northeast1-c/diskTypes/pd-balanced \
    --no-shielded-secure-boot \
    --shielded-vtpm \
    --shielded-integrity-monitoring \
    --labels=goog-ec-src=vm_add-gcloud \
    --reservation-affinity=any
```
## Query GCP VMs

```
gcloud compute instances list --format='table(name,status,lastStartTimestamp,lastStopTimestamp.list())'
```

## Google Cloud Logging

https://console.cloud.google.com/logging

## References

- [Comparison of Popular Cloud Platforms]( https://www.legendu.net/misc/blog/comparison-of-popular-cloud-platforms )

- [GCP - Create a VM with a custom machine type](https://cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type)

- [GCP - Free cloud features and trial offer](https://cloud.google.com/free/docs/free-cloud-features#compute)

- [GCP - Choosing the right virtual machine type](https://cloud.google.com/compute#section-6)

- [GCP Product Calculator](https://cloud.google.com/products/calculator)

- [GCP - Compute Engine Pricing](https://cloud.google.com/compute/all-pricing)


