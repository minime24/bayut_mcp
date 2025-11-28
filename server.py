#!/usr/bin/env python3
"""
Bayut MCP Server - Real Estate Search for UAE Properties
Provides tools to search locations and properties on Bayut.com
"""

import os
import httpx
from typing import Optional, List
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("Bayut Real Estate")

# API Configuration
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY", "")
BASE_URL = "https://bayut-api1.p.rapidapi.com"

HEADERS = {
    "x-rapidapi-key": RAPIDAPI_KEY,
    "x-rapidapi-host": "bayut-api1.p.rapidapi.com"
}


def make_request(method: str, endpoint: str, params: dict = None, json_data: dict = None) -> dict:
    """Make HTTP request to Bayut API"""
    url = f"{BASE_URL}{endpoint}"
    
    with httpx.Client(timeout=30.0) as client:
        if method == "GET":
            response = client.get(url, headers=HEADERS, params=params)
        elif method == "POST":
            response = client.post(url, headers=HEADERS, params=params, json=json_data)
        else:
            raise ValueError(f"Unsupported method: {method}")
        
        response.raise_for_status()
        return response.json()


@mcp.tool()
def search_locations(query: str, page: int = 0) -> dict:
    """
    Search for locations in UAE (cities, neighborhoods, buildings).
    Works like autocomplete - returns matching locations with IDs.
    
    Args:
        query: Search term (e.g., "dubai south", "downtown", "marina")
        page: Pagination index (default: 0)
    
    Returns:
        List of locations with IDs, hierarchy, and coordinates
    """
    params = {
        "query": query,
        "page": page,
        "langs": "en"
    }
    
    result = make_request("GET", "/locations_search", params=params)
    
    # Format output for better readability
    if "results" in result:
        locations = []
        for item in result["results"]:
            loc = {
                "id": item.get("id"),
                "name": item.get("name"),
                "level": item.get("level"),
                "full": item.get("full", {}),
                "coordinates": item.get("coordinates"),
                "completion_status": item.get("completion_status")
            }
            locations.append(loc)
        
        return {
            "total": result.get("count", 0),
            "locations": locations
        }
    
    return result


@mcp.tool()
def search_properties(
    purpose: str,
    locations_ids: List[int],
    category: Optional[str] = None,
    price_min: Optional[float] = None,
    price_max: Optional[float] = None,
    rooms: Optional[List[int]] = None,
    baths: Optional[List[int]] = None,
    area_min: Optional[float] = None,
    area_max: Optional[float] = None,
    is_furnished: Optional[bool] = None,
    sort_by: str = "popular",
    page: int = 0
) -> dict:
    """
    Search for properties with detailed filters.
    
    Args:
        purpose: "for-sale" or "for-rent"
        locations_ids: List of location IDs (from search_locations)
        category: Property type (apartments, villas, townhouses, etc.)
        price_min: Minimum price in AED
        price_max: Maximum price in AED
        rooms: List of bedroom counts [1, 2, 3, etc.]
        baths: List of bathroom counts
        area_min: Minimum area in sqft
        area_max: Maximum area in sqft
        is_furnished: Filter for furnished properties
        sort_by: Sort order (popular, latest, lowest_price, highest_price, verified)
        page: Pagination index
    
    Returns:
        List of properties with details
    """
    body = {
        "purpose": purpose,
        "locations_ids": locations_ids,
        "index": sort_by
    }
    
    # Add optional filters
    if category:
        body["category"] = category
    if price_min is not None:
        body["price_min"] = price_min
    if price_max is not None:
        body["price_max"] = price_max
    if rooms:
        body["rooms"] = rooms
    if baths:
        body["baths"] = baths
    if area_min is not None:
        body["area_min"] = area_min
    if area_max is not None:
        body["area_max"] = area_max
    if is_furnished is not None:
        body["is_furnished"] = is_furnished
    
    params = {"page": page, "langs": "en"}
    
    result = make_request("POST", "/properties_search", params=params, json_data=body)
    
    # Format output
    if "results" in result:
        properties = []
        for item in result["results"]:
            prop = {
                "id": item.get("id"),
                "title": item.get("title"),
                "price": item.get("price"),
                "area": item.get("area", {}),
                "details": item.get("details", {}),
                "location": item.get("location", {}),
                "purpose": item.get("purpose"),
                "type": item.get("type", {}),
                "url": item.get("meta", {}).get("url", f"https://www.bayut.com/property/details-{item.get('id')}.html"),
                "agent": item.get("agent", {}),
                "agency": item.get("agency", {}),
                "verification": item.get("verification", {})
            }
            properties.append(prop)
        
        return {
            "total": result.get("count", 0),
            "page": page,
            "properties": properties
        }
    
    return result


