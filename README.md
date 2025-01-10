# Obkio

## Problem Statement

The objective of this problem is to design and implement an Agents Monitoring API that will be used to track and display information about multiple agents deployed in various locations. Each agent periodically sends its IPv4 address to the API at regular intervals (for example, every 5 minutes). The API should receive and store these IP addresses, retrieve additional information about each IP address, such as its Autonomous System Number (ASN) and Internet Service Provider (ISP), and provide endpoints to query this information. You don't have to worry about the agents; you can simply make API calls with the IP address.

Functional Requirements:
API Endpoints:
Implement an endpoint that allows agents to send their IP addresses to the API.
Implement an endpoint to retrieve the list of all agents with their IP addresses.
Implement an endpoint to retrieve detailed information about a specific agent, including its IP address, ASN, and ISP.
Data Storage:
Design a database schema to store agent information, including IP addresses, ASNs, and ISPs.
IP Information Retrieval:
Use an external API (you can use an external API or have a local endpoint that returns IP information) to determine the ASN and ISP of each IP address received from the agents.
Store the ASN and ISP information in the database along with the IP addresses.

## Notes

### Authentication

The api endpoint is open to anyone, and no authentication was implemented as that was not part of the requirements, but this should obviously be added in a real life situation

### Agent Identification

Since the IP Address of the agent can change, we need some other way to uniquely identify it.
On create, the backend will set an ID, but this means that the agent will need to remember this ID, and re-use it in case of reboots.
Otherwise, the DB will be clutered if a new agent instance is created on each reboot.

### Postman

Try out the api on postman
https://www.postman.com/spaceflight-cosmologist-42752282/obkio/collection/6lx62d3/agents?action=share&creator=31974229
