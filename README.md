# Bayut MCP Server

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![MCP](https://img.shields.io/badge/MCP-1.1.0-orange.svg)

MCP (Model Context Protocol) server for UAE real estate search via the Bayut API. Enables direct property search and market analysis through Claude Desktop and other AI assistants.

## Features

### 🔍 Core Functionality
- **Location Search** - Autocomplete for UAE locations (cities, neighborhoods, buildings)
- **Property Search** - Extensive filtering options for sale/rent properties
- **Property Details** - Complete information including photos, floorplans, agent details
- **Transaction History** - Historical price data for Dubai properties
- **Market Analysis** - Quick market summaries and trends for specific areas

### 💡 Use Cases
- **Investment Research** - Find and analyze properties across Dubai and UAE
- **Market Intelligence** - Track price trends and transaction history
- **Golden Visa Planning** - Search for property portfolios meeting visa requirements
- **Rental Yield Analysis** - Compare returns across different areas
- **Property Comparison** - Evaluate multiple listings with detailed filters

## Installation

### Prerequisites
- Python 3.10 or higher
- [Claude Desktop](https://claude.ai/download)
- [RapidAPI Account](https://rapidapi.com/BayutAPI/api/bayut-api1) with Bayut API subscription

### Step 1: Install Dependencies

```bash
pip install mcp httpx
```

### Step 2: Get API Key

1. Sign up at [RapidAPI](https://rapidapi.com/BayutAPI/api/bayut-api1)
2. Subscribe to Bayut API (Free plan: 100 requests/month)
3. Copy your API key from the dashboard

### Step 3: Configure Claude Desktop

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

Add this configuration:

```json
{
  "mcpServers": {
    "bayut": {
      "command": "python",
      "args": ["/absolute/path/to/bayut_mcp/server.py"],
      "env": {
        "RAPIDAPI_KEY": "your-rapidapi-key-here"
      }
    }
  }
}
```

⚠️ **Important:** Use absolute path to `server.py`

### Step 4: Restart Claude Desktop

Completely quit and restart Claude Desktop to load the MCP server.

## Usage

Once configured, you can interact with Bayut directly through Claude:

### Example Queries

**Location Search:**
```
"Find location IDs for Dubai South"
```

**Property Search:**
```
"Show me studios in Dubai South under 500k AED"
"Find 1-bedroom apartments in Business Bay for rent"
```

**Market Analysis:**
```
"What are the average prices for studios in Dubai Marina?"
"Show me transaction history for Dubai South in the last year"
```

**Investment Planning:**
```
"Find 5 properties totaling under 2M AED with at least 7% rental yield"
"Compare rental yields between JVC and International City"
```

## Available Tools

| Tool | Description |
|------|-------------|
| `search_locations` | Search UAE locations with autocomplete |
| `search_properties` | Property search with extensive filters |
| `get_property_details` | Complete details for a specific property |
| `get_transactions` | Transaction records for price analysis |
| `get_market_summary` | Quick market overview for a location |

## API Limits

- **Free Plan**: 100 requests/month (~3 per day)
- **Basic Plan**: 1,000 requests/month - $19.99
- **Pro Plan**: 10,000 requests/month - $49.99

For testing and initial research, the free plan is sufficient.

## Advanced Usage

### Property Search Filters

```python
search_properties(
    purpose="for-sale",           # or "for-rent"
    locations_ids=[3355],          # Dubai South
    category="apartments",
    rooms=[0],                     # Studio
    price_max=500000,
    area_min=300,
    is_furnished=True,
    sort_by="lowest_price"
)
```

### Transaction Analysis

```python
get_transactions(
    purpose="for-sale",
    locations_ids=[3355],
    category="apartments",
    beds=[0],
    start_date="2024-01-01",
    end_date="2024-12-31"
)
```

## Troubleshooting

### "No tools available"
- Check `claude_desktop_config.json` syntax
- Verify absolute path to `server.py`
- Ensure API key is set
- Restart Claude Desktop

### "401 Unauthorized"
- API key is incorrect or missing
- Check the key in your config file

### "Module 'mcp' not found"
```bash
pip install mcp httpx
```

### "404 Not Found"
- Ensure you're subscribed to the correct Bayut API on RapidAPI
- Base URL should be: `https://bayut-api1.p.rapidapi.com`

## Development

### Project Structure
```
bayut_mcp/
├── server.py           # Main MCP server
├── pyproject.toml      # Package configuration
├── README.md           # Documentation
├── QUICKSTART.md       # Quick setup guide
└── examples.py         # Usage examples
```

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Resources

- [Bayut API Documentation](https://docs.bayutapi.com/)
- [RapidAPI Hub](https://rapidapi.com/BayutAPI/api/bayut-api1)
- [MCP Documentation](https://modelcontextprotocol.io)
- [Claude Desktop](https://claude.ai/download)

## License

MIT License - see LICENSE file for details

## Support

For issues or questions:
- Open an issue on GitHub
- Email: bayut.restapi@gmail.com (for Bayut API issues)

## Acknowledgments

- Built with [FastMCP](https://github.com/jlowin/fastmcp)
- Powered by [Bayut API](https://bayutapi.com/)
- UAE real estate data from [Bayut.com](https://www.bayut.com)

---

**Built for Claude Desktop** | **UAE Real Estate Data by Bayut**
