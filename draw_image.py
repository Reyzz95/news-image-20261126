import os
from PIL import Image, ImageDraw, ImageFont
import textwrap

# Create 1024x1024 canvas with cream background
width, height = 1024, 1024
image = Image.new("RGB", (width, height), "#fcfaf5")
draw = ImageDraw.Draw(image)

# Font paths
font_dir = "/usr/share/fonts/truetype/dejavu/"
font_serif_bold = ImageFont.truetype(os.path.join(font_dir, "DejaVuSerif-Bold.ttf"), 14)
font_serif_bold_lg = ImageFont.truetype(os.path.join(font_dir, "DejaVuSerif-Bold.ttf"), 22)
font_serif_bold_xl = ImageFont.truetype(os.path.join(font_dir, "DejaVuSerif-Bold.ttf"), 32)
font_serif = ImageFont.truetype(os.path.join(font_dir, "DejaVuSerif.ttf"), 11)
font_serif_sm = ImageFont.truetype(os.path.join(font_dir, "DejaVuSerif.ttf"), 9)
font_sans = ImageFont.truetype(os.path.join(font_dir, "DejaVuSans.ttf"), 10)
font_sans_bold = ImageFont.truetype(os.path.join(font_dir, "DejaVuSans-Bold.ttf"), 10)
font_sans_sm = ImageFont.truetype(os.path.join(font_dir, "DejaVuSans.ttf"), 9)

# Colors
COLOR_BG = "#fcfaf5"
COLOR_NAVY = "#112233"
COLOR_RED = "#b22222"
COLOR_BLACK = "#1a1a1a"
COLOR_MUTED = "#555555"
COLOR_BOX_BG = "#f4efe4"
COLOR_LEAD_BG = "#f7f2e8"
COLOR_BORDER = "#222222"

# Outer border
draw.rectangle([10, 10, width-10, height-10], outline=COLOR_NAVY, width=2)
draw.rectangle([12, 12, width-12, height-12], outline=COLOR_NAVY, width=1)

