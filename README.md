# music_school_backend

Python automation tool built for a music school client. Runs once a month and sends the director a single email with two reports: Google reviews summary and competitor pricing analysis.

## What this does

**1. Google Reviews**
- Fetches the latest reviews from Google Maps
- Parses rating, date, author, and review text
- Classifies sentiment (positive / negative / neutral)
- Builds a formatted summary table

**2. Competitor Pricing**
- Scrapes pricing pages of competitor music schools
- Extracts all pricing options: individual lessons, group formats, subscription packages, trial lessons, discounts
- Builds a detailed comparison table

**3. Email Report**
- Combines both tables into a single HTML email
- Sends automatically to the director's inbox
- Subject line includes the report date

## Example output

The email looks like this:

![Email report — reviews section](screenshots/email-reviews.png)
![Email report — pricing section](screenshots/email-pricing.png)

## Stack

- Python 3
- `requests` + `BeautifulSoup` — web scraping
- Google Maps API — reviews
- `smtplib` / Gmail API — email sending
- `schedule` — monthly trigger

## Setup

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and fill in:

```
GOOGLE_MAPS_API_KEY=your_key
GMAIL_USER=your_email@gmail.com
GMAIL_APP_PASSWORD=your_app_password
DIRECTOR_EMAIL=director@example.com
COMPETITOR_URLS=https://school1.com/prices,https://school2.com/prices
```

Then run:

```bash
python main.py
```

## Notes

Competitor URLs, email addresses, and API keys are not included. All personal data visible in screenshots has been blurred.
