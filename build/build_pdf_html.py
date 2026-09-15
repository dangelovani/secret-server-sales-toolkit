# -*- coding: utf-8 -*-
import sys, html
from pathlib import Path
BUILD_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BUILD_DIR))
from investor_data import SECTIONS, TSS
from outreach_messages import MESSAGES

def esc(s):
    return html.escape(s or "", quote=True)

def msg_html(txt):
    return esc(txt).replace("\n", "<br>")

total = sum(len(s["investors"]) for s in SECTIONS)

CSS = """
*{margin:0;padding:0;box-sizing:border-box;}
body{font-family:'Inter','Helvetica Neue',Arial,sans-serif;color:#1f2937;-webkit-print-color-adjust:exact;print-color-adjust:exact;font-size:11px;line-height:1.5;}
.masthead{display:flex;align-items:center;justify-content:space-between;background:linear-gradient(120deg,#0d2a4d,#2d5378);padding:16px 40px;color:#fff;}
.masthead img{height:44px;}
.mh-r{text-align:right;}
.mh-r .t{font-size:12px;font-weight:700;letter-spacing:2px;color:#cddbeb;}
.mh-r .s{font-size:9px;letter-spacing:3px;color:#8fb0cf;margin-top:2px;}
.wrap{padding:26px 40px 30px;}
/* Cover */
.cover{padding:60px 46px 40px;}
h1.title{font-size:30px;color:#0d2a4d;font-weight:800;letter-spacing:.3px;line-height:1.15;}
.subtitle{font-size:13px;color:#4682B4;font-weight:600;letter-spacing:1px;text-transform:uppercase;margin-top:8px;}
.rule{height:3px;width:80px;background:#c9a84c;margin:16px 0 22px;}
.lead{font-size:13px;color:#243b53;max-width:640px;}
.statgrid{display:flex;gap:14px;margin:26px 0 8px;flex-wrap:wrap;}
.statcard{background:#0d2a4d;color:#fff;border-radius:10px;padding:16px 18px;min-width:150px;flex:1;}
.statcard .n{font-size:26px;font-weight:800;color:#e7c96b;}
.statcard .l{font-size:10px;letter-spacing:.6px;color:#c7d6e6;margin-top:3px;text-transform:uppercase;}
.note{background:#f6f9fc;border-left:4px solid #4682B4;border-radius:0 8px 8px 0;padding:14px 18px;margin:16px 0;font-size:11px;max-width:660px;}
.note .h{font-weight:700;color:#0d2a4d;font-size:11px;text-transform:uppercase;letter-spacing:.6px;margin-bottom:4px;}
.toc{margin-top:20px;font-size:11.5px;max-width:660px;}
.toc div{padding:5px 0;border-bottom:1px solid #e3ecf5;display:flex;justify-content:space-between;}
.toc .c{color:#4682B4;font-weight:700;}
/* Section */
.pagebreak{page-break-before:always;}
.sechead{background:linear-gradient(120deg,#0d2a4d,#2d5378);color:#fff;padding:12px 18px;border-radius:8px;margin:6px 0 6px;}
.sechead .n{font-size:15px;font-weight:800;letter-spacing:.3px;}
.sechead .b{font-size:10px;color:#cddbeb;margin-top:3px;line-height:1.45;}
table{width:100%;border-collapse:collapse;margin:10px 0 4px;font-size:9.2px;}
th{background:#0d2a4d;color:#fff;text-align:left;padding:6px 7px;font-weight:700;font-size:8.6px;letter-spacing:.3px;}
td{padding:6px 7px;border-bottom:1px solid #e3ecf5;vertical-align:top;}
tr:nth-child(even) td{background:#f5f9fc;}
.firm{font-weight:700;color:#0d2a4d;}
.web{color:#4682B4;font-weight:600;}
.pill{display:inline-block;background:#eef3f8;color:#0d2a4d;font-weight:700;font-size:9.5px;letter-spacing:1.2px;text-transform:uppercase;padding:6px 14px;border-radius:20px;border:1px solid #d5e2ee;margin:18px 0 8px;}
.msgwrap{display:flex;gap:10px;margin:6px 0 2px;flex-wrap:nowrap;}
.msgbox{flex:1;background:#f6f9fc;border:1px solid #dce7f2;border-top:3px solid #4682B4;border-radius:6px;padding:10px 12px;font-size:8.6px;line-height:1.5;}
.msgbox.formal{border-top-color:#0d2a4d;}
.msgbox.conv{border-top-color:#4682B4;}
.msgbox.bold{border-top-color:#c9a84c;}
.msgbox .h{font-weight:800;color:#0d2a4d;font-size:9px;text-transform:uppercase;letter-spacing:.6px;margin-bottom:6px;}
.docfooter{background:#0d2a4d;color:#c7d6e6;padding:8px 40px;font-size:7.4px;line-height:1.45;text-align:justify;margin-top:26px;}
.docfooter b{color:#e7c96b;letter-spacing:1px;}
.contact{color:#9fbcd6;font-weight:600;}
"""

MH = ('<div class="masthead"><img src="__LOGO_TRANS__" alt="The Secret Server logo">'
      '<div class="mh-r"><div class="t">THE SECRET SERVER</div><div class="s">INVESTOR RELATIONS</div></div></div>')

