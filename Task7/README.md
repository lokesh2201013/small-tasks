
# Disaster Recovery & High Availability Strategy for Enterprise Applications in GCP
## 1. Introduction
Disaster Recovery (DR) ensures business continuity by minimizing downtime and data loss in case of failures.

 This document outlines the DR strategy for an enterprise application hosted on Google Cloud Platform (GCP), focusing on Recovery Time Objective (RTO) and Recovery Point Objective (RPO).

## 2. Key DR Concepts
Recovery Time Objective (RTO): The maximum time allowed to restore operations after a failure.

Recovery Point Objective (RPO): The maximum acceptable data loss in case of a disaster.

Application Component	RTO	RPO	Strategy

Compute Instances	5 mins	0 mins	Auto-healing, instance snapshots

Databases (Cloud SQL, Spanner)	15 mins	5 mins

Automated backups & point-in-time recovery

Storage (GCS, Filestore)	5 mins	0 mins	Multi-region replication

Kubernetes (GKE)	10 mins	0 mins	Multi-zone clusters, backup with Velero

## 3. Disaster Recovery Strategies
### A. Backup & Recovery Strategies
Compute Engine Backup

Create snapshots of VM disks automatically using Snapshot Schedules.

Use Instance Templates and Managed Instance Groups (MIGs) for auto-recovery.

Database Backup (Cloud SQL & Spanner)

Enable automated backups for daily backups.

Use point-in-time recovery (PITR) for Cloud SQL to restore to any time within the retention period.

Replicate databases across multiple regions for high availability.

Storage Backup (Cloud Storage & Filestore)

Enable bucket versioning to keep multiple versions of files.

Use Object Lifecycle Management to transition data to lower-cost storage (Nearline, Coldline).

Replicate data across multiple regions to prevent data loss.

Kubernetes Backup (GKE)

Use Velero to back up cluster configurations, workloads, and persistent volumes.

Store backups in a remote Cloud Storage bucket.

### B. High Availability Strategies
Multi-Region Deployments

Deploy applications in multiple regions for failover support.

Use Cloud Load Balancing for global traffic distribution.

Auto-healing Mechanisms

Use Managed Instance Groups (MIGs) to automatically replace unhealthy instances.

Configure GKE node auto-repair for Kubernetes clusters.
Network Redundancy

Use Cloud CDN and Cloud Armor for improved latency and security.

Set up Cloud VPN or Interconnect for secure connectivity between regions.

### README.md – Setting Up Automated Backups in GCP

# Automated Backup Setup in Google Cloud Platform (GCP)

This document explains how to configure automated backups for Compute Engine, Cloud SQL, and Cloud Storage in GCP.

## 1. Compute Engine: Setting Up VM Snapshots
To create automatic VM snapshots:

1. **Create a Snapshot Schedule**
   ```sh
   gcloud compute resource-policies create snapshot-schedule daily-backup \
     --description "Daily backups at 12 AM UTC" \
     --max-retention-days 7 \
     --daily-schedule 00:00
Attach the Snapshot Policy to a Disk

``` sh
gcloud compute disks add-resource-policies my-disk \
  --resource-policies daily-backup \
  --zone us-east1-b
```
2. **Cloud SQL: Enabling Automated Backups**
Enable automated backups for a Cloud SQL instance:

Modify the SQL instance settings:

```sh

gcloud sql instances patch my-instance \
  --backup-start-time 23:00 \
  --enable-binlog
Restore a Backup:
```
```sh
gcloud sql backups list --instance=my-instance
gcloud sql backups restore BACKUP_ID --instance=my-instance
```

3. **Cloud Storage: Enabling Object Versioning**
Enable versioning for a storage bucket:

```sh
gcloud storage buckets update my-bucket --versioning
To list and delete old versions:
```
```sh
gcloud storage objects list --versions -b my-bucket
gcloud storage objects delete OBJECT_NAME --generation=GENERATION_NUMBER
```
4. **Kubernetes: Backing Up GKE Clusters with Velero**
Install Velero
```sh
velero install \
    --provider gcp \
    --plugins velero/velero-plugin-for-gcp \
    --bucket my-backup-bucket \
    --backup-location-config serviceAccount=my-velero-sa
```
Take a Backup
```sh
velero backup create my-cluster-backup --include-namespaces=my-namespace
```
Restore from Backup
```sh
velero restore create --from-backup my-cluster-backup
```