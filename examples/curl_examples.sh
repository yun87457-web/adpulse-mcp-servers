#!/usr/bin/env bash
# Quickstart cURL examples for all 5 AdPulse Labs hosted Streamable HTTP MCP servers.
# Export APIFY_TOKEN before running.
set -euo pipefail

: "${APIFY_TOKEN:?Set APIFY_TOKEN to your Apify API token first}"

mcp_call() {
  local label="$1"
  local url="$2"
  local payload="$3"
  echo ""
  echo "==> ${label}"
  curl -sS -X POST "${url}" \
    -H "Authorization: Bearer ${APIFY_TOKEN}" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json, text/event-stream" \
    -d "${payload}"
  echo ""
}

mcp_call "1. Google Ads Transparency MCP: search_google_ads" \
  "https://spiky-closet--google-ads-transparency-scraper.apify.actor/mcp" \
  '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"search_google_ads","arguments":{"query":"shopify.com","region":"DE","dateRangePreset":"LAST_30_DAYS","maxResults":3}}}'

mcp_call "2. Tech Stack & Ad Pixel Detector MCP: scan_domains" \
  "https://spiky-closet--tech-stack-ad-pixel-detector.apify.actor/mcp" \
  '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"scan_domains","arguments":{"domains":["hubspot.com","klaviyo.com","ceo@linear.app"],"checkAdsTxt":true}}}'

mcp_call "3. Unified 6-ATS Jobs & Hiring Intelligence MCP: screen_hiring_signals" \
  "https://spiky-closet--ats-jobs-hiring-intel.apify.actor/mcp" \
  '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"screen_hiring_signals","arguments":{"companies":["stripe.com","ramp.com"]}}}'

mcp_call "4. Website Contacts, Pricing & /llms.txt MCP: enrich_company_website" \
  "https://spiky-closet--website-contacts-pricing-intel.apify.actor/mcp" \
  '{"jsonrpc":"2.0","id":4,"method":"tools/call","params":{"name":"enrich_company_website","arguments":{"domain":"linear.app","includePricing":true,"includeLlmsTxt":true}}}'

mcp_call "5. SEC EDGAR Form D, Form 4 & 8-K MCP: search_startup_funding" \
  "https://spiky-closet--sec-funding-insider-mcp.apify.actor/mcp" \
  '{"jsonrpc":"2.0","id":5,"method":"tools/call","params":{"name":"search_startup_funding","arguments":{"days":7,"excludeFunds":true,"excludeSpvs":true,"maxResults":3}}}'
