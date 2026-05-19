name: Update NSE Stocks to Google Sheet

on:
  push:
    branches:
      - main
  schedule:
    - cron: '0 5 * * 1-5' # Mon-Fri har din dopahar 10:30 AM IST par chalega (NSE data aane ke baad)
  workflow_dispatch:

env:
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: "true"

jobs:
  update-sheet:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v6

      - name: Set up Python
        uses: actions/setup-python@v6
        with:
          python-version: '3.11'

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run Update Script
        env:
          # Google Cloud Console ki credentials key yahan pass hogi
          GCP_CREDENTIALS: ${{ secrets.GCP_CREDENTIALS }}
        run: |
          python main.py  # Agar aapki file ka naam alag hai, to main.py ki jagah wo likhein
