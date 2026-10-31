import json, os, urllib.request
from datetime import datetime, timezone
U = "bitWithKunal"
def api(p):
    h = {"User-Agent": U}
    if t := os.environ.get("GITHUB_TOKEN"): h["Authorization"] = f"Bearer {t}"
    try: return json.load(urllib.request.urlopen(urllib.request.Request("https://api.github.com/" + p, headers=h), timeout=20))
    except Exception: return None  # ponytail: skip live section if API is down
P = json.load(open("projects.json"))
star = lambda n: "★" * n + "☆" * (5 - n)
cats = list(dict.fromkeys(p["cat"] for p in P))
top = sorted(P, key=lambda p: -p["rating"])[:5]
def row(p):
    n = f"[**{p['name']}**]({p['url']})" if p.get("url") else f"**{p['name']}**"
    return f"| {n} | {p['desc']} | `{p['tech']}` | {star(p['rating'])} |"
tables = "\n".join(
    f"### {c}\n| Tool | What it does | Tech | Rating |\n|---|---|---|---|\n" +
    "\n".join(row(p) for p in sorted((p for p in P if p["cat"] == c), key=lambda p: -p["rating"])) + "\n"
    for c in cats)
techs = sorted({t.strip() for p in P for t in p["tech"].split("·")})
live = ""
ev = api(f"users/{U}/events/public")
if ev:
    live = "\n".join(f"- `{e['type'].replace('Event','')}` on **{e['repo']['name'].split('/')[1]}** · {e['created_at'][:10]}" for e in ev[:5])
u = api(f"users/{U}") or {}
now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
dark = "bg_color=0d1117&title_color=7aa2f7&text_color=c0caf5&icon_color=ff9e64&hide_border=true"
md = f"""<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=200&section=header&text=Kunal%20Saraswat&fontSize=52&fontColor=fff&animation=twinkling&desc=Physical%20Design%20Engineer%20%C2%B7%20Tool%20Builder&descSize=18&descAlignY=68" width="100%"/>

[![Typing](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=7AA2F7&center=true&vCenter=true&width=640&lines=Automation+over+repetition;Building+VLSI+%26+AI+engineering+tools;{len(P)}+tools+shipped+and+counting;Ship+it%2C+then+polish+it)](https://github.com/{U})

![Profile views](https://komarev.com/ghpvc/?username={U}&style=for-the-badge&color=7aa2f7&label=PROFILE+VIEWS)
![Followers](https://img.shields.io/github/followers/{U}?style=for-the-badge&color=bb9af7&logo=github)
![Tools](https://img.shields.io/badge/TOOLS-{len(P)}-ff9e64?style=for-the-badge)
![Avg rating](https://img.shields.io/badge/AVG_RATING-{sum(p['rating'] for p in P)/len(P):.1f}%2F5-1D9E75?style=for-the-badge)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kunalsaraswat/)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:kunalsaraswat30@gmail.com)

</div>

> I build **production-grade tools** for real engineering pain: VLSI physical design automation, browser-based editors, AI utilities. Most of my work lives in private repos, so this page is the showcase.

## 🏆 Top Rated
{chr(10).join(f"{i+1}. **{p['name']}** {star(p['rating'])} · {p['desc']}" for i, p in enumerate(top))}

## 🛠️ All Tools (ranked by rating)
{tables}
## 💻 Tech Stack
<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tcl](https://img.shields.io/badge/Tcl-E4CC98?style=for-the-badge&logoColor=black)
![Verilog](https://img.shields.io/badge/Verilog-8B8B8B?style=for-the-badge)
![Shell](https://img.shields.io/badge/Shell-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Batch](https://img.shields.io/badge/Batch-4EAA25?style=for-the-badge)
![Tkinter](https://img.shields.io/badge/Tkinter-FF6F00?style=for-the-badge)
![PyInstaller](https://img.shields.io/badge/PyInstaller-3776AB?style=for-the-badge)
![Inno Setup](https://img.shields.io/badge/Inno_Setup-264de4?style=for-the-badge)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Netlify](https://img.shields.io/badge/Netlify-00C7B7?style=for-the-badge&logo=netlify&logoColor=white)

</div>

## 📊 Live Stats
<div align="center">

![Stats](https://github-readme-stats.vercel.app/api?username={U}&show_icons=true&theme=radical&{dark}&count_private=true)
![Langs](https://github-readme-stats.vercel.app/api/top-langs/?username={U}&layout=compact&theme=radical&{dark})

![Streak](https://streak-stats.demolab.com?user={U}&theme=tokyonight&hide_border=true)

![Activity](https://github-readme-activity-graph.vercel.app/graph?username={U}&bg_color=0d1117&color=7aa2f7&line=ff9e64&point=bb9af7&area=true&area_color=7aa2f7&hide_border=true)

</div>

## ⚡ Recent Public Activity
{live or "_quiet lately, most work is private_"}

## 🧠 Philosophy
`Automation over repetition` · `Tools over scripts` · `Config-driven (JSON > hardcode)` · `Engineer-first UX` · `Ship it, then polish it`

## 🔜 Building Next
PD Master (unified PD dashboard) · UPF Tool · LogicVerse AI · TclForge v2 · Plugin system for web tools

<div align="center">
<sub>Auto-built {now} · {u.get('public_repos','?')} public repos · edit <code>projects.json</code> to change tools &amp; ratings</sub>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=100&section=footer" width="100%"/>
</div>
"""
open("README.md", "w").write(md)
