import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["text.parse_math"]=False
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# company, composite, class, primary $B (last round; † model), secondary $B, flag
D=[("Databricks",8.19,"AIBQ",134,139.4,""),("Stripe",8.15,"PBQ",159,167.2,""),
("Canva",7.92,"PBQ",42,42.11,""),("Revolut",7.85,"PBQ",75,87.06,""),
("SpaceX",7.60,"PBQ",2026.24,2110.0,"m"),("Rippling",7.24,"PBQ",16.8,16.98,""),
("Anthropic",7.22,"AIBQ",965,989.6,""),("Ramp",7.15,"PBQ",32,33.99,""),
("Deel",6.98,"PBQ",17.3,15.47,""),("Anduril",6.94,"PBQ",61,74.5,""),
("Applied Intuition",6.91,"AIBQ",15,20.47,""),("Epic Games",6.89,"PBQ",22.5,14.47,""),
("Kraken",6.69,"PBQ",20,9.88,""),("Ripple",6.58,"PBQ",40,21.23,""),
("OpenAI",6.30,"AIBQ",852,787.2,""),("Cursor",6.05,"AIBQ",29.3,38.21,""),
("Cerebras",5.92,"AIBQ",57.1,61.45,"m"),("Perplexity",5.12,"AIBQ",20,17.25,""),
("Figure AI",3.75,"AIBQ",39,30.14,""),("Neuralink",2.50,"PBQ",9.65,42.84,"")]

AIBQ="#2a78d6"; PBQ="#eb6834"
INK="#0b0b0b"; SEC="#52514e"; MUT="#8a8983"; SURF="#fcfcfb"; GRID="#e8e8e4"; LEAD="#b9b9b2"

OFF_P={"Databricks":(-46,14,True),"Stripe":(30,-13,True),"Canva":(0,15,False),
"Revolut":(0,15,False),"SpaceX":(0,15,False),"Rippling":(-30,20,True),
"Anthropic":(-6,-19,False),"Ramp":(24,10,True),"Deel":(-32,8,True),
"Anduril":(26,6,True),"Applied Intuition":(-32,-14,True),"Epic Games":(34,-8,True),
"Kraken":(0,-20,False),"Ripple":(28,-4,True),"OpenAI":(0,-19,False),
"Cursor":(24,-6,True),"Cerebras":(0,-19,False),"Perplexity":(0,-18,False),
"Figure AI":(0,15,False),"Neuralink":(0,-18,False)}
OFF_S={"Databricks":(-46,14,True),"Stripe":(30,-13,True),"Canva":(0,15,False),
"Revolut":(0,15,False),"SpaceX":(0,15,False),"Rippling":(-34,17,True),
"Anthropic":(-6,-19,False),"Ramp":(-26,13,True),"Deel":(-30,0,True),
"Anduril":(26,6,True),"Applied Intuition":(28,-12,True),"Epic Games":(0,-20,False),
"Kraken":(0,-20,False),"Ripple":(26,-9,True),"OpenAI":(0,-19,False),
"Cursor":(-26,-11,True),"Cerebras":(0,-19,False),"Perplexity":(0,-18,False),
"Figure AI":(0,15,False),"Neuralink":(0,-18,False)}

