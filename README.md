# Bayut MCP Server

MCP Server für UAE Real Estate Suche über die Bayut API. Ermöglicht direkten Zugriff auf Property-Listings, Transaktionsdaten und Market Intelligence.

## Features

### 🔍 Location Search
- Autocomplete für UAE Locations (Cities, Neighborhoods, Buildings)
- Hierarchische Location-Daten mit IDs für weitere Suchen

### 🏠 Property Search
Umfangreiche Filter-Optionen:
- Purpose: for-sale / for-rent
- Price Range (AED)
- Rooms & Bathrooms
- Area (sqft)
- Property Category (Apartments, Villas, Studios, etc.)
- Furnishing Status
- Sortierung nach Price, Date, Popularity

### 📊 Market Intelligence
- Transaction History für Dubai Properties
- Price Trends und Historical Data
- Market Summary Tool für schnelle Area-Analysen

### 🏢 Property Details
- Komplette Property Information
- Photos & Floorplans
- Agent & Agency Details
- Amenities & Features

## Installation

### 1. Prerequisites
```bash
# Python 3.10+ erforderlich
python --version

# RapidAPI Account & API Key
# Get your key at: https://rapidapi.com/datascraper/api/bayut
```

### 2. Setup
```bash
# Navigate to directory
cd bayut_mcp

# Install dependencies
pip install -e .

# Set API Key
export RAPIDAPI_KEY='your-rapidapi-key-here'
```

### 3. Claude Desktop Configuration

Füge zur `claude_desktop_config.json` hinzu:

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

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

### 4. Restart Claude Desktop

Nach der Konfiguration Claude Desktop neu starten.

## Usage Examples

### Location Search
```python
# Finde Location IDs für Dubai South
search_locations("dubai south")

# Finde Business Bay
search_locations("business bay")
```

### Property Search
```python
# Studios zum Verkauf in Dubai South, max 500k AED
search_properties(
    purpose="for-sale",
    locations_ids=[123456],  # Dubai South ID
    category="apartments",
    rooms=[0],  # Studio
    price_max=500000,
    sort_by="lowest_price"
)

# 1-Bedroom zur Miete in Marina
search_properties(
    purpose="for-rent",
    locations_ids=[789012],  # Marina ID
    rooms=[1],
    price_max=80000,
    is_furnished=True
)
```

### Market Analysis
```python
# Quick Summary für eine Area
get_market_summary("Dubai South", purpose="for-sale")

# Transaction History
get_transactions(
    purpose="for-sale",
    locations_ids=[123456],
    category="apartments",
    beds=[0],  # Studios
    start_date="2024-01-01",
    end_date="2024-12-31"
)
```

### Property Details
```python
# Vollständige Info zu einem Property
get_property_details(11065329)
```

## Tools Overview

| Tool | Beschreibung |
|------|-------------|
| `search_locations` | Suche UAE Locations mit Autocomplete |
| `search_properties` | Property Search mit umfangreichen Filtern |
| `get_property_details` | Komplette Details zu einem Property |
| `get_transactions` | Transaction Records für Price Analysis |
| `get_market_summary` | Quick Market Overview für eine Location |

## Use Cases

### 1. Investment Research
- Finde Studios in Dubai South unter 500k AED
- Analysiere Historical Prices über Transactions
- Vergleiche verschiedene Areas

### 2. Rental Market Analysis
- Durchschnittliche Mieten für 1-Bedroom in verschiedenen Areas
- Furnished vs Unfurnished Preisdifferenzen
- Occupancy Trends über Transaction Data

### 3. Golden Visa Planning
- Suche nach 5 Properties für Golden Visa Threshold
- Budget-Optimierung über verschiedene Areas
- ROI-Berechnung mit Rental Yields

## API Limits

- RapidAPI Free Tier: 100 requests/month
- Basic Plan: 1,000 requests/month ($19.99)
- Pro Plan: 10,000 requests/month ($49.99)

## Troubleshooting

### "RAPIDAPI_KEY not set"
```bash
export RAPIDAPI_KEY='your-key-here'
```

### MCP Server not showing in Claude
1. Check `claude_desktop_config.json` Syntax
2. Verify absolute paths
3. Restart Claude Desktop
4. Check Claude Desktop logs

### API Errors
- 401 Unauthorized: API Key falsch oder abgelaufen
- 429 Too Many Requests: Rate Limit erreicht
- 503 Service Unavailable: Bayut API temporär down

## Development

```bash
# Test the server directly
python server.py

# Check MCP protocol
uv --version
```

## Resources

- [Bayut API Docs](https://bayutapi.com/documentation.html)
- [RapidAPI Hub](https://rapidapi.com/datascraper/api/bayut)
- [MCP Documentation](https://modelcontextprotocol.io)

## Support

Bei Fragen oder Issues:
- Bayut API: bayut.restapi@gmail.com
- MCP Issues: [GitHub](https://github.com/modelcontextprotocol)

---

**Built with FastMCP** | **UAE Real Estate Data by Bayut**
