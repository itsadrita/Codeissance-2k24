import pandas as pd
import random
from faker import Faker
import numpy as np

# Initialize Faker
fake = Faker()

# Parameters
num_customers = random.randint(20, 30)  # Between 20 and 30 customers
num_transactions_per_customer = 20  # Each customer has 20 transactions
total_transactions = num_customers * num_transactions_per_customer

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
suspicious_activity_tracking = {customer_id: {'flags': 0, 'high_risk_triggered': {}, 'large_txn_count': {}} for customer_id, _ in customers}

# Generate transactions with necessary updates
for customer_id, customer_name in customers:
    customer_transactions = []
    amounts = []
    receiver_list = []  # Track all receivers for this customer

    for _ in range(num_transactions_per_customer):
        # Basic transaction details
        transaction_id = fake.unique.random_number(digits=8)
        receiver_id = random.choice(customers)[0]
        receiver_name = fake.name()
        transaction_amount = random.uniform(300, 1000)  # Normal amounts between 300 and 1000
        amounts.append(transaction_amount)
        receiver_list.append((receiver_id, receiver_name))
        
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

    # Calculate mean transaction amount for this customer
    mean_transaction_amount = np.mean(amounts)

    # Introduce 5 transactions to the same receiver, with 3 large suspicious amounts
    selected_receiver = random.choice(receiver_list)  # Pick a random receiver for 5 transactions
    selected_transactions = random.sample(customer_transactions, k=5)  # Select 5 transactions to assign to the same receiver

    for i, transaction in enumerate(selected_transactions):
        transaction['Receiver ID'] = selected_receiver[0]
        transaction['Receiver Name'] = selected_receiver[1]

        # Make 3 of these transactions large to trigger suspicion
        if i < 3:
            # Generate large suspicious amount: between 2x and 3x the mean transaction amount
            transaction['Transaction Amount'] = random.uniform(mean_transaction_amount * 2, mean_transaction_amount * 3)

    # Now, after sorting by date, assign risk levels and flag suspicious activity
    for transaction in customer_transactions:
        receiver_id = transaction['Receiver ID']
        txn_amount = transaction['Transaction Amount']

        # Check if transaction amount is larger than the mean
        if txn_amount > mean_transaction_amount:
            # Initialize large_txn_count for this receiver if not present
            if receiver_id not in suspicious_activity_tracking[customer_id]['large_txn_count']:
                suspicious_activity_tracking[customer_id]['large_txn_count'][receiver_id] = 0
            
            # If it's the first large transaction with this receiver, flag as Medium Risk
            if suspicious_activity_tracking[customer_id]['large_txn_count'][receiver_id] == 0:
                transaction['Risk Level'] = 'Medium'
                transaction['Suspicious Activity'] = 'Yes'
                suspicious_activity_tracking[customer_id]['large_txn_count'][receiver_id] += 1
            else:
                # If more than one large transaction to the same receiver, mark it as High Risk
                transaction['Risk Level'] = 'High'
                transaction['Suspicious Activity'] = 'Yes'

            # Update flag count for the customer
            suspicious_activity_tracking[customer_id]['flags'] += 1
            transaction['Previous Flags'] = suspicious_activity_tracking[customer_id]['flags']

    data.extend(customer_transactions)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('data8.csv', index=False)
