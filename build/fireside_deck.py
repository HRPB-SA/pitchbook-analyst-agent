#!/usr/bin/env python3
"""
Build the PitchBook x Madrona fireside deck:
"Durability, IPOs and the Duopoly Myth" (Segments 1, 3, 4).

Generates matplotlib chart PNGs (dark, transparent) then assembles a 16:9
PowerPoint with python-pptx. All figures verified July 2026; Databricks
updated to the $188B strategic round (term sheet signed Jul 16 2026, Coatue).

Run:  python3 build/fireside_deck.py
Out:  output/Fireside_Durability_IPOs_Duopoly_Jul2026.pptx
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import numpy as np
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, "build", "deck_charts")
os.makedirs(CH, exist_ok=True)
OUT = os.path.join(ROOT, "output", "Fireside_Durability_IPOs_Duopoly_Jul2026.pptx")

# ---------------- palette (dark broadcast) ----------------
BG      = "#111309"
PANEL   = "#1a1c11"
INK     = "#f6f6ee"
INK2    = "#c6c5ba"
MUTED   = "#8f9084"
BRAND   = "#4bb488"
BRAND2  = "#6fca9f"
AMBER   = "#e0a94b"
POS     = "#49c46e"
NEG     = "#e8695d"
S1 = "#3d8be8"  # blue
S2 = "#3aa53a"  # green
S4 = "#d29a2e"  # yellow
S5 = "#1fae7c"  # aqua
S6 = "#e0643a"  # orange
GRID = "#33342a"
AXIS = "#4a4b3d"

def hx(c): return RGBColor.from_string(c.lstrip("#"))

# matplotlib defaults
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 13,
    "text.color": INK,
    "axes.edgecolor": AXIS,
    "axes.labelcolor": INK2,
    "xtick.color": MUTED,
    "ytick.color": INK2,
    "figure.dpi": 200,
    "savefig.dpi": 200,
})

def newfig(w, h):
    fig = plt.figure(figsize=(w, h))
    fig.patch.set_alpha(0)
    return fig

def styleax(ax):
    ax.set_facecolor("none")
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(length=0)
    return ax

def save(fig, name):
    p = os.path.join(CH, name)
    fig.savefig(p, transparent=True, bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)
    return p

# ============================================================
# CHARTS
# ============================================================
def c_ia40():
    fig = newfig(9.2, 3.0)
    ax = styleax(fig.add_subplot(111))
    # top: composition of 40
    ax.barh([1.6], [27], height=0.5, color=S1, zorder=3)
    ax.barh([1.6], [13], left=[27], height=0.5, color=S4, zorder=3)
    ax.text(27/2, 1.6, "27", ha="center", va="center", color="#fff", fontweight="bold", fontsize=13)
    ax.text(27+13/2, 1.6, "13", ha="center", va="center", color="#1a1c11", fontweight="bold", fontsize=13)
    ax.text(0, 2.05, "2025 IA40 cohort: 40 winners", color=INK, fontsize=12.5, fontweight="bold")
    ax.text(40, 2.05, "~50% replaced each year", color=MUTED, ha="right", fontsize=11)
    # survivorship
    ax.barh([0.7], [4], height=0.34, color=S5, zorder=3)
    ax.text(4.4, 0.7, "4  (Abnormal, Databricks, Hugging Face, Runway)", va="center", color=INK, fontsize=11)
    ax.text(0, 0.98, "Made all 4 lists, 2021 to 2024", color=INK2, fontsize=10.5)
    ax.barh([0.0], [1], height=0.34, color=BRAND, zorder=3)
    ax.text(1.4, 0.0, "1  (Databricks)", va="center", color=INK, fontsize=11, fontweight="bold")
    ax.text(0, 0.28, "Made all 5 lists, 2021 to 2025", color=INK2, fontsize=10.5)
    ax.set_xlim(0, 40); ax.set_ylim(-0.35, 2.3)
    ax.set_xticks([]); ax.set_yticks([])
    return save(fig, "ia40.png")

def c_split():
    fig = newfig(9.2, 2.5)
    ax = styleax(fig.add_subplot(111))
    rows = [
        ("Share of deals\n1,603 deals", [("Horizontal",26.5,S1),("Vertical",63.8,S5),("Other",9.7,"#2b2c20")]),
        ("Share of capital\n$73.6B",     [("Horizontal",70,S1),("Vertical",26,S5),("Other",4,"#2b2c20")]),
    ]
    for i,(lab,segs) in enumerate(rows):
        x=0
        for nm,v,c in segs:
            ax.barh([i],[v],left=[x],height=0.5,color=c,zorder=3)
            if v>12:
                ax.text(x+v/2,i,f"{round(v)}%",ha="center",va="center",
                        color="#fff" if nm!="Other" else INK2,fontweight="bold",fontsize=12)
            x+=v
        ax.text(-2,i,lab,ha="right",va="center",color=INK,fontsize=11,fontweight="bold")
    ax.set_xlim(0,100); ax.set_ylim(-0.5,1.5)
    ax.set_xticks([]); ax.set_yticks([])
    return save(fig, "split.png")

def c_spacex():
    fig = newfig(9.2, 2.6)
    ax = styleax(fig.add_subplot(111))
    data=[("SpaceX, first-day market cap  (Jun 12 2026)",2100,S6),
          ("All US VC-backed IPOs since 2016  (combined)",1500,S1),
          ("US IPO proceeds, full-year 2025  (all sectors)",45,MUTED)]
    ys=range(len(data))
    for i,(lab,v,c) in enumerate(data):
        ax.barh([i],[v],height=0.46,color=c,zorder=3)
        vt = f"${v/1000:.2f}T" if v>=1000 else f"${v}B"
        ax.text(v+30,i,vt,va="center",color=INK,fontsize=12.5,fontweight="bold")
        ax.text(0,i+0.36,lab,va="center",color=INK2,fontsize=11)
    for g in [0,500,1000,1500,2000]:
        ax.axvline(g,color=GRID,lw=1,zorder=0)
        ax.text(g,-0.75,f"${g/1000:.1f}T".replace(".0T","T"),ha="center",color=MUTED,fontsize=9.5)
    ax.invert_yaxis()
    ax.set_xlim(0,2300); ax.set_ylim(2.7,-0.7)
    ax.set_xticks([]); ax.set_yticks([])
    return save(fig, "spacex.png")

def c_logline(name, pts, color, lo, hi, dashed_to=None, dashed_lab=None):
    """pts: list of (xlabel, value_$B, show_label_bool)."""
    fig = newfig(9.2, 3.1)
    ax = styleax(fig.add_subplot(111))
    xs=np.arange(len(pts)); ys=[p[1] for p in pts]
    ax.set_yscale("log")
    ax.plot(xs,ys,color=color,lw=2.6,zorder=3,solid_capstyle="round")
    ax.scatter(xs,ys,s=46,color=color,zorder=4,edgecolors=BG,linewidths=2)
    for i,(xl,v,show) in enumerate(pts):
        if show:
            vt = (f"${v/1000:.2f}T" if v>=1000 else (f"${v:g}B" if v>=1 else f"${round(v*1000)}M"))
            ax.annotate(vt,(xs[i],ys[i]),textcoords="offset points",xytext=(0,11),
                        ha="center",color=INK,fontsize=12,fontweight="bold")
    if dashed_to is not None:
        ax.plot([xs[-1],xs[-1]+0.9],[ys[-1],dashed_to],color=AMBER,lw=2.2,ls=(0,(3,3)),zorder=3)
        ax.scatter([xs[-1]+0.9],[dashed_to],s=52,color=AMBER,zorder=4,edgecolors=BG,linewidths=2)
        vt=f"${dashed_to/1000:.2f}T" if dashed_to>=1000 else f"${dashed_to:g}B"
        ax.annotate(vt,(xs[-1]+0.9,dashed_to),textcoords="offset points",xytext=(6,10),
                    ha="left",color=AMBER,fontsize=12.5,fontweight="bold")
        if dashed_lab:
            ax.annotate(dashed_lab,(xs[-1]+0.9,dashed_to),textcoords="offset points",xytext=(2,-20),
                        ha="center",color=MUTED,fontsize=9.5)
    ax.set_xticks(xs); ax.set_xticklabels([p[0] for p in pts],fontsize=10.5,color=MUTED)
    ax.set_xlim(-0.4,len(pts)-0.1+(1.4 if dashed_to else 0.2))
    ax.set_ylim(lo,hi)
    ax.grid(axis="y",color=GRID,lw=1)
    # y ticks as $ decades
    ticks=[t for t in [0.1,1,10,100,1000] if lo<=t<=hi]
    ax.set_yticks(ticks)
    ax.set_yticklabels([(f"${int(t/1000)}T" if t>=1000 else (f"${int(t)}B" if t>=1 else f"${int(t*1000)}M")) for t in ticks],
                       fontsize=10.5,color=INK2)
    ax.tick_params(axis="y",length=0)
    return save(fig, name)

def c_dbx():
    pts=[("'13",0.047,False),("'14",0.923,False),("'16",0.56,False),("'18",0.985,False),
         ("'19",2.75,False),("'19",6.2,False),("'21",28,False),("'21",38,False),
         ("'23",43.2,True),("'24",62,False),("'25",100,False),("'26",134,True)]
    return c_logline("dbx.png",pts,S1,0.04,320,dashed_to=188,dashed_lab="term sheet, Jul 2026")

def c_anth():
    pts=[("Jan24",0.087,True),("Dec24",1,False),("'25",9,False),("Feb26",14,False),
         ("Apr26",30,False),("May26",47,True)]
    return c_logline("anth.png",pts,S2,0.07,90)

def c_ratio():
    data=[("Formal math","Axiom / Harmonic",1.10),
          ("Foundation models","Anthropic / OpenAI",1.13),
          ("Legal AI","Harvey / Legora",1.96),
          ("AI inference chips","Cerebras / Groq",2.03),
          ("AI coding","Cursor / Cognition",2.31),
          ("Defense AI","Anduril / Helsing",3.39),
          ("Customer support","Sierra / Decagon",3.51),
          ("Healthcare scribes","Abridge / Ambience",4.24),
          ("AI recruiting","Mercor / Eightfold",4.76),
          ("Humanoid robotics","Figure / Physical Intel.",7.22),
          ("AI web search","Perplexity / Exa",9.09),
          ("Enterprise search","Glean / Hebbia",10.29),
          ("Video generation","Runway / Pika",11.28),
          ("Meeting notetakers","Granola / Otter",15.96),
          ("Sales / GTM","Clay / Artisan",20.0),
          ("Voice AI","ElevenLabs / Cartesia",30.4)]
    fig = newfig(9.4, 5.0)
    ax = styleax(fig.add_subplot(111))
    ax.set_xscale("log")
    ys=np.arange(len(data))[::-1]
    for i,(v,pair,r) in enumerate(data):
        c = S2 if r<1.5 else (S6 if r>10 else S1)
        ax.barh([ys[i]],[r-1],left=[1],height=0.62,color=c,zorder=3)
        ax.text(r*1.04,ys[i],f"{r:.1f}x" if r<10 else f"{r:.0f}x",va="center",color=INK,
                fontsize=11,fontweight="bold")
        ax.text(0.92,ys[i],v,va="center",ha="right",color=INK,fontsize=11)
    for g,lab,em in [(1,"1x",0),(2,"2x",1),(5,"5x",0),(10,"10x",1),(20,"20x",0),(40,"40x",0)]:
        ax.axvline(g,color=(AXIS if em else GRID),lw=1,ls=("--" if em else "-"),zorder=0)
        ax.text(g,-1.1,lab,ha="center",color=MUTED,fontsize=9.5)
    ax.set_xlim(0.85,46); ax.set_ylim(-1.6,len(data)-0.3)
    ax.set_xticks([]); ax.set_yticks([])
    return save(fig, "ratio.png")

def c_fund():
    fig = newfig(9.2, 3.2)
    ax = styleax(fig.add_subplot(111))
    groups=[("Data labeling",[("Scale AI",29,1.0,False,False),("Surge AI",0,1.4,True,False)]),
            ("Meeting notes",[("Granola",1.5,0,False,True),("Otter.ai",0.094,0.1,False,False)])]
    maxv=29
    def bw(v): return 0 if v<=0 else max(np.sqrt(v)/np.sqrt(maxv),0.01)
    y=0; ylabels=[]
    for gi,(g,items) in enumerate(groups):
        ax.text(-0.02,y+0.5,g,color=BRAND2,fontsize=11,fontweight="bold",ha="left")
        y-=1
        for nm,val,rev,novc,norev in items:
            ax.barh([y],[bw(val)],height=0.34,color=S1,zorder=3)
            if novc: ax.text(0.01,y,"no VC valuation",va="center",color=MUTED,fontsize=9.5)
            else: ax.text(bw(val)+0.012,y,f"${val:g}B" if val>=1 else f"${round(val*1000)}M",va="center",color=INK,fontsize=10.5,fontweight="bold")
            ax.barh([y-0.42],[bw(rev)],height=0.34,color=S2,zorder=3)
            if norev: ax.text(0.01,y-0.42,"revenue undisclosed",va="center",color=MUTED,fontsize=9.5)
            else: ax.text(bw(rev)+0.012,y-0.42,f"${rev:g}B" if rev>=1 else f"${round(rev*1000)}M",va="center",color=INK,fontsize=10.5,fontweight="bold")
            ax.text(-0.02,y-0.21,nm,va="center",ha="right",color=INK,fontsize=11,fontweight="bold")
            y-=1.15
        y-=0.35
    ax.set_xlim(-0.16,1.15); ax.set_ylim(y+0.5,1.1)
    ax.set_xticks([]); ax.set_yticks([])
    return save(fig, "fund.png")

def c_matrix():
    funds=["a16z","Nvidia","Sequoia","Kleiner P.","Gen. Catalyst"]
    verts=["Legal","Health\nscribes","Coding","Ent.\nsearch","Voice","Formal\nmath","Defense"]
    # (row,col): 1 = backs #1 (filled), 2 = backs #2 (ring), 3 = both
    M={
        (0,0):3,(0,1):3,(0,2):1,(0,4):1,(0,6):1,          # a16z
        (1,0):2,(1,2):1,                                   # nvidia
        (2,0):1,(2,3):1,(2,4):1,(2,5):2,                   # sequoia
        (3,0):1,(3,3):1,(3,5):2,                           # kleiner
        (4,0):2,(4,2):2,(4,3):1,                           # gen catalyst
    }
    fig = newfig(9.2, 3.4)
    ax = styleax(fig.add_subplot(111))
    nr,nc=len(funds),len(verts)
    for i in range(nr+1): ax.axhline(i-0.5,color=GRID,lw=1)
    for j in range(nc+1): ax.axvline(j-0.5,color=GRID,lw=1)
    for (r,c),v in M.items():
        yy=nr-1-r
        if v in (1,3): ax.scatter([c],[yy],s=150,color=BRAND,zorder=3)
        if v in (2,3): ax.scatter([c],[yy],s=210,facecolors="none",edgecolors=AMBER,linewidths=2.4,zorder=4)
    ax.set_xticks(range(nc)); ax.set_xticklabels(verts,fontsize=10,color=INK2)
    ax.set_yticks(range(nr)); ax.set_yticklabels(funds[::-1],fontsize=11,color=INK,fontweight="bold")
    ax.xaxis.set_ticks_position("top"); ax.xaxis.set_label_position("top")
    ax.tick_params(length=0)
    ax.set_xlim(-0.5,nc-0.5); ax.set_ylim(-0.5,nr-0.5)
    return save(fig, "matrix.png")

print("Rendering charts...")
FIG_IA40=c_ia40(); FIG_SPLIT=c_split(); FIG_SPACEX=c_spacex()
FIG_DBX=c_dbx(); FIG_ANTH=c_anth(); FIG_RATIO=c_ratio()
FIG_FUND=c_fund(); FIG_MATRIX=c_matrix()

# ============================================================
# DECK
# ============================================================
prs = Presentation()
prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]
SW, SH = prs.slide_width, prs.slide_height

# ---- HTML mirror (for visual QA only) ----
PXI = 96.0
HTML_SLIDES = []   # list of html-string buffers, one per slide
def _h(x): HTML_SLIDES[-1].append(x)

def slide(bg=BG):
    s = prs.slides.add_slide(BLANK)
    r = s.shapes.add_shape(MSO_SHAPE.RECTANGLE,0,0,SW,SH)
    r.fill.solid(); r.fill.fore_color.rgb = hx(bg); r.line.fill.background()
    r.shadow.inherit=False
    HTML_SLIDES.append([f'<div class="slide" style="background:{bg}">'])
    s._bg = bg
    return s

def box(s,l,t,w,h,fill=None,line=None,lw=1.0,rad=False):
    shp = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if rad else MSO_SHAPE.RECTANGLE,
                             Inches(l),Inches(t),Inches(w),Inches(h))
    if fill: shp.fill.solid(); shp.fill.fore_color.rgb=hx(fill)
    else: shp.fill.background()
    if line: shp.line.color.rgb=hx(line); shp.line.width=Pt(lw)
    else: shp.line.fill.background()
    shp.shadow.inherit=False
    st=(f'position:absolute;left:{l*PXI}px;top:{t*PXI}px;width:{w*PXI}px;height:{h*PXI}px;'
        f'{"background:"+fill+";" if fill else ""}{"border:"+str(lw)+"px solid "+line+";" if line else ""}'
        f'{"border-radius:9px;" if rad else ""}box-sizing:border-box;')
    _h(f'<div style="{st}"></div>')
    return shp

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
            f.size=Pt(sz); f.color.rgb=hx(col); f.bold=bold
            f.name=font or "Arial"
            if spc is not None:
                rPr=run._r.get_or_add_rPr(); rPr.set("spc",str(int(spc*100)))
            fam="ui-monospace,Consolas,monospace" if font in ("Consolas",) else "Arial,system-ui,sans-serif"
            ls=f"letter-spacing:{spc}em;" if spc else ""
            esc=(txt or "&nbsp;").replace("&","&amp;").replace("<","&lt;")
            spans.append(f'<span style="font-size:{sz}px;color:{col};font-weight:{700 if bold else 400};'
                         f'font-family:{fam};{ls}">{esc}</span>')
        parts.append(f'<div style="margin:0 0 {sp_after}px;line-height:{line_sp};text-align:{al}">'+"".join(spans)+'</div>')
    st=(f'position:absolute;left:{l*PXI}px;top:{t*PXI}px;width:{w*PXI}px;height:{h*PXI}px;'
        f'display:flex;flex-direction:column;justify-content:{va};box-sizing:border-box;overflow:visible;')
    _h(f'<div style="{st}">'+"".join(parts)+'</div>')
    return tb

def pic(s,path,l,t,w=None,h=None):
    p=s.shapes.add_picture(path,Inches(l),Inches(t),
                           Inches(w) if w else None,Inches(h) if h else None)
    import os as _os
    rel=_os.path.basename(path)
    ww=(w*PXI) if w else (p.width/914400*PXI)
    _h(f'<img src="{rel}" style="position:absolute;left:{l*PXI}px;top:{t*PXI}px;width:{ww}px"/>')
    return p

MONO="Consolas"; SANS="Arial"

def eyebrow(s,l,t,txt,col=BRAND):
    text(s,l,t,10,0.3,[[(txt,12,col,True,MONO,0.22)]])

def lockup(s,l=0.6,t=0.42):
    text(s,l,t,6,0.4,[[("PitchBook",13,INK,True,MONO),("  x  ",13,MUTED,False,MONO),("Madrona",13,INK,True,MONO)]])

def footer(s,n):
    box(s,0,7.12,13.333,0.02,fill=GRID)
    text(s,0.6,7.18,8,0.3,[[("PitchBook x Madrona  /  Live fireside  /  July 2026",9.5,MUTED,False,MONO,0.06)]])
    text(s,11.6,7.18,1.2,0.3,[[(f"{n:02d}",9.5,MUTED,False,MONO)]],align=PP_ALIGN.RIGHT)

def segno(s,l,t,txt):
    b=box(s,l,t,1.05,0.42,line=BRAND,lw=1.25,rad=True)
    tf=b.text_frame; tf.margin_top=0;tf.margin_bottom=0
    p=tf.paragraphs[0]; p.alignment=PP_ALIGN.CENTER
    run=p.add_run(); run.text=txt; run.font.size=Pt(12); run.font.bold=True
    run.font.color.rgb=hx(BRAND); run.font.name=MONO
    _h(f'<div style="position:absolute;left:{l*PXI}px;top:{t*PXI}px;width:{1.05*PXI}px;height:{0.42*PXI}px;'
       f'display:flex;align-items:center;justify-content:center;color:{BRAND};font-weight:700;font-size:12px;'
       f'font-family:ui-monospace,monospace">{txt}</div>')

def chart_panel(s,path,l,t,w,h):
    box(s,l-0.15,t-0.15,w+0.3,h+0.3,fill=PANEL,rad=True)
    # fit image within panel keeping aspect
    from PIL import Image
    iw,ih=Image.open(path).size; ar=iw/ih
    pw,ph=w,h
    if pw/ph>ar: pw=ph*ar
    else: ph=pw/ar
    pic(s,path,l+(w-pw)/2,t+(h-ph)/2,w=pw)

N=[0]
def num(): N[0]+=1; return N[0]

# ---- 1 TITLE ----
s=slide()
box(s,0,0,0.22,7.5,fill=BRAND)
lockup(s,0.7,0.5)
text(s,0.7,0.62,8,0.4,[[("LIVE",10.5,NEG,True,MONO,0.18),("  PODCAST RECORDING",10.5,MUTED,False,MONO,0.18)]] ,align=PP_ALIGN.RIGHT)
text(s,0.7,2.15,11.8,2.2,[[("Durability, IPOs,",54,INK,True,SANS)],
                          [("and the Duopoly Myth",54,INK,True,SANS)]],line_sp=1.0)
text(s,0.72,4.35,10.6,1.4,[[("Three questions the AI market keeps asking, answered with the data ",19,INK2,False,SANS)],
    [("underneath them: what makes an AI startup defensible, why the biggest ",19,INK2,False,SANS)],
    [("companies stay private, and whether \"two winners per category\" is real.",19,INK2,False,SANS)]],line_sp=1.05)
text(s,0.72,6.35,12,0.4,[[("Segments 01 . 03 . 04",12,BRAND,True,MONO,0.08),
    ("      Prepared July 17, 2026      Every figure sourced to PitchBook Premium or named press",12,MUTED,False,MONO,0.04)]])

# ---- 2 AGENDA ----
s=slide(); lockup(s); footer(s,num())
eyebrow(s,0.6,1.05,"THE RUNDOWN")
text(s,0.6,1.4,11,0.9,[[("Three corrections to how the market talks",34,INK,True,SANS)]])
items=[("01","Durability","Defensibility is measurable, and the exit predictor already keeps a history you can chart. The IA40's churn is the signal.",BRAND),
       ("03","AI IPOs","Not a drought, a backlog. 945 unicorns worth $5.3T are sitting private because capital is cheap and one listing now dwarfs a decade.",S1),
       ("04","The Duopoly","It is winner-take-most, miscounted. Count the business, not the round, and the second name usually disappears.",S6)]
x=0.6
for n,h,d,c in items:
    box(s,x,2.6,3.85,3.4,fill=PANEL,rad=True)
    text(s,x+0.35,2.95,1.5,0.8,[[(n,40,c,True,SANS)]])
    text(s,x+0.35,3.95,3.2,0.5,[[(h,20,INK,True,SANS)]])
    text(s,x+0.35,4.55,3.2,1.4,[[(d,13.5,INK2,False,SANS)]],line_sp=1.06)
    x+=4.06
text(s,0.6,6.35,12,0.4,[[("Segment 02 (market structure) is out of scope for this brief.",11.5,MUTED,False,MONO)]])

# ---- 3 SEG 1 DIVIDER ----
s=slide(); lockup(s); footer(s,num())
segno(s,0.6,3.0,"SEG 01")
eyebrow(s,0.6,3.62,"WHAT DOES THE DATA SHOW ON DURABILITY?")
text(s,0.6,4.0,12,1.6,[[("Defensibility is measurable,",40,INK,True,SANS)],
                       [("and the tool already has a memory",40,BRAND,True,SANS)]])

# ---- 4 VCEP KPIs ----
s=slide(); lockup(s); footer(s,num())
eyebrow(s,0.6,1.0,"SEG 01 . THE EXIT PREDICTOR")
text(s,0.6,1.35,12.1,0.9,[[("Does PitchBook's exit predictor keep history? Yes.",30,INK,True,SANS)]])
text(s,0.6,2.25,12.1,0.8,[[("Every scored company carries a Historical Predictions chart: success, IPO and M&A probability tracked over time, with financing rounds overlaid. The compelling angle is on the table.",15,INK2,False,SANS)]],line_sp=1.05)
kp=[("EXIT PREDICTOR KEEPS HISTORY","Yes",POS,"Per-company time series on every profile"),
    ("SUCCESS VS NO-EXIT ACCURACY","71%",INK,"Out-of-sample"),
    ("M&A VS IPO ACCURACY","94%",INK,"Given a successful exit"),
    ("IA40 TURNOVER PER YEAR","~50%",INK,"27 first-time winners in 2025"),
    ("NAMES ON ALL FIVE IA40 LISTS","1",BRAND,"Databricks, only")]
x=0.6; w=2.42
for l,v,c,d in kp:
    box(s,x,3.4,w-0.12,2.5,fill=PANEL,rad=True)
    text(s,x+0.25,3.65,w-0.5,0.9,[[(l,10,MUTED,True,MONO,0.04)]],line_sp=1.0)
    text(s,x+0.25,4.55,w-0.5,0.8,[[(v,38,c,True,SANS)]])
    text(s,x+0.25,5.35,w-0.5,0.5,[[(d,11,INK2,False,SANS)]],line_sp=1.0)
    x+=w
text(s,0.6,6.1,12,0.4,[[("Caveat: the productized time series is per-company. A vertical-wide trend is a cohort pull, not a built-in view.",11.5,MUTED,False,MONO)]])

# ---- 5 IA40 chart ----
s=slide(); lockup(s); footer(s,num())
eyebrow(s,0.6,1.0,"SEG 01 . FIG 1")
text(s,0.6,1.35,12.1,0.6,[[("IA40 staying power is rare: churn is the durability signal",26,INK,True,SANS)]])
chart_panel(s,FIG_IA40,0.6,2.3,8.1,3.9)
text(s,9.05,2.5,3.7,4,[[("2025 was the fifth annual list.",15,INK,True,SANS)],
    [("Roughly half the cohort is replaced every year. Of the four names that made all four lists through 2024, only Databricks carried into 2025, the sole five-time winner.",13.5,INK2,False,SANS)],
    [("",6,INK2,False,SANS)],
    [("Application-layer names rotate out; the infrastructure layer compounds.",13.5,BRAND2,True,SANS)]],line_sp=1.08,sp_after=8)
text(s,0.6,6.4,12,0.3,[[("Source: Madrona / PitchBook IA40 (ia40.com), 2025 edition. Methodology uses the VC Exit Predictor Opportunity Score as an input.",10,MUTED,False,MONO)]])

# ---- 6 split + last mile ----
s=slide(); lockup(s); footer(s,num())
eyebrow(s,0.6,1.0,"SEG 01 . FIG 2")
text(s,0.6,1.35,12.1,0.6,[[("The last mile, priced in dollars",26,INK,True,SANS)]])
chart_panel(s,FIG_SPLIT,0.6,2.15,7.2,2.5)
text(s,0.6,4.95,7.4,1.5,[[("Q1 2025 set a record for AI/ML venture at $73.6B across 1,603 deals. Vertical apps were ~60% of the deals but under a third of the capital: many small bets. A vertical model costs ~$3M to $10M to build; a horizontal LLM costs hundreds of millions.",13,INK2,False,SANS)]],line_sp=1.08)
# last mile cards
box(s,8.2,2.15,4.5,2.0,fill=PANEL,line=NEG,lw=1.25,rad=True)
text(s,8.45,2.32,4,0.4,[[("SHORT LAST MILE",10.5,NEG,True,MONO,0.1)]])
text(s,8.45,2.68,4.1,1.4,[[("Absorbed by the frontier: little between the model and the outcome. ",12.5,INK2,False,SANS),
    ("Copy, images, coding assistants, first-pass drafts.",12.5,INK,True,SANS)]],line_sp=1.05)
box(s,8.2,4.3,4.5,2.15,fill=PANEL,line=BRAND,lw=1.25,rad=True)
text(s,8.45,4.47,4,0.4,[[("LONG LAST MILE",10.5,BRAND,True,MONO,0.1)]])
text(s,8.45,4.83,4.1,1.5,[[("Regulation and liability sit between model and outcome. ",12.5,INK2,False,SANS),
    ("Tax filing, audit-ready accounting, licensed healthcare. Owning liability is insurance pricing.",12.5,INK,True,SANS)]],line_sp=1.05)
text(s,0.6,6.55,12,0.3,[[("Source: PitchBook Q1 2025 AI & ML VC Trends; framework: N. Bobba, Better Tomorrow Ventures (Feb 2026), not Madrona / Sabrina Wu.",10,MUTED,False,MONO)]])

# ---- 7 SEG 3 DIVIDER ----
s=slide(); lockup(s); footer(s,num())
segno(s,0.6,3.0,"SEG 03")
eyebrow(s,0.6,3.62,"STATE OF AI IPOs")
text(s,0.6,4.0,12.2,1.6,[[("The drought is a mirage.",40,INK,True,SANS)],
                         [("The value is real, it is just private",40,S1,True,SANS)]])

# ---- 8 backlog KPIs ----
s=slide(); lockup(s); footer(s,num())
eyebrow(s,0.6,1.0,"SEG 03 . THE PRIVATE BACKLOG")
text(s,0.6,1.35,12.1,0.6,[[("There is no shortage of exit-scale companies",28,INK,True,SANS)]])
kp=[("ACTIVE US UNICORNS","945","Record, Q2 2026",INK),
    ("AGGREGATE UNICORN VALUE","$5.3T","+9.4% vs year-end 2025",INK),
    ("HELD BY SPACEX, OPENAI, ANTHROPIC",">25%","Three names, a quarter of the herd",INK),
    ("2025 UNICORN IPOs","17","14 priced below their mark",NEG),
    ("LP CASH OUT > CASH BACK","4 yrs","Distributions have trailed",INK)]
x=0.6; w=2.42
for l,v,d,c in kp:
    box(s,x,2.55,w-0.12,2.55,fill=PANEL,rad=True)
    text(s,x+0.22,2.8,w-0.42,0.95,[[(l,9.5,MUTED,True,MONO,0.03)]],line_sp=1.0)
    text(s,x+0.22,3.78,w-0.42,0.8,[[(v,34,c,True,SANS)]])
    text(s,x+0.22,4.5,w-0.42,0.5,[[(d,10.5,INK2,False,SANS)]],line_sp=1.0)
    x+=w
text(s,0.6,5.4,12.1,1.2,[[("The backlog is a liquidity choice, not an absence of exits. Mega-rounds plus secondary markets (annualized ~$112B in Q1 2026) let companies stay private while an IPO is telegraphed. ~30% of unicorns are AI-native or AI-adjacent.",15,INK2,False,SANS)]],line_sp=1.1)

# ---- 9 spacex ----
s=slide(); lockup(s); footer(s,num())
eyebrow(s,0.6,1.0,"SEG 03 . FIG 3")
text(s,0.6,1.35,12.2,0.6,[[("One listing versus a decade of the asset class",26,INK,True,SANS)]])
chart_panel(s,FIG_SPACEX,0.6,2.25,8.0,3.5)
text(s,8.95,2.5,3.8,4,[[("SpaceX priced at a $1.78T valuation and closed day one near $2.1T.",16,INK,True,SANS)],
    [("That single number exceeds the combined value of every US venture-backed public listing since 2016.",13.5,INK2,False,SANS)],
    [("",6,INK2,False,SANS)],
    [("\"IPO drought\" is the wrong frame: the pipe is holding a few objects too large to move.",13.5,BRAND2,True,SANS)]],line_sp=1.08,sp_after=8)
text(s,0.6,6.15,12,0.3,[[("Source: PitchBook Q2 2026 Venture Monitor; CNBC Jun 12 2026. The looser \"half of every tech IPO since the internet\" claim is not sourceable; this is the verifiable version.",10,MUTED,False,MONO)]])

# ---- 10 databricks (UPDATED $188B) ----
s=slide(); lockup(s); footer(s,num())
eyebrow(s,0.6,1.0,"SEG 03 . FIG 4")
text(s,0.6,1.35,12.2,0.6,[[("Databricks: a $47M to $188B climb, still private",26,INK,True,SANS)]])
chart_panel(s,FIG_DBX,0.6,2.25,8.0,3.7)
text(s,8.95,2.5,3.85,4,[[("NEW: $188B strategic round.",15.5,AMBER,True,SANS)],
    [("Term sheet signed July 16 2026, led by Coatue, expected to close this summer, up from the $134B Series L (Feb 2026).",13.5,INK2,False,SANS)],
    [("",6,INK2,False,SANS)],
    [("Why raise at this scale? Private capital is cheap and CEO Ali Ghodsi called 2026 \"a terrible year to go public.\" The company never needed the exit.",13.5,INK,False,SANS)]],line_sp=1.06,sp_after=8)
text(s,0.6,6.25,12,0.3,[[("Source: Databricks newsroom & Bloomberg, Jul 16-17 2026 ($188B term sheet); PitchBook Premium financing records (entity 59199-40). $134B is the last closed round.",10,MUTED,False,MONO)]])

# ---- 11 anthropic ----
s=slide(); lockup(s); footer(s,num())
eyebrow(s,0.6,1.0,"SEG 03 . FIG 5")
text(s,0.6,1.35,12.2,0.6,[[("Anthropic: the revenue the IPO is timed around",26,INK,True,SANS)]])
chart_panel(s,FIG_ANTH,0.6,2.25,8.0,3.7)
text(s,8.95,2.5,3.85,4,[[("$87M to ~$47B run-rate in 17 months,",15.5,INK,True,SANS)],
    [("overtaking OpenAI on ARR in April 2026. Now $965B (Series H), filed confidentially in June for an expected October listing.",13.5,INK2,False,SANS)],
    [("",6,INK2,False,SANS)],
    [("The risk is the narrative, not demand: an enterprise shift away from \"token maxing,\" plus export-control uncertainty on chips.",13.5,BRAND2,True,SANS)]],line_sp=1.06,sp_after=8)
text(s,0.6,6.25,12,0.3,[[("Source: PitchBook Premium; TechCrunch / VentureBeat / CNBC, Jan 2024 to May 2026. Run-rate figures annualized.",10,MUTED,False,MONO)]])

# ---- 12 SEG 4 DIVIDER ----
s=slide(); lockup(s); footer(s,num())
segno(s,0.6,3.0,"SEG 04")
eyebrow(s,0.6,3.62,"THE IDEA: TWO WINNERS IN EVERY CATEGORY")
text(s,0.6,4.0,12.4,1.6,[[("It is not a duopoly.",40,INK,True,SANS)],
                         [("It is winner-take-most, miscounted",40,S6,True,SANS)]])

# ---- 13 ratio (money slide) ----
s=slide(); lockup(s); footer(s,num())
eyebrow(s,0.6,0.95,"SEG 04 . FIG 6")
text(s,0.6,1.28,12.2,0.6,[[("The #1-to-#2 valuation ratio across 16 AI verticals",24,INK,True,SANS)]])
chart_panel(s,FIG_RATIO,0.55,1.95,8.2,5.0)
text(s,9.0,2.2,3.8,4.6,[[("A true duopoly sits near 1x.",16,INK,True,SANS)],
    [("Only formal math and foundation models qualify (green).",13,INK2,False,SANS)],
    [("",5,INK2,False,SANS)],
    [("Of 16 verticals: 2 near-parity, 5 above 10x, and 3 more where the #2 has no venture mark at all.",13,INK,True,SANS)],
    [("",5,INK2,False,SANS)],
    [("The modal outcome is not a split. It is one company many times larger than whatever sits in second.",13,BRAND2,True,SANS)]],line_sp=1.05,sp_after=6)
text(s,9.0,6.55,3.9,0.4,[[("Voice AI uses ElevenLabs' $11B priced mark; the rumored $22B secondary reads as 61x.",9,MUTED,False,MONO)]],line_sp=1.05)

# ---- 14 fund != business ----
s=slide(); lockup(s); footer(s,num())
eyebrow(s,0.6,1.0,"SEG 04 . FIG 7")
text(s,0.6,1.35,12.2,0.6,[[("The biggest round is not the biggest business",26,INK,True,SANS)]])
chart_panel(s,FIG_FUND,0.6,2.2,7.4,4.1)
text(s,8.3,2.4,4.5,4,[[("Blue: valuation.  Green: disclosed revenue.",12.5,INK2,True,MONO)],
    [("",8,INK,False,SANS)],
    [("Surge out-earns Scale with zero venture funding. Otter out-earns Granola on disclosed revenue. Midjourney does ~$500M and has no valuation to plot.",14,INK,False,SANS)],
    [("",8,INK,False,SANS)],
    [("Frame winners by round size and you miss the best unit economics in the category.",14,BRAND2,True,SANS)]],line_sp=1.1,sp_after=6)
text(s,0.6,6.5,12,0.3,[[("Source: PitchBook Premium. Scale ~$1B rev / $29B val; Surge ~$1.4B rev, no VC; Otter ~$0.1B rev / $94M val; Granola $1.5B val, rev undisclosed.",10,MUTED,False,MONO)]])

# ---- 15 crossover matrix ----
s=slide(); lockup(s); footer(s,num())
eyebrow(s,0.6,1.0,"SEG 04 . FIG 8")
text(s,0.6,1.35,12.2,0.6,[[("Who manufactures the \"2\": the same funds sit on both sides",25,INK,True,SANS)]])
chart_panel(s,FIG_MATRIX,0.6,2.15,7.6,4.2)
text(s,8.5,2.4,4.3,0.5,[[("●",14,BRAND,True,SANS),("  Backs the #1        ",12.5,INK2,False,MONO),("○",14,AMBER,True,SANS),("  Backs the #2",12.5,INK2,False,MONO)]])
text(s,8.5,3.1,4.35,3.4,[[("a16z holds both #1 and #2 in legal (Harvey + Legora) and health scribes (Abridge + Ambience).",14,INK,True,SANS)],
    [("",6,INK,False,SANS)],
    [("Concentration is not only at the company level. The same handful of crossover funds capitalizes both seats, a hedge that manufactures a \"2\" rather than picking a winner.",13.5,INK2,False,SANS)]],line_sp=1.08,sp_after=8)
text(s,0.6,6.5,12,0.3,[[("Source: PitchBook Premium investor records. Sequoia backs Harvey but not Legora; Kleiner backs Harvey and Harmonic but not Cerebras.",10,MUTED,False,MONO)]])

# ---- 16 frontier paradox ----
s=slide(); lockup(s); footer(s,num())
eyebrow(s,0.6,1.0,"SEG 04 . AT THE FRONTIER")
text(s,0.6,1.35,12.2,0.6,[[("The two-name story breaks at the top too",26,INK,True,SANS)]])
box(s,0.6,2.4,5.9,3.5,fill=PANEL,rad=True)
text(s,0.95,2.7,5.3,0.5,[[("THE VALUATION-QUALITY PARADOX",11,AMBER,True,MONO,0.06)]])
text(s,0.95,3.25,5.2,0.8,[[("Databricks",30,BRAND,True,SANS),("  AIBQ 8.7",18,INK2,True,SANS)]])
text(s,0.95,4.0,5.2,0.5,[[("Tops the Frontier Five, only member with positive free cash flow.",13,INK2,False,SANS)]],line_sp=1.05)
box(s,0.95,4.75,5.2,0.02,fill=GRID)
text(s,0.95,4.95,5.2,0.8,[[("OpenAI",30,NEG,True,SANS),("  AIBQ 4.8",18,INK2,True,SANS)]])
text(s,0.95,5.7,5.2,0.4,[[("Highest profile, lowest business-quality score.",13,INK2,False,SANS)]])
text(s,6.9,2.5,6,4,[[("\"Anthropic vs OpenAI\" reads as a clean 1.1x duopoly ($965B vs $852B).",17,INK,True,SANS)],
    [("",6,INK,False,SANS)],
    [("But PitchBook's Frontier Five note counts five, not two, and the highest-valued names score lowest on quality. And xAI is not a standalone third: it is $250B folded inside a ~$2.4T SpaceX.",14.5,INK2,False,SANS)],
    [("",6,INK,False,SANS)],
    [("The two-name story does not survive contact with the cap tables.",15,BRAND2,True,SANS)]],line_sp=1.1,sp_after=8)

# ---- 17 closing ----
s=slide(); lockup(s); footer(s,num())
box(s,0,0,0.22,7.5,fill=BRAND)
eyebrow(s,0.7,1.2,"THE THROUGH-LINE")
text(s,0.7,1.7,11.6,2.0,[[("Count the business,",44,INK,True,SANS)],[("not the round",44,BRAND,True,SANS)]])
pts=[("Durability is measurable","and has a history you can chart. It moved up the stack from the model to the workflow."),
     ("The IPO drought is a choice","not an absence of exit-scale companies. The value is private, and enormous."),
     ("The \"duopoly\" is winner-take-most","with a nominal second place that funding data overstates.")]
x=0.7
for h,d in pts:
    box(s,x,4.15,3.9,2.1,fill=PANEL,rad=True)
    text(s,x+0.3,4.4,3.4,0.8,[[(h,16,INK,True,SANS)]],line_sp=1.0)
    text(s,x+0.3,5.35,3.4,0.9,[[(d,12.5,INK2,False,SANS)]],line_sp=1.05)
    x+=4.1
text(s,0.7,6.55,12,0.4,[[("Sources: PitchBook Premium (financing, investors, VC Exit Predictor, Venture Monitor, Frontier Five); Madrona/PitchBook IA40; company disclosures; CNBC, Bloomberg, TechCrunch. Figures verified July 17, 2026.",9.5,MUTED,False,MONO)]],line_sp=1.1)

prs.save(OUT)
print("Saved", OUT, "with", len(prs.slides._sldIdLst), "slides")

# ---- write HTML preview mirror ----
body="".join("".join(buf)+"</div>" for buf in HTML_SLIDES)
html=("<!doctype html><meta charset='utf-8'><style>"
      "body{margin:0;background:#333;font-family:Arial,system-ui,sans-serif}"
      ".slide{position:relative;width:1280px;height:720px;margin:16px auto;overflow:hidden}"
      "</style>"+body)
prev=os.path.join(CH,"preview.html")
open(prev,"w").write(html)
print("Preview", prev)
