import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["text.parse_math"]=False
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

RAW=[("Databricks",8.19,134,139.4,""),("Stripe",8.15,159,167.2,""),("Canva",7.92,42,42.11,""),
("Revolut",7.85,75,87.06,""),("SpaceX",7.60,2026.24,1376.55,"m"),("Rippling",7.24,16.8,16.98,""),
("Anthropic",7.22,965,989.6,""),("Ramp",7.15,32,33.99,""),("Deel",6.98,17.3,15.47,""),
("Anduril",6.94,61,74.5,""),("Applied Intuition",6.91,15,20.47,""),("Epic Games",6.89,22.5,14.47,""),
("Kraken",6.69,20,9.88,""),("Ripple",6.58,40,21.23,""),("OpenAI",6.30,852,787.2,""),
("Cursor",6.05,29.3,38.21,""),("Cerebras",5.92,57.1,61.45,"m"),("Perplexity",5.12,20,17.25,""),
("Figure AI",3.75,39,30.14,""),("Neuralink",2.50,9.65,42.84,"")]
D=[(n,s,ref/s,mkt/s,fl) for n,s,ref,mkt,fl in RAW]

ABOVE="#2a78d6"; BELOW="#eb6834"
INK="#0b0b0b"; SEC="#52514e"; MUT="#8a8983"; SURF="#fcfcfb"

def spread(pairs,min_gap=0.055):
    # pairs: list of (key, log10 y). Return dict key->adjusted log y, preserving order, min gap apart.
    s=sorted(pairs,key=lambda p:p[1])
    out={}
    prev=None
    for k,v in s:
        if prev is not None and v-prev<min_gap: v=prev+min_gap
        out[k]=v; prev=v
    return out

fig,ax=plt.subplots(figsize=(10.2,10.4),dpi=200)
fig.patch.set_facecolor(SURF); ax.set_facecolor(SURF)

XL,XR=0.32,0.68
Lpos=spread([(n,np.log10(pp)) for n,_,pp,_,_ in D])
Rpos=spread([(n,np.log10(ps)) for n,_,_,ps,_ in D])

for name,sc,pp,ps,fl in D:
    c=ABOVE if ps>=pp else BELOW
    ax.plot([XL,XR],[np.log10(pp),np.log10(ps)],color=c,lw=1.8,alpha=0.85,zorder=3,solid_capstyle="round")
    ax.scatter([XL],[np.log10(pp)],s=42,color="#8a8983",edgecolor=SURF,linewidth=1.1,zorder=4)
    ax.scatter([XR],[np.log10(ps)],s=48,color=c,edgecolor=SURF,linewidth=1.1,zorder=5)
    dag="†" if fl=="m" else ""
    ax.text(XL-0.022,Lpos[name],f"{name}{dag}  ${pp:,.1f}B",ha="right",va="center",fontsize=8.4,color=INK)
    ax.text(XR+0.022,Rpos[name],f"${ps:,.1f}B  {name}{dag}",ha="left",va="center",fontsize=8.4,color=INK)
    if abs(Lpos[name]-np.log10(pp))>0.012:
        ax.plot([XL-0.02,XL-0.006],[Lpos[name],np.log10(pp)],color="#d0d0ca",lw=0.6,zorder=2)
    if abs(Rpos[name]-np.log10(ps))>0.012:
        ax.plot([XR+0.006,XR+0.02],[np.log10(ps),Rpos[name]],color="#d0d0ca",lw=0.6,zorder=2)

ax.text(XL,np.log10(430),"PRIMARY MARKET\nlast round per point",ha="center",va="bottom",fontsize=9.5,color=SEC,fontweight="bold")
ax.text(XR,np.log10(430),"SECONDARY MARKET\ntraded value per point",ha="center",va="bottom",fontsize=9.5,color=SEC,fontweight="bold")

ax.text(0.5,np.log10(52),"no company in either market prices between about \$21B and \$125B per point:\nthe price of quality is two-tier",
        ha="center",va="center",fontsize=9,color="#8a8983",style="italic")
ax.set_xlim(0,1); ax.set_ylim(np.log10(1.1),np.log10(650))
ax.axis("off")

fig.text(0.008,0.978,"Where the Two Markets Re-Rank the Price of Quality",
         fontsize=15,fontweight="bold",color=INK,va="top")
fig.text(0.008,0.950,"Valuation per point of AIBQ/PBQ composite in each market, log scale. Flat lines mean agreement.",
         fontsize=9.8,color=SEC,va="top")
fig.text(0.008,0.930,"The steep lines are the disagreements: Neuralink re-prices upward on a stale 2021 round, Kraken and Ripple downward.",
         fontsize=9.8,color=SEC,va="top")

leg=[Line2D([0],[0],color=ABOVE,lw=2,label="Secondary pays more per point"),
     Line2D([0],[0],color=BELOW,lw=2,label="Secondary pays less per point")]
ax.legend(handles=leg,loc="lower center",frameon=False,fontsize=9,labelcolor=SEC,ncol=2,
          bbox_to_anchor=(0.5,-0.01))

fig.text(0.008,0.040,"Source: AIBQ/PBQ Panel as of 2026-06-30 (composites); Unicorn Monitor Top20_Marks (valuations).",
         fontsize=7.6,color=MUT,va="bottom")
fig.text(0.008,0.018,"† SpaceX and Cerebras have no private last round; their primary reference is the model valuation.",
         fontsize=7.6,color=MUT,va="bottom")
fig.subplots_adjust(left=0.03,right=0.97,top=0.885,bottom=0.075)
out="/home/user/pitchbook-analyst-agent/templates/q2_2026_quality_per_dollar_slope.png"
fig.savefig(out,facecolor=SURF)
print("wrote",out)
