# FilingSignal — SEC EDGAR Form D Startup Funding, Form 4 Insiders & 8-K Events MCP Server

[![FilingSignal SEC EDGAR MCP connector](https://glama.ai/mcp/connectors/io.github.yun87457-web/sec-edgar-funding-insider-mcp/badges/score.svg)](https://glama.ai/mcp/connectors/io.github.yun87457-web/sec-edgar-funding-insider-mcp)

Direct official SEC EDGAR XML/JSON extractor in browserless Go (`v1.0.5`) for **US startup funding rounds (Form D)** with dual SPV/pooled-fund filtering, **Form 4 insider buys & multi-insider cluster buys** (VWAP-consolidated partial fills, `%` holdings delta, 10b5-1 & OTC filters), and **Form 8-K material corporate events** with `EX-99.1` press release text extraction.

## Access Channels

- **Apify Store (Batch + Standby + `$0` Start Fee):** https://apify.com/spiky_closet/sec-funding-insider-mcp
- **RapidAPI Hub (REST API, Free Basic Plan):** https://rapidapi.com/HYunLe/api/sec-edgar-form-d-funding-form-4-insider-8-k-api
- **Official MCP Registry:** `io.github.yun87457-web/sec-edgar-funding-insider-mcp`
- **npm (`stdio`):** `npx -y filingsignal-sec-edgar-mcp`
- **Interactive Explorer:** https://yun87457-web.github.io/sec-edgar-funding-insider-mcp/

## MCP Tools (Streamable HTTP & `stdio`)

Endpoint: `https://spiky-closet--sec-funding-insider-mcp.apify.actor/mcp`

| Tool | Description |
|---|---|
| `search_startup_funding` | Search US startup Form D funding rounds with `excludeFunds`, `excludeSpvs`, `minAmountSoldUsd`, `states`, and `industries` filters. |
| `search_insider_trades` | Query Form 4 open-market buys/sells with share-weighted VWAP partial-fill consolidation, `exclude10b51`, `cSuiteOnly`, and `majorExchangesOnly`. |
| `find_insider_cluster_buys` | Detect multi-insider open-market cluster buys (`minBuyers >= 2`, `netBuyOnly: true`) on Nasdaq/NYSE/CBOE/TXSE. |
| `search_corporate_events` | Search Form 8-K events by item codes (`2.02`, `5.02`, `1.05`, `2.05`) or category presets with `EX-99.1` press release extraction. |
| `get_company_sec_dossier` | Single-call ticker/CIK company SEC dossier combining exchange metadata, recent Form 8-K events, and Form 4 insider activity. |
| `get_filing_document` | Fetch and clean a specific SEC EDGAR filing or `EX-99.1` exhibit into agent-ready plain text. |

## Quick Setup

### Remote Streamable HTTP
```json
{
  "mcpServers": {
    "sec-edgar-funding-insider": {
      "url": "https://spiky-closet--sec-funding-insider-mcp.apify.actor/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_APIFY_API_TOKEN"
      }
    }
  }
}
```

### Local `npx` (`stdio`)
```json
{
  "mcpServers": {
    "sec-edgar-funding-insider": {
      "command": "npx",
      "args": ["-y", "filingsignal-sec-edgar-mcp"]
    }
  }
}
```

## n8n Workflow Template

Import [`n8n-template.json`](./n8n-template.json) into n8n to run a weekly SPV-filtered SEC Form D startup funding monitor with `$1M+` round filtering and Slack alerts (complete with step-by-step Sticky Notes).
