from pathlib import Path
root=Path(__file__).resolve().parent
cssp=root/"css"/"upgrade.css"
css=cssp.read_text(encoding="utf-8")
marker="/* End-of-page Instagram Reels carousel */"
if marker not in css: raise SystemExit("Could not find old carousel CSS block.")
css=css[:css.index(marker)]+"/* Full-width, continuous Instagram video marquee. No cards or slider controls. */\n.instagram-reels-panel{\n  position:relative;\n  margin:42px 0 22px;\n  padding:0;\n  border:0;\n  border-radius:0;\n  background:none;\n  box-shadow:none;\n}\n.instagram-reels-copy{\n  max-width:760px;\n  margin:0 auto;\n  text-align:center;\n}\n.instagram-reels-copy .mini-label{\n  display:inline-block;\n  margin-bottom:8px;\n  color:#f1a8bd;\n  font-size:9px;\n  font-weight:900;\n  letter-spacing:2.5px;\n}\n.instagram-reels-copy h3{\n  margin:0 0 8px;\n  color:#fff;\n  font:900 clamp(25px,3vw,36px)/1.08 var(--heading);\n  letter-spacing:-.9px;\n}\n.instagram-reels-copy p{\n  max-width:620px;\n  margin:0 auto;\n  color:rgba(255,255,255,.68);\n  font-size:12px;\n  line-height:1.6;\n}\n.instagram-profile-link{\n  display:inline-flex;\n  margin-top:11px;\n  color:#f5a7bc;\n  font-size:11px;\n  font-weight:850;\n  text-decoration:none;\n}\n.instagram-marquee{\n  position:relative;\n  width:100vw;\n  margin-left:calc(50% - 50vw);\n  overflow:hidden;\n  padding:7px 0 11px;\n  isolation:isolate;\n}\n.instagram-marquee::before,\n.instagram-marquee::after{\n  content:\"\";\n  position:absolute;\n  z-index:3;\n  top:0;\n  bottom:0;\n  width:clamp(24px,5vw,88px);\n  pointer-events:none;\n}\n.instagram-marquee::before{\n  left:0;\n  background:linear-gradient(90deg,#041329,rgba(4,19,41,0));\n}\n.instagram-marquee::after{\n  right:0;\n  background:linear-gradient(270deg,#05152e,rgba(5,21,46,0));\n}\n.instagram-marquee-track{\n  display:flex;\n  width:max-content;\n  transform:translate3d(-50%,0,0);\n  animation:instagram-videos-move-right 54s linear infinite;\n  will-change:transform;\n}\n.instagram-marquee-group{\n  display:flex;\n  flex:0 0 auto;\n  align-items:stretch;\n  gap:18px;\n  padding-right:18px;\n}\n.instagram-marquee-item{\n  position:relative;\n  display:block;\n  flex:0 0 clamp(190px,17vw,250px);\n  width:clamp(190px,17vw,250px);\n  aspect-ratio:9/16;\n  overflow:hidden;\n  border:0;\n  border-radius:12px;\n  background:#061225;\n  text-decoration:none;\n  cursor:pointer;\n}\n.instagram-marquee-item iframe{\n  position:absolute;\n  inset:0;\n  display:block;\n  width:100%;\n  height:100%;\n  border:0;\n  pointer-events:none;\n  background:#061225;\n}\n.instagram-marquee-item:focus-visible{\n  outline:3px solid #f5a7bc;\n  outline-offset:4px;\n}\n.instagram-marquee:hover .instagram-marquee-track,\n.instagram-marquee:focus-within .instagram-marquee-track{\n  animation-play-state:paused;\n}\n.instagram-reels-note{\n  margin:7px 0 0;\n  color:rgba(255,255,255,.43);\n  font-size:9px;\n  line-height:1.5;\n  text-align:center;\n}\n@keyframes instagram-videos-move-right{\n  from{transform:translate3d(-50%,0,0)}\n  to{transform:translate3d(0,0,0)}\n}\n@media(max-width:720px){\n  .instagram-reels-panel{margin:32px 0 18px}\n  .instagram-reels-copy{padding:0 8px}\n  .instagram-reels-copy h3{font-size:25px}\n  .instagram-reels-copy p{font-size:11px}\n  .instagram-marquee-track{animation-duration:44s}\n  .instagram-marquee-group{gap:13px;padding-right:13px}\n  .instagram-marquee-item{flex-basis:190px;width:190px}\n}\n@media(max-width:420px){\n  .instagram-marquee-track{animation-duration:39s}\n  .instagram-marquee-item{flex-basis:170px;width:170px}\n}\n@media(prefers-reduced-motion:reduce){\n  .instagram-marquee{overflow-x:auto}\n  .instagram-marquee-track{animation:none;transform:none}\n  .instagram-marquee-group[aria-hidden=\"true\"]{display:none}\n}\n"
cssp.write_text(css,encoding="utf-8")

jsp=root/"js"/"upgrade.js"
js=jsp.read_text(encoding="utf-8")
js_marker="  // Horizontal Instagram Reel carousel."
if js_marker in js:
    i=js.index(js_marker)
    j=js.index("})();",i)
    js=js[:i]+js[j:]
jsp.write_text(js,encoding="utf-8")

hp=root/"index.html"
html=hp.read_text(encoding="utf-8-sig")
html=html.replace("homepage-reels-20261115-1","reels-marquee-right-20261115-1")
hp.write_text(html,encoding="utf-8-sig")
print("Removed card carousel CSS.")
print("Added edge-to-edge continuous marquee CSS moving left-to-right.")
print("Removed arrow-scroll JavaScript.")
print("Updated stylesheet cache version.")
