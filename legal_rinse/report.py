from typing import Iterable, Dict


def generate_report(results: Iterable[Dict[str, str]]) -> str:
    """Generate a plain-text summary of verification results."""
    lines = []
    for res in results:
        if res.get("verified"):
            link = res.get("link", "")
            lines.append(f"✅ {res['citation']} - {link}")
        else:
            reason = res.get("error", "not found")
            lines.append(f"❌ {res['citation']} - {reason}")
    return "\n".join(lines)
