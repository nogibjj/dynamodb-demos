# DynamoDB Demos

## CLI Demo

### Create Table

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

### List Tables

```bash
aws dynamodb list-tables
```

### Put Item

```bash
aws dynamodb put-item \
    --table-name customers \
    --item \
        '{"customer_id": {"N": "1"}, "name": {"S": "John Doe"}}'
```

### Get Item

```bash
aws dynamodb get-item \
    --table-name customers \
    --key \
        '{"customer_id": {"N": "1"}}'
```

### Update Item

```bash
aws dynamodb update-item \
    --table-name customers \
    --key \
        '{"customer_id": {"N": "1"}}' \
    --update-expression \
        "SET #name = :name" \
    --expression-attribute-names \
        '{"#name": "name"}' \
    --expression-attribute-values \
        '{":name": {"S": "Jane Doe"}}'
```

### Query Items

```bash
aws dynamodb query \
    --table-name customers \
    --key-condition-expression \
        "customer_id = :customer_id" \
    --expression-attribute-values \
        '{":customer_id": {"N": "1"}}'
```

### Scan Items

```bash
aws dynamodb scan \
    --table-name customers
```

### Delete Item

```bash
aws dynamodb delete-item \
    --table-name customers \
    --key \
        '{"customer_id": {"N": "1"}}'
```

### Delete Table

```bash
aws dynamodb delete-table \
    --table-name customers
```


### Upload Records via JSON

batch write json to dynamo
```
aws dynamodb 

```


```json
// records.json

[
  {
    "customer_id": {"N": "1"}, 
    "name": {"S": "John Doe"}
  },
  {
    "customer_id": {"N": "2"},
    "name": {"S": "Jane Smith"} 
  },
  {
    "customer_id": {"N": "3"},
    "name": {"S": "Bob Johnson"}
  },
  {
    "customer_id": {"N": "4"},
    "name": {"S": "Sarah Davies"}
  },
  {
    "customer_id": {"N": "5"},
    "name": {"S": "Mike Wong"}
  }
]
```




## References