# 1. MASTHEAD (y = 15 to 95)
draw.text((width//2, 22), "THE WORLD IN ONE DAY", font=font_serif_bold_xl, fill=COLOR_NAVY, anchor="mt")
draw.line([(30, 60), (width-30, 60)], fill=COLOR_RED, width=2)
draw.text((width//2, 66), "ONE DAY OF WORLD NEWS, ONE PICTURE — THURSDAY 26 NOVEMBER 2026", font=font_sans_bold, fill=COLOR_MUTED, anchor="mt")
draw.line([(30, 82), (width-30, 82)], fill=COLOR_NAVY, width=1)

# 2. THE DAY IN UTC (y = 86 to 155)
draw.rectangle([20, 86, width-20, 155], fill=COLOR_BOX_BG, outline=COLOR_BORDER, width=1)
draw.rectangle([20, 86, width-20, 102], fill=COLOR_NAVY)
draw.text((30, 88), "THE DAY IN UTC — TIMELINE (26 NOV 2026)", font=font_sans_bold, fill="#ffffff")

utc_items = [
    "00:22 Zambia bans protest",
    "00:41 ISIL attack in Syria",
    "00:47 Cairo tanker fire (31)",
    "01:00 Puerto Rico Luma contract",
    "01:39 Ukraine hits airbase",
    "02:54 US tariffs on India (25%)",
    "03:53 Kashmir terror-ops report",
    "14:00 Gukesh-Sindarov Chess Game 3"
]

# Draw UTC items in 4 columns x 2 rows
col_w = (width - 60) // 4
for i, item in enumerate(utc_items):
    c = i % 4
    r = i // 4
    x = 30 + c * col_w
    y = 108 + r * 22
    draw.text((x, y), "• " + item, font=font_sans_sm, fill=COLOR_BLACK)

# 3. THE DAY IN NUMBERS (y = 159 to 226)
draw.rectangle([20, 159, width-20, 226], fill=COLOR_BOX_BG, outline=COLOR_BORDER, width=1)
draw.rectangle([20, 159, width-20, 175], fill=COLOR_RED)
draw.text((30, 161), "THE DAY IN NUMBERS", font=font_sans_bold, fill="#ffffff")

num_items = [
    "31 killed in Cairo fire",
    "100th Macy's parade postponed",
    "4.3% US Q3 GDP growth",
    "5 planes hit at Savasleyka",
    "14 partners face tariffs",
    "1M SpaceX satellites",
    "76 hostages freed in Colombia",
    "$227M meth lab seized"
]

for i, item in enumerate(num_items):
    c = i % 4
    r = i // 4
    x = 30 + c * col_w
    y = 181 + r * 22
    draw.text((x, y), "■ " + item, font=font_sans_bold, fill=COLOR_NAVY)

# 4. THREE LARGE LEAD TILES (y = 230 to 465)
lead_w = (width - 56) // 3
leads = [
    {
        "title": "Macy's 100th Parade Postponed",
        "sub": "First time in 100-year history due to 70 mph Nor'easter; moved to Sat 28 Nov.",
        "color": "#e74c3c",
        "art": "PARADE"
    },
    {
        "title": "Cairo Fuel Tanker Fire Kills 31",
        "sub": "Tanker overturns on Ring Road in Warraq, sparking massive inferno; 21 injured.",
        "color": "#d35400",
        "art": "FIRE"
    },
    {
        "title": "Ukraine Hits Airbase & Refineries",
        "sub": "5 aircraft damaged at Savasleyka; Rosneft refineries burn in Samara.",
        "color": "#2980b9",
        "art": "STRIKE"
    }
]

for i, lead in enumerate(leads):
    lx = 20 + i * (lead_w + 8)
    ly = 230
    lh = 235
    draw.rectangle([lx, ly, lx + lead_w, ly + lh], fill=COLOR_LEAD_BG, outline=COLOR_BORDER, width=1)
    # Header bar
    draw.rectangle([lx, ly, lx + lead_w, ly + 20], fill=COLOR_NAVY)
    draw.text((lx + 8, ly + 3), f"LEAD STORY {i+1}", font=font_sans_bold, fill="#ffffff")
    
    # Mini illustration box
    art_box = [lx + 10, ly + 26, lx + lead_w - 10, ly + 95]
    draw.rectangle(art_box, fill="#ffffff", outline=COLOR_NAVY, width=1)
    
    # Draw simple vector art depending on lead
    if lead["art"] == "PARADE":
        # Balloon / float art
        draw.ellipse([art_box[0]+30, art_box[1]+10, art_box[0]+80, art_box[1]+60], fill=COLOR_RED)
        draw.line([art_box[0]+55, art_box[1]+60, art_box[0]+55, art_box[1]+80], fill=COLOR_NAVY, width=2)
        draw.rectangle([art_box[0]+45, art_box[1]+50, art_box[0]+65, art_box[1]+60], fill="#333")
        draw.text((art_box[0]+90, art_box[1]+25), "NOR'EASTER\n70 MPH GUSTS", font=font_sans_sm, fill=COLOR_NAVY)
    elif lead["art"] == "FIRE":
        # Flame art
        draw.polygon([
            (art_box[0]+50, art_box[1]+70),
            (art_box[0]+30, art_box[1]+40),
            (art_box[0]+45, art_box[1]+30),
            (art_box[0]+55, art_box[1]+15),
            (art_box[0]+65, art_box[1]+30),
            (art_box[0]+80, art_box[1]+40),
            (art_box[0]+60, art_box[1]+70)
        ], fill="#e67e22")
        draw.text((art_box[0]+90, art_box[1]+25), "RING ROAD\nWARRAQ, CAIRO", font=font_sans_sm, fill=COLOR_NAVY)
    else:
        # Jet / drone / fire art
        draw.polygon([
            (art_box[0]+20, art_box[1]+40),
            (art_box[0]+70, art_box[1]+25),
            (art_box[0]+50, art_box[1]+50)
        ], fill="#34495e")
        draw.ellipse([art_box[0]+55, art_box[1]+35, art_box[0]+85, art_box[1]+65], fill="#e74c3c")
        draw.text((art_box[0]+90, art_box[1]+25), "SAVASLEYKA\n& SAMARA", font=font_sans_sm, fill=COLOR_NAVY)

    # Headline & summary
    wrapped_title = textwrap.wrap(lead["title"], width=28)
    ty = ly + 102
    for t_line in wrapped_title:
        draw.text((lx + 10, ty), t_line, font=font_serif_bold, fill=COLOR_NAVY)
        ty += 16
        
    wrapped_sub = textwrap.wrap(lead["sub"], width=38)
    sy = ty + 4
    for s_line in wrapped_sub:
        draw.text((lx + 10, sy), s_line, font=font_serif, fill=COLOR_BLACK)
        sy += 13

# 5. SECOND ROW & MORE STORIES (y = 470 to 855)
# Let's arrange stories 4 to 30 in a compact 3-column newspaper grid or rows.
stories = [
    # Second row (4-7)
    ("Trump Tariffs on 14 Partners", "China, EU, Japan, SK, India (25%), Vietnam (35%) hit by new US trade overcapacity tariffs."),
    ("US Q3 GDP Grows 4.3%", "Revised sharply up from 3.4%; fastest growth in 3 years with 4.2% consumer spending."),
    ("COP31 Climate Summit Collapses", "Turkiye talks end with no deal; first COP failure since Copenhagen 2009 ('worst COP ever')."),
    ("Kim Orders Nuclear Expansion", "North Korea calls for wider tactical nuclear deployment; expels Swiss diplomat, closes office."),
    
    # More stories (8-30)
    ("Gukesh & Sindarov Draw Game 2", "World Chess Championship in Geneva tied 1-1 after 20-move draw; Game 3 on Thursday."),
    ("Puerto Rico Cancels Luma Contract", "Supreme Court voids Luma Energy power contract in 5-4 ruling over grid failures."),
    ("Colombia Frees 76 Hostages", "Forces rescue 76 captives after 17-hour supermarket siege in Cartagena."),
    ("Nigeria Seizes $227M Meth Lab", "Anti-narcotics agents raid industrial lab, arresting five Mexican nationals."),
    ("Andy Taylor Passes Away at 65", "Legendary Duran Duran lead guitarist loses courageous battle with stage 4 prostate cancer."),
    ("Pakistan Aboard Tiangong", "Zeeshan Ali becomes the first foreign astronaut aboard China's space station."),
    ("Poland No-Fly Zone Plan", "Warsaw creates buffer near Ukrainian border following persistent airspace incursions."),
    ("Netanyahu Bribery Case Urged Drop", "Israeli judges advise prosecutors to drop Case 4000 amid lengthy proceedings."),
    ("FCC Clears 1M SpaceX Satellites", "Regulators greenlight massive constellation expansion for orbital data centres."),
    ("Six Dead in Mississippi Crash", "Two children among six killed in tragic small plane crash off the Gulf coast."),
    ("India Marks 18 Yrs of 26/11", "Nation observes Constitution Day and solemn anniversary of Mumbai terror attacks."),
    ("SA President Farmgate Reprieve", "Cyril Ramaphosa wins legal reprieve from impeachment inquiry into Phala Phala."),
    ("Australia-Solomon Islands Pact", "Canberra and Honiara sign sweeping bilateral security agreement."),
    ("Second Judge Blocks Citizenship", "Federal judge halts Trump's executive order ending birthright citizenship."),
    ("ISIL Attack in Hasakah Kills Two", "Suicide bombing targets security personnel in northeastern Syria."),
    ("Zambia Bans Term Limit Protest", "Police block demonstrations against proposed removal of presidential term limits."),
    ("Lebanon Second Airport in Dec", "Beirut prepares to open a second international commercial airport next month."),
    ("Houthis Claim Saudi Refinery Strike", "Oil rallies above $90/bbl after drone/missile attack reported on Saudi facility."),
    ("Murmansk Governor Held", "Russian regional governor detained in pre-trial custody on corruption charges."),
    ("Dozens Urge Halt to Riot Agent", "UN member states demand Russia stop alleged use of CS/riot control agents in Ukraine."),
    ("Hong Kong Fire Survivors Mark Year", "City remembers victims one year after the deadliest apartment fire in decades."),
    ("Ecuador-US Security Talks", "Quito minister confirms discussions focused on reviewing bilateral operations."),
    ("India Wins Venice Biennale Lion", "National pavilion clinchesVisitors' Lion for Best National Pavilion at 61st Venice Biennale.")
]

# We have 27 stories here. Total stories = 3 leads + 4 second row + 23 more = 30 stories!
draw.rectangle([20, 470, width-20, 855], fill=COLOR_BOX_BG, outline=COLOR_BORDER, width=1)
draw.rectangle([20, 470, width-20, 486], fill=COLOR_NAVY)
draw.text((30, 472), "WORLD NEWS IN BRIEF — 30 STORIES FROM THURSDAY 26 NOVEMBER 2026", font=font_sans_bold, fill="#ffffff")

# Draw in 3 columns
col_width = (width - 56) // 3
col_heights = [492, 492, 492]
col_xs = [28, 28 + col_width + 8, 28 + (col_width + 8) * 2]

for idx, (stitle, sdesc) in enumerate(stories):
    # distribute across 3 columns
    c_idx = idx % 3
    x = col_xs[c_idx]
    y = col_heights[c_idx]
    
    # Draw bullet/marker
    draw.rectangle([x, y+2, x+4, y+6], fill=COLOR_RED)
    
    # Title & short desc
    draw.text((x + 8, y), f"{idx+4}. {stitle}", font=font_sans_bold, fill=COLOR_NAVY)
    y += 13
    
    wrapped = textwrap.wrap(sdesc, width=42)
    for w_line in wrapped[:2]: # max 2 lines per story
        draw.text((x + 8, y), w_line, font=font_serif_sm, fill=COLOR_BLACK)
        y += 11
    y += 4
    col_heights[c_idx] = y

# 6. WHERE IT HAPPENED (y = 860 to 925)
draw.rectangle([20, 860, width-20, 925], fill=COLOR_LEAD_BG, outline=COLOR_BORDER, width=1)
draw.rectangle([20, 860, width-20, 875], fill=COLOR_NAVY)
draw.text((30, 862), "WHERE IT HAPPENED — REGIONAL ROUNDUP", font=font_sans_bold, fill="#ffffff")

regions = [
    ("North America", "New York, Washington, Puerto Rico, Mississippi"),
    ("South America", "Cartagena, Ecuador"),
    ("Europe", "Geneva, Samara, Savasleyka, Poland, Turkiye, Murmansk"),
    ("Middle East", "Cairo, Israel, Lebanon, Syria, Saudi Arabia, Yemen"),
    ("Africa", "Nigeria, Zambia, South Africa"),
    ("Asia-Pacific", "North Korea, India, China, Pakistan, Australia, Solomon Islands")
]

reg_col_w = (width - 60) // 3
for i, (r_name, r_places) in enumerate(regions):
    c = i % 3
    r = i // 3
    rx = 30 + c * reg_col_w
    ry = 880 + r * 22
    draw.text((rx, ry), f"■ {r_name}:", font=font_sans_bold, fill=COLOR_RED)
    draw.text((rx, ry + 10), r_places, font=font_sans_sm, fill=COLOR_BLACK)

# 7. FOOTER (y = 930 to 1012)
draw.rectangle([20, 930, width-20, 1012], fill=COLOR_NAVY)
draw.text((width//2, 938), "DATE CHECK — THURSDAY 26 NOVEMBER 2026", font=font_serif_bold, fill="#ffffff", anchor="mt")
draw.text((width//2, 962), "Sources: AP, Reuters, AFP, BBC, WSJ, UN  |  Original drawings & editorial", font=font_sans, fill="#dddddd", anchor="mt")
draw.text((width//2, 986), "make.fun bounty: news-image-20261126 ($100, top 50 share)  ·  Reyzz95", font=font_sans_sm, fill="#aaaaaa", anchor="mt")

# Save image
output_path = "entry.png"
image.save(output_path, "PNG", optimize=True)
print(f"Successfully generated {output_path} ({os.path.getsize(output_path)} bytes, 1024x1024)")
