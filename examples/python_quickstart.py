#!/usr/bin/env python3
"""Minimal Python quickstart for AdPulse Labs RapidAPI REST endpoints (stdlib only)."""
import json
import os
import urllib.request

RAPIDAPI_KEY = os.environ["RAPIDAPI_KEY"]

def post_json(host: str, path: str, payload: dict) -> dict:
    req = urllib.request.Request(
        f"https://{host}{path}",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "x-rapidapi-key": RAPIDAPI_KEY,
            "x-rapidapi-host": host,
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

if __name__ == "__main__":
    tech = post_json(
        "website-tech-stack-ad-pixels-and-saas-detector.p.rapidapi.com",
        "/scan",
        {
            "domains": ["allbirds.com", "klaviyo.com", "linear.app"],
            "onlyWithAdPixels": True,
            "mustHaveAll": ["Shopify"],
            "mustNotHave": ["Klaviyo"],
        },
    )
    print("Qualified Shopify+PaidAds (No Klaviyo) leads:", [x["domain"] for x in tech.get("items", [])])

    ads = post_json(
        "google-ads-transparency-creative-spy.p.rapidapi.com",
        "/screen",
        {"domains": ["ceo@shopify.com", "https://www.klaviyo.com/pricing"]},
    )
    print("Active Google Ads screen:", [(x.get("domain"), x.get("hasActiveAds")) for x in ads.get("items", [])])