@mcp.tool()
def get_property_details(property_id: int) -> dict:
    """
    Get complete details for a specific property.
    
    Args:
        property_id: Property ID (from search results or Bayut URL)
    
    Returns:
        Complete property information including photos, floorplans, agent details
    """
    result = make_request("GET", f"/property/{property_id}", params={"langs": "en"})
    
    if result:
        # Extract key information
        formatted = {
            "id": result.get("id"),
            "title": result.get("title"),
            "description": result.get("description"),
            "price": result.get("price"),
            "price_formatted": result.get("price_formatted"),
            "rooms": result.get("rooms"),
            "baths": result.get("baths"),
            "area": result.get("area"),
            "location": result.get("location"),
            "purpose": result.get("purpose"),
            "category": result.get("category"),
            "furnishing_status": result.get("furnishing_status"),
            "amenities": result.get("amenities", []),
            "url": result.get("url"),
            "agent": result.get("agent"),
            "agency": result.get("agency"),
            "photos": result.get("photos", [])[:5],  # Limit to first 5 photos
            "phone_number": result.get("phone_number"),
            "verified": result.get("verification", {}).get("eligible", False)
        }
        return formatted
    
    return result


@mcp.tool()
def get_transactions(
    purpose: str,
    locations_ids: List[int],
    category: Optional[str] = None,
    price_min: Optional[int] = None,
    price_max: Optional[int] = None,
    beds: Optional[List[int]] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    sort_by: str = "date",
    order: str = "desc",
    page: int = 0
) -> dict:
    """
    Get real estate transaction records for Dubai properties.
    Useful for price analysis and market trends.
    
    Args:
        purpose: "for-sale" or "for-rent"
        locations_ids: List of location IDs
        category: Property category
        price_min: Minimum transaction price (AED)
        price_max: Maximum transaction price (AED)
        beds: List of bedroom counts
        start_date: Start date (YYYY-MM-DD)
        end_date: End date (YYYY-MM-DD)
        sort_by: Sort field (date, amount, rent, builtup_area, beds)
        order: Sort order (asc or desc)
        page: Pagination index
    
    Returns:
        List of transaction records with prices and details
    """
    body = {
        "purpose": purpose,
        "locations_ids": locations_ids,
        "sort_by": sort_by,
        "order": order
    }
    
    # Add optional filters
    if category:
        body["category"] = category
    if price_min is not None:
        body["price_min"] = price_min
    if price_max is not None:
        body["price_max"] = price_max
    if beds:
        body["beds"] = beds
    if start_date:
        body["start_date"] = start_date
    if end_date:
        body["end_date"] = end_date
    
    params = {"page": page}
    
    result = make_request("POST", "/transactions", params=params, json_data=body)
    
    # Format output
    if "results" in result:
        transactions = []
        for item in result["results"]:
            trans = {
                "price": item.get("amount") or item.get("rent"),
                "property": item.get("property", {}),
                "location": item.get("location", {}),
                "date": item.get("date"),
                "contract": item.get("contract", {}),
                "category": item.get("category"),
                "agent_id": item.get("agent_id")
            }
            transactions.append(trans)
        
        return {
            "total": result.get("count", 0),
            "page": page,
            "transactions": transactions
        }
    
    return result


@mcp.tool()
def get_market_summary(location_query: str, purpose: str = "for-sale") -> dict:
    """
    Get a quick market summary for a location including available properties
    and recent transactions. Perfect for quick area analysis.
    
    Args:
        location_query: Location name (e.g., "Dubai South", "Business Bay")
        purpose: "for-sale" or "for-rent"
    
    Returns:
        Summary with property stats and transaction data
    """
    # First, find the location
    locations = search_locations(location_query)
    
    if not locations.get("locations"):
        return {"error": "Location not found"}
    
    # Get first matching location
    location = locations["locations"][0]
    location_id = location["id"]
    location_name = location["name"]
    
    # Search properties
    props = search_properties(
        purpose=purpose,
        locations_ids=[location_id],
        sort_by="latest",
        page=0
    )
    
    # Get transactions
    trans = get_transactions(
        purpose=purpose,
        locations_ids=[location_id],
        page=0
    )
    
    # Calculate averages
    properties = props.get("properties", [])
    transactions = trans.get("transactions", [])
    
    avg_price = sum(p["price"] for p in properties if p.get("price")) / len(properties) if properties else 0
    
    trans_prices = [t["price"] for t in transactions if t.get("price")]
    avg_trans_price = sum(trans_prices) / len(trans_prices) if trans_prices else 0
    
    return {
        "location": location_name,
        "location_id": location_id,
        "purpose": purpose,
        "current_listings": {
            "total": props.get("total", 0),
            "average_price": round(avg_price, 2),
            "properties": properties[:5]  # Top 5
        },
        "recent_transactions": {
            "total": trans.get("total", 0),
            "average_price": round(avg_trans_price, 2),
            "transactions": transactions[:5]  # Top 5
        }
    }


if __name__ == "__main__":
    # Check for API key
    if not RAPIDAPI_KEY:
        print("⚠️  Warning: RAPIDAPI_KEY not set!")
        print("Set it with: export RAPIDAPI_KEY='your-key-here'")
    
    mcp.run()
