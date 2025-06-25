from parser import read_text
from extractor import extract_citations
from verifier import verify_citation
from quote_checker import verify_quote
from report import generate_report
from utils import log


def run_verification(input_source: str) -> None:
    text = read_text(input_source)
    citations = extract_citations(text)
    log(f"Found {len(citations)} citation(s)")
    results = []
    for c in citations:
        result = verify_citation(c)
        # Quote verification placeholder
        results.append(result)
    summary = generate_report(results)
    print(summary)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python -m legal_rinse.main <file-or-text>")
        raise SystemExit(1)
    run_verification(sys.argv[1])
