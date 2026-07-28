import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["text.parse_math"]=False
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np, csv

# company, composite, class, primary $B (last round), secondary $B (None = no secondary data), source
D=[("Databricks",8.19,"AIBQ",134,139.4),("Stripe",8.15,"PBQ",159,167.2),
("Canva",7.92,"PBQ",42,42.11),("Revolut",7.85,"PBQ",75,87.06),
("Rippling",7.24,"PBQ",16.8,16.98),("Anthropic",7.22,"AIBQ",965,989.6),
("Ramp",7.15,"PBQ",32,33.99),("Deel",6.98,"PBQ",17.3,15.47),
("Anduril",6.94,"PBQ",61,74.5),("Applied Intuition",6.91,"AIBQ",15,20.47),
("Epic Games",6.89,"PBQ",22.5,14.47),("Kraken",6.69,"PBQ",20,9.88),
("Ripple",6.58,"PBQ",40,21.23),("OpenAI",6.30,"AIBQ",852,787.2),
("Cursor",6.05,"AIBQ",29.3,38.21),("Perplexity",5.12,"AIBQ",20,17.25),
("Figure AI",3.75,"AIBQ",39,30.14),("Neuralink",2.50,"PBQ",9.65,42.84),
("xAI",5.38,"AIBQ",250,None),("Waymo",5.22,"AIBQ",126,None)]

x=np.log10([r[3] for r in D]); y=np.array([r[1] for r in D])
b,a=np.polyfit(x,y,1)
r2=1-np.sum((y-(a+b*x))**2)/np.sum((y-np.mean(y))**2)
rows=[]
for name,s,cls,vp,vs in D:
    rp=s-(a+b*np.log10(vp))
    rs=(s-(a+b*np.log10(vs))) if vs else None
    rows.append((name,s,cls,vp,vs,rp,rs))
rows.sort(key=lambda r:-r[5])

ABOVE="#2a78d6"; BELOW="#eb6834"; PRIM="#8a8983"
INK="#0b0b0b"; SEC="#52514e"; MUT="#8a8983"; SURF="#fcfcfb"; GRID="#e8e8e4"

fig,ax=plt.subplots(figsize=(11.8,9.3),dpi=200)
fig.patch.set_facecolor(SURF); ax.set_facecolor(SURF)
n=len(rows)
ax.axvspan(-0.5,0.5,color="#f0f0ec",zorder=0)
ax.text(0,n+0.58,"noise band (±0.5)",ha="center",va="bottom",fontsize=7.8,color=MUT,zorder=1)

ys=list(range(n,0,-1))
for (name,s,cls,vp,vs,rp,rs),yy in zip(rows,ys):
    if rs is not None:
        c=ABOVE if vs>=vp else BELOW
        ax.plot([rp,rs],[yy,yy],color=c,lw=2,zorder=3,solid_capstyle="round")
        ax.scatter([rs],[yy],s=80,color=c,edgecolor=SURF,linewidth=1.4,zorder=5)
        lab=("0.0" if abs(rs)<0.05 else f"{rs:+.1f}")
    else:
        lab=f"{rp:+.1f}‡"
    ax.scatter([rp],[yy],s=64,facecolor=SURF,edgecolor=PRIM,linewidth=1.8,zorder=4)
    note=""
    if name=="Kraken": note="   its secondary discount raises quality for size"
    if name=="Neuralink": note="   the stale-round artifact deepens"
    xa=max([v for v in (rp,rs) if v is not None])
    ax.text(xa+0.13,yy,f"{lab}{note}",va="center",ha="left",fontsize=8.3,color=SEC,zorder=5)

ax.axvline(0,color="#9a9a94",lw=1.0,zorder=2)
ax.set_yticks(ys)
ax.set_yticklabels([f"{r[0]}   {r[1]:.2f}" for r in rows],fontsize=9.2,color=INK)
ax.tick_params(axis="y",length=0)
ax.set_xlim(-4.6,3.4)
ax.set_xticks(range(-4,4))
ax.set_xticklabels([f"{t:+d}" if t!=0 else "0" for t in range(-4,4)],fontsize=9.5,color=SEC)
ax.grid(axis="x",color=GRID,lw=0.7,zorder=0); ax.set_axisbelow(True)
ax.set_xlabel("Composite score above or below the level predicted by company size (points)",
              fontsize=10,color=SEC,labelpad=9)
for s_ in ("top","right","left"): ax.spines[s_].set_visible(False)
ax.spines["bottom"].set_color("#d9d9d3")
ax.set_ylim(0.3,n+0.9)

fig.text(0.008,0.974,"Quality for Size: Who Carries More Quality Than Their Valuation Predicts",
         fontsize=15.5,fontweight="bold",color=INK,va="top")
fig.text(0.008,0.944,f"Composite minus the score predicted by valuation (fit of score on log valuation across the twenty, R² = {r2:.0%}), "
         "under primary and secondary pricing.",fontsize=9.8,color=SEC,va="top")
