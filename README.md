# BALA — Portfolio

A standalone HTML, CSS, and Python/Flask portfolio, matching the Lovable preview. This download has no React, JavaScript, Node, or CSS framework dependency. Google Fonts requires an internet connection; all artwork is included locally.

## Run

Python 3.10 or newer is recommended.

```sh
python -m venv .venv
# macOS/Linux: 
source .venv/bin/activate
# Windows instead:
# .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000. For production use a suitable WSGI host rather than Flask's development server.

## What is included

Seven portfolio pages, mobile navigation, CSS petal animations, reduced-motion support, three project-detail pages, four sample-photo pages, and server-rendered photography category filters. The preview uses pop-up viewers; this no-JavaScript version uses dedicated detail pages instead.

## Make it yours

Edit the HTML files in `templates/` and the design tokens in `static/styles.css`. Replace artwork in `static/images/` with your own files. Project descriptions and gallery images are sample content, not verified completed work or original photographs. The full name and Podaturpet address were supplied by the owner. Other biographical details follow the supplied visual references and should be reviewed before publishing.

No email address or resume was supplied: those are clearly marked as not yet available. Add your real email links in the templates. To add a resume, place it in `static/` and replace `/resume` links with `/static/resume.pdf`.

No message is sent and no personal information is collected or stored. There is no Gemini logo.

## Tests

```sh
python -m unittest discover -s tests
```
