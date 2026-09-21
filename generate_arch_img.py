import os
from PIL import Image, ImageDraw, ImageFont

def generate_architecture_diagram():
    width = 1600
    height = 900
    
    # Create image with dark cyber theme background
    img = Image.new("RGBA", (width, height), (9, 11, 16, 255))
    draw = ImageDraw.Draw(img)
    
    # Draw background dot grid
    grid_spacing = 30
    for x in range(0, width, grid_spacing):
        for y in range(0, height, grid_spacing):
            draw.point((x, y), fill=(255, 255, 255, 15))
            
    # Load fonts
    try:
        title_font = ImageFont.truetype("arialbd.ttf", 34)
        subtitle_font = ImageFont.truetype("arial.ttf", 16)
        card_title_font = ImageFont.truetype("arialbd.ttf", 19)
        card_sub_font = ImageFont.truetype("arial.ttf", 13)
        tag_font = ImageFont.truetype("arialbd.ttf", 11)
        kicker_font = ImageFont.truetype("arialbd.ttf", 12)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        card_title_font = ImageFont.load_default()
        card_sub_font = ImageFont.load_default()
        tag_font = ImageFont.load_default()
        kicker_font = ImageFont.load_default()

    # Header section
    hdr_txt = "SYSTEM ARCHITECTURE"
    hdr_bbox = draw.textbbox((0, 0), hdr_txt, font=kicker_font)
    hdr_w = hdr_bbox[2] - hdr_bbox[0] + 24
    draw.rounded_rectangle([60, 40, 60 + hdr_w, 68], radius=6, fill=(255, 87, 34, 25), outline=(255, 87, 34, 180), width=1)
    draw.text((72, 49), hdr_txt, fill=(255, 87, 34), font=kicker_font)
    draw.text((60, 80), "BUILDSPACE ECOSYSTEM", fill=(243, 244, 248), font=title_font)
    draw.text((60, 125), "High-Performance SSR Python Architecture · FastHTML + HTMX · Zero Bloat Client Runtime", fill=(155, 161, 178), font=subtitle_font)

    # Accent glow line under header
    draw.line([(60, 160), (1540, 160)], fill=(30, 35, 48), width=1)
    draw.line([(60, 160), (280, 160)], fill=(255, 87, 34), width=2)

    # Helper function to draw rounded boxes with border and tags
    def draw_card(x, y, w, h, kicker, title, desc_lines, tags, accent_color, badge_text=None):
        # Card background
        draw.rounded_rectangle([x, y, x + w, y + h], radius=12, fill=(15, 19, 27, 230), outline=accent_color, width=1)
        
        # Subtle header line inside card
        draw.line([(x, y + 42), (x + w, y + 42)], fill=(28, 33, 46), width=1)
        
        # Kicker & Badge
        draw.text((x + 18, y + 16), kicker.upper(), fill=accent_color, font=kicker_font)
        if badge_text:
            bbox = draw.textbbox((0, 0), badge_text, font=tag_font)
            bw = bbox[2] - bbox[0] + 16
            draw.rounded_rectangle([x + w - bw - 16, y + 12, x + w - 16, y + 32], radius=6, fill=(255, 255, 255, 12), outline=accent_color, width=1)
            draw.text((x + w - bw - 8, y + 16), badge_text, fill=(240, 240, 245), font=tag_font)

        # Title
        draw.text((x + 18, y + 54), title, fill=(243, 244, 248), font=card_title_font)
        
        # Desc lines
        curr_y = y + 84
        for line in desc_lines:
            draw.text((x + 18, curr_y), line, fill=(160, 166, 185), font=card_sub_font)
            curr_y += 18
            
        # Tags pills
        tag_x = x + 18
        tag_y = y + h - 34
        for tag in tags:
            tbox = draw.textbbox((0, 0), tag, font=tag_font)
            tw = tbox[2] - tbox[0] + 14
            draw.rounded_rectangle([tag_x, tag_y, tag_x + tw, tag_y + 20], radius=4, fill=(24, 29, 41), outline=(45, 52, 70), width=1)
            draw.text((tag_x + 7, tag_y + 4), tag, fill=(200, 205, 220), font=tag_font)
            tag_x += tw + 8

    # COLUMN 1: CLIENT & INTERACTION LAYER (X: 60, W: 450)
    draw_card(60, 190, 450, 190, "01 / CLIENT LAYER", "Browser & HTMX Runtime", 
              ["• Server-driven HTML hypermedia exchanges",
               "• Zero heavy client JS bundles (No React/Vue)",
               "• Instant DOM swaps via hx-get, hx-post, hx-target"],
              ["HTMX 1.9", "Native DOM", "Bespoke CSS", "Responsive"], (0, 240, 255, 140), "HYPERMEDIA")

    draw_card(60, 410, 450, 210, "02 / INTERACTION SUBSYSTEM", "Floating Chat & Modals", 
              ["• Asynchronous instant inquiry chat widget",
               "• Inline optimistic feedback & message state",
               "• Dynamic project deep-dive case study routes",
               "• Real-time validation & anti-spam defense"],
              ["Async HTMX", "Custom Modals", "Design Tokens"], (255, 87, 34, 180), "LIVE WIDGET")

    draw_card(60, 650, 450, 190, "03 / PRESENTATION SYSTEM", "Cyber-Dark Workshop UI", 
              ["• Rubik Glitch Pop + Grape Nuts handwritten accents",
               "• JetBrains Mono & Plus Jakarta Sans typography",
               "• Dark theme palette with glowing neon accents"],
              ["Design Tokens", "Hand Notes", "Glitch Pop", "CSS Grid"], (255, 179, 0, 160), "EDITORIAL")

    # COLUMN 2: APPLICATION RUNTIME & SSR (X: 575, W: 450)
    draw_card(575, 190, 450, 240, "04 / SERVER RUNTIME", "FastHTML + ASGI Server", 
              ["• Native Python ASGI architecture powered by Starlette",
               "• Component-based Functional HTML generation",
               "• Lightning-fast SSR with instant page loads",
               "• Route decorators & high-concurrency request dispatch"],
              ["Python 3.12", "FastHTML", "Starlette", "Uvicorn"], (0, 240, 255, 200), "CORE ENGINE")

    draw_card(575, 460, 450, 200, "05 / PAGE & SECTION ROUTING", "Component Tree & Logic", 
              ["• / (Home): Workbench, Selected Work, Experience, About",
               "• /projects/{slug}: Deep architectural case studies",
               "• /api/chat: Message intake & notification pipelines"],
              ["Home Page", "Case Studies", "Selected Work", "Modular"], (255, 87, 34, 180), "ROUTER")

    draw_card(575, 690, 450, 150, "06 / LOCAL DATA STORE", "Embedded SQLite Engine", 
              ["• Thread-safe local persistence for chat messages",
               "• Ephemeral serverless storage bridge for sessions"],
              ["SQLite 3", "Auto-Migrate", "Transactional"], (0, 230, 118, 160), "PERSISTENCE")

    # COLUMN 3: DEPLOYMENT & INTEGRATIONS (X: 1090, W: 450)
    draw_card(1090, 190, 450, 200, "07 / SERVERLESS HOSTING", "Vercel Edge Platform", 
              ["• Serverless Python ASGI entrypoint (api/index.py)",
               "• Global low-latency CDN edge routing",
               "• Automatic Git deployment pipeline on main push"],
              ["Vercel ASGI", "Serverless", "Edge CDN", "CI/CD"], (255, 87, 34, 200), "PRODUCTION")

    draw_card(1090, 420, 450, 220, "08 / EXTERNAL APIS & LLMS", "Intelligent Integrations", 
              ["• Web3Forms: Instant email alerts to developer inbox",
               "• Groq & Gemini LLM: Integrated into showcase systems",
               "• YouTube API: Video transcript seek & sync engines"],
              ["Web3Forms", "Groq LLM", "Gemini API", "YouTube Data"], (0, 240, 255, 160), "EXTERNAL")

    draw_card(1090, 670, 450, 170, "09 / FEATURED ECOSYSTEM", "Engineered Systems", 
              ["• Flowly (AI Productivity) · AI Smart Chat (Voice/LLM)",
               "• Clipwise (Video Search) · BillNest (Billing System)",
               "• HousePrice (ML Valuation API)"],
              ["Flutter/Dart", "FastAPI", "Machine Learning"], (255, 179, 0, 180), "PROJECTS")

    # Flow arrows (Connecting Col 1 -> Col 2 -> Col 3)
    def draw_arrow(x1, y1, x2, y2, color):
        draw.line([(x1, y1), (x2, y2)], fill=color, width=2)
        draw.polygon([(x2, y2), (x2 - 8, y2 - 5), (x2 - 8, y2 + 5)], fill=color)

    # Browser to FastHTML
    draw_arrow(510, 285, 575, 285, (0, 240, 255, 200))
    # Chat widget to FastHTML router
    draw_arrow(510, 515, 575, 515, (255, 87, 34, 200))
    
    # FastHTML to Vercel
    draw_arrow(1025, 285, 1090, 285, (255, 87, 34, 200))
    # Router to External APIs
    draw_arrow(1025, 520, 1090, 520, (0, 240, 255, 200))

    # Save output
    os.makedirs("static/images", exist_ok=True)
    out_path = "static/images/architecture.png"
    img.save(out_path, "PNG")
    print(f"Generated successfully: {out_path}")

if __name__ == "__main__":
    generate_architecture_diagram()