FOOTER = ('<div class="docfooter"><b>CONFIDENTIAL</b> &nbsp; \u00A9 2026 The Secret Server. This document is confidential and '
          'proprietary, provided solely for the named recipient\u2019s evaluation. It may not be reproduced, distributed or '
          'disclosed without prior written consent. Any personal data referenced is processed in accordance with the UK GDPR '
          'and the EU General Data Protection Regulation (EU) 2016/679. &nbsp;&bull;&nbsp; '
          '<span class="contact">832.637.6355 &bull; thesecretserver.co</span></div>')

parts = [f'<!DOCTYPE html><html lang="en-GB"><head><meta charset="UTF-8"><title>TSS Investor Directory Wave 1</title><style>{CSS}</style></head><body>']

# ---- COVER ----
parts.append(MH)
parts.append('<div class="cover">')
parts.append('<h1 class="title">Investor Directory</h1>')
parts.append('<div class="subtitle">Fundraising Prospect Database &nbsp;&bull;&nbsp; Wave 1</div>')
parts.append('<div class="rule"></div>')
parts.append(f'<p class="lead">A curated directory of venture funds, corporate and strategic investors, and angel networks '
             f'relevant to <b>The Secret Server</b> \u2014 {esc(TSS["one_liner"])}. Prospects span the United States, Canada, '
             f'the United Kingdom and the European Union, and are grouped by investor type with three ready-to-personalise '
             f'outreach messages per group.</p>')
parts.append('<div class="statgrid">')
parts.append(f'<div class="statcard"><div class="n">{total}</div><div class="l">Investors &amp; Networks</div></div>')
parts.append(f'<div class="statcard"><div class="n">{len(SECTIONS)}</div><div class="l">Investor Categories</div></div>')
parts.append('<div class="statcard"><div class="n">4</div><div class="l">Markets \u00b7 US CA UK EU</div></div>')
parts.append('<div class="statcard"><div class="n">3</div><div class="l">Outreach Tones Each</div></div>')
parts.append('</div>')

parts.append('<div class="note"><div class="h">A note on contact details</div>'
             'Every entry is a real, publicly known firm, fund or angel network. Direct personal emails and phone numbers '
             'for investment partners are frequently not published and cannot be verified from public sources; where they are '
             'not reliably known, those fields are left blank rather than guessed \u2014 no contact information has been '
             'fabricated. Each firm\u2019s website is the reliable contact anchor (team pages and pitch-submission forms live there).</div>')
parts.append('<div class="note"><div class="h">Recommended approach</div>'
             'Warm introductions convert far better than cold outreach. Where possible, seek a mutual connection before '
             'reaching out; when going direct, use each firm\u2019s submission form, personalise the [First Name] and [Firm] '
             'merge fields, and lead with the strategic fit noted for that investor type.</div>')

# TOC
parts.append('<div class="toc">')
for i, s in enumerate(SECTIONS, 1):
    parts.append(f'<div><span>{i}. {esc(s["name"])}</span><span class="c">{len(s["investors"])} investors</span></div>')
parts.append('</div>')
parts.append(FOOTER)
parts.append('</div>')  # end cover

# ---- SECTIONS ----
tone_meta = [("formal", "formal", "Formal / Corporate"), ("conversational", "conv", "Conversational Professional"), ("bold", "bold", "Bold / Disruptive")]
for s in SECTIONS:
    parts.append('<div class="pagebreak"></div>')
    parts.append(MH)
    parts.append('<div class="wrap">')
    parts.append(f'<div class="sechead"><div class="n">{esc(s["name"])}</div><div class="b">{esc(s["blurb"])}</div></div>')
    parts.append('<table><thead><tr>'
                 '<th style="width:19%">Firm / Name</th>'
                 '<th style="width:13%">Contact</th>'
                 '<th style="width:14%">Geography</th>'
                 '<th style="width:20%">Primary Sectors</th>'
                 '<th style="width:11%">Stage</th>'
                 '<th style="width:11%">Check Size</th>'
                 '<th style="width:12%">Website</th>'
                 '</tr></thead><tbody>')
    for inv in s["investors"]:
        firm, contact, title, geo, sectors, stage, check, website, email, phone, notes = inv
        c = esc(contact)
        if contact and title:
            c = f'{esc(contact)}<br><span style="color:#64748b">{esc(title)}</span>'
        parts.append('<tr>'
                     f'<td><span class="firm">{esc(firm)}</span></td>'
                     f'<td>{c or "&mdash;"}</td>'
                     f'<td>{esc(geo)}</td>'
                     f'<td>{esc(sectors)}</td>'
                     f'<td>{esc(stage)}</td>'
                     f'<td>{esc(check)}</td>'
                     f'<td><span class="web">{esc(website)}</span></td>'
                     '</tr>')
    parts.append('</tbody></table>')

    # outreach messages
    msgs = MESSAGES.get(s["id"], {})
    parts.append('<div class="pill">Outreach Messages \u2014 personalise [First Name] / [Firm]</div>')
    parts.append('<div class="msgwrap">')
    for key, cls, label in tone_meta:
        parts.append(f'<div class="msgbox {cls}"><div class="h">{label}</div>{msg_html(msgs.get(key, ""))}</div>')
    parts.append('</div>')
    parts.append(FOOTER)
    parts.append('</div>')  # end wrap

parts.append('</body></html>')

out = BUILD_DIR / 'html' / 'investor_directory.html'
out.parent.mkdir(parents=True, exist_ok=True)
with open(out, 'w', encoding='utf-8') as f:
    f.write(''.join(parts))
print('Wrote', out, 'sections', len(SECTIONS), 'total', total)
