name: Run Python Pipeline

on:
  workflow_dispatch:

jobs:
  run-pipeline:
    runs-on: self-hosted
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Ativar ambiente virtual
        shell: powershell
        run: |
          .\.venv\Scripts\Activate.ps1

      - name: Executar pipeline
        shell: powershell
        run: |
          .\.venv\Scripts\Activate.ps1
          python pipeline.py
