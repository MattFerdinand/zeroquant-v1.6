# ZeroQuant v2.0

Deployment-ready cockpit system.

## Legal Rinse Agent

This repository includes a small tool for verifying legal citations. You can run it from the command line or via a minimal web interface.

### Command Line

```bash
python -m legal_rinse.main <file-or-text>
```

### Web Interface

Install dependencies and start the Flask app:

```bash
pip install flask requests
python -m legal_rinse.app
```

Then open `http://localhost:5000` in your browser (iPhone, iPad, or desktop) and submit text or a document for verification.

