#!/usr/bin/env python3
"""
Google News RSS Fetcher

Fetch Google News Health channel RSS, output to data/news/google_rss.json
"""

import json
import hashlib
from datetime import datetime, timezone
from pathlib import Path

import feedparser

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "news"

# Google News Health channel RSS (India English)
GOOGLE_NEWS_HEALTH_RSS = (
    "https://news.google.com/rss/topics/"
    "CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JYcG9MVlJYS0FBUAE"
    "?hl=en-IN&gl=IN&ceid=IN:en"
)


def generate_id(title: str, link: str) -> str:
    """Generate news ID (hash based on title and link)"""
    content = f"{title}:{link}"
    return hashlib.sha256(content.encode()).hexdigest()[:12]


def parse_source(entry) -> dict:
    """Extract source info from RSS entry"""
    # Google News RSS source tag
    source_name = "Google News"
    if hasattr(entry, "source") and hasattr(entry.source, "title"):
        source_name = entry.source.title

    return {
        "name": source_name,
        "link": entry.get("link", "")
    }


def parse_published(entry) -> str:
    """Parse published time, convert to ISO 8601 format"""
    published = entry.get("published_parsed")
    if published:
        try:
            dt = datetime(*published[:6], tzinfo=timezone.utc)
            return dt.isoformat()
        except Exception:
            pass

    # If parsing fails, use current time
    return datetime.now(timezone.utc).isoformat()


def clean_summary(summary: str) -> str:
    """Clean summary text (remove HTML tags, etc.)"""
    import re
    # Remove HTML tags
    clean = re.sub(r"<[^>]+>", "", summary)
    # Remove extra whitespace
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean[:500] if len(clean) > 500 else clean


def fetch_google_news() -> list[dict]:
    """Fetch Google News Health channel"""
    print(f"Fetching Google News RSS...")
    print(f"  URL: {GOOGLE_NEWS_HEALTH_RSS[:80]}...")

    feed = feedparser.parse(GOOGLE_NEWS_HEALTH_RSS)

    if feed.bozo:
        print(f"  Warning: RSS parsing issue - {feed.bozo_exception}")

    news_items = []

    for entry in feed.entries:
        title = entry.get("title", "")
        link = entry.get("link", "")

        if not title or not link:
            continue

        news_id = generate_id(title, link)
        source = parse_source(entry)
        published = parse_published(entry)
        summary = clean_summary(entry.get("summary", ""))

        news_items.append({
            "id": news_id,
            "title": title,
            "published": published,
            "summary": summary,
            "sources": [source]
        })

    print(f"  Fetched {len(news_items)} news items")
    return news_items


def main():
    # Ensure directory exists
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Fetch news
    news_items = fetch_google_news()

    # Output
    output = {
        "source": "google_rss",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "count": len(news_items),
        "news": news_items
    }

    output_path = DATA_DIR / "google_rss.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nOutput: {output_path}")
    print(f"  - News count: {len(news_items)}")


if __name__ == "__main__":
    main()
