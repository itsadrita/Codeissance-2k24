# AI-Powered Anti-Money Laundering (AML) System

## Overview
The AI-Powered Anti-Money Laundering (AML) system is designed to detect and prevent suspicious financial activities by classifying transactions and alerting the necessary stakeholders. Using AI and machine learning models, the system identifies patterns, flags risky transactions, and enables administrators to take action. The system also generates reports for law enforcement, helping banks stay compliant with AML regulations.


## Key Features

### Classification Based on Risk
- **Automatic Detection**: Identifies circular transaction patterns (e.g., A → B → C → A).
- **Risk Classification**:
  - Classifies flagged transactions into **Low Risk**, **Medium Risk**, and **High Risk** based on:
    - Transaction frequency
    - Amount thresholds
    - Detected patterns
- **Risk Scoring**:
  - Uses historical data and graph-based features (e.g., centrality metrics) to inform scoring.

### Anomaly Detection
- Detects unusual or repetitive cycles within a transaction network.
- Flags suspicious accounts for further investigation.

---

## Dynamic Circular Pattern Blocking

### Threshold-Based Blocking
- Automatically freezes accounts involved in circular transactions exceeding a defined total value (e.g., two cycles totaling ₹50,000 or more).
- Blocked accounts must contact the bank for manual review and resolution.

---

## Admin Dashboard for Circular Transactions

### Manual Review Capabilities
- Admins can view flagged circular transactions with detailed insights, including:
  - Accounts involved
  - Total transaction amounts
  - Frequency of transactions in cycles
- Admins can manually block accounts if necessary.

### Blocked Account Restrictions
- Flagged accounts are restricted from receiving money until reviewed and cleared by the bank.

---

## Circular Transaction Report Generation for Law Enforcement

### Daily and Weekly Reports
- Generates reports of all flagged circular transactions for law enforcement purposes.
- **Report Contents**:
  - Details of flagged accounts
  - Total amounts cycled
  - Risk classifications
- Includes **geographic metadata** (longitude and latitude) of flagged transactions for further investigation.

---

## Real-Time Circular Risk Dashboard & Alerts

### Analytics Overview
- Provides a real-time dashboard to monitor:
  - Daily transaction volumes
  - Flagged cycles
  - Risk classifications
- Interactive visualizations of transaction networks.

### Alert System
- Sends alerts to admins when high-risk circular patterns are detected, enabling prompt action.


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository/aml-system.git
   cd aml-system
