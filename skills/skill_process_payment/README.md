# Skill: process payment

## Purpose

Handle payment processing for transactions.

## Input

{
"agent_id": "string",
"amount": 0.0,
"purpose": "string"
}

## Output

{
"status": "success | error",
"transaction_id": "string",
"confidence": 0.0
}

## Tools Used

- MCP Payment API