fig.text(0.008,0.922,"All-private roster: SpaceX and Cerebras, public since the quarter, are replaced by the next two largest scored "
         "private companies, xAI and Waymo.",fontsize=9.8,color=SEC,va="top")

leg=[Line2D([0],[0],marker="o",color="none",markerfacecolor=SURF,markeredgecolor=PRIM,
            markeredgewidth=1.8,markersize=9,label="Residual at the primary valuation (last round)"),
     Line2D([0],[0],marker="o",color="none",markerfacecolor=ABOVE,markeredgecolor=SURF,
            markersize=9,label="Residual at the secondary valuation, trades above reference"),
     Line2D([0],[0],marker="o",color="none",markerfacecolor=BELOW,markeredgecolor=SURF,
            markersize=9,label="Residual at the secondary valuation, trades below reference")]
ax.legend(handles=leg,loc="upper left",frameon=False,fontsize=8.8,labelcolor=SEC,
          handletextpad=0.6,borderpad=0.8,labelspacing=0.6)

fig.text(0.008,0.040,"Source: AIBQ/PBQ Panel and US AI/ML hand-scored panel (xAI, Waymo) as of 2026-06-30; Unicorn Monitor "
         "Top20_Marks (valuations). Residuals inside ±0.5 are within the noise band.",
         fontsize=7.6,color=MUT,va="bottom")
fig.text(0.008,0.016,"‡ xAI and Waymo are not Unicorn 20 constituents and have no secondary-market or model valuation data; "
         "their rows show the primary residual only.",fontsize=7.6,color=MUT,va="bottom")

fig.subplots_adjust(left=0.185,right=0.965,top=0.885,bottom=0.105)
fig.savefig("/home/user/pitchbook-analyst-agent/templates/q2_2026_quality_for_size.png",facecolor=SURF)
plt.close(fig)
print(f"fit: score = {a:.3f} + {b:.3f}*log10(V$B), R2={r2:.3f}")
for r in rows:
    print(f"  {r[0]:20s} rp={r[5]:+.2f}" + (f" rs={r[6]:+.2f}" if r[6] is not None else "  (no secondary)"))

out="/home/user/pitchbook-analyst-agent/templates/q2_2026_quality_for_size.csv"
with open(out,"w",newline="") as f:
    w=csv.writer(f)
    for line in [
     "# Quality for Size - AIBQ/PBQ composite residual vs company size, as of 2026-06-30",
     "# CONSTITUENTS: the 18 private Unicorn 20 constituents with AIBQ/PBQ panel scores, plus xAI and Waymo, the next two largest scored private companies (US AI/ML hand-scored panel, same framework and weights; confidence Medium). SpaceX and Cerebras are excluded: both listed publicly during the quarter.",
     "# METHODOLOGY:",
     f"# 1. Fit an ordinary least squares line of composite score on log10(primary valuation $B) across these 20 companies: score = {a:.3f} + {b:.3f} * log10(V). R-squared = {r2:.3f}.",
     "# 2. residual_primary = composite - predicted score at the primary valuation (last-round post-money).",
     "# 3. residual_secondary = composite - predicted score at the secondary valuation (secondary-implied value from observed share transactions), using the SAME fitted line, so the difference between the two residuals reflects only the valuation gap between markets. xAI and Waymo have no secondary-market data; their secondary fields are empty.",
     "# 4. Positive residual = more quality than companies of that size typically carry. Residuals inside +/-0.5 points are within the noise band and should not be ranked (score confidence bands are +/-2.75 to +/-3.75).",
     "# SOURCES: AIBQ/PBQ Panel as of 2026-06-30 (composites, point-in-time capped); US AI/ML hand-scored panel v2 (xAI, Waymo composites); Unicorn Monitor Top20_Marks (primary and secondary valuations).",
     "# Neuralink's secondary valuation reflects a stale 2021 last round, not demand; its secondary residual is an artifact of that base.",
    ]: f.write(line+"\n")
    w.writerow(["company","framework","composite_score","primary_valuation_bn","primary_basis",
                "secondary_valuation_bn","secondary_basis","predicted_score_primary","residual_primary",
                "predicted_score_secondary","residual_secondary","secondary_vs_reference","within_noise_band_primary"])
    for name,s,cls,vp,vs,rp,rs in rows:
        w.writerow([name,cls,f"{s:.2f}",f"{vp:.2f}","last_round_post_money",
                    (f"{vs:.2f}" if vs else ""),("secondary_implied" if vs else "no_secondary_data"),
                    f"{s-rp:.3f}",f"{rp:.3f}",
                    (f"{s-rs:.3f}" if rs is not None else ""),(f"{rs:.3f}" if rs is not None else ""),
                    ("above" if (vs and vs>=vp) else "below" if vs else "n/a"),
                    "yes" if abs(rp)<0.5 else "no"])
print("wrote",out)
