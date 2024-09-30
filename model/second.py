import pandas as pd
import random
from faker import Faker
import numpy as np

# Initialize Faker
fake = Faker()

# Parameters
num_customers = random.randint(20, 30)  # Between 20 and 30 customers
num_transactions_per_customer = 10  # Each customer has 10 transactions

# Create list for dataset
data = []

# Generate Customer Data
customers = []
for _ in range(num_customers):
    customer_id = fake.unique.random_number(digits=5)
    customer_name = fake.name()
    customers.append((customer_id, customer_name))

# Risk Levels and Transaction Types
transaction_types = ['Transfer', 'Withdrawal', 'Deposit', 'Payment']
methods_of_payment = ['Credit Card', 'Bank Transfer', 'Cash', 'Digital Wallet']

# Create a dictionary to store suspicious transaction history for each customer
suspicious_activity_tracking = {customer_id: {'flags': 0, 'large_txn_count': {}} for customer_id, _ in customers}

# Generate transactions with necessary updates
for customer_id, customer_name in customers:
    customer_transactions = []
    amounts = []
    
    # Random receiver for the 3 high-risk transactions (to repeat the same customer-receiver pair)
    receiver = random.choice(customers)
    receiver_id = receiver[0]
    receiver_name = fake.name()

    for i in range(num_transactions_per_customer):
        # Basic transaction details
        transaction_id = fake.unique.random_number(digits=8)

        # For the first 7 transactions, assign different receivers with normal transaction amounts
        if i < 7:
            transaction_amount = random.uniform(300, 1000)  # Default for normal transactions
            random_receiver = random.choice(customers)
            receiver_id = random_receiver[0]
            receiver_name = fake.name()
        else:
            # For the last 3 transactions, keep the same receiver and make them high-value transactions
            transaction_amount = random.uniform(50000, 100000)
        
        amounts.append(transaction_amount)
        
        # Risk level and other attributes
        transaction_date = fake.date_this_year()
        transaction_type = random.choice(transaction_types)
        country_origin = fake.country()
        country_destination = fake.country()
        payment_method = random.choice(methods_of_payment)
        previous_flags = suspicious_activity_tracking[customer_id]['flags']  # Track the current flag count
        
        customer_transactions.append({
            'Transaction ID': transaction_id,
            'Customer ID': customer_id,
            'Customer Name': customer_name,
            'Receiver ID': receiver_id,
            'Receiver Name': receiver_name,
            'Transaction Amount': transaction_amount,
            'Date': transaction_date,
            'Transaction Type': transaction_type,
            'Country of Origin': country_origin,
            'Country of Destination': country_destination,
            'Risk Level': 'Low',  # Initially set as Low
            'Method of Payment': payment_method,
            'Previous Flags': previous_flags,
            'Suspicious Activity': 'No'  # Initially no suspicious activity
        })

    # Sort transactions by date
    customer_transactions = sorted(customer_transactions, key=lambda x: x['Date'])

    # Calculate mean transaction amount for this customer (based on normal amounts)
    mean_transaction_amount = np.mean(amounts[:7])  # Only use normal amounts for mean calculation

    # Assign risk levels and flag suspicious activity
    for transaction in customer_transactions:
        txn_amount = transaction['Transaction Amount']
        receiver_id = transaction['Receiver ID']

        # Low Risk for transactions below 2000
        if 0 <= txn_amount <= 2000:
            transaction['Risk Level'] = 'Low'
            transaction['Suspicious Activity'] = 'No'
        
        # For large transactions (50,000 to 100,000)
        elif 50000 <= txn_amount <= 100000:
            # Check if receiver pair is repetitive or not
            if receiver_id not in suspicious_activity_tracking[customer_id]['large_txn_count']:
                # Non-repetitive case: first large transaction is Medium Risk
                transaction['Risk Level'] = 'Medium'
                transaction['Suspicious Activity'] = 'Yes'
                suspicious_activity_tracking[customer_id]['large_txn_count'][receiver_id] = 1  # Mark this receiver as used
            else:
                # Repetitive case: follow the previous rules for repetitive transactions
                if suspicious_activity_tracking[customer_id]['large_txn_count'][receiver_id] == 1:
                    transaction['Risk Level'] = 'High'
                    transaction['Suspicious Activity'] = 'Yes'

                    # Update the flag count only for High Risk transactions
                    suspicious_activity_tracking[customer_id]['flags'] += 1
                    transaction['Previous Flags'] = suspicious_activity_tracking[customer_id]['flags']

    data.extend(customer_transactions)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('data15.csv', index=False)
