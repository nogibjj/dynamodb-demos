#!/bin/bash
# Batch write JSON to dynamodb 'customers'
aws dynamodb batch-write-item \
--request-items file://records.json 
