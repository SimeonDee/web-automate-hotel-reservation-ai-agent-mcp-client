# web-automate-hotel-reservation-ai-agent-mcp-client

An AI Agent, built as MCP-client, that provide Web Automation, Web Search and Hotel Reservation tools to OpenAI GPT LLM through playright and airbnb MCP-Servers.

It is provided as a RESTfull API implemented using FastAPI.

## MCP Servers

- `Microsoft Playwright MCP-server`:
  A Model Context Protocol server that provides browser automation capabilities using Playwright. This server enables LLMs to interact with web pages, take screenshots, generate test code, web scraps the page and execute JavaScript in a real browser environment. See [Playwrite-MCP-Server](https://github.com/executeautomation/mcp-playwright)

- `DuckDuckGo MCP-server`:
  The MCP (Model Context Protocol) server enables search capabilities using Duck Duck Go as the backend search engine. It leverages SSE (Server-Sent Events) transport and is based on Open-WebUI's web search functionality. See [DuckDuckGo-MCP-Server](https://playbooks.com/mcp/nickclyde-duckduckgo-search). For text, image, and video search, see this mcp server repo [misanthropic-ai ddg-mcp](https://github.com/misanthropic-ai/ddg-mcp)

- `Airbnb MCP Server`:
  The Airbnb MCP Server allows you to search for Airbnb listings and retrieve detailed information about specific properties directly through Claude. This server provides structured data about accommodations, pricing, amenities, and other listing details without requiring an API key. See [Airbnb MCP Server](https://playbooks.com/mcp/openbnb-airbnb) and official [Airbnb MCP Server repo](https://github.com/openbnb-org/mcp-server-airbnb).

# Tools and Dependencies

- For list of dependencies See the [requirements.txt](!requirements.txt)

## Setup

- Create and activate a virtual environment
- Install dependencies

```bash
$ pip install uv
```

```bash
$ uv pip install -r requirements.txt
```

- To start the server FastAPI Server, run
  - Start as a dev server
  ```bash
  $ make run-server-dev
  ```
  - Start as a dev server
  ```bash
  $ make run-server-prod
  ```

## API Routes

- **BASE URL**: http://127.0.0.1:5000

- **Routes**:

  - POST `/agents/run`:

    Request Body:

    ```json
    {
      "message": "Your query here"
    }
    ```

    Response:

    ```json
    {
      "response": "agent response here"
    }
    ```

## Contacts

`Adedoyin Simeon Adeyemi` | [LinkedIn](https://www.linkedin.com/in/adedoyin-adeyemi-a7827b160/)
