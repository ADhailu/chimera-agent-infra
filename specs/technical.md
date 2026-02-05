## Generate Post API

Input:
{
"persona_id": "string",
"topic": "string",
"content_type": "text | image | video"
}

Output:
{
"status": "success | error",
"content_url": "string",
"confidence": 0.0
}

Table: agents

- id
- name
- persona_type
- wallet_address

Table: content_history

- id
- agent_id
- topic
- platform
- timestamp

Table: transactions

- id
- agent_id
- amount
- purpose
- status

Table: skills

- id
- agent_id
- skill_name
- version
