import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["text.parse_math"]=False
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import numpy as np

# company, composite, primary $B (last round; † model), flag
D=[("Databricks",8.19,134,""),("Stripe",8.15,159,""),("Canva",7.92,42,""),
("Revolut",7.85,75,""),("SpaceX",7.60,2026.24,"m"),("Rippling",7.24,16.8,""),
("Anthropic",7.22,965,""),("Ramp",7.15,32,""),("Deel",6.98,17.3,""),
("Anduril",6.94,61,""),("Applied Intuition",6.91,15,""),("Epic Games",6.89,22.5,""),
("Kraken",6.69,20,""),("Ripple",6.58,40,""),("OpenAI",6.30,852,""),
("Cursor",6.05,29.3,""),("Cerebras",5.92,57.1,"m"),("Perplexity",5.12,20,""),
("Figure AI",3.75,39,""),("Neuralink",2.50,9.65,"")]

POS="#2a78d6"; NEG="#eb6834"; NOISE="#c5c9d1"
INK="#0b0b0b"; SEC="#52514e"; MUT="#8a8983"; SURF="#fcfcfb"; GRID="#e8e8e4"

# ---------- Chart 2: quality-for-size residual ----------
x=np.log10([v for _,_,v,_ in D]); y=np.array([s for _,s,_,_ in D])
b,a=np.polyfit(x,y,1)
pred=a+b*x; res=y-pred
r2=1-np.sum((y-pred)**2)/np.sum((y-np.mean(y))**2)
rows=sorted(zip([n for n,_,_,_ in D],res,[f for _,_,_,f in D]),key=lambda r:-r[1])

fig,ax=plt.subplots(figsize=(11.6,9.0),dpi=200)
fig.patch.set_facecolor(SURF); ax.set_facecolor(SURF)
n=len(rows); ys=list(range(n,0,-1))
for (name,r,fl),yy in zip(rows,ys):
    c=NOISE if abs(r)<0.5 else (POS if r>0 else NEG)
    ax.barh(yy,r,height=0.62,color=c,zorder=3)
    dag="†" if fl=="m" else ""
    if r>=0:
        ax.text(r+0.06,yy,f"+{r:.1f}",va="center",ha="left",fontsize=8.4,color=SEC)
        ax.text(-0.06,yy,f"{name}{dag}",va="center",ha="right",fontsize=9.0,color=INK)
    else:
        ax.text(r-0.06,yy,f"{r:.1f}",va="center",ha="right",fontsize=8.4,color=SEC)
        ax.text(0.06,yy,f"{name}{dag}",va="center",ha="left",fontsize=9.0,color=INK)
ax.axvline(0,color="#9a9a94",lw=1.1,zorder=4)
ax.set_xlim(-3.4,2.4); ax.set_ylim(0.3,n+0.7)
ax.set_yticks([])
ax.set_xticks([-3,-2,-1,0,1,2])
ax.set_xticklabels(["-3","-2","-1","0","+1","+2"],fontsize=9.5,color=SEC)
ax.grid(axis="x",color=GRID,lw=0.7,zorder=0); ax.set_axisbelow(True)
ax.set_xlabel("Composite score above or below the level predicted by company size (points)",
              fontsize=10,color=SEC,labelpad=10)
for s in ("top","right","left"): ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color("#d9d9d3")

fig.text(0.008,0.972,"Quality for Size: Who Carries More Quality Than Their Valuation Predicts",
         fontsize=15,fontweight="bold",color=INK,va="top")
fig.text(0.008,0.940,f"Each bar is the company's composite minus the score predicted by its valuation "
         f"(fit of score on log valuation across the twenty, which explains {r2:.0%} of the variance).",
         fontsize=9.8,color=SEC,va="top")
fig.text(0.008,0.918,"Size drops out by construction: this is quality relative to companies of the same scale.",
         fontsize=9.8,color=SEC,va="top")
leg=[Patch(color=POS,label="More quality than size predicts"),
     Patch(color=NEG,label="Less quality than size predicts"),
     Patch(color=NOISE,label="Within the noise band (about half a point)")]
ax.legend(handles=leg,loc="upper left",frameon=False,fontsize=9,labelcolor=SEC,borderpad=0.8)
fig.text(0.008,0.034,"Source: AIBQ/PBQ Panel as of 2026-06-30; Unicorn Monitor Top20_Marks (primary valuations). "
         "Score confidence bands are ±2.75 to ±3.75, so residuals under half a point are not ranked.",
         fontsize=7.6,color=MUT,va="bottom")
