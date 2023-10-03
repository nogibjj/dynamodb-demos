/*
A rust version of DynamoDB some CRUD
*/
use aws_sdk_dynamodb::operation::create_table::CreateTableOutput;
use aws_sdk_dynamodb::types::AttributeValue;
use aws_sdk_dynamodb::types::{AttributeDefinition, KeySchemaElement, ScalarAttributeType};
use aws_sdk_dynamodb::{Client, Error};
use std::time::Duration;

pub struct Item {
    pub username: String,
}

#[derive(Debug, PartialEq)]
pub struct ItemOut {
    pub username: Option<AttributeValue>,
}
const TABLE_NAME: &str = "customers";

async fn create_table() -> Result<CreateTableOutput, Error> {
    let shared_config = aws_config::load_from_env().await;
    let client = Client::new(&shared_config);
    let ad = AttributeDefinition::builder()
        .attribute_name("username")
        .attribute_type(ScalarAttributeType::S)
        .build();
    let ks = KeySchemaElement::builder()
        .attribute_name("username")
        .key_type(aws_sdk_dynamodb::types::KeyType::Hash)
        .build();
    let pt = aws_sdk_dynamodb::types::ProvisionedThroughput::builder()
        .read_capacity_units(10)
        .write_capacity_units(5)
        .build();
    let request = client
        .create_table()
        .table_name(TABLE_NAME)
        .attribute_definitions(ad)
        .key_schema(ks)
        .provisioned_throughput(pt);
    let resp = request.send().await?;
    println!("{:?}", resp);
    Ok(resp)
}

async fn list_tables() -> Result<(), Error> {
    let shared_config = aws_config::load_from_env().await;
    let client = Client::new(&shared_config);
    let req = client.list_tables().limit(10);
    let resp = req.send().await?;
    println!("Current DynamoDB tables: {:?}", resp.table_names);
    Ok(())
}

async fn put_item() -> Result<ItemOut, Error> {
    let shared_config = aws_config::load_from_env().await;
    let client = Client::new(&shared_config);
    let item = Item {
        username: "JohnDoe".to_string(),
    };
    let user_name = AttributeValue::S(item.username);
    let request = client
        .put_item()
        .table_name(TABLE_NAME)
        .item("username", user_name.clone());
    let resp = request.send().await?;
    println!("{:?}", resp);
    Ok(ItemOut {
        username: Some(user_name),
    })
}

async fn scan_items() -> Result<ItemOut, Error> {
    let shared_config = aws_config::load_from_env().await;
    let client = Client::new(&shared_config);
    let request = client.scan().table_name(TABLE_NAME);
    let resp = request.send().await?;
    println!("{:?}", resp);
    Ok(ItemOut {
        username: resp.items.unwrap().get(0).unwrap().get("username").cloned(),
    })
}

async fn delete_table() -> Result<(), Error> {
    let shared_config = aws_config::load_from_env().await;
    let client = Client::new(&shared_config);
    let request = client.delete_table().table_name(TABLE_NAME);
    let resp = request.send().await?;
    println!("{:?}", resp);
    Ok(())
}

#[tokio::main]
async fn main() -> Result<(), Error> {
    //run a few operations
    create_table().await?;
    println!("Created table....waiting ten seconds");
    // Pause execution for 10 seconds
    tokio::time::sleep(Duration::from_secs(10)).await;
    //print tables
    println!("Listing all tables");
    list_tables().await?;
    println!("put item");
    put_item().await?;
    scan_items().await?;
    println!("delete table");
    delete_table().await?;
    Ok(())
}
