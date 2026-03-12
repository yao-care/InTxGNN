#!/usr/bin/env python3
"""
News Processing Script

Functions:
1. Read all data/news/*.json source files
2. Load keywords.json for keyword matching
3. Cross-site deduplication (merge similar titles)
4. Output matched_news.json
"""

import json
import re
from datetime import datetime, timezone, timedelta
from difflib import SequenceMatcher
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "news"

# Settings
SIMILARITY_THRESHOLD = 0.8  # Title similarity threshold
TIME_WINDOW_HOURS = 24  # Dedup time window (hours)
MAX_NEWS_AGE_DAYS = 30  # Maximum news age to keep (days)


def load_json(path: Path) -> dict | list:
    """Load JSON file"""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data: dict | list, path: Path):
    """Save JSON file"""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_all_sources() -> list[dict]:
    """Load news from all sources"""
    all_news = []
    excluded = {"keywords.json", "matched_news.json", "synonyms.json"}

    for json_file in DATA_DIR.glob("*.json"):
        if json_file.name in excluded:
            continue

        try:
            data = load_json(json_file)
            source_name = data.get("source", json_file.stem)
            news_items = data.get("news", [])
            print(f"  - {json_file.name}: {len(news_items)} items")

            for item in news_items:
                item["_source_file"] = source_name
                all_news.append(item)

        except Exception as e:
            print(f"  Warning: Cannot load {json_file.name} - {e}")

    return all_news


def filter_old_news(news_items: list[dict]) -> list[dict]:
    """Filter news older than 30 days"""
    cutoff = datetime.now(timezone.utc) - timedelta(days=MAX_NEWS_AGE_DAYS)
    filtered = []

    for item in news_items:
        try:
            published = datetime.fromisoformat(item.get("published", ""))
            if published >= cutoff:
                filtered.append(item)
        except (ValueError, TypeError):
            # Cannot parse date, keep it
            filtered.append(item)

    removed = len(news_items) - len(filtered)
    if removed > 0:
        print(f"  Filtered old news: {removed} items")

    return filtered


def title_similarity(title1: str, title2: str) -> float:
    """Calculate similarity between two titles"""
    # Remove source markers (e.g., "- Times of India")
    clean1 = re.sub(r"\s*[-–—]\s*[^\s]+$", "", title1).strip()
    clean2 = re.sub(r"\s*[-–—]\s*[^\s]+$", "", title2).strip()

    return SequenceMatcher(None, clean1, clean2).ratio()


def deduplicate_news(news_items: list[dict]) -> list[dict]:
    """Cross-site deduplication, merge sources of similar news"""
    # Sort by published time (newest first)
    sorted_news = sorted(
        news_items,
        key=lambda x: x.get("published", ""),
        reverse=True
    )

    merged = []
    used_indices = set()

    for i, item in enumerate(sorted_news):
        if i in used_indices:
            continue

        # Find similar news
        similar_items = [item]
        item_time = datetime.fromisoformat(
            item.get("published", datetime.now(timezone.utc).isoformat())
        )

        for j, other in enumerate(sorted_news[i + 1:], start=i + 1):
            if j in used_indices:
                continue

            # Check time window
            other_time = datetime.fromisoformat(
                other.get("published", datetime.now(timezone.utc).isoformat())
            )
            time_diff = abs((item_time - other_time).total_seconds() / 3600)

            if time_diff > TIME_WINDOW_HOURS:
                continue

            # Check title similarity
            if title_similarity(item["title"], other["title"]) >= SIMILARITY_THRESHOLD:
                similar_items.append(other)
                used_indices.add(j)

        # Merge sources
        all_sources = []
        seen_links = set()
        for sim_item in similar_items:
            for source in sim_item.get("sources", []):
                if source["link"] not in seen_links:
                    seen_links.add(source["link"])
                    all_sources.append(source)

        # Use earliest published time
        earliest_time = min(
            datetime.fromisoformat(s.get("published", datetime.now(timezone.utc).isoformat()))
            for s in similar_items
        )

        merged_item = {
            "id": item["id"],
            "title": re.sub(r"\s*[-–—]\s*[^\s]+$", "", item["title"]).strip(),
            "published": earliest_time.isoformat(),
            "summary": item.get("summary", ""),
            "sources": all_sources,
            "matched_keywords": []  # To be filled later
        }
        merged.append(merged_item)
        used_indices.add(i)

    print(f"  After dedup: {len(merged)} items (merged {len(news_items) - len(merged)} items)")
    return merged


