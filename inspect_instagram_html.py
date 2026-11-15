from pathlib import Path
import re
p=Path(r"C:\Users\user\AppData\Local\Temp\amreen_instagram_profile.html")
s=p.read_text(encoding="utf-8",errors="replace")
ids=["Dfug-TKSKzl","DftyC_7yDX4","DfrbBDeSn0C","Dfp1GYazrM3","DfnHp2fSJzE","DfmtpI1S5w-","DfmsAc5yFhn","DfmgPhqyMxi","DfmUBMky2gW"]
for ident in ids:
    i=s.find(ident)
    print("\n---",ident,"index",i,"---")
    if i<0: continue
    chunk=s[max(0,i-1600):i+2200]
    urls=re.findall(r'https?:\\?/\\?/[^"\\ ]+(?:cdninstagram|fbcdn)[^"\\ ]+',chunk)
    for u in urls[:8]: print(u[:600])
    for pat in [r'"thumbnail_url":"([^"]+)"',r'"display_url":"([^"]+)"',r'"src":"([^"]+)"',r'"accessibility_caption":"([^"]+)"']:
        m=re.search(pat,chunk)
        if m: print(pat, m.group(1)[:600])
    print(chunk[:500].replace("\n"," "))
