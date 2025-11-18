#!/usr/bin/env python3
import requests
from pathlib import Path
from urllib.parse import urlparse
import time

def get_claude_code_urls():
    """Get URLs from claude_code_en_docs.txt"""
    try:
        with open('claude_code_en_docs.txt', 'r') as f:
            urls = f.read().strip().split('\n')
        return [url for url in urls if url.strip()]
    except FileNotFoundError:
        print("claude_code_en_docs.txt not found")
        return []

def download_markdown(url):
    """Download markdown content directly."""
    md_url = url + '.md'
    try:
        response = requests.get(md_url, timeout=30)
        response.raise_for_status()
        return f"{md_url}\n\n{response.text}"
    except Exception as e:
        print(f"Error downloading {md_url}: {e}")
        return f"{md_url}\n\nError: {e}"

def url_to_filename(url):
    """Convert URL to filename with claude.code prefix."""
    path = urlparse(url).path
    # Get the last part after /en/
    parts = path.split('/en/')
    if len(parts) > 1:
        last_part = parts[1].rstrip('/').replace('/', '_')
        if not last_part:
            last_part = 'overview'
        return f"claude.code.{last_part}.md"
    return "claude.code.unknown.md"

def main():
    urls = get_claude_code_urls()
    if not urls:
        print("No URLs found")
        return
    
    print(f"Found {len(urls)} Claude Code docs URLs")
    
    docs_dir = Path('docs')
    docs_dir.mkdir(exist_ok=True)
    
    for url in urls:
        print(f"Downloading: {url}")
        content = download_markdown(url)
        
        filename = url_to_filename(url)
        filepath = docs_dir / filename
        filepath.write_text(content, encoding='utf-8')
        print(f"Saved: {filename}")
        
        time.sleep(0.5)

if __name__ == "__main__":
    main()
