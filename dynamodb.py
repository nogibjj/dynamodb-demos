"""
Implements identical example the CLI in Python

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
"""

import boto3
from boto3.dynamodb.conditions import Key


def create_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    table = dynamodb.create_table(
        TableName="customers",
        KeySchema=[
            {"AttributeName": "customer_id", "KeyType": "HASH"}  # Partition key
        ],
        AttributeDefinitions=[{"AttributeName": "customer_id", "AttributeType": "N"}],
        ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
    )

    return table


def list_tables(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    return dynamodb.tables.all()


def put_item(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("customers")
    response = table.put_item(Item={"customer_id": 1, "name": "John Doe"})

    return response


def get_item(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("customers")
    response = table.get_item(Key={"customer_id": 1})

    return response


def update_item(dynamodb=None):
    """Updates the name for customer_id = 1 to Jane Doe"""

    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("customers")

    response = table.update_item(
        Key={"customer_id": 1},
        UpdateExpression="SET #name = :new_name",
        ExpressionAttributeNames={"#name": "name"},
        ExpressionAttributeValues={":new_name": "Jane Doe"},
        ReturnValues="UPDATED_NEW",
    )


def query_items(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("customers")

    response = table.query(KeyConditionExpression=Key("customer_id").eq(1))

    return response


def scan_items(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("customers")
    response = table.scan()

    return response


def delete_item(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("customers")
    response = table.delete_item(Key={"customer_id": 1})

    return response


def delete_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("customers")
    table.delete()

    return table
