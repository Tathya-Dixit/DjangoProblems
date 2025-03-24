## Bank System

### 1. Lend Endpoint
**Endpoint**: `http://127.0.0.1:8000/api/lend/`

#### Request Details
- **Method**: POST
- **Form Data**:
  ```
  customer: 5
  loan_amount: 1500000
  loan_period: 8
  interest_rate: 6
  ```

#### Response
```json
{
    "loan_id": 6,
    "total_amount": 1590000.00,
    "monthly_emi": 198750.00,
    "no_of_emis": 8
}
```

### 2. Payment Endpoint
**Endpoint**: `http://127.0.0.1:8000/api/payment/`

#### Request Details
- **Method**: POST
- **Form Data**:
  ```
  loan: 6
  transaction_type: LUMPSUM
  transaction_amount: 300000.00
  ```

#### Response
```json
{
    "total_amount": "1590000.00",
    "remaining_amount": "791250.00",
    "monthly_emi": "113035.71",
    "no_of_emis": 7
}
```

### 3. Ledger Endpoint
**Endpoint**: `http://127.0.0.1:8000/api/ledger/`

#### Request Details
- **Method**: POST
- **Form Data**:
  ```
  loan: 6
  ```

#### Response
```json
{
    "balance_amount": 711250.00,
    "total_amount": 1590000.00,
    "remaining_amount": 791250.00,
    "monthly_emi": 113035.71,
    "no_of_emis": 7,
    "transactions": [
        {
            "id": 10,
            "transaction_amount": 1500000.00,
            "transaction_type": "LEND",
            "transaction_date": "2025-03-24T21:31:24.753747Z",
            "loan": 6
        },
        {
            "id": 11,
            "transaction_amount": 198750.00,
            "transaction_type": "EMI",
            "transaction_date": "2025-03-24T21:31:31.209966Z",
            "loan": 6
        },
        {
            "id": 12,
            "transaction_amount": 300000.00,
            "transaction_type": "LUMPSUM",
            "transaction_date": "2025-03-24T21:32:29.768425Z",
            "loan": 6
        },
        {
            "id": 13,
            "transaction_amount": 300000.00,
            "transaction_type": "LUMPSUM",
            "transaction_date": "2025-03-24T21:34:50.864901Z",
            "loan": 6
        }
    ]
}
```

### 4. Account Overview Endpoint
**Endpoint**: `http://127.0.0.1:8000/api/account_overview/`

#### Request Details
- **Method**: POST
- **Form Data**:
  ```
  customer: 5
  ```

#### Response
```json
{
    "name": "Tathya Dixit",
    "balance_amount": 711250.00,
    "loans": [
        {
            "id": 6,
            "amount_paid": 708750.00,
            "loan_amount": 1500000.00,
            "interest_rate": 6,
            "loan_period": 8,
            "total_amount": 1590000.00,
            "monthly_emi": 113035.71,
            "no_of_emis": 7,
            "remaining_amount": 791250.00,
            "loan_date": "2025-03-24T21:31:24.731438Z",
            "customer": 5
        }
    ]
}
```
