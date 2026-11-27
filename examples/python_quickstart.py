#!/usr/bin/env python3
"""Minimal Python quickstart for all 5 AdPulse Labs RapidAPI REST endpoints (stdlib only)."""
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
    # 1. Google Ads Transparency
    ads = post_json(
        "google-ads-transparency-creative-spy.p.rapidapi.com",
        "/screen",
        {"domains": ["ceo@shopify.com", "https://www.klaviyo.com/pricing"]},
    )
    print("1. Active Google Ads screen:", [(x.get("domain"), x.get("hasActiveAds")) for x in ads.get("items", [])])

    # 2. Tech Stack, Ad Pixels & DNS SaaS
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
    print("2. Qualified Shopify+PaidAds (No Klaviyo):", [x.get("domain") for x in tech.get("items", [])])

    # 3. Unified 6-ATS Jobs & Hiring Intelligence
    ats = post_json(
        "unified-multi-ats-jobs-salary-hiring-intelligence.p.rapidapi.com",
        "/screen",
        {"companies": ["stripe.com", "ramp.com"]},
    )
    print("3. 6-ATS Hiring signals:", [(x.get("company"), x.get("atsPlatform"), x.get("totalOpenJobs")) for x in ats.get("items", [])])

    # 4. Website Contacts, Socials, Pricing & /llms.txt Brief
    site = post_json(
        "website-contacts-socials-pricing-llm-brief-api.p.rapidapi.com",
        "/enrich",
        {"domains": ["linear.app", "vercel.com"], "includePricing": True, "includeLlmsTxt": True},
    )
    print("4. Website enrichment:", [(x.get("domain"), x.get("briefSource"), len(x.get("emails") or [])) for x in site.get("items", [])])

    # 5. SEC EDGAR Form D Startup Funding, Form 4 Insiders & 8-K
    sec = post_json(
        "sec-edgar-form-d-funding-form-4-insider-8-k-api.p.rapidapi.com",
        "/funding",
        {"days": 7, "excludeFunds": True, "excludeSpvs": True, "minAmountSoldUsd": 1000000, "maxResults": 5},
    )
    print("5. SEC Form D startup rounds:", [(x.get("companyName"), x.get("totalAmountSoldUsd")) for x in sec.get("items", [])])
