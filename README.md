# PlantOn Redesign

A modern redesign of the PlantOn website (https://planton.me) - a Croatian Food Tech startup that enables remote garden rental services.

## Project Structure

```
planton-redesign/
├── index.html          # New redesigned page
├── styles.css          # Modern CSS styling
├── scrape.py           # Web scraper script
├── scraped/            # Scraped content from original site
│   ├── original.html   # Original HTML from planton.me
│   ├── content.json    # Structured content data
│   ├── text_content.txt # Extracted text content
│   └── body_only.html  # Body content only
└── README.md           # This file
```

## Features

### Design Improvements
- **Modern, clean UI** with soft green gradients and rounded corners
- **Responsive design** that works on mobile, tablet, and desktop
- **Improved typography** with better hierarchy and readability
- **Interactive elements** with smooth hover effects and transitions
- **FAQ accordion** for better content organization
- **Sticky navigation** for easy access to sections

### Content Sections
1. **Hero Section** - Eye-catching introduction with key value propositions
2. **How It Works** - 3-step process explanation
3. **Services** - Detailed breakdown of what's included
4. **FAQ** - Frequently asked questions with expandable answers
5. **Contact** - Contact information sidebar
6. **Footer** - Site links and legal information

## Getting Started

### View the Redesigned Page

Simply open `index.html` in your web browser:

```bash
open index.html
# or
python3 -m http.server 8000
# Then visit http://localhost:8000
```

### Scrape Original Content

To re-scrape the original PlantOn website:

```bash
python3 scrape.py
```

This will:
- Download the original HTML
- Extract structured content to JSON
- Save plain text content
- Create a body-only HTML version

### Requirements

The scraper requires Python 3 with:
- `requests`
- `beautifulsoup4`

Install dependencies:

```bash
pip3 install requests beautifulsoup4
```

## Design Philosophy

The redesign focuses on:
- **Clarity** - Easy to understand value proposition
- **Trust** - Professional appearance builds confidence
- **Accessibility** - Semantic HTML and good contrast
- **Performance** - Lightweight CSS, no external dependencies
- **Modern Aesthetics** - Contemporary design trends while maintaining brand identity

## Color Palette

- **Primary Green**: `#3ca66b` - Main brand color
- **Dark Green**: `#237348` - Accents and headings
- **Background**: `#f5f8f4` - Soft green tint
- **Text**: `#132018` - Dark green-black
- **Muted**: `#6b7b6f` - Secondary text

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Notes

- All content is in Croatian (hr) as per the original site
- The design is fully static HTML/CSS with minimal JavaScript for FAQ interactions
- No build process required - just open and view
- Original scraped content is preserved in the `scraped/` directory for reference

## License

This is a redesign project for educational/demonstration purposes.

