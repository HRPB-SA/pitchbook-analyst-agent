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
INK="#0b0b0b"; SEC="#52514e"; MUT="#8a8983"; SURF="#fcfcfb"; GRID="#e8e8e4"

fig,ax=plt.subplots(figsize=(10.6,9.6),dpi=200)
fig.patch.set_facecolor(SURF); ax.set_facecolor(SURF)

lo,hi=1.1,420
xs=np.array([lo,hi])
ax.fill_between(xs,xs,hi,color="#eef3f9",zorder=0)
ax.fill_between(xs,lo,xs,color="#fdf3ee",zorder=0)
ax.plot([lo,hi],[lo,hi],color="#b9b9b2",lw=1.1,zorder=2)
ax.text(150,120,"secondary = primary",rotation=38,fontsize=8.5,color=MUT,va="top",ha="center")
ax.text(2.1,300,"secondary market pays more\nper quality point",fontsize=9,color=ABOVE,va="top")
ax.text(60,1.55,"secondary market pays less\nper quality point",fontsize=9,color=BELOW,va="bottom",ha="left")

for name,sc,pp,ps,fl in D:
    c=ABOVE if ps>=pp else BELOW
    ax.scatter([pp],[ps],s=110,color=c,edgecolor=SURF,linewidth=1.5,zorder=5)

OFF={"Applied Intuition":(-8,12,"right"),"Rippling":(10,-8,"left"),"Deel":(-10,-4,"right"),
"Kraken":(8,-10,"left"),"Epic Games":(10,-4,"left"),"Neuralink":(0,13,"center"),
"Perplexity":(11,2,"left"),"Ramp":(-11,4,"right"),"Cursor":(-10,8,"right"),
"Canva":(11,-2,"left"),"Ripple":(10,-6,"left"),"Anduril":(-11,6,"right"),
"Revolut":(11,4,"left"),"Cerebras":(11,-7,"left"),"Figure AI":(11,-2,"left"),
"Databricks":(-11,6,"right"),"Stripe":(11,-4,"left"),"Anthropic":(-11,7,"right"),
"OpenAI":(11,-6,"left"),"SpaceX":(-11,-10,"right")}
for name,sc,pp,ps,fl in D:
    dx,dy,ha=OFF[name]
    dag="†" if fl=="m" else ""
    ax.annotate(f"{name}{dag}",(pp,ps),textcoords="offset points",xytext=(dx,dy),
                ha=ha,va="center",fontsize=8.4,color=INK,zorder=6)

ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlim(lo,hi); ax.set_ylim(lo,hi)
ticks=[2,5,10,25,50,100,250]
ax.set_xticks(ticks); ax.set_xticklabels([f"${t}B" for t in ticks],fontsize=9,color=SEC)
ax.set_yticks(ticks); ax.set_yticklabels([f"${t}B" for t in ticks],fontsize=9,color=SEC)
ax.grid(color=GRID,lw=0.6,zorder=1); ax.set_axisbelow(True)
ax.set_xlabel("Primary market: last-round valuation per quality point (log scale)",fontsize=10,color=SEC,labelpad=9)
ax.set_ylabel("Secondary market: traded valuation per quality point (log scale)",fontsize=10,color=SEC,labelpad=9)
for s in ("top","right"): ax.spines[s].set_visible(False)
for s in ("left","bottom"): ax.spines[s].set_color("#d9d9d3")

fig.text(0.008,0.976,"Two Markets Price the Same Point of Quality Almost Identically",
         fontsize=15,fontweight="bold",color=INK,va="top")
fig.text(0.008,0.946,"Each dot is one company: what the primary market paid per point of AIBQ/PBQ composite against what the "
         "secondary market pays.",fontsize=9.8,color=SEC,va="top")
fig.text(0.008,0.925,"The cluster hugs the diagonal, so the disagreements, Neuralink and Kraken furthest from the line, are the story.",
         fontsize=9.8,color=SEC,va="top")

fig.text(0.008,0.030,"Source: AIBQ/PBQ Panel as of 2026-06-30 (composites); Unicorn Monitor Top20_Marks (valuations). "
         "† SpaceX and Cerebras have no private last round; their primary reference is the model valuation.",
         fontsize=7.6,color=MUT,va="bottom")
fig.subplots_adjust(left=0.075,right=0.972,top=0.88,bottom=0.10)
out="/home/user/pitchbook-analyst-agent/templates/q2_2026_quality_per_dollar_scatter.png"
fig.savefig(out,facecolor=SURF)
print("wrote",out)
