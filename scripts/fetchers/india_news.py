#!/usr/bin/env python3
"""
India Health News Fetcher

Collects health news from India:
- Google News India Health category
- Google News India Science category

Output: data/news/india_news.json
"""

import hashlib
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import feedparser

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "news"

# Google News India Health category RSS
GOOGLE_NEWS_HEALTH_RSS = (
    "https://news.google.com/rss/topics/"
    "CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JXVnVMVWRDS0FBUAE"
    "?hl=en-IN&gl=IN&ceid=IN:en"
)

# Google News India Science category RSS
GOOGLE_NEWS_SCIENCE_RSS = (
    "https://news.google.com/rss/topics/"
    "CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp0Y1RjU0JXVnVMVWRDR2dKSlRpZ0FQAQ"
    "?hl=en-IN&gl=IN&ceid=IN:en"
)

# Request delay
REQUEST_DELAY = 1.0  # seconds


def generate_id(title: str, link: str) -> str:
    """Generate news ID (hash-based on title and link)"""
    content = f"{title}:{link}"
    return hashlib.md5(content.encode()).hexdigest()[:12]


def parse_source(entry, default_source: str = "Unknown") -> dict:
    """Extract source information from RSS entry"""
    source_name = default_source
    if hasattr(entry, "source") and hasattr(entry.source, "title"):
        source_name = entry.source.title

    return {
        "name": source_name,
        "link": entry.get("link", "")
    }


def parse_published(entry) -> str:
    """Parse published time and convert to ISO 8601 format"""
    published = entry.get("published_parsed")
    if published:
        try:
            dt = datetime(*published[:6], tzinfo=timezone.utc)
            return dt.isoformat()
        except Exception:
            pass

    # Use current time if parsing fails
    return datetime.now(timezone.utc).isoformat()


def clean_summary(summary: str) -> str:
    """Clean summary text (remove HTML tags, etc.)"""
    # Remove HTML tags
    clean = re.sub(r"<[^>]+>", "", summary)
    # Remove excess whitespace
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean[:500] if len(clean) > 500 else clean


def fetch_rss(url: str, source_name: str) -> list[dict]:
    """Fetch news from RSS URL"""
    print(f"  Fetching: {source_name}")
    print(f"    URL: {url[:70]}...")

    try:
        # Fetch with custom headers
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; InTxGNN/1.0; +https://intxgnn.yao.care)",
            "Accept": "application/rss+xml, application/xml, text/xml",
            "Accept-Language": "en-IN,en;q=0.9,hi;q=0.8",
        }
        request = Request(url, headers=headers)
        with urlopen(request, timeout=30) as response:
            content = response.read()
    except (HTTPError, URLError) as e:
        print(f"    Error: {e}")
        return []

    feed = feedparser.parse(content)

    if feed.bozo:
        print(f"    Warning: RSS parsing issue - {feed.bozo_exception}")

    news_items = []

    for entry in feed.entries:
        title = entry.get("title", "")
        link = entry.get("link", "")

        if not title or not link:
            continue

        news_id = generate_id(title, link)
        source = parse_source(entry, source_name)
        published = parse_published(entry)
        summary = clean_summary(entry.get("summary", "") or entry.get("description", ""))

        news_items.append({
            "id": news_id,
            "title": title,
            "published": published,
            "summary": summary,
            "sources": [source]
        })

    print(f"    Retrieved: {len(news_items)} news items")
    return news_items


def fetch_google_news_health() -> list[dict]:
    """Fetch Google News India Health category"""
    return fetch_rss(GOOGLE_NEWS_HEALTH_RSS, "Google News India Health")


def fetch_google_news_science() -> list[dict]:
    """Fetch Google News India Science category"""
    return fetch_rss(GOOGLE_NEWS_SCIENCE_RSS, "Google News India Science")


def deduplicate_news(news_items: list[dict]) -> list[dict]:
    """Remove duplicate news (ID-based)"""
    seen_ids = set()
    unique_items = []

    for item in news_items:
        if item["id"] not in seen_ids:
            seen_ids.add(item["id"])
            unique_items.append(item)

    return unique_items


def filter_health_keywords(news_items: list[dict]) -> list[dict]:
    """Filter by health-related keywords"""
    health_keywords = [
        # Medical / Health general
        "medical", "medicine", "drug", "treatment", "therapy", "diagnosis",
        "surgery", "hospital", "clinic", "health", "disease", "disorder",
        "symptom", "infection", "virus", "bacteria",
        # Disease names
        "cancer", "diabetes", "hypertension", "heart", "stroke", "dementia",
        "Alzheimer", "depression", "insomnia", "asthma", "allergy",
        "hepatitis", "kidney", "liver", "lung", "brain", "tuberculosis",
        "malaria", "dengue", "COVID", "coronavirus",
        # Regulatory (India-specific)
        "CDSCO", "DCGI", "ICMR", "AIIMS", "approval", "clinical trial",
        # Drugs / Treatments
        "vaccine", "antibody", "immunotherapy", "gene therapy",
        "Ayurveda", "ayurvedic", "generic drug", "pharmaceutical",
        # Research
        "research", "discovery", "development", "efficacy", "side effect",
        "risk", "study", "breakthrough", "trial",
        # Pharma industry
        "pharma", "biotech", "biotechnology", "drugmaker",
        "Sun Pharma", "Cipla", "Dr. Reddy", "Lupin", "Biocon",
    ]

    filtered = []
    for item in news_items:
        text = f"{item['title']} {item.get('summary', '')}".lower()
        if any(keyword.lower() in text for keyword in health_keywords):
            filtered.append(item)

    return filtered


def main():
    print("Collecting India health news...")

    # Ensure directory exists
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    all_news = []

    # Google News India Health
    news = fetch_google_news_health()
    all_news.extend(news)
    time.sleep(REQUEST_DELAY)

    # Google News India Science
    news = fetch_google_news_science()
    all_news.extend(news)

    # Deduplicate
    unique_news = deduplicate_news(all_news)
    print(f"\nAfter deduplication: {len(unique_news)} items")

    # Health-related filtering
    health_news = filter_health_keywords(unique_news)
    print(f"After health filtering: {len(health_news)} items")

    # Sort by published date (newest first)
    health_news.sort(key=lambda x: x["published"], reverse=True)

    # Output
    output = {
        "source": "india_news",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "total_fetched": len(all_news),
        "unique_count": len(unique_news),
        "health_related_count": len(health_news),
        "news": health_news
    }

    output_path = DATA_DIR / "india_news.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nOutput: {output_path}")
    print(f"  - Total fetched: {len(all_news)}")
    print(f"  - Unique: {len(unique_news)}")
    print(f"  - Health-related: {len(health_news)}")


if __name__ == "__main__":
    main()
