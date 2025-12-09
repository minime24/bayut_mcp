# Bayut MCP Server

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![MCP](https://img.shields.io/badge/MCP-1.1.0-orange.svg)

MCP (Model Context Protocol) server for UAE real estate search via the Bayut API. Enables direct property search and market analysis through Claude Desktop and other AI assistants.

## Features

### 🏠 Core Functionality
- **Location Search** - Autocomplete for UAE locations (cities, neighborhoods, buildings)
- **Property Search** - Extensive filtering options for sale/rent properties
- **Property Details** - Complete information including photos, floorplans, agent details
- **Transaction History** - Historical price data for Dubai properties
- **Market Analysis** - Quick market summaries and trends for specific areas
- **AI Valuations** - TruEstimate™ market value estimates with comparable sales and rental yields

### 💡 Use Cases
- **Investment Research** - Find and analyze properties across Dubai and UAE
- **Market Intelligence** - Track price trends and transaction history
- **Property Valuation** - Get AI-powered market value estimates with confidence levels
- **Rental Yield Analysis** - Compare returns across different areas with comparable data
- **Golden Visa Planning** - Search for property portfolios meeting visa requirements
- **Property Comparison** - Evaluate multiple listings with detailed filters
- **Due Diligence** - Verify property prices against market comparables before purchase

## Installation

### Prerequisites
- Python 3.10 or higher
- [Claude Desktop](https://claude.ai/download)
- [RapidAPI Account](https://rapidapi.com/taviansol/api/uae-real-estate2) with UAE Real Estate API subscription

### Step 1: Install Dependencies

```bash
pip install mcp httpx
```

### Step 2: Get API Key

1. Sign up at [RapidAPI](https://rapidapi.com/taviansol/api/uae-real-estate2)
2. Subscribe to UAE Real Estate API (Free plan: 750 requests/month)
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
"Get market valuation for Elite Residences 3, Unit 710"
```

**Investment Planning:**
```
"Find 5 properties totaling under 2M AED with at least 7% rental yield"
"Compare rental yields between JVC and International City"
"Estimate the market value and rental yield for this property"
```

## Available Tools

| Tool | Description |
|------|-------------|
| `search_locations` | Search UAE locations with autocomplete |
| `search_properties` | Property search with extensive filters |
| `get_property_details` | Complete details for a specific property |
| `get_transactions` | Transaction records for price analysis |
| `get_market_summary` | Quick market overview for a location |
| `get_tru_estimate` | AI-powered property valuation with comparables and trends |


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

### Property Valuation

Get AI-powered market estimates with comparable sales and rental data:

```python
get_tru_estimate(
    location_id="15974",  # Building location ID
    unit_number="710"     # Unit number
)
```

Returns:
- **Estimated Market Value** with confidence level
- **Comparable Sales** (recent similar properties sold)
- **Comparable Rentals** (similar properties rented)
- **2-Year Price Trends** (historical price movements)
- **Yield Projections** (gross & net rental yields)
- **Service Charges** and maintenance costs

Alternative identifiers:
```python
# Using Title Deed
get_tru_estimate(title_deed="25671", year="2022")

# Using Oqood
get_tru_estimate(oqood="161920", year="2023")

# Using DEWA number
get_tru_estimate(dewa="392315580")
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
- Ensure you're subscribed to the UAE Real Estate API on RapidAPI
- Base URL should be: `https://uae-real-estate2.p.rapidapi.com`

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

- [UAE Real Estate API Documentation](https://rapidapi.com/taviansol/api/uae-real-estate2)
- [RapidAPI Hub](https://rapidapi.com/taviansol/api/uae-real-estate2)
- [MCP Documentation](https://modelcontextprotocol.io)
- [Claude Desktop](https://claude.ai/download)
- [Bayut.com](https://www.bayut.com) - Data source

## License

MIT License - see LICENSE file for details

## Support

For issues or questions:
- Open an issue on GitHub
- Check [RapidAPI Support](https://rapidapi.com/taviansol/api/uae-real-estate2) for API issues

## Acknowledgments

- Built with [FastMCP](https://github.com/jlowin/fastmcp)
- Powered by [UAE Real Estate API](https://rapidapi.com/taviansol/api/uae-real-estate2)
- UAE real estate data from [Bayut.com](https://www.bayut.com)
- TruEstimate™ valuations powered by AI market analysis

---

**Built for Claude Desktop** | **UAE Real Estate Data by Bayut**
**Built for Claude Desktop** | **UAE Real Estate Data by Bayut**
