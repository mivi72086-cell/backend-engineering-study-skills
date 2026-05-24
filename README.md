# 🛡️ Advanced Backend Engineering: Study Skills Matrix

Welcome to my core backend architecture and systems engineering repository. This project serves as a dedicated production sandbox documenting my journey mastering distributed systems, high-throughput data streams, horizontal scaling, and infrastructure resilience.

Every module inside this folder is written from scratch in Python, containerized using Docker, and focused on solving real-world global tech challenges.

---

## 🛠️ System Architecture Directory

### 📁 05-relational-databases-sql
* **The Problem:** Temporary runtime variables (`RAM`) clear whenever a server reboots or crashes, destroying user data.
* **The Solution:** Implemented a persistent relational storage layer using **SQLite**. 
* **Key Mechanisms:** * Strict database schemas with `PRIMARY KEY` uniqueness rules to prevent duplicate registrations.
  * Parameterized SQL queries (`?` placeholders) to completely immunize the system against **SQL Injection Attacks**.

### 📁 06-structured-logging-metrics
* **The Problem:** Standard text print statements (`print()`) are impossible for automated monitoring applications to parse at high scale.
* **The Solution:** Built a machine-readable **Structured JSON Flight Recorder** to track live performance metrics.
* **Key Mechanisms:**
  * Automated capturing of ISO-standard international timestamps.
  * Real-time execution tracking measuring processing latency down to the millisecond (`ms`) to detect downstream bottlenecks.

### 📁 07-kafka-partitions-scale
* **The Problem:** Single-channel pipelines create processing traffic jams when millions of users interact with an application at the same millisecond.
* **The Solution:** Engineered a horizontally scalable event stream using **Apache Kafka** and **Docker**.
* **Key Mechanisms:**
  * Provisioned a custom broker topic split into **3 parallel partitions**.
  * Implemented **Key-Based Hashing Routing** to dynamically balance incoming workloads evenly across parallel processing lanes.

---

## 🚀 Infrastructure Setup & Quickstart

### 📋 Prerequisites
Ensure you have the following infrastructure tools installed locally:
* Python 3.10+
* Docker Desktop

### 🏃 Setup Commands
To spin up the distributed architecture environment, execute the following commands in your terminal:

