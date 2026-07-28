# CONTEXT: AI-VC-BY-LAYER - single hero chart: cumulative VC equity by stack layer,
# house style (matches build/charts.py), one hue per layer, light-to-dark ramp for
# within-bar composition, every segment direct-labeled. 300 DPI PNG.
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

NAVY = "#1F2A44"
GREY = "#6B7280"
INK = "#2B3446"
SOFT = "#F2F5F9"

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "charts")
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    "text.parse_math": False, "font.family": "DejaVu Sans", "font.size": 8,
    "text.color": INK, "axes.edgecolor": "#D5DBE4", "axes.labelcolor": GREY,
    "axes.linewidth": 0.8, "xtick.color": GREY, "ytick.color": GREY,
    "xtick.labelsize": 7.5, "ytick.labelsize": 8.5,
    "figure.facecolor": "white", "axes.facecolor": "white",
    "savefig.facecolor": "white",
})

# layer -> ordered (segment label, $B, hex) light->dark ramps within each bar
MODEL = [("Rest of layer (28 cos)", 46.5, "#C7D2E0"), ("xAI", 42.2, "#8FA3BC"),
         ("Anthropic", 124.3, "#51749B"), ("OpenAI", 181.9, "#1F2A44")]
INFRA = [("32 companies", 50.3, "#1C5D46")]
APP = [("Ex-defense (30 cos)", 19.8, "#D9A08A"), ("Defense (3 cos)", 18.1, "#8F3421")]

fig, ax = plt.subplots(figsize=(7.6, 2.9))
rows = [("Application layer", APP), ("Data/infrastructure layer", INFRA),
        ("Model layer", MODEL)]
for y, (name, segs) in enumerate(rows):
    left = 0.0
    for label, val, color in segs:
        ax.barh(y, val, left=left, height=0.55, color=color, zorder=3,
                edgecolor="white", linewidth=1.4)
        mid = left + val / 2
        if val >= 90:
            ax.text(mid, y, f"{label}\n${val:,.1f}B", ha="center", va="center",
                    fontsize=7.2, color="white", zorder=4)
        elif name == "Data/infrastructure layer":
            ax.text(mid, y, f"${val:,.1f}B", ha="center", va="center",
                    fontsize=7.2, color="white", zorder=4)
        left += val
    total = sum(v for _, v, _ in segs)
    share = {"Model layer": "81.7%", "Data/infrastructure layer": "10.4%",
             "Application layer": "7.8%"}[name]
    ax.text(left + 4, y, f"${total:,.1f}B  ({share})", ha="left", va="center",
            fontsize=8.2, fontweight="bold", color=NAVY, zorder=4)

# callout labels for segments too narrow to label in-bar
ax.annotate("Ex-defense (30 cos) $19.8B", xy=(9.9, -0.32), xytext=(-4, -0.85),
            ha="left", fontsize=6.8, color=GREY,
            arrowprops=dict(arrowstyle="-", color=GREY, lw=0.6))
ax.annotate("Defense (3 cos) $18.1B", xy=(28.9, -0.32), xytext=(115, -0.85),
            ha="left", fontsize=6.8, color=GREY,
            arrowprops=dict(arrowstyle="-", color=GREY, lw=0.6))
ax.annotate("Rest of layer (28 cos) $46.5B", xy=(23, 2.32), xytext=(-4, 2.75),
            ha="left", fontsize=6.8, color=GREY,
            arrowprops=dict(arrowstyle="-", color=GREY, lw=0.6))
ax.annotate("xAI $42.2B", xy=(67, 2.32), xytext=(120, 2.75), ha="left",
            fontsize=6.8, color=GREY,
            arrowprops=dict(arrowstyle="-", color=GREY, lw=0.6))

ax.set_yticks(range(len(rows)))
ax.set_yticklabels([n for n, _ in rows])
ax.set_xlim(0, 470)
ax.set_ylim(-1.15, 3.05)
ax.set_xlabel("Cumulative VC equity raised, USD billions (completed rounds, ex-debt, ex-secondaries)",
              fontsize=7.2)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.grid(axis="x", color=SOFT, linewidth=0.9, zorder=0)
ax.set_axisbelow(True)
ax.tick_params(left=False)

fig.text(0.01, 1.06, "AI venture capital inverts the pyramid: 81.7% of equity sits in the model layer",
         ha="left", va="top", fontsize=10.5, fontweight="bold", color=NAVY)
fig.text(0.01, 0.99,
         "Cumulative VC equity, 96-company capital-weighted universe - PitchBook deal histories, pulled Jul 28, 2026. "
         "Excludes debt ($100.4B identified), IPO/PIPE proceeds,\nsecondaries, and Meta's $14.3B strategic stake in Scale AI.",
         ha="left", va="top", fontsize=7.0, color=GREY)

fig.savefig(os.path.join(OUT, "vc_by_layer.png"), dpi=300, bbox_inches="tight",
            pad_inches=0.14)
print("wrote charts/vc_by_layer.png")
