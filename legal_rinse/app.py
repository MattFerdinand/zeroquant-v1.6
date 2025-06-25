from flask import Flask, request, render_template_string
from parser import read_text
from extractor import extract_citations
from verifier import verify_citation
from report import generate_report
from utils import log

app = Flask(__name__)

FORM_HTML = """
<!doctype html>
<title>Legal Rinse Agent</title>
<h1>Verify Legal Citations</h1>
<form method=post enctype=multipart/form-data>
  <textarea name=text cols=80 rows=10 placeholder="Paste legal text here"></textarea><br>
  <input type=file name=file><br>
  <input type=submit value=Verify>
</form>
<pre>{{ result }}</pre>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        text = request.form.get('text') or ''
        if 'file' in request.files and request.files['file']:
            file = request.files['file']
            text += file.read().decode('utf-8')
        if text:
            log("Processing input text")
            citations = extract_citations(text)
            res = [verify_citation(c) for c in citations]
            result = generate_report(res)
    return render_template_string(FORM_HTML, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
