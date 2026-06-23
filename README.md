# Sensor reporting

Report generation for **(insert sensor name here)**. This uses python to create a tex file, which then can be used to generate the report

## Getting started
Requirements:
- Python 3
- A way to process LaTeX (ex: texlive)

Setup:
```
# Get the repo on your machine
git clone https://github.com/haltosan/sensor-vis
# or download the latest release

# Setup the python environment
python3 -m venv .env
. .env/bin/activate
pip install -r requirements.txt

# Generate the .tex report. Replace '<CSV_INPUT_FILE>'
python3 report.py <CSV_INPUT_FILE>

# Convert the .tex file to a pdf. Example with pdflatex
pdflatex out.tex

# Enjoy the out.pdf report
open out.pdf
