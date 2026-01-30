#!/usr/bin/env python3
"""
Scraper for PlantOn website (https://planton.me)
Saves the original HTML and extracts text content.
"""

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import os

URL = "https://planton.me"

def scrape_planton():
    """Scrape PlantOn website and save content."""
    print(f"Scraping {URL}...")
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        resp = requests.get(URL, headers=headers, timeout=15)
        resp.raise_for_status()
        
        # Save raw HTML
        html_content = resp.text
        with open("scraped/original.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        print("✓ Saved original HTML to scraped/original.html")
        
        # Parse with BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")
        
        # Extract structured content
        content = {
            "url": URL,
            "scraped_at": datetime.now().isoformat(),
            "title": soup.title.string if soup.title else "",
            "meta_description": "",
            "navigation": [],
            "sections": [],
            "faq": [],
            "footer": {}
        }
        
        # Meta description
        meta_desc = soup.find("meta", attrs={"name": "description"})
        if meta_desc:
            content["meta_description"] = meta_desc.get("content", "")
        
        # Navigation links
        nav_links = soup.find_all("a", href=True)
        nav_items = []
        for link in nav_links[:20]:  # Limit to first 20 links
            text = link.get_text(strip=True)
            href = link.get("href", "")
            if text and href:
                nav_items.append({"text": text, "href": href})
        content["navigation"] = nav_items
        
        # Extract main headings and paragraphs
        sections = []
        current_section = None
        
        for tag in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "div"]):
            tag_name = tag.name
            text = tag.get_text(strip=True)
            
            if not text or len(text) < 3:
                continue
            
            if tag_name.startswith("h"):
                if current_section:
                    sections.append(current_section)
                current_section = {
                    "type": tag_name,
                    "title": text,
                    "content": []
                }
            elif current_section and tag_name in ["p", "li"]:
                current_section["content"].append(text)
            elif not current_section and tag_name == "p":
                sections.append({
                    "type": "paragraph",
                    "title": "",
                    "content": [text]
                })
        
        if current_section:
            sections.append(current_section)
        
        content["sections"] = sections
        
        # Extract FAQ items (if structured)
        faq_items = []
        faq_section = soup.find(string=lambda text: text and "FAQ" in text.upper())
        if faq_section:
            parent = faq_section.find_parent()
            if parent:
                # Try to find FAQ questions/answers
                for item in parent.find_all(["h3", "h4", "p"], limit=20):
                    text = item.get_text(strip=True)
                    if text and len(text) > 10:
                        faq_items.append(text)
        content["faq"] = faq_items
        
        # Save structured content as JSON
        with open("scraped/content.json", "w", encoding="utf-8") as f:
            json.dump(content, f, ensure_ascii=False, indent=2)
        print("✓ Saved structured content to scraped/content.json")
        
        # Extract all text content (plain text)
        text_content = []
        for tag in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "span", "div"]):
            text = tag.get_text(strip=True)
            if text and len(text) > 5 and text not in text_content:
                text_content.append(text)
        
        with open("scraped/text_content.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(text_content))
        print("✓ Saved text content to scraped/text_content.txt")
        
        # Save a cleaned HTML version (just body content)
        if soup.body:
            body_content = str(soup.body)
            with open("scraped/body_only.html", "w", encoding="utf-8") as f:
                f.write(body_content)
            print("✓ Saved body content to scraped/body_only.html")
        
        print(f"\n✓ Scraping completed successfully!")
        print(f"  - Total sections found: {len(sections)}")
        print(f"  - Total text items: {len(text_content)}")
        
        return content
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Error fetching website: {e}")
        return None
    except Exception as e:
        print(f"✗ Error processing content: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    # Create scraped directory
    os.makedirs("scraped", exist_ok=True)
    
    # Run scraper
    result = scrape_planton()
    
    if result:
        print("\n" + "="*50)
        print("Scraping Summary:")
        print("="*50)
        print(f"Title: {result.get('title', 'N/A')}")
        print(f"Sections: {len(result.get('sections', []))}")
        print(f"Navigation items: {len(result.get('navigation', []))}")
        print("="*50)

