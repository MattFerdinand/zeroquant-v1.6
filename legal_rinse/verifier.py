import requests
from typing import Dict


def verify_citation(citation: str) -> Dict[str, str]:
    """Verify a citation using CourtListener's public API."""
    endpoint = "https://www.courtlistener.com/api/rest/v3/search/"
    params = {"q": citation, "type": "opinion"}
    try:
        resp = requests.get(endpoint, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except Exception as exc:
        return {"citation": citation, "verified": False, "error": str(exc)}

    results = data.get("results", [])
    if results:
        return {
            "citation": citation,
            "verified": True,
            "link": results[0].get("absolute_url"),
        }
    return {"citation": citation, "verified": False}
