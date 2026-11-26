# Browserless Go MCP Servers & REST APIs (2026)

Five fast, browserless Go MCP servers (Streamable HTTP `2025-03-26`) and REST APIs for competitive ad research, GTM/DNS tech-stack enrichment, 6-ATS hiring intelligence, `/llms.txt` + SaaS pricing extraction, and live SEC EDGAR Form D / Form 4 / 8-K monitoring.

*Independent tools, not affiliated with Google, Meta, BuiltWith, Wappalyzer, Shopify, Clay, OpenInsider, or the U.S. SEC.*

---

## Live Interactive Top-100 Open Datasets & Standalone Repos

| # | Tool | Latest | Live Open Dataset Explorer (MIT) | Standalone Repo & `npx` Stdio Bridge | Apify Store (Free Tier + MCP) |
| :- | :--- | :--- | :--- | :--- | :--- |
| **1** | **AdPulse** — Google Ads Transparency | `v1.4.2` | [Top 100 Brands 30d Index](https://yun87457-web.github.io/google-ads-transparency-mcp/) | [`google-ads-transparency-mcp`](https://github.com/yun87457-web/google-ads-transparency-mcp) | [Apify Store](https://apify.com/spiky_closet/google-ads-transparency-scraper) |
| **2** | **StackScope** — Tech Stack, GTM Pixels & DNS SaaS | `v1.2.4` | [Top 100 Shopify & SaaS Index](https://yun87457-web.github.io/tech-stack-ad-pixel-mcp/) | [`tech-stack-ad-pixel-mcp`](https://github.com/yun87457-web/tech-stack-ad-pixel-mcp) | [Apify Store](https://apify.com/spiky_closet/tech-stack-ad-pixel-detector) |
| **3** | **RoleSignal** — Unified 6-ATS Jobs & Salaries | `v1.1.3` | [Top 100 AI & Tech Jobs Index](https://yun87457-web.github.io/ats-jobs-hiring-intel-mcp/) | [`ats-jobs-hiring-intel-mcp`](https://github.com/yun87457-web/ats-jobs-hiring-intel-mcp) | [Apify Store](https://apify.com/spiky_closet/ats-jobs-hiring-intel) |
| **4** | **SiteBrief** — Contacts, Pricing & `/llms.txt` | `v1.1.2` | [Top 100 `/llms.txt` & Pricing Index](https://yun87457-web.github.io/website-contacts-pricing-mcp/) | [`website-contacts-pricing-mcp`](https://github.com/yun87457-web/website-contacts-pricing-mcp) | [Apify Store](https://apify.com/spiky_closet/website-contacts-pricing-intel) |
| **5** | **FilingSignal** — SEC EDGAR Form D, 4 & 8-K | `v1.0.2` | [Live SEC Form D & Form 4 Index](https://yun87457-web.github.io/sec-edgar-funding-insider-mcp/) | [`sec-edgar-funding-insider-mcp`](https://github.com/yun87457-web/sec-edgar-funding-insider-mcp) | [Apify Store](https://apify.com/spiky_closet/sec-funding-insider-mcp) |

---

## 1. Google Ads Transparency MCP Server (`v1.4.2`)

Search active and historical creatives from the Google Ads Transparency Center in real time — including EU/EEA DSA impression ranges, `EEA+TR` (`Türkiye` / `2792`) 31-country macro, audience targeting disclosures, structured ad copy, archived KVS creative images, 7-year political ad spend, and bulk domain ad-activity screening.

- **New in `v1.4.2`:** Explicit CRM screening metadata (`dateWindowApplied`, `countScope`, `daysSinceLastShown`, `activityStatus`: `active_7d`/`recent_30d`/`historical`/`none`, `matchConfidence`, `matchConfidenceScore`, `matchReason`, `primaryAdvertiserShare`) + Unicode `"Türkiye"` & `"EEA+TR"` macro.
- **Remote MCP URL:** `https://spiky-closet--google-ads-transparency-scraper.apify.actor/mcp`
- **Zero-install stdio:** `npx -y github:yun87457-web/google-ads-transparency-mcp`
- **Apify Store:** https://apify.com/spiky_closet/google-ads-transparency-scraper
- **RapidAPI Hub (REST):** https://rapidapi.com/HYunLe/api/google-ads-transparency-creative-spy

| Tool | Description |
| :--- | :--- |
| `search_google_ads` | Search creatives by domain (`shopify.com`), work email, brand, Advertiser ID (`AR...`), or Transparency URL. Filter by country/`EU`/`EEA`/`EEA+TR`/`Türkiye`, format, platform, date preset, `sortBy`, and `politicalAds`. |
| `check_domains_running_ads` | Batch-screen domains/emails/URLs into 1 deterministic CRM row per company (`hasActiveAds`, `activityStatus`, `daysSinceLastShown`, `matchConfidence`, `primaryAdvertiserShare`). |
| `get_google_ad_creative` | Fetch full details, A/B variations, per-country reach, and targeting flags for a specific `advertiserId` + `creativeId`. |

---

## 2. Website Tech Stack, Ad Pixels & DNS SaaS Detector MCP Server (`v1.2.4`)

Browserless Go engine (zero-copy Aho-Corasick DFA, `256MB` RAM) detecting **180+ website technologies**, unpacking static **Google Tag Manager (`gtm.js`) containers & macros** for consent-gated ad pixel IDs (`AW-`, `GT-`, Meta, LinkedIn, TikTok, Bing UET, Pinterest, Reddit, X, GA4), and verifying **70+ internal enterprise SaaS tools** (`Stripe`, `OpenAI`, `Anthropic`, `Cursor`, `HubSpot`, `Slack`, `Rippling`, `Google Workspace`) via public DNS (`MX`/`SPF`/`TXT`/`_dmarc`) — even when target homepages return `HTTP 403` WAF blocks.

- **New in `v1.2.4`:** Explicit CRM confidence fields (`htmlInspected`, `scanConfidence`: `high`/`medium`/`none`, `scanConfidenceScore`, `scanCoverageNote`, `scannedAt`) so downstream pipelines distinguish full HTTP+DNS scans from DNS-only WAF-blocked fallbacks.
- **Remote MCP URL:** `https://spiky-closet--tech-stack-ad-pixel-detector.apify.actor/mcp`
- **Zero-install stdio:** `npx -y github:yun87457-web/tech-stack-ad-pixel-mcp`
- **Apify Store:** https://apify.com/spiky_closet/tech-stack-ad-pixel-detector
- **RapidAPI Hub (REST):** https://rapidapi.com/HYunLe/api/website-tech-stack-ad-pixels-and-saas-detector

| Tool | Description |
| :--- | :--- |
| `scan_domains` | Full 4-layer scan (HTTP headers/HTML, static GTM pixel unpacking, DNS enterprise SaaS, optional `/ads.txt`) with `scanConfidence` and tech/pixel filters. |
| `extract_ad_pixels` | Focused paid-ad pixel & tracking ID extractor (`AW-`, Meta, LinkedIn, TikTok, Bing, GA4, HubSpot Portal ID). |
| `check_enterprise_saas` | Ultra-fast DNS-only (`skipHttp: true`) enterprise SaaS & email infrastructure check (`Google Workspace`, `Microsoft 365`, `DMARC`, `Stripe`, `OpenAI`, `Anthropic`). |

---

## 3. Unified 6-ATS Jobs, Salary & Hiring Intelligence MCP Server (`v1.1.3`)

Browserless Go engine unifying **6 major ATS platforms** (`Ashby`, `Greenhouse`, `Lever`, `SmartRecruiters`, `Workday`, `BambooHR`) behind a single input (`stripe.com`, `ceo@ramp.com`, career URLs, or slugs) with `<400ms` ATS auto-detection, normalized USD salary/equity bands, workplace/seniority classification, **135+ JD tech-stack signals**, `summaryMode` company hiring rollups, and `onlyNewJobs` incremental monitoring.

- **New in `v1.1.3`:** Job posting freshness (`postedDaysAgo`, `freshnessStatus`: `active_7d`/`recent_30d`/`aged_90d`/`stale`/`unknown`), company hiring activity (`freshJobs7d`, `freshJobs30d`, `newestJobDaysAgo`, `hiringActivityStatus`), and board attribution confidence (`boardDetectedVia`, `boardMatchConfidence`, `boardMatchScore`).
- **Remote MCP URL:** `https://spiky-closet--ats-jobs-hiring-intel.apify.actor/mcp`
- **Zero-install stdio:** `npx -y github:yun87457-web/ats-jobs-hiring-intel-mcp`
- **Apify Store:** https://apify.com/spiky_closet/ats-jobs-hiring-intel

| Tool | Description |
| :--- | :--- |
| `get_company_jobs` | Fetch normalized open jobs across 6 ATS platforms with `freshnessStatus`, salary bands, remote/department/tech filters. |
| `detect_company_ats` | Auto-detect which ATS platform and board slug a company uses in `<400ms` with `boardMatchConfidence`. |
| `screen_hiring_signals` | Batch-screen companies into 1 summary row per company (`totalOpenJobs`, `freshJobs7d`, `freshJobs30d`, `hiringActivityStatus`, `medianSalaryUsd`, `remotePct`, `topJdTechSignals`). |

---

## 4. Website Contacts, SaaS Pricing & `/llms.txt` MCP Server (`v1.1.2`)

Browserless Go enrichment engine extracting verified business emails (role-classified + DNS MX/SPF check), phones, 12+ social links, structured SaaS `/pricing` tiers, and `/llms.txt` AI-ready markdown briefs.

- **New in `v1.1.2`:** Conditional `HTTP 304 Not Modified` revalidation (`ETag` / `Last-Modified` / `llmsCacheTtlSeconds` default `300s`) for `/llms.txt` (`llmsTxtEtag`, `llmsTxtLastModified`, `llmsTxtCacheControl`, `llmsTxtNotModified`, `llmsTxtCacheStatus`, `llmsTxtFetchedAt`), while keeping `/pricing` live (`Cache-Control: no-cache`) so price changes are never served stale.
- **Remote MCP URL:** `https://spiky-closet--website-contacts-pricing-intel.apify.actor/mcp`
- **Zero-install stdio:** `npx -y github:yun87457-web/website-contacts-pricing-mcp`
- **Apify Store:** https://apify.com/spiky_closet/website-contacts-pricing-intel

| Tool | Description |
| :--- | :--- |
| `extract_website_intel` | Full company enrichment: emails, phones, 12+ social URLs, `/pricing` tiers, DNS MX/SPF, and conditional `/llms.txt` brief. |
| `extract_saas_pricing` | Focused live SaaS pricing-tier & billing-cadence extractor. |
| `fetch_llms_txt_brief` | Fast `/llms.txt` / `/llms-full.txt` retriever with `ETag` / `HTTP 304` freshness metadata. |

---

## 5. SEC EDGAR Form D Startup Funding, Form 4 Cluster Buys & Form 8-K MCP Server (`v1.0.2`)

Zero-browser Go engine querying official SEC EDGAR filings with zero API keys: **SPV-filtered Form D** operating startup funding rounds, **VWAP-consolidated Form 4** open-market insider buys (filtering out grants/10b5-1 noise and flagging multi-insider **cluster buys**), and **Form 8-K** material event alerts with `EX-99.1` press-release extraction.

- **Remote MCP URL:** `https://spiky-closet--sec-funding-insider-mcp.apify.actor/mcp`
- **Zero-install stdio:** `npx -y github:yun87457-web/sec-edgar-funding-insider-mcp`
- **Apify Store:** https://apify.com/spiky_closet/sec-funding-insider-mcp

| Tool | Description |
| :--- | :--- |
| `search_form_d_startups` | Screen recent SEC Form D equity raises with automatic SPV / pooled-fund filtering. |
| `scan_form4_cluster_buys` | Detect open-market insider buys & multi-executive VWAP cluster buys from Form 4 XML. |
| `get_form8k_events` | Fetch Form 8-K Item disclosures (M&A, leadership changes, earnings) with `EX-99.1` text. |

---

## Quick Setup (Claude Code, Claude Desktop, Cursor, VS Code)

All five remote Streamable HTTP MCP servers authenticate with your standard Apify API token (`Authorization: Bearer <APIFY_TOKEN>`):

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

---

## Verified Cloud Benchmarks (`256MB` RAM, `$0` Proxy)

- **AdPulse (`v1.4.2`):** 100 SaaS/AI/DTC brands screened in `LAST_30_DAYS` window in `8.08s` (`0` errors, `91/100` active 30d, `79/91` High Confidence, `12/91` Medium Confidence).
- **StackScope (`v1.2.4`):** 6 mixed domains (incl. WAF `403` DNS fallback) in `2.087s`; warm Standby `POST /scan` max `940ms`.
- **RoleSignal (`v1.1.3`):** 81 active AI & tech startup ATS boards (`9,556` open roles) with `freshJobs7d` / `freshJobs30d` freshness classification.
- **SiteBrief (`v1.1.2`):** 100 Dev/AI companies (`80%` ship `/llms.txt`, `94%` public `/pricing`); verified live `HTTP 304 Not Modified` on `vercel.com` with live `/pricing` isolation.
- **FilingSignal (`v1.0.2`):** Live SEC EDGAR Form D SPV-filtered startup rounds & Form 4 VWAP insider cluster buys.

See each tool subfolder (`./google-ads-transparency/`, `./tech-stack-ad-pixels/`, `./ats-jobs-hiring-intel/`, `./website-contacts-pricing-intel/`, `./sec-edgar-funding-insider/`) for ready-to-import `n8n-template.json` files and [`examples/`](./examples/) for `cURL` & Python quickstarts.
