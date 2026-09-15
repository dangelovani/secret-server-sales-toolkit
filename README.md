### The Secret Server — Sales Toolkit & Investor Resources

The Secret Server (TSS) is described by its founder as the **first patented 3D augmented-reality (AR) menu and staff-training platform for hospitality**. It combines interactive menu experiences with staff education for restaurants, bars, hotels, resorts and event venues. The patent/first-to-market wording is the company's positioning; this repository does not contain patent documentation or independent legal verification.

This private repository preserves the UK-localised sales toolkit, investor resources and the source scripts, HTML templates and brand assets used to build them. **It is a collateral repository, not the production AR application's source code.**

#### Ready-to-use documents

Open or download these files directly from GitHub; no build is needed to use the finished documents.

| Document | File |
|---|---|
| UK pitch deck | [TSS_Pitch_Deck_UK.pdf](TSS_Pitch_Deck_UK.pdf) |
| UK sell sheet | [TSS_Sell_Sheet_UK.pdf](TSS_Sell_Sheet_UK.pdf) |
| UK sell sheet and packages | [TSS_Sell_Sheet_and_Packages_UK.pdf](TSS_Sell_Sheet_and_Packages_UK.pdf) |
| UK comparison chart | [TSS_Comparison_Chart_UK.pdf](TSS_Comparison_Chart_UK.pdf) |
| UK asset pricing comparisons | [TSS_Asset_Pricing_Comparisons_UK.pdf](TSS_Asset_Pricing_Comparisons_UK.pdf) |
| UK conversation starter | [TSS_Start_the_Conversation_UK.pdf](TSS_Start_the_Conversation_UK.pdf) |
| UK pitch guidance | [TSS_Pitch_Perfect_UK.pdf](TSS_Pitch_Perfect_UK.pdf) |
| UK pitch scripts | [TSS_Pitch_Scripts_UK.pdf](TSS_Pitch_Scripts_UK.pdf) |
| UK prototype menu | [TSS_Prototype_Menu_UK.pdf](TSS_Prototype_Menu_UK.pdf) |
| Investor database — Wave 1 | [TSS_Investor_Database_Wave1.xlsx](TSS_Investor_Database_Wave1.xlsx) |
| Investor directory — Wave 1 | [TSS_Investor_Directory_Wave1.pdf](TSS_Investor_Directory_Wave1.pdf) |
| Five-year growth roadmap | [TSS_5_Year_Growth_Roadmap.pdf](TSS_5_Year_Growth_Roadmap.pdf) |

The spreadsheet contains **Investor Database**, **Outreach Messages**, and **Methodology & Notes** worksheets. Personalise outreach merge fields and check current investment criteria/contact information before contacting prospects. Inclusion does not imply investor interest, endorsement or a relationship with TSS.

#### Repository structure

```text
secret-server-sales-toolkit/
├── README.md
├── .gitignore
├── TSS_*_UK.pdf                       # Nine UK sales documents
├── TSS_Investor_Database_Wave1.xlsx
├── TSS_Investor_Directory_Wave1.pdf
├── TSS_5_Year_Growth_Roadmap.pdf
└── build/                            # Source files, not disposable build output
    ├── gen.js                        # Abacus HTML-to-PDF API client
    ├── build_xlsx.py                 # Investor workbook generator
    ├── build_pdf_html.py             # Investor HTML generator (not a PDF renderer)
    ├── investor_data.py              # TSS profile and investor records
    ├── outreach_messages.py          # Category-specific outreach messages
    ├── assets.json                   # Embedded logo and QR image data
    ├── logo_white.png
    ├── logo_transparent.png
    └── html/
        ├── pitch_deck.html
        ├── sell_sheet.html
        ├── sell_sheet_packages.html
        ├── comparison_chart.html
        ├── asset_pricing.html
        ├── start_conversation.html
        ├── pitch_perfect.html
        ├── pitch_scripts.html
        ├── menu.html
        └── investor_directory.html
```

#### Requirements

- Python 3.10+ and `openpyxl` for the investor workbook.
- Node.js 22+ for PDF generation (uses built-in `fetch`; no npm packages required).
- An Abacus API credential authorised for the HTML-to-PDF endpoints, plus internet access, to regenerate PDFs. Access and charges depend on your account.
- An XLSX reader and a PDF reader to use the finished deliverables.

#### Setup

Run from the repository root on your development machine:

```bash
git clone https://github.com/dangelovani/secret-server-sales-toolkit.git
cd secret-server-sales-toolkit
python3 -m venv .venv
source .venv/bin/activate
python -m pip install 'openpyxl>=3.1,<4'
```