def build(which,xcol,offs,title,sub1,sub2,out):
    fig,ax=plt.subplots(figsize=(11.5,7.6),dpi=200)
    fig.patch.set_facecolor(SURF); ax.set_facecolor(SURF)
    for lo,hi,lab,col in [(8.0,9.0,"Elite","#eef3f9"),(6.5,8.0,"Strong","#f5f7f9"),
                          (4.5,6.5,"Developing","#faf9f6"),(2.0,4.5,"Distressed","#fdf5f2")]:
        ax.axhspan(lo,hi,color=col,zorder=0)
        ax.text(0.995,hi-0.13,lab,transform=ax.get_yaxis_transform(),ha="right",va="top",
                fontsize=8.5,color=MUT,style="italic",zorder=1)
    for y in (4.5,6.5,8.0): ax.axhline(y,color="#dcdcd6",lw=0.9,zorder=1)
    ax.grid(axis="x",color=GRID,lw=0.7,zorder=1); ax.set_axisbelow(True)
    for name,sc,cls,pv,sv,fl in D:
        x=pv if xcol=="p" else sv
        c=AIBQ if cls=="AIBQ" else PBQ
        ax.scatter(x,sc,s=120,color=c,edgecolor=SURF,linewidth=1.8,zorder=5)
    for name,sc,cls,pv,sv,fl in D:
        x=pv if xcol=="p" else sv
        dx,dy,lead=offs[name]
        ha="center" if abs(dx)<6 else ("left" if dx>0 else "right")
        dag="†" if (fl=="m" and xcol=="p") else ""
        kw=dict(textcoords="offset points",xytext=(dx,dy),ha=ha,va="center",
                fontsize=8.8,color=INK,zorder=6)
        if lead:
            kw["arrowprops"]=dict(arrowstyle="-",color=LEAD,lw=0.7,shrinkA=2,shrinkB=6)
        ax.annotate(f"{name}{dag}",(x,sc),**kw)
    ax.set_xscale("log"); ax.set_xlim(6.5,4600); ax.set_ylim(2.0,9.0)
    ticks=[10,25,50,100,250,500,1000,2500]
    ax.set_xticks(ticks)
    ax.set_xticklabels([f"${t}B" if t<1000 else f"${t/1000:g}T" for t in ticks],fontsize=9.5,color=SEC)
    ax.set_yticks(range(2,10)); ax.set_yticklabels(range(2,10),fontsize=9.5,color=SEC)
    xlabel=("Primary market: last-round post-money valuation, log scale (as of June 30, 2026)"
            if xcol=="p" else
            "Secondary market: traded-implied valuation, log scale (as of June 30, 2026)")
    ax.set_xlabel(xlabel,fontsize=10,color=SEC,labelpad=10)
    ax.set_ylabel("AIBQ / PBQ composite score",fontsize=10,color=SEC,labelpad=10)
    for s in ("top","right"): ax.spines[s].set_visible(False)
    for s in ("left","bottom"): ax.spines[s].set_color("#d9d9d3")
    ax.tick_params(colors="#d9d9d3",length=3)
    fig.text(0.008,0.965,title,fontsize=16,fontweight="bold",color=INK,va="top")
    fig.text(0.008,0.925,sub1,fontsize=10.2,color=SEC,va="top")
    fig.text(0.008,0.902,sub2,fontsize=10.2,color=SEC,va="top")
    leg=[Line2D([0],[0],marker="o",color="none",markerfacecolor=AIBQ,markeredgecolor=SURF,
                markeredgewidth=1.5,markersize=10,label="AIBQ  ·  scored on compute independence"),
         Line2D([0],[0],marker="o",color="none",markerfacecolor=PBQ,markeredgecolor=SURF,
                markeredgewidth=1.5,markersize=10,label="PBQ  ·  scored on strategic velocity")]
    ax.legend(handles=leg,loc="lower right",frameon=False,fontsize=9.5,labelcolor=SEC,
              handletextpad=0.7,borderpad=1.0,labelspacing=0.7)
    src=("Source: AIBQ/PBQ Panel as of 2026-06-30; Unicorn Monitor Top20_Marks. "
         + ("† SpaceX and Cerebras have no private last round; their primary valuation is the Morningstar model estimate."
            if xcol=="p" else
            "Secondary-implied valuations from observed share transactions, marks as of June 22, 2026.\nSpaceX shown at its day-one public close (~$2.11T) and Cerebras at its public trading value."))
    fig.text(0.008,0.016,src,fontsize=7.7,color=MUT,va="bottom")
    fig.subplots_adjust(left=0.062,right=0.975,top=0.855,bottom=0.125)
    fig.savefig(out,facecolor=SURF)
    plt.close(fig)
    print("wrote",out)

build("primary","p",OFF_P,
  "Quality Against the Primary Market: Price Explains Little",
  "Each company's AIBQ/PBQ composite against its last-round post-money valuation.",
  "The two most valuable companies rank seventh and fifteenth on quality.",
  "/home/user/pitchbook-analyst-agent/templates/q2_2026_aibq_vs_primary.png")
build("secondary","s",OFF_S,
  "Quality Against the Secondary Market: The Outliers Move Into Line",
  "The same twenty companies against the valuation implied by actual share trades.",
  "Kraken and Ripple shift left toward their scores; Neuralink is priced far above the weakest score on the board.",
  "/home/user/pitchbook-analyst-agent/templates/q2_2026_aibq_vs_secondary.png")
