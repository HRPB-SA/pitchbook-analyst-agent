import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["text.parse_math"]=False      # dollar signs are literal
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

D=[("Databricks",134,8.19,"AIBQ"),("Stripe",159,8.15,"PBQ"),("Canva",42,7.92,"PBQ"),
("Revolut",75,7.85,"PBQ"),("SpaceX",2110,7.60,"PBQ"),("Rippling",16.8,7.24,"PBQ"),
("Anthropic",965,7.22,"AIBQ"),("Ramp",44.03,7.15,"PBQ"),("Deel",17.3,6.98,"PBQ"),
("Anduril",61,6.94,"PBQ"),("Applied Intuition",15,6.91,"AIBQ"),("Epic Games",22.5,6.89,"PBQ"),
("Kraken",20,6.69,"PBQ"),("Ripple",40,6.58,"PBQ"),("OpenAI",852,6.30,"AIBQ"),
("Cursor",60,6.05,"AIBQ"),("Cerebras",40.63,5.92,"AIBQ"),("Perplexity",20,5.12,"AIBQ"),
("Figure AI",39,3.75,"AIBQ"),("Neuralink",9.65,2.50,"PBQ")]

AIBQ="#2a78d6"; PBQ="#eb6834"
INK="#0b0b0b"; SEC="#52514e"; MUT="#8a8983"; SURF="#fcfcfb"; GRID="#e8e8e4"; LEAD="#b9b9b2"

fig,ax=plt.subplots(figsize=(12.4,7.6),dpi=200)
fig.patch.set_facecolor(SURF); ax.set_facecolor(SURF)

for lo,hi,lab,col in [(8.0,9.0,"Elite","#eef3f9"),(6.5,8.0,"Strong","#f5f7f9"),
                      (4.5,6.5,"Developing","#faf9f6"),(2.0,4.5,"Distressed","#fdf5f2")]:
    ax.axhspan(lo,hi,color=col,zorder=0)
    ax.text(0.995,hi-0.13,lab,transform=ax.get_yaxis_transform(),ha="right",va="top",
            fontsize=8.5,color=MUT,style="italic",zorder=1)
for y in (4.5,6.5,8.0): ax.axhline(y,color="#dcdcd6",lw=0.9,zorder=1)
ax.grid(axis="x",color=GRID,lw=0.7,zorder=1); ax.set_axisbelow(True)

# label offsets in points; lead=True draws a thin leader line
OFF={"Databricks":(-46,16,True),"Stripe":(30,-15,True),"Canva":(0,15,False),
"Revolut":(0,15,False),"SpaceX":(0,15,False),"Rippling":(-34,19,True),
"Anthropic":(-6,-19,False),"Ramp":(28,7,True),"Deel":(30,17,True),
"Anduril":(26,6,True),"Applied Intuition":(-14,-21,True),"Epic Games":(34,-9,True),
"Kraken":(-6,-20,True),"Ripple":(30,2,True),"OpenAI":(0,-19,False),
"Cursor":(26,-3,True),"Cerebras":(0,-19,False),"Perplexity":(0,-18,False),
"Figure AI":(0,15,False),"Neuralink":(0,-18,False)}

for name,val,sc,cls in D:
    c=AIBQ if cls=="AIBQ" else PBQ
    ax.scatter(val,sc,s=120,color=c,edgecolor=SURF,linewidth=1.8,zorder=5)

for name,val,sc,cls in D:
    dx,dy,lead=OFF[name]
    ha="center" if abs(dx)<6 else ("left" if dx>0 else "right")
    kw=dict(textcoords="offset points",xytext=(dx,dy),ha=ha,va="center",
            fontsize=8.8,color=INK,zorder=6)
    if lead:
        kw["arrowprops"]=dict(arrowstyle="-",color=LEAD,lw=0.7,
                              shrinkA=2,shrinkB=6,connectionstyle="arc3,rad=0")
    ax.annotate(name,(val,sc),**kw)

ax.set_xscale("log"); ax.set_xlim(6.5,4600); ax.set_ylim(2.0,9.0)
ticks=[10,25,50,100,250,500,1000,2500]
ax.set_xticks(ticks)
ax.set_xticklabels([f"${t}B" if t<1000 else f"${t/1000:g}T" for t in ticks],fontsize=9.5,color=SEC)
ax.set_yticks(range(2,10)); ax.set_yticklabels(range(2,10),fontsize=9.5,color=SEC)
ax.set_xlabel("Post-money valuation, log scale (as of June 30, 2026)",fontsize=10,color=SEC,labelpad=10)
ax.set_ylabel("AIBQ / PBQ composite score",fontsize=10,color=SEC,labelpad=10)
for s in ("top","right"): ax.spines[s].set_visible(False)
for s in ("left","bottom"): ax.spines[s].set_color("#d9d9d3")
ax.tick_params(colors="#d9d9d3",length=3)

fig.text(0.008,0.965,"Price Barely Tracks Quality Across the Top 20 Unicorns",
         fontsize=16,fontweight="bold",color=INK,va="top")
fig.text(0.008,0.918,"Valuation explains roughly 15% of the variation in quality score. "
         "The two most valuable companies rank seventh and fifteenth.",
         fontsize=10.2,color=SEC,va="top")

leg=[Line2D([0],[0],marker="o",color="none",markerfacecolor=AIBQ,markeredgecolor=SURF,
            markeredgewidth=1.5,markersize=10,label="AIBQ  ·  scored on compute independence"),
     Line2D([0],[0],marker="o",color="none",markerfacecolor=PBQ,markeredgecolor=SURF,
            markeredgewidth=1.5,markersize=10,label="PBQ  ·  scored on strategic velocity")]
ax.legend(handles=leg,loc="lower right",frameon=False,fontsize=9.5,labelcolor=SEC,
          handletextpad=0.7,borderpad=1.0,labelspacing=0.7)

fig.text(0.008,0.038,"Source: AIBQ/PBQ Panel as of 2026-06-30; PitchBook deal-level unicorn tracker.",
         fontsize=7.8,color=MUT,va="bottom")
fig.text(0.008,0.014,"Composites carry confidence bands of \u00b12.75 to \u00b13.75, so adjacent ranks overlap. "
         "Revolut shown at its $75B quarter-end valuation (panel carries $200B in-process).",
         fontsize=7.8,color=MUT,va="bottom")

fig.subplots_adjust(left=0.062,right=0.975,top=0.875,bottom=0.145)
out="/home/user/pitchbook-analyst-agent/templates/q2_2026_quality_vs_valuation.png"
fig.savefig(out,facecolor=SURF)
print("wrote",out)
