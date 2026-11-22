# AdPulse Labs — Hosted MCP Servers & APIs

Two fast, browserless Go MCP servers (Streamable HTTP `2025-03-26`) and REST APIs for competitive ad research and B2B lead qualification.

*Independent tools, not affiliated with Google, Meta, BuiltWith, Wappalyzer, or Shopify.*

---

## 1. Google Ads Transparency MCP Server (`v1.4.2`)

Search active and historical creatives from the Google Ads Transparency Center in real time — including EU/EEA DSA impression ranges, audience targeting disclosures, structured ad copy, archived KVS creative images, 7-year political ad spend, and bulk domain ad-activity screening.

- **Remote MCP URL (Streamable HTTP):** `https://spiky-closet--google-ads-transparency-scraper.apify.actor/mcp`
- **Apify Store:** https://apify.com/spiky_closet/google-ads-transparency-scraper
- **RapidAPI Hub (REST):** https://rapidapi.com/HYunLe/api/google-ads-transparency-creative-spy

### Tools Exposed
| Tool | Description |
| :--- | :--- |
| `search_google_ads` | Search creatives by domain (`shopify.com`), work email (`ceo@shopify.com`), brand (`삼성전자`, `Nike`), Advertiser ID (`AR...`), `AR.../CR...` pair, or Transparency URL. Filter by country/`EU`/`EEA`, `TEXT`/`IMAGE`/`VIDEO`, `YOUTUBE`/`SEARCH`/`SHOPPING`/`MAPS`/`PLAY`, date presets, `sortBy`, and `politicalAds`. |
| `check_domains_running_ads` | Batch-screen domains/emails/URLs to return 1 deterministic active-ad summary row per company (`hasActiveAds`, ad count range, legal entity, latest ad date). |
| `get_google_ad_creative` | Fetch full details, A/B variations, per-country reach, and targeting flags for a specific `advertiserId` + `creativeId`. |

---

## 2. Website Tech Stack, Ad Pixels & SaaS Detector MCP Server (`v1.2.1`)

Browserless Go engine (zero-copy Aho-Corasick DFA, `256MB` RAM) detecting **180+ website technologies**, unpacking static **Google Tag Manager (`gtm.js`) containers & macros** for consent-gated ad pixel IDs (`AW-`, `GT-`, Meta, LinkedIn, TikTok, Bing UET, Pinterest, Reddit, X, GA4), and verifying **70+ internal enterprise SaaS tools** (`Stripe`, `OpenAI`, `Anthropic`, `Cursor`, `HubSpot`, `Slack`, `Rippling`, `Google Workspace`) via public DNS (`MX`/`SPF`/`TXT`/`_dmarc`) — even when target homepages return `HTTP 403` WAF blocks.

- **Remote MCP URL (Streamable HTTP):** `https://spiky-closet--tech-stack-ad-pixel-detector.apify.actor/mcp`
- **Apify Store:** https://apify.com/spiky_closet/tech-stack-ad-pixel-detector
- **RapidAPI Hub (REST):** https://rapidapi.com/HYunLe/api/website-tech-stack-ad-pixels-and-saas-detector

### Tools Exposed
| Tool | Description |
| :--- | :--- |
| `scan_domains` | Full 4-layer scan (HTTP headers/HTML, static GTM pixel unpacking, DNS enterprise SaaS, optional `/ads.txt` even on WAF `403` publishers) with `mustHaveAny`, `mustHaveAll`, `mustNotHave`, and `onlyWithAdPixels` filters. |
| `extract_ad_pixels` | Focused paid-ad pixel & tracking ID extractor (`AW-`, Meta, LinkedIn, TikTok, Bing, GA4, HubSpot Portal ID). |
| `check_enterprise_saas` | Ultra-fast DNS-only (`skipHttp: true`) enterprise SaaS & email infrastructure check (`Google Workspace`, `Microsoft 365`, `DMARC`, `Stripe`, `OpenAI`, `Anthropic`, etc.). |

---

## Quick Setup (Claude Code, Claude Desktop, Cursor, VS Code)

Both remote servers authenticate using your standard Apify API token (`Authorization: Bearer <APIFY_TOKEN>`).

```json
{
  "mcpServers": {
    "google-ads-transparency": {
      "url": "https://spiky-closet--google-ads-transparency-scraper.apify.actor/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_APIFY_API_TOKEN"
      }
    },
    "tech-stack-ad-pixels": {
      "url": "https://spiky-closet--tech-stack-ad-pixel-detector.apify.actor/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_APIFY_API_TOKEN"
      }
    }
  }
}
```

### Example Prompts Once Connected
- *"Check whether `allbirds.com`, `klaviyo.com`, and `linear.app` run paid ad pixels, extract their Meta/Google Ads IDs, and check which ones use Stripe and OpenAI."*
- *"Pull the top 5 highest-impression EU Google Ads for `shopify.com` in the last 30 days with structured ad copy."*
- *"Screen these 20 B2B lead emails to see which companies are actively spending on Google Ads right now."*

---

## Pricing & Verified Performance

- **Apify Pay-Per-Event (`$0` start fee):** Starting at `$0.0015` per ad creative / scanned domain on Free tier down to `$0.0010` on Gold+ (`$0` charged on filtered-out, unreachable, or deduplicated `onlyNewAds` rows). See the Pricing tab on each Apify Store page for current rates.
- **RapidAPI REST Tiers:** Free Basic tier (`$0/mo`, hard cap) plus Pro (`$19/mo`), Ultra (`$49/mo`), and Mega (`$149/mo`).
- **Measured Cloud Runs (`256MB` RAM, `$0` proxy):**
  - 6 mixed domains (`hubspot.com`, `klaviyo.com`, `ceo@linear.app`, `allbirds.com`, `nytimes.com` WAF 403 + `ads.txt`, `openai.com`): `2.087s` total batch (`Run wP0WaGqtalpeQGRqi`).
  - 3-domain warm Standby `POST /scan`: `940ms` max server scan time.
  - 5 EU Google Ads creatives with details + KVS image archiving: `Run ADv1FpU6Rq02VtwOc` (`SUCCEEDED`, signed `image/png` archived).

See [`examples/`](./examples/) for `cURL` and Python quickstarts.
