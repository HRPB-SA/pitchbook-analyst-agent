#!/usr/bin/env python3
"""
Build the PitchBook x Madrona fireside deck (LIGHT PitchBook template):
"Durability, IPOs and the Duopoly Myth" (Segments 1, 3, 4).

Light navy/gold/cream house style. Adds the full 19-vertical duopoly map
(named companies) plus the "what is actually interesting" analysis. Charts are
matplotlib PNGs (light, transparent). Databricks reflects the $188B strategic
round (term sheet Jul 16 2026, Coatue). The deck is verified via an HTML mirror
render (LibreOffice conversion is unavailable in this environment).

Run:  python3 build/fireside_deck.py
Out:  output/Fireside_Durability_IPOs_Duopoly_Jul2026.pptx
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, "build", "deck_charts")
os.makedirs(CH, exist_ok=True)
OUT = os.path.join(ROOT, "output", "Fireside_Durability_IPOs_Duopoly_Jul2026.pptx")

# ---------------- palette (light PitchBook) ----------------
CREAM  = "#f7f4ed"   # page
PANEL  = "#ffffff"
CARD   = "#fbf9f3"
NAVY   = "#152a4d"   # ink / headers
NAVY2  = "#1f3a66"
INK2   = "#48546e"
MUTED  = "#8b8676"
BORDER = "#ddd6c8"
GOLD   = "#e2a413"   # accent
GOLD_L = "#efd79a"   # light arc
POS    = "#1a7a3c"
NEG    = "#c0392f"
# validated categorical (light surface) - NAVY is chrome only, not a series hue
S1 = "#2a78d6"  # blue
S2 = "#1c7d3f"  # green
S4 = "#d99400"  # yellow/gold-ish
S5 = "#1baf7a"  # aqua
S6 = "#e0643a"  # orange
GRID = "#e7e2d6"
AXIS = "#cfc9ba"

def hx(c): return RGBColor.from_string(c.lstrip("#"))

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 13, "text.color": NAVY,
    "axes.edgecolor": AXIS, "axes.labelcolor": INK2,
    "xtick.color": MUTED, "ytick.color": INK2,
    "figure.dpi": 200, "savefig.dpi": 200,
})

def newfig(w, h):
    f = plt.figure(figsize=(w, h)); f.patch.set_alpha(0); return f
def styleax(ax):
    ax.set_facecolor("none")
    for s in ax.spines.values(): s.set_visible(False)
    ax.tick_params(length=0); return ax
def save(fig, name):
    p = os.path.join(CH, name)
    fig.savefig(p, transparent=True, bbox_inches="tight", pad_inches=0.06)
    plt.close(fig); return p

# ============================================================
# CHARTS  (light)
# ============================================================
def c_ia40():
    fig = newfig(9.2, 3.0); ax = styleax(fig.add_subplot(111))
    ax.barh([1.6],[27],height=0.5,color=S1,zorder=3)
    ax.barh([1.6],[13],left=[27],height=0.5,color=S4,zorder=3)
    ax.text(27/2,1.6,"27",ha="center",va="center",color="#fff",fontweight="bold",fontsize=13)
    ax.text(27+13/2,1.6,"13",ha="center",va="center",color="#fff",fontweight="bold",fontsize=13)
    ax.text(0,2.05,"2025 IA40 cohort: 40 winners",color=NAVY,fontsize=12.5,fontweight="bold")
    ax.text(40,2.05,"~50% replaced each year",color=MUTED,ha="right",fontsize=11)
    ax.barh([0.7],[4],height=0.34,color=S5,zorder=3)
    ax.text(4.4,0.7,"4  (Abnormal, Databricks, Hugging Face, Runway)",va="center",color=NAVY,fontsize=11)
    ax.text(0,0.98,"Made all 4 lists, 2021 to 2024",color=INK2,fontsize=10.5)
    ax.barh([0.0],[1],height=0.34,color=S2,zorder=3)
    ax.text(1.4,0.0,"1  (Databricks)",va="center",color=NAVY,fontsize=11,fontweight="bold")
    ax.text(0,0.28,"Made all 5 lists, 2021 to 2025",color=INK2,fontsize=10.5)
    ax.set_xlim(0,40); ax.set_ylim(-0.35,2.3); ax.set_xticks([]); ax.set_yticks([])
    return save(fig,"ia40.png")

def c_split():
    fig = newfig(9.2,2.5); ax = styleax(fig.add_subplot(111))
    rows=[("Share of deals\n1,603 deals",[("Horizontal",26.5,S1),("Vertical",63.8,S5),("Other",9.7,"#e5e0d3")]),
          ("Share of capital\n$73.6B",[("Horizontal",70,S1),("Vertical",26,S5),("Other",4,"#e5e0d3")])]
    for i,(lab,segs) in enumerate(rows):
        x=0
        for nm,v,c in segs:
            ax.barh([i],[v],left=[x],height=0.5,color=c,zorder=3)
            if v>12: ax.text(x+v/2,i,f"{round(v)}%",ha="center",va="center",
                             color="#fff" if nm!="Other" else INK2,fontweight="bold",fontsize=12)
            x+=v
        ax.text(-2,i,lab,ha="right",va="center",color=NAVY,fontsize=11,fontweight="bold")
    ax.set_xlim(0,100); ax.set_ylim(-0.5,1.5); ax.set_xticks([]); ax.set_yticks([])
    return save(fig,"split.png")

def c_spacex():
    fig = newfig(9.2,2.6); ax = styleax(fig.add_subplot(111))
    data=[("SpaceX, first-day market cap  (Jun 12 2026)",2100,S6),
          ("All US VC-backed IPOs since 2016  (combined)",1500,S1),
          ("US IPO proceeds, full-year 2025  (all sectors)",45,MUTED)]
    for i,(lab,v,c) in enumerate(data):
        ax.barh([i],[v],height=0.46,color=c,zorder=3)
        ax.text(v+30,i,f"${v/1000:.2f}T" if v>=1000 else f"${v}B",va="center",color=NAVY,fontsize=12.5,fontweight="bold")
        ax.text(0,i+0.36,lab,va="center",color=INK2,fontsize=11)
    for g in [0,500,1000,1500,2000]:
        ax.axvline(g,color=GRID,lw=1,zorder=0)
        ax.text(g,-0.75,f"${g/1000:.1f}T".replace(".0T","T"),ha="center",color=MUTED,fontsize=9.5)
    ax.invert_yaxis(); ax.set_xlim(0,2300); ax.set_ylim(2.7,-0.7); ax.set_xticks([]); ax.set_yticks([])
    return save(fig,"spacex.png")

def c_logline(name,pts,color,lo,hi,dashed_to=None,dashed_lab=None):
    fig=newfig(9.2,3.1); ax=styleax(fig.add_subplot(111))
    xs=np.arange(len(pts)); ys=[p[1] for p in pts]; ax.set_yscale("log")
    ax.plot(xs,ys,color=color,lw=2.6,zorder=3,solid_capstyle="round")
    ax.scatter(xs,ys,s=46,color=color,zorder=4,edgecolors=CREAM,linewidths=2)
    for i,(xl,v,show) in enumerate(pts):
        if show:
            vt=(f"${v/1000:.2f}T" if v>=1000 else (f"${v:g}B" if v>=1 else f"${round(v*1000)}M"))
            ax.annotate(vt,(xs[i],ys[i]),textcoords="offset points",xytext=(0,11),ha="center",color=NAVY,fontsize=12,fontweight="bold")
    if dashed_to is not None:
        ax.plot([xs[-1],xs[-1]+0.9],[ys[-1],dashed_to],color=GOLD,lw=2.4,ls=(0,(3,3)),zorder=3)
        ax.scatter([xs[-1]+0.9],[dashed_to],s=54,color=GOLD,zorder=4,edgecolors=CREAM,linewidths=2)
        vt=f"${dashed_to/1000:.2f}T" if dashed_to>=1000 else f"${dashed_to:g}B"
        ax.annotate(vt,(xs[-1]+0.9,dashed_to),textcoords="offset points",xytext=(6,10),ha="left",color="#b5820c",fontsize=12.5,fontweight="bold")
        if dashed_lab:
            ax.annotate(dashed_lab,(xs[-1]+0.9,dashed_to),textcoords="offset points",xytext=(2,-20),ha="center",color=MUTED,fontsize=9.5)
    ax.set_xticks(xs); ax.set_xticklabels([p[0] for p in pts],fontsize=10.5,color=MUTED)
    ax.set_xlim(-0.4,len(pts)-0.1+(1.4 if dashed_to else 0.2)); ax.set_ylim(lo,hi)
    ax.grid(axis="y",color=GRID,lw=1)
    ticks=[t for t in [0.1,1,10,100,1000] if lo<=t<=hi]; ax.set_yticks(ticks)
    ax.set_yticklabels([(f"${int(t/1000)}T" if t>=1000 else (f"${int(t)}B" if t>=1 else f"${int(t*1000)}M")) for t in ticks],fontsize=10.5,color=INK2)
    ax.tick_params(axis="y",length=0); return save(fig,name)

def c_dbx():
    pts=[("'13",0.047,False),("'14",0.923,False),("'16",0.56,False),("'18",0.985,False),
         ("'19",2.75,False),("'19",6.2,False),("'21",28,False),("'21",38,False),
         ("'23",43.2,True),("'24",62,False),("'25",100,False),("'26",134,True)]
    return c_logline("dbx.png",pts,S1,0.04,320,dashed_to=188,dashed_lab="term sheet, Jul 2026")
def c_anth():
    pts=[("Jan24",0.087,True),("Dec24",1,False),("'25",9,False),("Feb26",14,False),("Apr26",30,False),("May26",47,True)]
    return c_logline("anth.png",pts,S2,0.07,90)

def c_ratio():
    data=[("Formal math","Axiom / Harmonic",1.10),("Foundation models","Anthropic / OpenAI",1.13),
          ("Legal AI","Harvey / Legora",2.0),("AI inference chips","Cerebras / Groq",2.0),
          ("AI coding","Cursor / Cognition",2.3),("Defense AI","Anduril / Helsing",3.4),
          ("Customer support","Sierra / Decagon",3.5),("Healthcare scribes","Abridge / Ambience",4.2),
          ("AI recruiting","Mercor / Eightfold",4.8),("Humanoid robotics","Figure / Physical Intel.",7.2),
          ("AI web search","Perplexity / Exa",9.1),("Enterprise search","Glean / Hebbia",10.3),
          ("Video generation","Runway / Pika",11.0),("Meeting notetakers","Granola / Otter",16.0),
          ("Sales / GTM","Clay / Artisan",20.0),("Voice AI","ElevenLabs / Cartesia",61.0)]
    fig=newfig(9.4,5.0); ax=styleax(fig.add_subplot(111)); ax.set_xscale("log")
    ys=np.arange(len(data))[::-1]
    for i,(v,pair,r) in enumerate(data):
        c=S2 if r<1.5 else (S6 if r>10 else S1)
        ax.barh([ys[i]],[r-1],left=[1],height=0.62,color=c,zorder=3)
        ax.text(r*1.05,ys[i],f"{r:.1f}x" if r<10 else f"{r:.0f}x",va="center",color=NAVY,fontsize=11,fontweight="bold")
        ax.text(0.92,ys[i],v,va="center",ha="right",color=NAVY,fontsize=11)
    for g,lab,em in [(1,"1x",0),(2,"2x",1),(5,"5x",0),(10,"10x",1),(20,"20x",0),(40,"40x",0),(80,"80x",0)]:
        ax.axvline(g,color=(AXIS if em else GRID),lw=1,ls=("--" if em else "-"),zorder=0)
        ax.text(g,-1.1,lab,ha="center",color=MUTED,fontsize=9.5)
    ax.set_xlim(0.85,95); ax.set_ylim(-1.6,len(data)-0.3); ax.set_xticks([]); ax.set_yticks([])
    return save(fig,"ratio.png")

def c_fund():
    fig=newfig(9.2,3.2); ax=styleax(fig.add_subplot(111))
    groups=[("Data labeling",[("Scale AI",29,1.0,False,False),("Surge AI",0,1.4,True,False)]),
            ("Meeting notes",[("Granola",1.5,0,False,True),("Otter.ai",0.094,0.1,False,False)])]
    maxv=29
    def bw(v): return 0 if v<=0 else max(np.sqrt(v)/np.sqrt(maxv),0.01)
    y=0
    for g,items in groups:
        ax.text(-0.02,y+0.5,g,color=NAVY2,fontsize=11,fontweight="bold",ha="left"); y-=1
        for nm,val,rev,novc,norev in items:
            ax.barh([y],[bw(val)],height=0.34,color=S1,zorder=3)
            if novc: ax.text(0.01,y,"no VC valuation",va="center",color=MUTED,fontsize=9.5)
            else: ax.text(bw(val)+0.012,y,f"${val:g}B" if val>=1 else f"${round(val*1000)}M",va="center",color=NAVY,fontsize=10.5,fontweight="bold")
            ax.barh([y-0.42],[bw(rev)],height=0.34,color=S2,zorder=3)
            if norev: ax.text(0.01,y-0.42,"revenue undisclosed",va="center",color=MUTED,fontsize=9.5)
            else: ax.text(bw(rev)+0.012,y-0.42,f"${rev:g}B" if rev>=1 else f"${round(rev*1000)}M",va="center",color=NAVY,fontsize=10.5,fontweight="bold")
            ax.text(-0.02,y-0.21,nm,va="center",ha="right",color=NAVY,fontsize=11,fontweight="bold"); y-=1.15
        y-=0.35
    ax.set_xlim(-0.16,1.15); ax.set_ylim(y+0.5,1.1); ax.set_xticks([]); ax.set_yticks([])
    return save(fig,"fund.png")

def c_matrix():
    funds=["a16z","Nvidia","Sequoia","Kleiner P.","Gen. Catalyst"]
    verts=["Legal","Health\nscribes","Coding","Ent.\nsearch","Voice","Formal\nmath","Defense"]
    M={(0,0):3,(0,1):3,(0,2):1,(0,4):1,(0,6):1,(1,0):2,(1,2):1,
       (2,0):1,(2,3):1,(2,4):1,(2,5):2,(3,0):1,(3,3):1,(3,5):2,(4,0):2,(4,2):2,(4,3):1}
    fig=newfig(9.2,3.4); ax=styleax(fig.add_subplot(111)); nr,nc=len(funds),len(verts)
    for i in range(nr+1): ax.axhline(i-0.5,color=GRID,lw=1)
    for j in range(nc+1): ax.axvline(j-0.5,color=GRID,lw=1)
    for (r,c),v in M.items():
        yy=nr-1-r
        if v in (1,3): ax.scatter([c],[yy],s=150,color=NAVY,zorder=3)
        if v in (2,3): ax.scatter([c],[yy],s=215,facecolors="none",edgecolors=GOLD,linewidths=2.6,zorder=4)
    ax.set_xticks(range(nc)); ax.set_xticklabels(verts,fontsize=10,color=INK2)
    ax.set_yticks(range(nr)); ax.set_yticklabels(funds[::-1],fontsize=11,color=NAVY,fontweight="bold")
    ax.xaxis.set_ticks_position("top"); ax.tick_params(length=0)
    ax.set_xlim(-0.5,nc-0.5); ax.set_ylim(-0.5,nr-0.5); return save(fig,"matrix.png")

print("Rendering charts...")
c_ia40(); c_split(); c_spacex(); c_dbx(); c_anth(); c_ratio(); c_fund(); c_matrix()
FIG_IA40=os.path.join(CH,"ia40.png"); FIG_SPLIT=os.path.join(CH,"split.png")
FIG_SPACEX=os.path.join(CH,"spacex.png"); FIG_DBX=os.path.join(CH,"dbx.png")
FIG_ANTH=os.path.join(CH,"anth.png"); FIG_RATIO=os.path.join(CH,"ratio.png")
FIG_FUND=os.path.join(CH,"fund.png"); FIG_MATRIX=os.path.join(CH,"matrix.png")

# ============================================================
# DECK
# ============================================================
prs = Presentation(); prs.slide_width=Inches(13.333); prs.slide_height=Inches(7.5)
BLANK=prs.slide_layouts[6]; SW,SH=prs.slide_width,prs.slide_height
PXI=96.0; HTML_SLIDES=[]
def _h(x): HTML_SLIDES[-1].append(x)
MONO="Consolas"; SANS="Arial"

def slide(bg=CREAM):
    s=prs.slides.add_slide(BLANK)
    r=s.shapes.add_shape(MSO_SHAPE.RECTANGLE,0,0,SW,SH)
    r.fill.solid(); r.fill.fore_color.rgb=hx(bg); r.line.fill.background(); r.shadow.inherit=False
    HTML_SLIDES.append([f'<div class="slide" style="background:{bg}">'])
    return s

def box(s,l,t,w,h,fill=None,line=None,lw=1.0,rad=False):
    shp=s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if rad else MSO_SHAPE.RECTANGLE,
                           Inches(l),Inches(t),Inches(w),Inches(h))
    if fill: shp.fill.solid(); shp.fill.fore_color.rgb=hx(fill)
    else: shp.fill.background()
    if line: shp.line.color.rgb=hx(line); shp.line.width=Pt(lw)
    else: shp.line.fill.background()
    shp.shadow.inherit=False
    st=(f'position:absolute;left:{l*PXI}px;top:{t*PXI}px;width:{w*PXI}px;height:{h*PXI}px;'
        f'{"background:"+fill+";" if fill else ""}{"border:"+str(lw)+"px solid "+line+";" if line else ""}'
        f'{"border-radius:9px;" if rad else ""}box-sizing:border-box;')
    _h(f'<div style="{st}"></div>'); return shp

def circle_outline(s,cx,cy,r,color,lw):
    shp=s.shapes.add_shape(MSO_SHAPE.OVAL,Inches(cx-r),Inches(cy-r),Inches(2*r),Inches(2*r))
    shp.fill.background(); shp.line.color.rgb=hx(color); shp.line.width=Pt(lw); shp.shadow.inherit=False
    _h(f'<div style="position:absolute;left:{(cx-r)*PXI}px;top:{(cy-r)*PXI}px;width:{2*r*PXI}px;'
       f'height:{2*r*PXI}px;border:{lw}px solid {color};border-radius:50%;box-sizing:border-box"></div>')

def arcs(s,dark=False):
    col = "#2a4a7a" if dark else GOLD_L
    cx,cy=(SW/914400),(SH/914400)  # bottom-right corner in inches
    for r in ([1.0,1.7,2.4] if not dark else [1.4,2.2,3.0,3.8]):
        circle_outline(s,cx,cy,r,col,1.25)

def text(s,l,t,w,h,runs,align=PP_ALIGN.LEFT,anchor=MSO_ANCHOR.TOP,sp_after=4,line_sp=1.0):
    tb=s.shapes.add_textbox(Inches(l),Inches(t),Inches(w),Inches(h)); tf=tb.text_frame
    tf.word_wrap=True; tf.vertical_anchor=anchor
    tf.margin_left=0; tf.margin_right=0; tf.margin_top=0; tf.margin_bottom=0
    if isinstance(runs[0],tuple): runs=[runs]
    al={PP_ALIGN.LEFT:"left",PP_ALIGN.CENTER:"center",PP_ALIGN.RIGHT:"right"}[align]
    va={MSO_ANCHOR.TOP:"flex-start",MSO_ANCHOR.MIDDLE:"center",MSO_ANCHOR.BOTTOM:"flex-end"}[anchor]
    parts=[]
    for i,para in enumerate(runs):
        p=tf.paragraphs[0] if i==0 else tf.add_paragraph()
        p.alignment=align; p.space_after=Pt(sp_after); p.space_before=Pt(0); p.line_spacing=line_sp
        spans=[]
        for rr in para:
            txt,sz,col,bold=rr[0],rr[1],rr[2],rr[3]
            font=rr[4] if len(rr)>4 else None; spc=rr[5] if len(rr)>5 else None
            run=p.add_run(); run.text=txt; f=run.font
            f.size=Pt(sz); f.color.rgb=hx(col); f.bold=bold; f.name=font or "Arial"
            if spc is not None:
                rPr=run._r.get_or_add_rPr(); rPr.set("spc",str(int(spc*100)))
            fam="ui-monospace,Consolas,monospace" if font=="Consolas" else "Arial,system-ui,sans-serif"
            ls=f"letter-spacing:{spc}em;" if spc else ""
            esc=(txt if txt else " ").replace("&","&amp;").replace("<","&lt;")
            spans.append(f'<span style="font-size:{sz}px;color:{col};font-weight:{700 if bold else 400};font-family:{fam};{ls}">{esc}</span>')
        parts.append(f'<div style="margin:0 0 {sp_after}px;line-height:{line_sp};text-align:{al}">'+"".join(spans)+'</div>')
    st=(f'position:absolute;left:{l*PXI}px;top:{t*PXI}px;width:{w*PXI}px;height:{h*PXI}px;'
        f'display:flex;flex-direction:column;justify-content:{va};box-sizing:border-box;overflow:visible;')
    _h(f'<div style="{st}">'+"".join(parts)+'</div>'); return tb

def pic(s,path,l,t,w=None,h=None):
    p=s.shapes.add_picture(path,Inches(l),Inches(t),Inches(w) if w else None,Inches(h) if h else None)
    ww=(w*PXI) if w else (p.width/914400*PXI)
    _h(f'<img src="{os.path.basename(path)}" style="position:absolute;left:{l*PXI}px;top:{t*PXI}px;width:{ww}px"/>')
    return p

def chart_panel(s,path,l,t,w,h,border=True):
    box(s,l-0.15,t-0.15,w+0.3,h+0.3,fill=PANEL,line=BORDER if border else None,lw=1,rad=True)
    from PIL import Image
    iw,ih=Image.open(path).size; ar=iw/ih; pw,ph=w,h
    if pw/ph>ar: pw=ph*ar
    else: ph=pw/ar
    pic(s,path,l+(w-pw)/2,t+(h-ph)/2,w=pw)

def eyebrow(s,l,t,txt,col=GOLD):
    text(s,l,t,11,0.3,[[(txt,12,col,True,MONO,0.2)]])
def logo(s,l=0.62,t=6.98):
    text(s,l,t,6,0.3,[[("PitchBook",12,NAVY,True,SANS),("  with Madrona",12,MUTED,False,SANS)]])
def footer(s,n):
    box(s,0.6,7.0,12.13,0.014,fill=BORDER)
    text(s,0.6,7.12,7,0.3,[[("PitchBook, a Morningstar company  .  with Madrona",9,MUTED,False,SANS)]])
    text(s,10.8,7.12,1.9,0.3,[[(f"CONFIDENTIAL . {n:02d}",9,MUTED,False,SANS)]],align=PP_ALIGN.RIGHT)
def segno(s,l,t,txt):
    box(s,l,t,1.05,0.42,fill=NAVY,rad=True)
    text(s,l,t,1.05,0.42,[[(txt,12,GOLD,True,MONO)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
def htitle(s,l,t,w,parts):
    text(s,l,t,w,1.2,[parts])

N=[0]
def num(): N[0]+=1; return N[0]

def content(seg,fig=None):
    s=slide(); arcs(s); logo(s); footer(s,num())
    return s

# ---------- 1 TITLE ----------
s=slide(NAVY); arcs(s,dark=True)
box(s,0,0,0.22,7.5,fill=GOLD)
text(s,0.75,0.55,8,0.4,[[("PitchBook",15,"#ffffff",True,SANS),("  x  ",15,"#8aa0c4",False,SANS),("Madrona",15,"#ffffff",True,SANS)]])
text(s,0.75,0.6,11.8,0.4,[[("LIVE",10.5,"#f4b23e",True,MONO,0.16),("  PODCAST RECORDING",10.5,"#8aa0c4",False,MONO,0.16)]],align=PP_ALIGN.RIGHT)
text(s,0.78,2.35,10.4,2.2,[[("Durability, IPOs,",50,"#ffffff",True,SANS)],[("and the Duopoly Myth",50,"#f4c65a",True,SANS)]],line_sp=1.02)
box(s,0.82,4.35,2.1,0.045,fill=GOLD)
text(s,0.82,4.6,10.6,1.3,[[("A late-stage private-company research brief: what makes an AI startup ",18,"#d7deea",False,SANS)],
    [("defensible, why the biggest companies stay private, and whether ",18,"#d7deea",False,SANS)],
    [("\"two winners per category\" is a real pattern or a counting error.",18,"#d7deea",False,SANS)]],line_sp=1.1)
text(s,0.82,6.5,12,0.4,[[("Segments 01 . 03 . 04",12,"#f4b23e",True,MONO,0.06),("      Prepared July 17, 2026      Sources: PitchBook Premium and named press",12,"#8aa0c4",False,MONO,0.03)]])

# ---------- 2 AGENDA ----------
s=content("agenda")
eyebrow(s,0.6,1.0,"THE RUNDOWN")
htitle(s,0.6,1.36,12,[("Three corrections to how the market talks",32,NAVY,True,SANS)])
items=[("01","Durability","Defensibility is measurable, and the exit predictor already keeps a history you can chart. The IA40's churn is the signal.",GOLD),
       ("03","AI IPOs","Not a drought, a backlog. 945 unicorns worth $5.3T sit private because capital is cheap and one listing now dwarfs a decade.",GOLD),
       ("04","The Duopoly","It is winner-take-most, miscounted. Count the business, not the round, and the second name usually disappears.",GOLD)]
x=0.6
for n,h,d,c in items:
    box(s,x,2.55,3.85,3.5,fill=PANEL,line=BORDER,lw=1,rad=True)
    box(s,x,2.55,3.85,0.12,fill=GOLD)
    text(s,x+0.34,2.9,1.6,0.8,[[(n,38,NAVY,True,SANS)]])
    text(s,x+0.34,3.85,3.2,0.5,[[(h,20,NAVY,True,SANS)]])
    text(s,x+0.34,4.5,3.25,1.5,[[(d,13.5,INK2,False,SANS)]],line_sp=1.08)
    x+=4.06
text(s,0.6,6.35,12,0.3,[[("Segment 02 (market structure) is out of scope for this brief.",11,MUTED,False,SANS)]])

# ---------- 3 SEG 1 DIVIDER ----------
s=content("d1"); segno(s,0.6,3.0,"SEG 01")
eyebrow(s,0.6,3.62,"WHAT DOES THE DATA SHOW ON DURABILITY?")
htitle(s,0.6,4.0,12.4,[("Defensibility is measurable, and the tool has a memory",38,NAVY,True,SANS)])

# ---------- 4 VCEP KPIs ----------
s=content("vcep")
eyebrow(s,0.6,1.0,"SEG 01 . THE EXIT PREDICTOR")
htitle(s,0.6,1.35,12.1,[("Does PitchBook's exit predictor keep history? Yes.",30,NAVY,True,SANS)])
text(s,0.6,2.25,12.1,0.8,[[("Every scored company carries a Historical Predictions chart: success, IPO and M&A probability tracked over time, with financing rounds overlaid. The compelling angle is on the table.",15,INK2,False,SANS)]],line_sp=1.05)
kp=[("EXIT PREDICTOR KEEPS HISTORY","Yes",POS,"Per-company time series on every profile"),
    ("SUCCESS VS NO-EXIT ACCURACY","71%",NAVY,"Out-of-sample"),
    ("M&A VS IPO ACCURACY","94%",NAVY,"Given a successful exit"),
    ("IA40 TURNOVER PER YEAR","~50%",NAVY,"27 first-time winners in 2025"),
    ("NAMES ON ALL FIVE IA40 LISTS","1",GOLD,"Databricks, only")]
x=0.6; w=2.42
for l,v,c,d in kp:
    box(s,x,3.4,w-0.12,2.5,fill=PANEL,line=BORDER,lw=1,rad=True)
    text(s,x+0.25,3.65,w-0.5,0.9,[[(l,10,MUTED,True,SANS,0.02)]],line_sp=1.0)
    text(s,x+0.25,4.55,w-0.5,0.8,[[(v,38,c,True,SANS)]])
    text(s,x+0.25,5.35,w-0.5,0.5,[[(d,11,INK2,False,SANS)]],line_sp=1.0)
    x+=w
text(s,0.6,6.1,12,0.3,[[("Caveat: the productized time series is per-company. A vertical-wide trend is a cohort pull, not a built-in view.",11,MUTED,False,SANS)]])

# ---------- 5 IA40 ----------
s=content("ia40")
eyebrow(s,0.6,1.0,"SEG 01 . FIG 1")
htitle(s,0.6,1.35,12.1,[("IA40 staying power is rare: churn is the durability signal",25,NAVY,True,SANS)])
chart_panel(s,FIG_IA40,0.6,2.3,8.1,3.9)
text(s,9.05,2.5,3.7,4,[[("2025 was the fifth annual list.",15,NAVY,True,SANS)],
    [("Roughly half the cohort is replaced every year. Of the four names that made all four lists through 2024, only Databricks carried into 2025, the sole five-time winner.",13.5,INK2,False,SANS)],
    [("Application-layer names rotate out; the infrastructure layer compounds.",13.5,NAVY,True,SANS)]],line_sp=1.08,sp_after=10)
text(s,0.6,6.4,12,0.3,[[("Source: Madrona / PitchBook IA40 (ia40.com), 2025 edition. Methodology uses the VC Exit Predictor Opportunity Score as an input.",10,MUTED,False,SANS)]])

# ---------- 6 split + last mile ----------
s=content("split")
eyebrow(s,0.6,1.0,"SEG 01 . FIG 2")
htitle(s,0.6,1.35,12.1,[("The last mile, priced in dollars",25,NAVY,True,SANS)])
chart_panel(s,FIG_SPLIT,0.6,2.15,7.2,2.5)
text(s,0.6,4.95,7.4,1.5,[[("Q1 2025 set a record for AI/ML venture at $73.6B across 1,603 deals. Vertical apps were ~60% of the deals but under a third of the capital: many small bets. A vertical model costs ~$3M to $10M to build; a horizontal LLM costs hundreds of millions.",13,INK2,False,SANS)]],line_sp=1.08)
box(s,8.2,2.15,4.5,2.0,fill=PANEL,line=NEG,lw=1.25,rad=True)
text(s,8.45,2.32,4,0.4,[[("SHORT LAST MILE",10.5,NEG,True,MONO,0.1)]])
text(s,8.45,2.68,4.1,1.4,[[("Absorbed by the frontier: little between the model and the outcome. ",12.5,INK2,False,SANS),("Copy, images, coding assistants, first-pass drafts.",12.5,NAVY,True,SANS)]],line_sp=1.05)
box(s,8.2,4.3,4.5,2.15,fill=PANEL,line=POS,lw=1.25,rad=True)
text(s,8.45,4.47,4,0.4,[[("LONG LAST MILE",10.5,POS,True,MONO,0.1)]])
text(s,8.45,4.83,4.1,1.5,[[("Regulation and liability sit between model and outcome. ",12.5,INK2,False,SANS),("Tax filing, audit-ready accounting, licensed healthcare. Owning liability is insurance pricing.",12.5,NAVY,True,SANS)]],line_sp=1.05)
text(s,0.6,6.55,12,0.3,[[("Source: PitchBook Q1 2025 AI & ML VC Trends; framework: N. Bobba, Better Tomorrow Ventures (Feb 2026), not Madrona / Sabrina Wu.",10,MUTED,False,SANS)]])

# ---------- 7 SEG 3 DIVIDER ----------
s=content("d3"); segno(s,0.6,3.0,"SEG 03")
eyebrow(s,0.6,3.62,"STATE OF AI IPOs")
htitle(s,0.6,4.0,12.4,[("The drought is a mirage. The value is real, just private",38,NAVY,True,SANS)])

# ---------- 8 backlog KPIs ----------
s=content("backlog")
eyebrow(s,0.6,1.0,"SEG 03 . THE PRIVATE BACKLOG")
htitle(s,0.6,1.35,12.1,[("There is no shortage of exit-scale companies",28,NAVY,True,SANS)])
kp=[("ACTIVE US UNICORNS","945","Record, Q2 2026",NAVY),
    ("AGGREGATE UNICORN VALUE","$5.3T","+9.4% vs year-end 2025",NAVY),
    ("HELD BY SPACEX, OPENAI, ANTHROPIC",">25%","Three names, a quarter of the herd",NAVY),
    ("2025 UNICORN IPOs","17","14 priced below their mark",NEG),
    ("LP CASH OUT > CASH BACK","4 yrs","Distributions have trailed",NAVY)]
x=0.6; w=2.42
for l,v,d,c in kp:
    box(s,x,2.55,w-0.12,2.55,fill=PANEL,line=BORDER,lw=1,rad=True)
    text(s,x+0.22,2.8,w-0.42,0.95,[[(l,9.5,MUTED,True,SANS,0.02)]],line_sp=1.0)
    text(s,x+0.22,3.78,w-0.42,0.8,[[(v,34,c,True,SANS)]])
    text(s,x+0.22,4.5,w-0.42,0.5,[[(d,10.5,INK2,False,SANS)]],line_sp=1.0)
    x+=w
text(s,0.6,5.4,12.1,1.2,[[("The backlog is a liquidity choice, not an absence of exits. Mega-rounds plus secondary markets (annualized ~$112B in Q1 2026) let companies stay private while an IPO is telegraphed. ~30% of unicorns are AI-native or AI-adjacent.",15,INK2,False,SANS)]],line_sp=1.1)

# ---------- 9 spacex ----------
s=content("spacex")
eyebrow(s,0.6,1.0,"SEG 03 . FIG 3")
htitle(s,0.6,1.35,12.2,[("One listing versus a decade of the asset class",25,NAVY,True,SANS)])
chart_panel(s,FIG_SPACEX,0.6,2.25,8.0,3.5)
text(s,8.95,2.5,3.8,4,[[("SpaceX priced at a $1.78T valuation and closed day one near $2.1T.",16,NAVY,True,SANS)],
    [("That single number exceeds the combined value of every US venture-backed public listing since 2016.",13.5,INK2,False,SANS)],
    [("\"IPO drought\" is the wrong frame: the pipe is holding a few objects too large to move.",13.5,NAVY,True,SANS)]],line_sp=1.08,sp_after=10)
text(s,0.6,6.15,12,0.3,[[("Source: PitchBook Q2 2026 Venture Monitor; CNBC Jun 12 2026. The looser \"half of every tech IPO since the internet\" claim is not sourceable; this is the verifiable version.",10,MUTED,False,SANS)]])

# ---------- 10 databricks ----------
s=content("dbx")
eyebrow(s,0.6,1.0,"SEG 03 . FIG 4")
htitle(s,0.6,1.35,12.2,[("Databricks: a $47M to $188B climb, still private",25,NAVY,True,SANS)])
chart_panel(s,FIG_DBX,0.6,2.25,8.0,3.7)
text(s,8.95,2.5,3.85,4,[[("NEW: $188B strategic round.",15.5,"#b5820c",True,SANS)],
    [("Term sheet signed July 16 2026, led by Coatue, expected to close this summer, up from the $134B Series L (Feb 2026).",13.5,INK2,False,SANS)],
    [("Why raise at this scale? Private capital is cheap and CEO Ali Ghodsi called 2026 \"a terrible year to go public.\" The company never needed the exit.",13.5,NAVY,False,SANS)]],line_sp=1.06,sp_after=10)
text(s,0.6,6.25,12,0.3,[[("Source: Databricks newsroom & Bloomberg, Jul 16-17 2026 ($188B term sheet); PitchBook Premium financing records (entity 59199-40). $134B is the last closed round.",10,MUTED,False,SANS)]])

# ---------- 11 anthropic ----------
s=content("anth")
eyebrow(s,0.6,1.0,"SEG 03 . FIG 5")
htitle(s,0.6,1.35,12.2,[("Anthropic: the revenue the IPO is timed around",25,NAVY,True,SANS)])
chart_panel(s,FIG_ANTH,0.6,2.25,8.0,3.7)
text(s,8.95,2.5,3.85,4,[[("$87M to ~$47B run-rate in 17 months,",15.5,NAVY,True,SANS)],
    [("overtaking OpenAI on ARR in April 2026. Now $965B (Series H), filed confidentially in June for an expected October listing.",13.5,INK2,False,SANS)],
    [("The risk is the narrative, not demand: an enterprise shift away from \"token maxing,\" plus export-control uncertainty on chips.",13.5,NAVY,True,SANS)]],line_sp=1.06,sp_after=10)
text(s,0.6,6.25,12,0.3,[[("Source: PitchBook Premium; TechCrunch / VentureBeat / CNBC, Jan 2024 to May 2026. Run-rate figures annualized.",10,MUTED,False,SANS)]])

# ---------- 12 SEG 4 DIVIDER ----------
s=content("d4"); segno(s,0.6,3.0,"SEG 04")
eyebrow(s,0.6,3.62,"THE IDEA: TWO WINNERS IN EVERY CATEGORY")
htitle(s,0.6,4.0,12.4,[("It is not a duopoly. It is winner-take-most, miscounted",36,NAVY,True,SANS)])

# ---------- 13 ratio (money) ----------
s=content("ratio")
eyebrow(s,0.6,0.95,"SEG 04 . FIG 6")
htitle(s,0.6,1.28,12.2,[("The #1-to-#2 valuation ratio across 16 AI verticals",23,NAVY,True,SANS)])
chart_panel(s,FIG_RATIO,0.55,1.95,8.2,5.0)
text(s,9.0,2.2,3.8,4.6,[[("A true duopoly sits near 1x.",16,NAVY,True,SANS)],
    [("Only formal math and foundation models qualify (green).",13,INK2,False,SANS)],
    [("Of 16 verticals: 2 near-parity, 6 above 10x, and 3 more where the #2 has no venture mark at all.",13,NAVY,True,SANS)],
    [("The modal outcome is not a split. It is one company many times larger than whatever sits in second.",13,INK2,False,SANS)]],line_sp=1.05,sp_after=8)
text(s,9.0,6.55,3.9,0.4,[[("Voice AI shown at ElevenLabs' pending $22B secondary (61x); the last priced mark, $11B, reads as 30x.",9,MUTED,False,SANS)]],line_sp=1.05)

# ---------- 14 & 15 THE FULL MAP (named) ----------
def table_slide(title, rows, part):
    s=content("map"+part)
    eyebrow(s,0.6,0.9,"SEG 04 . THE FULL MAP  ("+part+")")
    htitle(s,0.6,1.22,12.2,[(title,23,NAVY,True,SANS)])
    cols=[("VERTICAL",2.05),("#1  (valuation, date)",2.75),("#2  (valuation, date)",2.6),("RATIO",0.9),("PATTERN",3.55)]
    x0=0.6; y0=1.95; cx=x0
    # header
    box(s,x0,y0,11.85,0.4,fill=NAVY)
    cxx=x0
    for name,w in cols:
        text(s,cxx+0.12,y0,w-0.12,0.4,[[(name,9.5,"#f2d79a",True,SANS,0.03)]],anchor=MSO_ANCHOR.MIDDLE)
        cxx+=w
    ry=y0+0.4; rh=(6.55-ry)/len(rows)
    for i,(v,one,two,ratio,pat,band) in enumerate(rows):
        if i%2==0: box(s,x0,ry,11.85,rh,fill=CARD)
        box(s,x0,ry+rh,11.85,0.008,fill=BORDER)
        cc=x0
        vals=[(v,NAVY,True),(one,INK2,False),(two,INK2,False),(ratio, (POS if band=='p' else (NEG if band=='b' else NAVY)),True),(pat,INK2,False)]
        for (name,w),(val,col,bold) in zip(cols,vals):
            fs=9.5 if w>1 else 11
            if name=="PATTERN": fs=8.8
            text(s,cc+0.12,ry,w-0.18,rh,[[(val,fs,col,bold,SANS)]],anchor=MSO_ANCHOR.MIDDLE,line_sp=1.02)
            cc+=w
        ry+=rh
    return s

rows1=[
 ("Foundation models","Anthropic  $965B","OpenAI  $852B","1.1x","Near parity; xAI ~$1.76T inside SpaceX breaks the top-2 frame","p"),
 ("Formal math AI","Axiom  $1.6B  3/26","Harmonic  $1.45B  11/25","1.1x","Genuine dead-heat duopoly","p"),
 ("Legal AI","Harvey  $11B  3/26","Legora  $5.6B  4/26","2.0x","Clean hierarchy; real exit, Robin AI to Microsoft","n"),
 ("AI inference chips","Cerebras  $40.6B IPO  5/26","Groq  $20B (to Nvidia)  12/25","2.0x","Real dual exits: one IPO, one M&A","n"),
 ("AI coding","Cursor  $60B (to SpaceX)  6/26","Cognition  $26B  5/26","2.3x","Clean hierarchy; real $60B exit","n"),
 ("Defense AI","Anduril  $61B ($4.3B rev)  5/26","Helsing  $18B  5/26","3.4x","Real duopoly, but geographic: US vs EU sovereign-tech","n"),
 ("Customer support","Sierra  $15.8B  5/26","Decagon  $4.5B  1/26","3.5x","Clear leader","n"),
 ("Healthcare scribes","Abridge  $5.3B  6/25","Ambience  $1.25B  7/25","4.2x","Clear leader","n"),
 ("AI recruiting","Mercor  $10B  10/25","Eightfold  $2.1B  2021 (stale)","4.8x","LLM-native disruptor eclipsing pre-genAI incumbent","n"),
 ("Humanoid robotics","Figure  $39B  5/25 (stale)","Physical Intelligence  $5.4B","7.2x","Clear leader; ~$11B PI round pending would be 3.5x","n"),
]
rows2=[
 ("AI web search","Perplexity  $20B  9/25-5/26","Exa  $2.2B  5/26","9.1x","False duopoly: agent-search infra vs consumer answers","n"),
 ("Enterprise search","Glean  $7.2B  11/25","Hebbia  $700M  10/24 (stale)","10.3x","Blowout","b"),
 ("Video generation","Runway  $5.3B  2/26","Pika  $470M  7/24 (stale)","11x","Blowout; also Sora, Veo, not a 2-name story","b"),
 ("Meeting notetakers","Granola  $1.5B  3/26","Otter.ai  $94M  2021 (stale)","16x","Inverted on revenue: Otter discloses $100M TTM, Granola none","b"),
 ("Sales / GTM agents","Clay  $3B  6/25","Artisan  $150M  5/25","20x","Blowout","b"),
 ("Voice AI","ElevenLabs  $22B  7/26 (pending)","Cartesia  $362M  3/25","61x","Blowout","b"),
 ("Image generation","Black Forest Labs  $3.1B  12/25","Midjourney  no VC, $500M rev","n/a","Revenue leader invisible to funding-concentration data","n"),
 ("Data labeling, RLHF","Scale AI  $29B  6/25 (Meta stake)","Surge AI  no VC, $1.4B rev","n/a","Funding leader is not the revenue leader (Surge > Scale)","n"),
 ("AI companion apps","Character.ai  $1B (frozen 8/24)","Replika  $33M  2017 (frozen)","n/a","Category stagnation, not concentration","n"),
]
table_slide("Every #1 and #2, named: near-parity to blowout", rows1, "1 of 2")
table_slide("Every #1 and #2, named: the blowouts and the invisibles", rows2, "2 of 2")

# ---------- 16 funding != business ----------
s=content("fund")
eyebrow(s,0.6,1.0,"SEG 04 . FIG 7")
htitle(s,0.6,1.35,12.2,[("The biggest round is not the biggest business",25,NAVY,True,SANS)])
chart_panel(s,FIG_FUND,0.6,2.2,7.4,4.1)
text(s,8.3,2.4,4.5,4,[[("Blue: valuation.  Green: disclosed revenue.",12.5,NAVY,True,SANS)],
    [("Surge out-earns Scale with zero venture funding. Otter out-earns Granola on disclosed revenue. Midjourney does ~$500M and has no valuation to plot.",14,INK2,False,SANS)],
    [("Frame winners by round size and you miss the best unit economics in the category.",14,NAVY,True,SANS)]],line_sp=1.1,sp_after=10)
text(s,0.6,6.5,12,0.3,[[("Source: PitchBook Premium. Scale ~$1B rev / $29B val; Surge ~$1.4B rev, no VC; Otter ~$0.1B rev / $94M val; Granola $1.5B val, rev undisclosed.",10,MUTED,False,SANS)]])

# ---------- 17 crossover matrix ----------
s=content("matrix")
eyebrow(s,0.6,1.0,"SEG 04 . FIG 8")
htitle(s,0.6,1.35,12.2,[("Who manufactures the \"2\": the same funds sit on both sides",23,NAVY,True,SANS)])
chart_panel(s,FIG_MATRIX,0.6,2.15,7.6,4.2)
text(s,8.5,2.4,4.3,0.5,[[("●",14,NAVY,True,SANS),("  Backs the #1        ",12.5,INK2,False,SANS),("○",14,GOLD,True,SANS),("  Backs the #2",12.5,INK2,False,SANS)]])
text(s,8.5,3.1,4.35,3.4,[[("a16z holds both #1 and #2 in legal (Harvey + Legora) and health scribes (Abridge + Ambience).",14,NAVY,True,SANS)],
    [("The same 10 to 15 crossover funds capitalize both seats, a hedge that manufactures a \"2\" rather than picking a winner.",13.5,INK2,False,SANS)]],line_sp=1.08,sp_after=10)
text(s,0.6,6.5,12,0.3,[[("Source: PitchBook Premium investor records. Sequoia backs Harvey but not Legora; Kleiner backs Harvey and Harmonic but not Cerebras.",10,MUTED,False,SANS)]])

# ---------- 18 six real exits ----------
s=content("exits")
eyebrow(s,0.6,1.0,"SEG 04 . THE EXITS ARE ALREADY LIVE")
htitle(s,0.6,1.35,12.2,[("Six real exits, and strategics paid up for the #1",25,NAVY,True,SANS)])
ex=[("Cursor → SpaceX","$60B","M&A","Category leader in AI coding, bought at the top"),
    ("Cerebras → Nasdaq","$40.6B","IPO","Profitable print (warrant-aided); AI inference chips"),
    ("Scale AI → Meta","$29B*","Stake + CEO","Effective absorption: large stake, CEO poached"),
    ("Groq → Nvidia","$20B","M&A","Now an Nvidia subsidiary; still raising"),
    ("Robin AI → Microsoft","n/d","Acquihire","The sub-scale \"priced out\" case, the counter-example"),
    ("Neeva → Snowflake","n/d","M&A","Search talent and tech folded into a platform")]
x=0.6; y=2.35; wc=3.9; hc=1.75
for i,(nm,val,typ,d) in enumerate(ex):
    r,c=divmod(i,3); xx=0.6+c*4.06; yy=2.35+r*2.0
    box(s,xx,yy,wc,hc,fill=PANEL,line=BORDER,lw=1,rad=True)
    box(s,xx,yy,0.1,hc,fill=GOLD)
    text(s,xx+0.28,yy+0.18,wc-0.5,0.4,[[(nm,15,NAVY,True,SANS)]])
    text(s,xx+0.28,yy+0.62,wc-0.5,0.3,[[(val,17,NAVY,True,SANS),("   "+typ,11,MUTED,True,MONO,0.04)]])
    text(s,xx+0.28,yy+1.08,wc-0.5,0.6,[[(d,11.5,INK2,False,SANS)]],line_sp=1.05)
text(s,0.6,6.5,12,0.3,[[("*Meta took a ~$14.3B stake and hired the CEO. Pattern: strategics buy the outright #1, not the struggling runner-up. The AI-vertical exit environment is live now, not five years out.",10,MUTED,False,SANS)]])

# ---------- 19 sub-patterns ----------
s=content("patterns")
eyebrow(s,0.6,1.0,"SEG 04 . BEFORE YOU CALL IT A DUOPOLY")
htitle(s,0.6,1.35,12.2,[("When you see a \"2\", check which kind it is",25,NAVY,True,SANS)])
cards=[("GEOGRAPHIC, NOT COMPETITIVE","A US champion beside a non-US sovereign-tech champion serving different regulatory buyers. Defense: Anduril (US) vs Helsing (EU). Legal: Harvey (US) vs Legora (Stockholm). A 1 + 1, not a head-to-head 2."),
       ("STAGNATION, NOT CONCENTRATION","AI companions: Character.ai frozen since its founders left for Google (Aug 2024), Replika since 2017. The real winners became features inside Grok and Meta AI. Some categories converge to zero investable names."),
       ("MANUFACTURED BY THE SAME CAPITAL","Sequoia, a16z, Kleiner, Founders Fund, Index, General Catalyst back both seats vertical after vertical. The \"2\" is often a deliberate hedge, not two independent winners.")]
x=0.6
for h,d in cards:
    box(s,x,2.4,3.85,3.5,fill=PANEL,line=BORDER,lw=1,rad=True); box(s,x,2.4,3.85,0.12,fill=GOLD)
    text(s,x+0.3,2.75,3.3,0.9,[[(h,12.5,NAVY,True,MONO,0.03)]],line_sp=1.05)
    text(s,x+0.3,3.75,3.3,2.0,[[(d,13,INK2,False,SANS)]],line_sp=1.1)
    x+=4.06
text(s,0.6,6.2,12.2,0.6,[[("The modal outcome is winner-take-most. Real two-way splits show up about one in ten; the other nine times it is a 10x-to-60x gap, or the biggest business never took venture money at all.",13,NAVY,True,SANS)]],line_sp=1.1)

# ---------- 20 frontier paradox ----------
s=content("frontier")
eyebrow(s,0.6,1.0,"SEG 04 . AT THE FRONTIER")
htitle(s,0.6,1.35,12.2,[("The two-name story breaks at the top too",25,NAVY,True,SANS)])
box(s,0.6,2.4,5.9,3.5,fill=PANEL,line=BORDER,lw=1,rad=True)
text(s,0.95,2.7,5.3,0.5,[[("THE VALUATION-QUALITY PARADOX",11,"#b5820c",True,MONO,0.05)]])
text(s,0.95,3.25,5.2,0.8,[[("Databricks",30,NAVY,True,SANS),("  AIBQ 8.7",18,INK2,True,SANS)]])
text(s,0.95,4.0,5.2,0.5,[[("Tops the Frontier Five, only member with positive free cash flow.",13,INK2,False,SANS)]],line_sp=1.05)
box(s,0.95,4.75,5.2,0.014,fill=BORDER)
text(s,0.95,4.95,5.2,0.8,[[("OpenAI",30,NEG,True,SANS),("  AIBQ 4.8",18,INK2,True,SANS)]])
text(s,0.95,5.7,5.2,0.4,[[("Highest profile, lowest business-quality score.",13,INK2,False,SANS)]])
text(s,6.9,2.5,6,4,[[("\"Anthropic vs OpenAI\" reads as a clean 1.1x duopoly ($965B vs $852B).",17,NAVY,True,SANS)],
    [("But PitchBook's Frontier Five note counts five, not two, and the highest-valued names score lowest on quality. And xAI is not a standalone third: it is folded inside a ~$2.4T SpaceX.",14.5,INK2,False,SANS)],
    [("The two-name story does not survive contact with the cap tables.",15,NAVY,True,SANS)]],line_sp=1.1,sp_after=10)

# ---------- 21 closing ----------
s=slide(NAVY); arcs(s,dark=True); box(s,0,0,0.22,7.5,fill=GOLD)
text(s,0.75,0.55,8,0.4,[[("PitchBook",13,"#ffffff",True,SANS),("  with Madrona",13,"#8aa0c4",False,SANS)]])
eyebrow(s,0.78,1.3,"THE THROUGH-LINE",GOLD)
text(s,0.78,1.75,11.6,2.0,[[("Count the business, not the round",42,"#ffffff",True,SANS)]])
box(s,0.82,3.5,2.1,0.045,fill=GOLD)
pts=[("Durability is measurable","and has a history you can chart. It moved up the stack from the model to the workflow."),
     ("The IPO drought is a choice","not an absence of exit-scale companies. The value is private, and enormous."),
     ("The \"duopoly\" is winner-take-most","with a nominal second place that funding data overstates.")]
x=0.78
for h,d in pts:
    box(s,x,4.15,3.85,2.05,fill="#1b3057",line="#2a4372",lw=1,rad=True)
    text(s,x+0.3,4.42,3.3,0.8,[[(h,16,"#f4c65a",True,SANS)]],line_sp=1.0)
    text(s,x+0.3,5.35,3.35,0.9,[[(d,12.5,"#d7deea",False,SANS)]],line_sp=1.05)
    x+=4.02
text(s,0.78,6.55,12,0.4,[[("Sources: PitchBook Premium (financing, investors, VC Exit Predictor, Venture Monitor, Frontier Five); Madrona/PitchBook IA40; company disclosures; CNBC, Bloomberg, TechCrunch. Verified July 17, 2026.",9.5,"#8aa0c4",False,SANS)]],line_sp=1.1)

prs.save(OUT)
print("Saved", OUT, "with", len(prs.slides._sldIdLst), "slides")
body="".join("".join(b)+"</div>" for b in HTML_SLIDES)
open(os.path.join(CH,"preview.html"),"w").write(
    "<!doctype html><meta charset='utf-8'><style>body{margin:0;background:#666}"
    ".slide{position:relative;width:1280px;height:720px;margin:16px auto;overflow:hidden;"
    "font-family:Arial,system-ui,sans-serif}</style>"+body)
print("Preview", os.path.join(CH,"preview.html"))
