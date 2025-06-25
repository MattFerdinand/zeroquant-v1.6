import re
from typing import List

CITATION_REGEX = re.compile(
    r"\b([A-Z][a-zA-Z]+ v\. [A-Z][a-zA-Z]+, \d+ [A-Z\.]+ \d+ \(\d{4}\))\b"
)


def extract_citations(text: str) -> List[str]:
    """Return a list of legal citation strings."""
    return CITATION_REGEX.findall(text)
