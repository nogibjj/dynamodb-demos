aws dynamodb query \
    --table-name customers \
    --key-condition-expression "customer_id = :v_id" \
    --filter-expression "address = :v_addr" \
    --expression-attribute-values file://values.json