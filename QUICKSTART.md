# Bayut MCP - Quick Start Guide

## Setup in 5 Minutes

### 1. Get RapidAPI Key
1. Gehe zu: https://rapidapi.com/datascraper/api/bayut
2. Registriere dich (kostenlos)
3. Subscribe to Free Plan (100 requests/month)
4. Kopiere deinen API Key

### 2. Configure Claude Desktop

**macOS:**
```bash
code ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

**Windows:**
```bash
code %APPDATA%\Claude\claude_desktop_config.json
```

Füge hinzu:
```json
{
  "mcpServers": {
    "bayut": {
      "command": "python",
      "args": ["/absolute/path/to/bayut_mcp/server.py"],
      "env": {
        "RAPIDAPI_KEY": "YOUR-KEY-HERE"
      }
    }
  }
}
```

⚠️ **Wichtig:** Verwende den **absoluten Pfad** zu server.py!

### 3. Install Dependencies
```bash
cd bayut_mcp
pip install -e .
```

### 4. Restart Claude Desktop

Komplett beenden und neu starten.

## First Search

Jetzt kannst du in Claude fragen:

```
"Suche mir Studios in Dubai South die unter 500k AED kosten"
```

Claude wird automatisch:
1. `search_locations("dubai south")` verwenden
2. Die location_ids extrahieren
3. `search_properties()` mit deinen Filtern aufrufen
4. Die Ergebnisse formatiert präsentieren

## Common Use Cases

### Investment Research
```
"Zeig mir die durchschnittlichen Preise für Studios in JVC, Dubai South und International City"
```

### Rental Yield Analysis
```
"Vergleiche die Rental Yields für 1-Bedroom Apartments in Business Bay vs. Dubai Marina"
```

### Golden Visa Planning
```
"Finde 5 Properties die zusammen unter 2M AED kosten und mindestens 7% Yield haben"
```

### Market Trends
```
"Zeig mir die Transaction History für Studios in Dubai South in den letzten 12 Monaten"
```

## Available Tools

Wenn Claude nicht automatisch die richtigen Tools verwendet, kannst du auch direkt fragen:

- `search_locations` - "Finde Location IDs für..."
- `search_properties` - "Suche Properties mit..."
- `get_property_details` - "Zeig Details für Property ID..."
- `get_transactions` - "Zeig Transaction History für..."
- `get_market_summary` - "Gib mir einen Market Summary für..."

## Troubleshooting

### "No tools available"
→ Claude Desktop Config überprüfen und neu starten

### "401 Unauthorized"
→ API Key in der Config überprüfen

### "Module not found"
→ Dependencies installieren: `pip install -e .`

### Slow Responses
→ Normal bei ersten Requests (API warmup)

## Tips

1. **Location IDs merken**: Einmal gefundene IDs kannst du wiederverwenden
2. **Price Ranges**: Sei realistisch mit Filtern (Dubai South Studios: 350-600k)
3. **Pagination**: Große Suchen über mehrere Pages verteilt
4. **Rate Limits**: Free Plan = 100 requests/month (ca. 3 pro Tag)

## Next Steps

1. Teste verschiedene Areas
2. Baue eine Property Watchlist auf
3. Tracke Price Changes über Zeit
4. Analysiere Rental Yields
5. Upgrade zu Basic Plan wenn du mehr brauchst

---

**Pro Tip:** Kombiniere mit deinen Excel/Spreadsheet Skills - export die Daten und baue dir ein Investment Dashboard!
