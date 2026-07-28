import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["text.parse_math"]=False
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# company, composite, reference $B (last round; model† for public listings), market $B (secondary/public), flag
D=[("Databricks",8.19,134,139.4,""),("Stripe",8.15,159,167.2,""),("Canva",7.92,42,42.11,""),
("Revolut",7.85,75,87.06,""),("SpaceX",7.60,2026.24,1376.55,"m"),("Rippling",7.24,16.8,16.98,""),
("Anthropic",7.22,965,989.6,""),("Ramp",7.15,32,33.99,""),("Deel",6.98,17.3,15.47,""),
("Anduril",6.94,61,74.5,""),("Applied Intuition",6.91,15,20.47,""),("Epic Games",6.89,22.5,14.47,""),
("Kraken",6.69,20,9.88,""),("Ripple",6.58,40,21.23,""),("OpenAI",6.30,852,787.2,""),
("Cursor",6.05,29.3,38.21,""),("Cerebras",5.92,57.1,61.45,"m"),("Perplexity",5.12,20,17.25,""),
("Figure AI",3.75,39,30.14,""),("Neuralink",2.50,9.65,42.84,"")]

ABOVE="#2a78d6"; BELOW="#eb6834"; PRIM="#8a8983"
INK="#0b0b0b"; SEC="#52514e"; MUT="#8a8983"; SURF="#fcfcfb"; GRID="#e8e8e4"

fig,ax=plt.subplots(figsize=(11.8,9.3),dpi=200)
fig.patch.set_facecolor(SURF); ax.set_facecolor(SURF)

n=len(D)
ys=list(range(n,0,-1))
for (name,sc,ref,mkt,fl),y in zip(D,ys):
    c=ABOVE if mkt>=ref else BELOW
    ax.plot([ref,mkt],[y,y],color=c,lw=2,zorder=3,solid_capstyle="round")
    ax.scatter([ref],[y],s=64,facecolor=SURF,edgecolor=PRIM,linewidth=1.8,zorder=4)
    ax.scatter([mkt],[y],s=80,color=c,edgecolor=SURF,linewidth=1.4,zorder=5)
    gap=mkt/ref-1
    dag="†" if fl=="m" else ""
    ax.text(max(ref,mkt)*1.18,y,f"{gap:+.0%}{dag}",va="center",ha="left",fontsize=8.3,
            color=(ABOVE if gap>=0 else BELOW),zorder=5)

ax.set_yticks(ys)
ax.set_yticklabels([f"{name}   {sc:.2f}" for name,sc,_,_,_ in D],fontsize=9.2,color=INK)
ax.tick_params(axis="y",length=0)

ax.set_xscale("log")
ax.set_xlim(7,5200)
ticks=[10,25,50,100,250,500,1000,2500]
ax.set_xticks(ticks)
ax.set_xticklabels([f"${t}B" if t<1000 else f"${t/1000:g}T" for t in ticks],fontsize=9,color=SEC)
ax.grid(axis="x",color=GRID,lw=0.7,zorder=0); ax.set_axisbelow(True)
ax.set_xlabel("Valuation, log scale (as of June 30, 2026)",fontsize=10,color=SEC,labelpad=9)
for s in ("top","right","left"): ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color("#d9d9d3")
ax.set_ylim(0.3,n+0.9)

ineur=[i for i,(nm,_,_,_,_) in enumerate(D) if nm=="Neuralink"][0]
ax.annotate("stale 2021 round, not demand",xy=(42.84,ys[ineur]),xytext=(90,ys[ineur]-0.05),
            fontsize=8,color=SEC,va="center",
            arrowprops=dict(arrowstyle="-",color="#b9b9b2",lw=0.7,shrinkB=4))

fig.text(0.008,0.974,"The Secondary Market Agrees With the Quality Scores",
         fontsize=15.5,fontweight="bold",color=INK,va="top")
fig.text(0.008,0.944,"All twenty companies sorted by AIBQ/PBQ composite (shown beside each name).",fontsize=9.8,color=SEC,va="top")
fig.text(0.008,0.922,"Higher-scored companies trade above their reference valuation; lower-scored ones trade below it.",fontsize=9.8,color=SEC,va="top")

leg=[Line2D([0],[0],marker="o",color="none",markerfacecolor=SURF,markeredgecolor=PRIM,
            markeredgewidth=1.8,markersize=9,label="Reference: last private round († = model valuation)"),
     Line2D([0],[0],marker="o",color="none",markerfacecolor=ABOVE,markeredgecolor=SURF,
            markersize=9,label="Market price above reference"),
     Line2D([0],[0],marker="o",color="none",markerfacecolor=BELOW,markeredgecolor=SURF,
            markersize=9,label="Market price below reference")]
ax.legend(handles=leg,loc="lower right",frameon=False,fontsize=9,labelcolor=SEC,
          handletextpad=0.6,borderpad=0.8,labelspacing=0.6)

fig.text(0.008,0.036,"Source: AIBQ/PBQ Panel as of 2026-06-30 (composites); Unicorn Monitor Top20_Marks (valuations). "
         "Labels show the market premium or discount to the reference.",fontsize=7.6,color=MUT,va="bottom")
fig.text(0.008,0.014,"† SpaceX and Cerebras listed publicly during the quarter and have no private last round; their "
         "reference is the Morningstar model valuation and the filled dot is their public market value.",
         fontsize=7.6,color=MUT,va="bottom")

fig.subplots_adjust(left=0.185,right=0.965,top=0.885,bottom=0.105)
out="/home/user/pitchbook-analyst-agent/templates/q2_2026_quality_vs_secondary.png"
fig.savefig(out,facecolor=SURF)
print("wrote",out)