fig.text(0.008,0.012,"† SpaceX and Cerebras have no private last round; their valuation is the Morningstar model estimate.",
         fontsize=7.6,color=MUT,va="bottom")
fig.subplots_adjust(left=0.05,right=0.975,top=0.88,bottom=0.10)
fig.savefig("/home/user/pitchbook-analyst-agent/templates/q2_2026_quality_for_size.png",facecolor=SURF)
plt.close(fig)
print("wrote residual chart; fit: score = %.2f + %.2f*log10(V), R2=%.3f"%(a,b,r2))

# ---------- Chart 3: rank gap bump ----------
byval=sorted(D,key=lambda r:(-r[2],-r[1]))     # valuation rank (tie -> higher score first)
byq=sorted(D,key=lambda r:-r[1])               # quality rank
vr={r[0]:i+1 for i,r in enumerate(byval)}
qr={r[0]:i+1 for i,r in enumerate(byq)}

fig,ax=plt.subplots(figsize=(10.6,10.6),dpi=200)
fig.patch.set_facecolor(SURF); ax.set_facecolor(SURF)
XL,XR=0.34,0.66
def vfmt(v): return f"${v/1000:.2f}T" if v>=1000 else f"${v:g}B"
for name,sc,val,fl in D:
    g=vr[name]-qr[name]
    c=NOISE if g==0 else (POS if g>0 else NEG)
    ax.plot([XL,XR],[vr[name],qr[name]],color=c,lw=1.9,alpha=0.9,zorder=3,solid_capstyle="round")
    ax.scatter([XL],[vr[name]],s=40,color="#8a8983",edgecolor=SURF,linewidth=1.0,zorder=4)
    ax.scatter([XR],[qr[name]],s=46,color=c,edgecolor=SURF,linewidth=1.0,zorder=5)
    dag="†" if fl=="m" else ""
    ax.text(XL-0.02,vr[name],f"{vr[name]}.  {name}{dag}   {vfmt(val)}",ha="right",va="center",fontsize=8.6,color=INK)
    gs=f"  ({'+' if g>0 else ''}{g})" if g!=0 else "  (0)"
    ax.text(XR+0.02,qr[name],f"{qr[name]}.  {name}   {sc:.2f}{gs}",ha="left",va="center",fontsize=8.6,color=INK)
ax.text(XL,-0.4,"RANKED BY VALUATION",ha="center",va="top",fontsize=9.5,color=SEC,fontweight="bold")
ax.text(XR,-0.4,"RANKED BY QUALITY",ha="center",va="top",fontsize=9.5,color=SEC,fontweight="bold")
ax.set_xlim(0,1); ax.set_ylim(21.0,-1.2)
ax.axis("off")
fig.text(0.008,0.977,"Price Rank Against Quality Rank: Twelve Places of Disagreement",
         fontsize=15,fontweight="bold",color=INK,va="top")
fig.text(0.008,0.949,"The same twenty companies ranked by primary valuation and by AIBQ/PBQ composite. The number in "
         "parentheses is places gained or lost on quality.",fontsize=9.8,color=SEC,va="top")
fig.text(0.008,0.928,"Rippling climbs twelve places on quality. OpenAI falls twelve. Neuralink is last on both lists.",
         fontsize=9.8,color=SEC,va="top")
leg=[Line2D([0],[0],color=POS,lw=2,label="Ranks higher on quality than on price"),
     Line2D([0],[0],color=NEG,lw=2,label="Ranks lower on quality than on price")]
ax.legend(handles=leg,loc="lower center",frameon=False,fontsize=9,labelcolor=SEC,ncol=2,bbox_to_anchor=(0.5,-0.055))
fig.text(0.008,0.030,"Source: AIBQ/PBQ Panel as of 2026-06-30; Unicorn Monitor Top20_Marks (primary valuations). "
         "Kraken and Perplexity share a $20B valuation and are tie-broken by score.",fontsize=7.6,color=MUT,va="bottom")
fig.text(0.008,0.010,"† SpaceX and Cerebras have no private last round; their valuation is the Morningstar model estimate.",
         fontsize=7.6,color=MUT,va="bottom")
fig.subplots_adjust(left=0.02,right=0.98,top=0.895,bottom=0.075)
fig.savefig("/home/user/pitchbook-analyst-agent/templates/q2_2026_rank_gap.png",facecolor=SURF)
plt.close(fig)
print("wrote rank chart; biggest moves:",sorted(((vr[n]-qr[n],n) for n,_,_,_ in D))[:2],
      sorted(((vr[n]-qr[n],n) for n,_,_,_ in D))[-2:])