def match_keywords(news_items: list[dict], keywords: dict) -> list[dict]:
    """Match keywords in news items"""
    drugs = keywords.get("drugs", [])
    indications = keywords.get("indications", [])

    matched_count = 0

    for item in news_items:
        text_to_search = f"{item['title']} {item.get('summary', '')}".lower()
        matches = []

        # Match drugs
        for drug in drugs:
            drug_name = drug["name"]
            drug_id = drug.get("drugbank_id", "")

            # English keywords
            for kw in drug["keywords"].get("en", []):
                if kw.lower() in text_to_search:
                    matches.append({
                        "type": "drug",
                        "drugbank_id": drug_id,
                        "keyword": kw,
                        "name": drug_name
                    })
                    break  # Only record once per drug

            # Local language keywords
            for kw in drug["keywords"].get("local", []):
                if kw in item["title"] or kw in item.get("summary", ""):
                    # Ensure no duplicates
                    if not any(m.get("drugbank_id") == drug_id and m["type"] == "drug" for m in matches):
                        matches.append({
                            "type": "drug",
                            "drugbank_id": drug_id,
                            "keyword": kw,
                            "name": drug_name
                        })
                    break

        # Match indications
        for ind in indications:
            ind_name = ind["name"]
            ind_id = ind.get("disease_id", "")

            # English keywords
            for kw in ind["keywords"].get("en", []):
                if kw.lower() in text_to_search:
                    matches.append({
                        "type": "indication",
                        "disease_id": ind_id,
                        "name": ind_name,
                        "keyword": kw
                    })
                    break

            # Local language keywords
            for kw in ind["keywords"].get("local", []):
                if kw in item["title"] or kw in item.get("summary", ""):
                    if not any(m.get("keyword") == kw and m["type"] == "indication" for m in matches):
                        matches.append({
                            "type": "indication",
                            "disease_id": ind_id,
                            "name": ind_name,
                            "keyword": kw
                        })
                    break

        item["matched_keywords"] = matches
        if matches:
            matched_count += 1

    print(f"  Matched keywords: {matched_count} items")
    return news_items


def main():
    print("Processing news data...")

    # 1. Load all sources
    print("\nLoading source files:")
    all_news = load_all_sources()
    print(f"  Total: {len(all_news)} items")

    if not all_news:
        print("\nNo news found. Run fetchers first (scripts/fetchers/google_rss.py)")
        return

    # 2. Filter old news
    print("\nFiltering old news:")
    all_news = filter_old_news(all_news)

    # 3. Deduplicate
    print("\nCross-site deduplication:")
    all_news = deduplicate_news(all_news)

    # 4. Load keywords and match
    print("\nKeyword matching:")
    keywords_path = DATA_DIR / "keywords.json"
    if not keywords_path.exists():
        print(f"  Error: {keywords_path} not found. Run generate_news_keywords.py first.")
        return

    keywords = load_json(keywords_path)
    print(f"  Keywords: {keywords['drug_count']} drugs + {keywords['indication_count']} indications")
    all_news = match_keywords(all_news, keywords)

    # 5. Output matched_news.json
    output = {
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "total_count": len(all_news),
        "matched_count": sum(1 for n in all_news if n.get("matched_keywords")),
        "news": all_news
    }
    output_path = DATA_DIR / "matched_news.json"
    save_json(output, output_path)
    print(f"\nOutput: {output_path}")
    print(f"  - Total news: {output['total_count']}")
    print(f"  - Matched news: {output['matched_count']}")

    print("\nDone!")


if __name__ == "__main__":
    main()
