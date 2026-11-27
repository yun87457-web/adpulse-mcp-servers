# AdPulse Labs — Hosted MCP Servers & APIs (5 Production Go Engines)

Five fast, browserless Go MCP servers (Streamable HTTP `2025-03-26` + zero-setup `npx` stdio wrappers) and REST APIs for competitive ad intelligence, technographics, hiring signals, B2B website enrichment, and official SEC EDGAR filings.

*Independent tools, not affiliated with Google, Meta, BuiltWith, Wappalyzer, Shopify, Ashby, Greenhouse, Lever, Workday, SmartRecruiters, BambooHR, or the U.S. SEC.*

---

## Live Server Catalog

| # | Server | Live Apify Version | Published `npx` Package | Apify Store | RapidAPI REST | Interactive Explorer |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- |
| 1 | [**Google Ads Transparency**](./google-ads-transparency/) | `v1.4.6` | `adpulse-google-ads-transparency-mcp` | [Apify](https://apify.com/spiky_closet/google-ads-transparency-scraper) | [RapidAPI](https://rapidapi.com/HYunLe/api/google-ads-transparency-creative-spy) | [Live Tester](https://yun87457-web.github.io/google-ads-transparency-mcp/) |
| 2 | [**Tech Stack, Ad Pixels & DNS SaaS**](./tech-stack-ad-pixels/) | `v1.2.5` | `stackscope-tech-stack-ad-pixel-mcp` | [Apify](https://apify.com/spiky_closet/tech-stack-ad-pixel-detector) | [RapidAPI](https://rapidapi.com/HYunLe/api/website-tech-stack-ad-pixels-and-saas-detector) | [Live Tester](https://yun87457-web.github.io/tech-stack-ad-pixel-mcp/) |
| 3 | [**Unified 6-ATS Jobs & Hiring Intel**](./ats-jobs-hiring-intel/) | `v1.1.7` | `rolesignal-ats-jobs-intel-mcp` | [Apify](https://apify.com/spiky_closet/ats-jobs-hiring-intel) | [RapidAPI](https://rapidapi.com/HYunLe/api/unified-multi-ats-jobs-salary-hiring-intelligence) | [Live Tester](https://yun87457-web.github.io/ats-jobs-hiring-intel-mcp/) |
| 4 | [**Website Contacts, Pricing & `/llms.txt`**](./website-contacts-pricing-intel/) | `v1.0.6` | `sitebrief-website-contacts-pricing-mcp` | [Apify](https://apify.com/spiky_closet/website-contacts-pricing-intel) | [RapidAPI](https://rapidapi.com/HYunLe/api/website-contacts-socials-pricing-llm-brief-api) | [Live Tester](https://yun87457-web.github.io/website-contacts-pricing-mcp/) |
| 5 | [**SEC EDGAR Form D, Form 4 & 8-K**](./sec-edgar-funding-insider/) | `v1.0.5` | `filingsignal-sec-edgar-mcp` | [Apify](https://apify.com/spiky_closet/sec-funding-insider-mcp) | [RapidAPI](https://rapidapi.com/HYunLe/api/sec-edgar-form-d-funding-form-4-insider-8-k-api) | [Live Tester](https://yun87457-web.github.io/sec-edgar-funding-insider-mcp/) |

---

## 1. Google Ads Transparency MCP Server (`v1.4.6`)

[![Google Ads Transparency MCP connector](https://glama.ai/mcp/connectors/io.github.yun87457-web/google-ads-transparency-mcp/badges/score.svg)](https://glama.ai/mcp/connectors/io.github.yun87457-web/google-ads-transparency-mcp)

Search active and historical creatives from the Google Ads Transparency Center in real time — including EU/EEA DSA impression ranges, audience targeting disclosures, structured ad copy, archived KVS creative images, 7-year political ad spend, and bulk domain ad-activity screening.

- **Remote MCP URL:** `https://spiky-closet--google-ads-transparency-scraper.apify.actor/mcp`
- **Official MCP Registry:** `io.github.yun87457-web/google-ads-transparency-mcp`
- **npm (`stdio`):** `npx -y adpulse-google-ads-transparency-mcp`
- **GitHub Repo & Explorer:** https://github.com/yun87457-web/google-ads-transparency-mcp | https://yun87457-web.github.io/google-ads-transparency-mcp/
- **n8n Workflow Template:** [`google-ads-transparency/n8n-template.json`](./google-ads-transparency/n8n-template.json)

| Tool | Description |
| :--- | :--- |
| `search_google_ads` | Search creatives by domain (`shopify.com`), work email (`ceo@shopify.com`), brand (`삼성전자`, `Nike`), Advertiser ID (`AR...`), `AR.../CR...` pair, or Transparency URL with region/EU/EEA, format, platform, date preset, and `politicalAds` filters. |
| `check_domains_running_ads` | Batch-screen domains/emails/URLs to return 1 deterministic active-ad summary row per company (`hasActiveAds`, ad count range, `activityStatus`, `matchConfidence`, latest ad date). |
| `get_google_ad_creative` | Fetch full creative details, A/B variations, per-country EU DSA reach, and targeting disclosures for an `advertiserId` + `creativeId`. |

---

## 2. Website Tech Stack, Ad Pixels & SaaS Detector MCP Server (`v1.2.5`)

[![Tech Stack & Ad Pixel Detector MCP connector](https://glama.ai/mcp/connectors/io.github.yun87457-web/tech-stack-ad-pixel-detector-mcp/badges/score.svg)](https://glama.ai/mcp/connectors/io.github.yun87457-web/tech-stack-ad-pixel-detector-mcp)

Browserless Go engine (single-pass Aho-Corasick DFA, `256MB` RAM) detecting **180+ website technologies**, unpacking static **Google Tag Manager (`gtm.js`) containers & macros** for consent-gated ad pixel IDs (`AW-`, `GT-`, Meta, LinkedIn, TikTok, Bing UET, Pinterest, Reddit, X, GA4), and verifying **70+ internal enterprise SaaS tools** (`Stripe`, `OpenAI`, `Anthropic`, `Cursor`, `HubSpot`, `Slack`, `Rippling`, `Google Workspace`) via public DNS (`MX`/`SPF`/`TXT`/`_dmarc`) — even when target homepages return `HTTP 403` WAF blocks.

- **Remote MCP URL:** `https://spiky-closet--tech-stack-ad-pixel-detector.apify.actor/mcp`
- **Official MCP Registry:** `io.github.yun87457-web/tech-stack-ad-pixel-detector-mcp`
- **npm (`stdio`):** `npx -y stackscope-tech-stack-ad-pixel-mcp`
- **GitHub Repo & Explorer:** https://github.com/yun87457-web/tech-stack-ad-pixel-mcp | https://yun87457-web.github.io/tech-stack-ad-pixel-mcp/
- **n8n Workflow Template:** [`tech-stack-ad-pixels/n8n-template.json`](./tech-stack-ad-pixels/n8n-template.json)

| Tool | Description |
| :--- | :--- |
| `scan_domains` | Full 4-layer scan (HTTP headers/HTML, static GTM pixel unpacking, DNS enterprise SaaS, optional `/ads.txt` even on WAF `403` publishers) with `mustHaveAny`, `mustHaveAll`, `mustNotHave`, and `onlyWithAdPixels` filters. |
| `extract_ad_pixels` | Focused paid-ad pixel & tracking ID extractor (`AW-`, Meta, LinkedIn, TikTok, Bing, GA4, HubSpot Portal ID). |
| `check_enterprise_saas` | Ultra-fast DNS-only (`skipHttp: true`) enterprise SaaS & email infrastructure check (`Google Workspace`, `Microsoft 365`, `DMARC`, `Stripe`, `OpenAI`, `Anthropic`, etc.). |

---

## 3. Unified 6-ATS Jobs, Salary & Hiring Intelligence MCP Server (`v1.1.7`)

[![Unified 6-ATS Jobs & Hiring Intel MCP connector](https://glama.ai/mcp/connectors/io.github.yun87457-web/ats-jobs-hiring-intel-mcp/badges/score.svg)](https://glama.ai/mcp/connectors/io.github.yun87457-web/ats-jobs-hiring-intel-mcp)

Browserless Go engine unifying **6 major ATS platforms** (`Ashby`, `Greenhouse`, `Lever`, `SmartRecruiters`, `Workday`, `BambooHR`) behind a single input (`stripe.com`, `ceo@ramp.com`, career URLs, or slugs) with `<400ms` ATS auto-detection, normalized salary/equity bands, workplace/seniority classification, **135+ JD tech-stack signals**, `summaryMode` company hiring rollups, freshness metrics, and `onlyNewJobs` incremental monitoring.

- **Remote MCP URL:** `https://spiky-closet--ats-jobs-hiring-intel.apify.actor/mcp`
- **Official MCP Registry:** `io.github.yun87457-web/ats-jobs-hiring-intel-mcp`
- **npm (`stdio`):** `npx -y rolesignal-ats-jobs-intel-mcp`
- **GitHub Repo & Explorer:** https://github.com/yun87457-web/ats-jobs-hiring-intel-mcp | https://yun87457-web.github.io/ats-jobs-hiring-intel-mcp/
- **n8n Workflow Template:** [`ats-jobs-hiring-intel/n8n-template.json`](./ats-jobs-hiring-intel/n8n-template.json)

| Tool | Description |
| :--- | :--- |
| `get_company_jobs` | Fetch normalized open jobs across 6 ATS platforms from domains, emails, URLs, or slugs with remote/salary/department/title/recency/tech filters. |
| `detect_company_ats` | Auto-detect which ATS platform and board slug a company uses in `<400ms`. |
| `screen_hiring_signals` | Batch-screen companies into 1 summary row per company (`totalOpenJobs`, `boardTotalJobs`, `medianSalaryUsd`, `salaryCoveragePct`, `remotePct`, `topJdTechSignals`, `freshJobs7d`). |

---

## 4. Website Contacts, Socials, Pricing & `/llms.txt` Brief MCP Server (`v1.0.6`)

[![Website Contacts, Pricing & LLM Brief MCP connector](https://glama.ai/mcp/connectors/io.github.yun87457-web/website-contacts-pricing-intel-mcp/badges/score.svg)](https://glama.ai/mcp/connectors/io.github.yun87457-web/website-contacts-pricing-intel-mcp)

Extract verified emails (with role classification), phone numbers, `12+` social profiles, live SaaS `/pricing` tiers & PLG flags, DNS `MX`/`SPF` email provider signals, and `/llms.txt` (with `ETag`/`If-Modified-Since` conditional `304` revalidation) or clean Markdown company briefs from any company domain or work email.

- **Remote MCP URL:** `https://spiky-closet--website-contacts-pricing-intel.apify.actor/mcp`
- **Official MCP Registry:** `io.github.yun87457-web/website-contacts-pricing-intel-mcp`
- **npm (`stdio`):** `npx -y sitebrief-website-contacts-pricing-mcp`
- **GitHub Repo & Explorer:** https://github.com/yun87457-web/website-contacts-pricing-mcp | https://yun87457-web.github.io/website-contacts-pricing-mcp/
- **n8n Workflow Template:** [`website-contacts-pricing-intel/n8n-template.json`](./website-contacts-pricing-intel/n8n-template.json)

| Tool | Description |
| :--- | :--- |
| `enrich_company_website` | Extract contacts, phones, 12+ socials, `/pricing` tiers, DNS `MX`/`SPF`, and `/llms.txt` or clean Markdown brief for one domain/email. |
| `batch_enrich_domains` | Enrich multiple domains/emails concurrently with automatic deduplication, WAF DNS preservation, and `$0` billing on unreachable domains. |
| `extract_page_markdown` | Convert any public webpage URL into clean, token-efficient Markdown for AI agents and RAG pipelines. |

---

## 5. SEC EDGAR Form D Startup Funding, Form 4 Insiders & 8-K MCP Server (`v1.0.5`)

[![FilingSignal SEC EDGAR MCP connector](https://glama.ai/mcp/connectors/io.github.yun87457-web/sec-edgar-funding-insider-mcp/badges/score.svg)](https://glama.ai/mcp/connectors/io.github.yun87457-web/sec-edgar-funding-insider-mcp)

Direct official SEC EDGAR XML/JSON intelligence engine extracting **US startup funding rounds (Form D)** with dual SPV & pooled-fund filtering, **Form 4 insider buys & multi-insider cluster buys** (VWAP-consolidated partial fills, `%` holdings delta, 10b5-1 & OTC filters), and **Form 8-K material corporate events** with `EX-99.1` press release text extraction.

- **Remote MCP URL:** `https://spiky-closet--sec-funding-insider-mcp.apify.actor/mcp`
- **Official MCP Registry:** `io.github.yun87457-web/sec-edgar-funding-insider-mcp`
- **npm (`stdio`):** `npx -y filingsignal-sec-edgar-mcp`
- **GitHub Repo & Explorer:** https://github.com/yun87457-web/sec-edgar-funding-insider-mcp | https://yun87457-web.github.io/sec-edgar-funding-insider-mcp/
- **n8n Workflow Template:** [`sec-edgar-funding-insider/n8n-template.json`](./sec-edgar-funding-insider/n8n-template.json)

| Tool | Description |
| :--- | :--- |
| `search_startup_funding` | Search recent SEC Form D filings with `excludeFunds`, `excludeSpvs`, `minAmountSoldUsd`, `states`, and `industries` filters. |
| `search_insider_trades` | Query Form 4 open-market insider buys/sells with VWAP partial-fill consolidation, `exclude10b51`, `cSuiteOnly`, and `majorExchangesOnly`. |
| `find_insider_cluster_buys` | Detect multi-insider open-market cluster buys (`minBuyers >= 2`, `netBuyOnly: true`) across major US exchanges. |
| `search_corporate_events` | Pull Form 8-K filings by SEC item codes (`2.02`, `5.02`, `1.05`, `2.05`) or presets (`earnings`, `m_and_a`, `layoffs`, `cybersecurity`) with `EX-99.1` press release extraction. |
| `get_company_sec_dossier` | Single-call ticker/CIK lookup combining company metadata, exchange, recent Form 8-K events, and Form 4 insider activity. |
| `get_filing_document` | Fetch and clean a specific SEC EDGAR filing or `EX-99.1` exhibit into agent-safe text. |

---

## Quick Setup (Claude Code, Claude Desktop, Cursor, VS Code)

### Option A: Zero-Install Remote Streamable HTTP (Recommended)

All five remote servers authenticate using your standard Apify API token (`Authorization: Bearer <APIFY_TOKEN>`):

```json
{
  "mcpServers": {
    "google-ads-transparency": {
      "url": "https://spiky-closet--google-ads-transparency-scraper.apify.actor/mcp",
      "headers": { "Authorization": "Bearer YOUR_APIFY_API_TOKEN" }
    },
    "tech-stack-ad-pixels": {
      "url": "https://spiky-closet--tech-stack-ad-pixel-detector.apify.actor/mcp",
      "headers": { "Authorization": "Bearer YOUR_APIFY_API_TOKEN" }
    },
    "ats-jobs-hiring-intel": {
      "url": "https://spiky-closet--ats-jobs-hiring-intel.apify.actor/mcp",
      "headers": { "Authorization": "Bearer YOUR_APIFY_API_TOKEN" }
    },
    "website-contacts-pricing": {
      "url": "https://spiky-closet--website-contacts-pricing-intel.apify.actor/mcp",
      "headers": { "Authorization": "Bearer YOUR_APIFY_API_TOKEN" }
    },
    "sec-edgar-funding-insider": {
      "url": "https://spiky-closet--sec-funding-insider-mcp.apify.actor/mcp",
      "headers": { "Authorization": "Bearer YOUR_APIFY_API_TOKEN" }
    }
  }
}
```

### Option B: Local `npx` (`stdio`) Wrappers

For clients that prefer `stdio` MCP servers (works keyless in free trial mode or with `APIFY_TOKEN` for full quota):

```json
{
  "mcpServers": {
    "google-ads-transparency": { "command": "npx", "args": ["-y", "adpulse-google-ads-transparency-mcp"] },
    "tech-stack-ad-pixels": { "command": "npx", "args": ["-y", "stackscope-tech-stack-ad-pixel-mcp"] },
    "ats-jobs-hiring-intel": { "command": "npx", "args": ["-y", "rolesignal-ats-jobs-intel-mcp"] },
    "website-contacts-pricing": { "command": "npx", "args": ["-y", "sitebrief-website-contacts-pricing-mcp"] },
    "sec-edgar-funding-insider": { "command": "npx", "args": ["-y", "filingsignal-sec-edgar-mcp"] }
  }
}
```

### Example Prompts Once Connected
- *"Check whether `allbirds.com`, `klaviyo.com`, and `linear.app` run paid ad pixels, extract their Meta/Google Ads IDs, and check which ones use Stripe and OpenAI."*
- *"Pull the top 5 highest-impression EU Google Ads for `shopify.com` in the last 30 days with structured ad copy."*
- *"Screen `stripe.com`, `ramp.com`, and `anthropic.com` for open engineering roles, median salary bands, and JD tech signals."*
- *"Enrich `linear.app` and `vercel.com` with verified emails, `/pricing` tiers, and `/llms.txt` briefs."*
- *"Find US operating startups that raised $2M+ in SEC Form D filings over the last 7 days (excluding SPVs and funds) plus any multi-insider Form 4 cluster buys."*

---

## Pricing & Examples

- **Apify Pay-Per-Event (`$0` start fee):** Free Apify tier includes `$5/mo` credit (up to 10,000 enriched domains or 5,000 ATS jobs/mo), with 6-tier volume discounts (`FREE` → `DIAMOND`) and `$0` charged on filtered-out, unreachable, or deduplicated rows.
- **RapidAPI REST Tiers:** Free Basic plan (`$0/mo`, hard cap) plus Pro, Ultra, and Mega plans across all 5 APIs.
- **Code Quickstarts:** See [`examples/curl_examples.sh`](./examples/curl_examples.sh) and [`examples/python_quickstart.py`](./examples/python_quickstart.py) covering all 5 servers.