The private repository requires GitHub authentication. On Windows, activate the environment with `.venv\Scripts\Activate.ps1` in PowerShell instead.

#### Rebuild the investor resources

Edit `build/investor_data.py` and `build/outreach_messages.py`, then run:

```bash
python build/build_xlsx.py
python build/build_pdf_html.py
```

These commands overwrite `TSS_Investor_Database_Wave1.xlsx` and `build/html/investor_directory.html` respectively, relative to the checkout rather than a particular computer. Commit or back up edits first. Editing the XLSX directly will not update the Python data source.

#### Generate PDFs

Supply `ABACUSAI_API_KEY` (or `ABACUS_API_KEY`) through your shell's environment or secret manager. Never commit real credentials. Alternatively, put `ABACUSAI_API_KEY=your-key` in a local, ignored `.env` file and use Node's `--env-file=.env` option. The script does not automatically read `.env` files.

```bash
# With the credential already in your environment:
node build/gen.js build/html/sell_sheet.html TSS_Sell_Sheet_UK.pdf A4 false

# Or explicitly load your local .env file:
node --env-file=.env build/gen.js build/html/sell_sheet.html TSS_Sell_Sheet_UK.pdf A4 false
```

General syntax:

```text
node build/gen.js <htmlFile> <outPdf> [format] [landscape] [width] [height] [mode]
```

- Default paper format is `A4`; landscape is enabled only by the literal `true`.
- When both width and height are provided, those dimensions override the paper format.
- `textfooter` mode adds a confidentiality footer and a 24 mm bottom margin. Templates may already include footer text; check for duplication before using this option.
- `assets.json` replaces `__LOGO_WHITE__`, `__LOGO_TRANS__` and `__QR__` placeholders before rendering. Updating the standalone PNGs alone does not update embedded image data.
- HTML content and embedded assets are sent to Abacus for conversion. Confirm you are authorised to send any confidential data. The client polls for completion and exits with an error on failure or timeout.

Suggested commands matching the archived documents' general dimensions:

```bash
node build/gen.js build/html/pitch_deck.html TSS_Pitch_Deck_UK.pdf A4 false 1440px 810px
node build/gen.js build/html/sell_sheet.html TSS_Sell_Sheet_UK.pdf A4 false
node build/gen.js build/html/sell_sheet_packages.html TSS_Sell_Sheet_and_Packages_UK.pdf A4 false
node build/gen.js build/html/comparison_chart.html TSS_Comparison_Chart_UK.pdf A4 true
node build/gen.js build/html/asset_pricing.html TSS_Asset_Pricing_Comparisons_UK.pdf A4 false
node build/gen.js build/html/start_conversation.html TSS_Start_the_Conversation_UK.pdf A4 false
node build/gen.js build/html/pitch_perfect.html TSS_Pitch_Perfect_UK.pdf A4 false
node build/gen.js build/html/pitch_scripts.html TSS_Pitch_Scripts_UK.pdf A4 false
node build/gen.js build/html/menu.html TSS_Prototype_Menu_UK.pdf A4 false 384px 1210px
node build/gen.js build/html/investor_directory.html TSS_Investor_Directory_Wave1.pdf A4 false
```

These are rebuild starting points, not a guarantee of pixel-identical output. Review pagination, images, logos and footers before replacing approved collateral. Some HTML templates reference remote CDN imagery; those images are not included as separate local assets and must remain reachable for rebuilding. The logo PNGs and embedded logo/QR data are included. The growth roadmap is an archived PDF only: no matching source template or generator was supplied.

#### Review and maintenance

1. Work on a new branch and edit the appropriate source or template.
2. Rebuild affected documents and review them visually; verify pricing, claims and contact details.
3. Commit sources and their corresponding PDF/XLSX outputs together.
4. Open a pull request for review before merging into `main`.

The supplied PDF and XLSX files are preserved as received. The import makes only portability changes to the build scripts: repository-relative Python paths and environment-based API credentials. Live PDF API conversion is not verified by this import; consuming existing PDFs does not require API access.

#### Confidentiality and security

Keep this repository private. It contains commercially sensitive collateral, investor research and outreach material. Share only with authorised collaborators and follow applicable privacy and direct-marketing rules. The company description, commercial claims and data are supplied content, not independent due diligence.

`.gitignore` excludes dependency folders, environment files, private-key files, caches, temporary files and local metadata. It intentionally retains `build/`, PDFs and XLSX files. Check staged changes for secrets before every push; ignore rules do not remove credentials already tracked by Git.

No open-source licence is granted by this repository. TSS branding and proprietary materials remain subject to their owners' rights.
