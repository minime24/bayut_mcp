#!/usr/bin/env python3
"""
Example usage of Bayut MCP tools
Run this to test the server functionality
"""

import json

# Example 1: Find Dubai South location
print("=" * 60)
print("EXAMPLE 1: Location Search - Dubai South")
print("=" * 60)

location_search_example = {
    "tool": "search_locations",
    "params": {
        "query": "dubai south"
    }
}

print(json.dumps(location_search_example, indent=2))
print("\n")

# Example 2: Search for studios in Dubai South under 500k
print("=" * 60)
print("EXAMPLE 2: Property Search - Studios under 500k AED")
print("=" * 60)

property_search_example = {
    "tool": "search_properties",
    "params": {
        "purpose": "for-sale",
        "locations_ids": [1, 1010, 10100],  # Example IDs - replace with actual
        "category": "apartments",
        "rooms": [0],  # Studio
        "price_max": 500000,
        "sort_by": "lowest_price",
        "page": 0
    }
}

print(json.dumps(property_search_example, indent=2))
print("\n")

# Example 3: Market Summary
print("=" * 60)
print("EXAMPLE 3: Market Summary - Quick Overview")
print("=" * 60)

market_summary_example = {
    "tool": "get_market_summary",
    "params": {
        "location_query": "dubai south",
        "purpose": "for-sale"
    }
}

print(json.dumps(market_summary_example, indent=2))
print("\n")

# Example 4: Transaction History
print("=" * 60)
print("EXAMPLE 4: Transaction History - Last 6 Months")
print("=" * 60)

transactions_example = {
    "tool": "get_transactions",
    "params": {
        "purpose": "for-sale",
        "locations_ids": [1, 1010, 10100],
        "category": "apartments",
        "beds": [0],
        "start_date": "2024-06-01",
        "end_date": "2024-12-01",
        "sort_by": "date",
        "order": "desc"
    }
}

print(json.dumps(transactions_example, indent=2))
print("\n")

# Example 5: Property Details
print("=" * 60)
print("EXAMPLE 5: Property Details")
print("=" * 60)

property_details_example = {
    "tool": "get_property_details",
    "params": {
        "property_id": 11065329  # Example from documentation
    }
}

print(json.dumps(property_details_example, indent=2))
print("\n")

# Example 6: Compare Multiple Areas
print("=" * 60)
print("EXAMPLE 6: Multi-Area Comparison Workflow")
print("=" * 60)

comparison_workflow = """
# Workflow to compare investment opportunities across areas:

1. Search locations:
   - search_locations("dubai south")
   - search_locations("jumeirah village circle")
   - search_locations("international city")

2. Get market summaries for each:
   - get_market_summary("dubai south", "for-sale")
   - get_market_summary("jumeirah village circle", "for-sale")
   - get_market_summary("international city", "for-sale")

3. Deep dive on best candidate:
   - search_properties() with specific filters
   - get_transactions() for price history
   - get_property_details() for promising listings

4. Calculate ROI:
   - Purchase price from listings
   - Rental income from for-rent search
   - Annual yield = (annual_rent / purchase_price) * 100
"""

print(comparison_workflow)
print("\n")

# Example 7: Golden Visa Property Hunt
print("=" * 60)
print("EXAMPLE 7: Golden Visa - 5 Studios under 2M AED total")
print("=" * 60)

golden_visa_strategy = """
# Strategy for finding 5 studios totaling ~2M AED for Golden Visa:

Target: 5 properties × 400k AED average = 2M AED total

1. Find locations with studios in 350-450k range:
   search_properties(
       purpose="for-sale",
       locations_ids=[...],  # Multiple affordable areas
       rooms=[0],
       price_min=350000,
       price_max=450000,
       sort_by="lowest_price"
   )

2. Focus areas (typically affordable):
   - Dubai South
   - Jumeirah Village Circle (JVC)
   - International City
   - Discovery Gardens
   - Liwan / Queue Point

3. Analyze rental yields:
   - Get rental comps: search_properties(purpose="for-rent", ...)
   - Calculate yield: (annual_rent / purchase_price) * 100
   - Target: Minimum 7-8% gross yield

4. Check transaction history:
   get_transactions() to verify prices are stable/appreciating

5. Verify property details:
   - Ready to move-in (completed)
   - Good building reputation
   - Amenities (pool, gym, parking)
   - Developer track record
"""

print(golden_visa_strategy)

print("\n" + "=" * 60)
print("Ready to use! Start with: search_locations('dubai south')")
print("=" * 60)
