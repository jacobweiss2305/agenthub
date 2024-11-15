# Personal shopper

This Swarm is a personal shopping bee that can help with making sales and refunding orders.
This example uses the helper function `run_demo_loop`, which allows us to create an interactive Swarm session.
In this example, we also use a Sqlite3 database with customer information and transaction data.

## Overview

The personal shopper example includes three main bees to handle various customer service requests:

1. **Triage Bee**: Determines the type of request and transfers to the appropriate bee.
2. **Refund Bee**: Manages customer refunds, requiring both user ID and item ID to initiate a refund.
3. **Sales Bee**: Handles actions related to placing orders, requiring both user ID and product ID to complete a purchase.

## Setup

Once you have installed dependencies and Swarm, run the example using:

```shell
python3 main.py
```
