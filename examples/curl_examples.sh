#!/usr/bin/env bash
# Quickstart cURL examples for both AdPulse Labs remote MCP servers & REST APIs.
# Export APIFY_TOKEN (for Apify Standby MCP/REST) or RAPIDAPI_KEY (for RapidAPI Hub) before running.
set -euo pipefail

: "${APIFY_TOKEN:?Set APIFY_TOKEN to your Apify API token first}"

echo "==> 1. Google Ads Transparency MCP: tools/call (search_google_ads)"
curl -sS -X POST "https://spiky-closet--google-ads-transparency-scraper.apify.actor/mcp" \
  -H "Authorization: Bearer ${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"search_google_ads","arguments":{"query":"shopify.com","region":"DE","dateRangePreset":"LAST_30_DAYS","maxResults":3}}}'

echo ""
echo "==> 2. Tech Stack & Ad Pixel Detector MCP: tools/call (scan_domains)"
curl -sS -X POST "https://spiky-closet--tech-stack-ad-pixel-detector.apify.actor/mcp" \
  -H "Authorization: Bearer ${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"scan_domains","arguments":{"domains":["hubspot.com","klaviyo.com","ceo@linear.app"],"checkAdsTxt":true}}}'
echo ""
