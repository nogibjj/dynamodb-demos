## Extended Project

### Tasks


* Create a DynamoDB table with a given name and primary key
* Load sample data into the table using a JSON file
* Write a query to retrieve items based on multiple filter conditions
* Delete all items in the table and delete the table

### Challenge

* Add a global secondary index to the table
* Load data from a CSV file instead of JSON
* Try different query scenarios and scan operations

### Reflection

* What are the benefits of NoSQL databases like DynamoDB?
* How can you model data effectively for fast queries?
* What factors determine provisioned capacity needs?
* How was your experience with DynamoDB CLI vs Console?

### Create a Table

```bash
aws dynamodb create-table \
    --table-name customers \
    --attribute-definitions \
        AttributeName=customer_id,AttributeType=N \
    --key-schema \
        AttributeName=customer_id,KeyType=HASH \
    --provisioned-throughput \
        ReadCapacityUnits=5,WriteCapacityUnits=5

```

### Write batch to dynamo

```bash
aws dynamodb batch-write-item \
--request-items file://records.json 
```
```json
{
  "customers": [
    {
      "PutRequest": { 
        "Item": {
          "customer_id": {"N": "1"},
          "name": {"S": "John Doe"},
          "address": {"S": "123 Main St"}
        }
      }
    },
    {
      "PutRequest": {
        "Item": {
          "customer_id": {"N": "2"},
          "name": {"S": "Jane Smith"},
          "address": {"S": "456 Oak Rd"}
        }
      }
    },
    {
      "PutRequest": {
        "Item": {
          "customer_id": {"N": "3"},
          "name": {"S": "Bob Johnson"},
          "address": {"S": "789 Elm St"}  
        }
      }
    },
    {
      "PutRequest": {
        "Item": {
          "customer_id": {"N": "4"},
          "name": {"S": "Sarah Davies"},
          "address": {"S": "246 Pine Ave"}
        }
      }
    },
    {
      "PutRequest": {
        "Item": {
          "customer_id": {"N": "5"},
          "name": {"S": "Mike Wong"},
          "address": {"S": "135 Birch Ln"}
        }
      }
    }
  ]
}
```

### Query with values
```bash
aws dynamodb query \
    --table-name customers \
    --key-condition-expression "customer_id = :v_id" \
    --filter-expression "address = :v_addr" \
    --expression-attribute-values file://values.json
```

```json
{
    ":v_id": {"N": "3"},
    ":v_addr": {"S": "789 Elm St"} 
}
```

### Delete Items and Table

delete items and table
```bash
aws dynamodb delete-table --table-name customers
```