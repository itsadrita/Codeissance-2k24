# AI-Powered Anti-Money Laundering (AML) System

## Overview
The AI-Powered Anti-Money Laundering (AML) system is designed to detect and prevent suspicious financial activities by classifying transactions and alerting the necessary stakeholders. Using AI and machine learning models, the system identifies patterns, flags risky transactions, and enables administrators to take action. The system also generates reports for law enforcement, helping banks stay compliant with AML regulations.

## Key Features

1. **Automated Transaction Monitoring & Classification**:
   - Classifies transactions into **Low Risk**, **Medium Risk**, and **High Risk** based on historical data and patterns.
   - Detects anomalies and flags suspicious activities for review.

2. **Dynamic Account Blocking**:
   - Automatically blocks customer accounts after two transactions over 50,000, requiring them to contact the bank for resolution.

3. **Admin Dashboard for Manual Review**:
   - Admins can manually review and flag transactions, blocking accounts when necessary.
   - Flagged accounts cannot receive money until further review by the bank.

4. **Report Generation for Law Enforcement**:
   - Generates daily/weekly reports of suspicious transactions and customer behavior.
   - Includes geographic information such as **longitude** and **latitude** of flagged transactions.

5. **Real-time Risk Dashboard & Alerts**:
   - Real-time analytics for daily transactions, risk detection, and flagged accounts.
   - Alerts admins when high-risk thresholds are met.


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository/aml-system.git
   cd aml-system
