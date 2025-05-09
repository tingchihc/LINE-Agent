# LINE-Agent

## Requirements
  - Get `LINE_CHANNEL_ACCESS_TOKEN` and `LINE_CHANNEL_SECRET`. [Tutorial](setting/LINE_setting.md)
  - Fill up ```.env``` information
  - Put your domain knowledge in MongoDB. [Tutorial](docs/README.md)

## LLM Multi-Agent System with Semantic Kernel, MongoDB, and Redis

This repository hosts a multi-agent system powered by Large Language Models (LLMs), built using [Microsoft's Semantic Kernel](https://github.com/microsoft/semantic-kernel), MongoDB, and Redis. Designed for real-time interaction on LINE, our system coordinates multiple intelligent agents to handle diverse tasks such as information retrieval, conversation management, and personalized responses.

### Key Components

- **Semantic Kernel**: Orchestrates and coordinates agent skills, memory, and planning logic.
- **MongoDB**: Serves as persistent storage for user profiles, chat history, and agent metadata.
- **Redis**: Enables fast, in-memory storage for session management and context tracking across conversations.
- **LINE Integration**: Delivers multi-agent interaction capabilities directly to users via LINE messaging.

This system is built for scalability, modularity, and extensibility—ideal for research, prototyping, or production use in real-world LLM-powered assistant applications.

## How to use:

- Step 1. Terminal one: ```docker-compose up --build```  
- Step 2. Terminal two: ```ngrok http 8501```
- Step 3. Fill up LINE Webhook URL: ```https://xxxx-xxx-xx-xxx-xx.ngrok-free.app/webhook```

## Acknowledge

- [semantic-kerne](https://github.com/microsoft/semantic-kernel)
