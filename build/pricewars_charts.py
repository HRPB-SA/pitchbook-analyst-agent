"""Charts for 'The Frontier AI Price Wars' note. Three PNGs at 300 DPI.
Asserts every headline number in the note's Section 1 and 2 arithmetic before
rendering; fails loudly on drift between text and figures.
Categorical palette: dataviz validated slots 1-5, fixed entity order, direct
labels as relief for the low-contrast slots (aqua, yellow).
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

NAVY = "#1F2A44"
GREY = "#6B7280"
SOFT = "#F2F5F9"
INK = "#2B3446"

# fixed entity -> hue mapping, used identically in every chart
MODELS = [
    ("Claude Opus 4.8", 5.00, 25.00, "#2a78d6"),
    ("GPT-5.6 Sol", 5.00, 30.00, "#1baf7a"),
    ("GPT-5.6 Luna", 1.00, 6.00, "#eda100"),
    ("Grok 4.5", 2.00, 6.00, "#008300"),
    ("Muse Spark 1.1", 1.25, 4.25, "#4a3aa7"),
]
ARR_BLUE = "#2a78d6"
OP_ORANGE = "#eb6834"

TOK_IN, TOK_OUT = 60_000, 12_000
REMED = 17.0

# Claude Mythos 5 is Anthropic's limited-availability flagship above Opus 4.8.
# Published list price per the Anthropic pricing page: $10 / $50 per Mtok,
# exactly twice Opus. Not an assumption.
MYTHOS_IN, MYTHOS_OUT = 10.0, 50.0

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "charts")
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    "text.parse_math": False,
    "font.family": "DejaVu Sans",
    "font.size": 8,
    "text.color": INK,
    "axes.edgecolor": "#D5DBE4",
    "axes.labelcolor": GREY,
    "axes.titlesize": 10.5,
    "axes.linewidth": 0.8,
    "xtick.color": GREY,
    "ytick.color": GREY,
    "xtick.labelsize": 7.5,
    "ytick.labelsize": 7.5,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white",
})


def style_ax(ax, grid_axis="y"):
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    if grid_axis:
        ax.grid(axis=grid_axis, color=SOFT, linewidth=0.9, zorder=0)
    ax.set_axisbelow(True)


def title_block(fig, title, subtitle, x=0.01):
    fig.text(x, 0.985, title, ha="left", va="top", fontsize=10.5,
             fontweight="bold", color=NAVY)
    fig.text(x, 0.915, subtitle, ha="left", va="top", fontsize=7.6, color=GREY)


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=300, bbox_inches="tight",
                pad_inches=0.12)
    plt.close(fig)
    print("wrote", name)


def attempt_cost(pin, pout):
    return TOK_IN * pin / 1e6 + TOK_OUT * pout / 1e6


def loaded(c, p):
    return (c + REMED * (1 - p)) / p


# ---- assert the note's arithmetic before drawing anything ----
costs = {name: attempt_cost(pin, pout) for name, pin, pout, _ in MODELS}
assert abs(costs["Claude Opus 4.8"] - 0.60) < 1e-9
assert abs(costs["GPT-5.6 Sol"] - 0.66) < 1e-9
assert abs(costs["GPT-5.6 Luna"] - 0.132) < 1e-9
assert abs(costs["Grok 4.5"] - 0.192) < 1e-9
assert abs(costs["Muse Spark 1.1"] - 0.126) < 1e-9
ratio = costs["Claude Opus 4.8"] / costs["Muse Spark 1.1"]
assert round(ratio, 1) == 4.8                       # "a factor of 4.8"
assert round((1 - 0.90 / ratio) * 100) == 81        # "fail more than 81%"
opus_90 = loaded(costs["Claude Opus 4.8"], 0.90)
assert round(opus_90, 2) == 2.56                    # "$2.56 per completed task"
muse_75 = loaded(costs["Muse Spark 1.1"], 0.75)
assert round(muse_75, 2) == 5.83                    # "$5.83 per completed task"
assert round(muse_75 / opus_90, 1) == 2.3           # "2.3x more expensive"
muse_be = (costs["Muse Spark 1.1"] + REMED) / (opus_90 + REMED)
assert round(muse_be * 100, 1) == 87.6              # "p = 87.6%"
assert round((1 - 7 / 25) * 100) == 72              # "roughly a 70% gross margin"
assert round((1 - 7 / 6) * 100) == -17              # "negative 17% at $6"
assert round((1 - 7 / 4.25) * 100) == -65           # "negative 65% at $4.25"

# break-even failure cost F* where Opus loaded == Muse loaded, at Opus p=0.90:
# F* = (p_o*c_m - p_m*c_o) / (p_m - p_o). Section 2 sensitivity line.
c_muse = costs["Muse Spark 1.1"]
c_opus = costs["Claude Opus 4.8"]
def f_star(p_muse, p_opus=0.90):
    return (p_opus * c_muse - p_muse * c_opus) / (p_muse - p_opus)
assert round(f_star(0.75), 2) == 2.24               # "$2.24 at a 15-point edge"
assert round(f_star(0.80), 2) == 3.67               # "$3.67 at a 10-point edge"
assert round(f_star(0.85), 2) == 7.93               # "$7.93 at a 5-point edge"
print("arithmetic assertions pass")

# --------------------------------------- 0. the true-cost inversion (hero)
# Cost per completed task at a fixed quality bar, illustrative per-model
# reliabilities, with the $17 remediation cost. The point: the highest
# sticker price is the lowest true cost.
REL = {"Claude Opus 4.8": 0.90, "GPT-5.6 Sol": 0.89, "Grok 4.5": 0.82,
       "GPT-5.6 Luna": 0.78, "Muse Spark 1.1": 0.76}
STICK = {"Claude Opus 4.8": 25, "GPT-5.6 Sol": 30, "Grok 4.5": 6,
         "GPT-5.6 Luna": 6, "Muse Spark 1.1": 4.25}
true_cost = {m: (costs[m] + REMED * (1 - p)) / p for m, p in REL.items()}
assert min(true_cost, key=true_cost.get) == "Claude Opus 4.8"
assert round(true_cost["Claude Opus 4.8"], 2) == 2.56
order = sorted(true_cost, key=true_cost.get)
fig, ax = plt.subplots(figsize=(7.2, 3.7))
fig.subplots_adjust(top=0.80, left=0.16, right=0.95, bottom=0.12)
y = np.arange(len(order))[::-1]
bar_colors = {"Claude Opus 4.8": "#2a78d6", "GPT-5.6 Sol": "#1baf7a",
              "Grok 4.5": "#008300", "GPT-5.6 Luna": "#eda100",
              "Muse Spark 1.1": "#4a3aa7"}
for yi, m in zip(y, order):
    ax.barh(yi, true_cost[m], height=0.62, color=bar_colors[m], zorder=3,
            edgecolor="white", linewidth=0.8)
    ax.annotate(f"${true_cost[m]:.2f}", xy=(true_cost[m] + 0.08, yi),
                va="center", fontsize=8.4, fontweight="bold", color=INK)
    ax.annotate(f"sticker ${STICK[m]:g}/Mtok out", xy=(0.12, yi),
                va="center", fontsize=7.0, color="white")
ax.set_yticks(y)
ax.set_yticklabels(order, fontsize=8.4)
ax.set_xlim(0, 6.6)
ax.set_xlabel("true cost per completed enterprise task, $ (lower is better)")
ax.annotate("cheapest to RUN,\nnear-highest sticker", xy=(2.56, y[0]),
            xytext=(3.7, y[0] + 0.35), fontsize=7.4, color="#1C5D46",
            fontweight="bold",
            arrowprops=dict(arrowstyle="->", color="#1C5D46", lw=1.0))
ax.annotate("cheapest sticker, most expensive to RUN",
            xy=(true_cost["Muse Spark 1.1"], 0.28),
            xytext=(2.5, 0.62), fontsize=7.4, color="#8F3421",
            fontweight="bold", va="center",
            arrowprops=dict(arrowstyle="->", color="#8F3421", lw=1.0))
style_ax(ax)
title_block(fig,
            "The priciest tier runs cheapest; the cheapest sticker runs dearest",
            "Cost per completed agentic task at a fixed quality bar, $17 remediation per failed attempt, illustrative "
            "per-model reliabilities. Sticker prices are published; the reliability spread is our assumption.")
save(fig, "pw_true_cost.png")

# ------------------------------------------------ 0b. the pricing ladder
# Horizontal log ladder of output list price per Mtok, from the commodity
# floor to the restricted premium anchor, with the consumer free tier shown
# as priced-at-zero (monetized off-token).
ladder = [
    ("Muse Spark 1.1", 4.25, "#4a3aa7", "cheap"),
    ("GPT-5.6 Luna", 6.00, "#eda100", "cheap"),
    ("Grok 4.5", 6.00, "#008300", "cheap"),
    ("Claude Opus 4.8", 25.00, "#2a78d6", "premium"),
    ("GPT-5.6 Sol", 30.00, "#1baf7a", "premium"),
    ("Claude Mythos 5", MYTHOS_OUT, "#e34948", "premium"),
]
fig, ax = plt.subplots(figsize=(7.2, 3.6))
fig.subplots_adjust(top=0.79, left=0.30, right=0.92, bottom=0.14)
y = np.arange(len(ladder))
for yi, (name, price, color, band) in zip(y, ladder):
    ax.barh(yi, price, height=0.6, color=color, zorder=3,
            hatch="///" if "est." in name else None,
            edgecolor="white", linewidth=0.8)
    ax.annotate(f"${price:g}", xy=(price * 1.06, yi), va="center",
                fontsize=7.8, color=INK, fontweight="bold")
ax.set_xscale("log")
ax.set_yticks(y)
ax.set_yticklabels([n for n, *_ in ladder], fontsize=8)
ax.set_xlim(0.5, 82)
ax.set_xticks([1, 3, 10, 30, 50])
ax.set_xticklabels(["$1", "$3", "$10", "$30", "$50"])
ax.set_xlabel("output list price, $ per Mtok (log scale)")
# consumer free tier band, labeled inside the band so it clears the bars
ax.axvspan(0.5, 0.82, color=GREY, alpha=0.12, zorder=0)
ax.text(0.64, 2.5, "consumer free tier: $0 per token, monetized off-token",
        fontsize=6.8, color=GREY, rotation=90, ha="center", va="center")
ax.axhspan(-0.5, 2.5, color="#4a3aa7", alpha=0.05, zorder=0)
ax.axhspan(2.5, 5.5, color="#2a78d6", alpha=0.05, zorder=0)
ax.annotate("commodity floor", xy=(11, 1), fontsize=7, color=GREY,
            ha="left", va="center", style="italic")
ax.annotate("reliability premium", xy=(56, 4), fontsize=7, color=GREY,
            ha="left", va="center", style="italic")
for s in ["top", "right"]:
    ax.spines[s].set_visible(False)
ax.set_axisbelow(True)
title_block(fig,
            "One market, two crowded ends and a hollow middle",
            "Output list price per million tokens, log scale. Published prices run from Muse Spark at $4.25 to Claude "
            "Mythos 5 at $50, roughly twelvefold, and the free consumer tier makes the full spread unbounded.")
save(fig, "pw_pricing_ladder.png")

# ---------------------------------------------------- 1. cost curves
fig, ax = plt.subplots(figsize=(7.2, 3.7))
fig.subplots_adjust(top=0.80, left=0.08, right=0.83, bottom=0.14)
p = np.linspace(0.50, 0.99, 300)
for name, pin, pout, color in MODELS:
    # Luna dashed so it stays visible where the Muse curve overlaps it
    ls = (0, (3, 2)) if name == "GPT-5.6 Luna" else "solid"
    ax.plot(p * 100, loaded(attempt_cost(pin, pout), p), color=color,
            linewidth=2, linestyle=ls, label=name, zorder=3)
ax.set_yscale("log")
ax.axhline(opus_90, color=GREY, linewidth=1, linestyle=(0, (4, 3)), zorder=2)
ax.annotate("Opus 4.8 at p = 90%: $2.56", xy=(51, opus_90 * 1.12),
            fontsize=7.2, color=GREY)
ax.plot([muse_be * 100], [opus_90], marker="o", markersize=8,
        markerfacecolor="white", markeredgecolor="#4a3aa7",
        markeredgewidth=1.6, zorder=4)
ax.annotate("break-even: Muse Spark\nmatches Opus at p = 87.6%",
            xy=(muse_be * 100, opus_90 * 0.93), xytext=(62, 0.85),
            fontsize=7.2, color=INK,
            arrowprops=dict(arrowstyle="-", color=GREY, lw=0.7))
# direct labels at the right edge (relief for aqua/yellow slots); Luna and
# Muse curves sit within 5% of each other, labeled jointly
ends = {name: loaded(attempt_cost(pin, pout), 0.99)
        for name, pin, pout, _ in MODELS}
ax.annotate("Sol", xy=(99.3, ends["GPT-5.6 Sol"] * 1.06), fontsize=7.4,
            color="#1baf7a", fontweight="bold", annotation_clip=False)
ax.annotate("Opus 4.8", xy=(99.3, ends["Claude Opus 4.8"] * 0.82),
            fontsize=7.4, color="#2a78d6", fontweight="bold",
            annotation_clip=False)
ax.annotate("Grok 4.5", xy=(99.3, ends["Grok 4.5"] * 1.14), fontsize=7.4,
            color="#008300", fontweight="bold", annotation_clip=False)
ax.annotate("Luna / Muse Spark", xy=(99.3, ends["Muse Spark 1.1"] * 0.88),
            fontsize=7.4, color="#4a3aa7", fontweight="bold",
            annotation_clip=False)
ax.set_xlabel("per-attempt task-success rate (%)")
ax.set_ylabel("$ per completed task (log)")
ax.set_yticks([0.3, 1, 3, 10])
ax.set_yticklabels(["$0.30", "$1", "$3", "$10"])
ax.legend(loc="lower left", fontsize=7, frameon=False, ncol=2)
style_ax(ax)
title_block(fig,
            "Below ~85% success, token price is noise; above it, reliability is the price",
            "Fully loaded cost per completed task: (cost per attempt + $17 x (1 - p)) / p. "
            "Workload 60k in / 12k out per attempt. List prices T1; workload and $17 remediation our assumptions, T2.")
save(fig, "pw_cost_curves.png")

# --------------------------------- 1b. failure-cost sensitivity of premium
fig, ax = plt.subplots(figsize=(7.2, 3.6))
fig.subplots_adjust(top=0.80, left=0.09, right=0.96, bottom=0.14)
edges = np.linspace(2, 40, 300)          # reliability edge in points, Opus - Muse
pm = 0.90 - edges / 100.0
Fcurve = (0.90 * c_muse - pm * c_opus) / (pm - 0.90)
ax.plot(edges, Fcurve, color="#2a78d6", linewidth=2.2, zorder=4)
ax.fill_between(edges, Fcurve, 60, color="#1baf7a", alpha=0.10, zorder=1)
ax.fill_between(edges, 0.4, Fcurve, color="#e34948", alpha=0.08, zorder=1)
ax.set_yscale("log")
ax.set_ylim(0.8, 60)
ax.set_xlim(2, 40)
for e, f in [(15, 2.24), (10, 3.67), (5, 7.93)]:
    ax.plot([e], [f], marker="o", markersize=8, color="#1F2A44", zorder=5,
            markeredgecolor="white", markeredgewidth=1.4)
    ax.annotate(f"{e}-pt edge:\n${f:.2f}", xy=(e, f), xytext=(e + 1.2, f * 1.9),
                fontsize=7.2, color=INK,
                arrowprops=dict(arrowstyle="-", color=GREY, lw=0.7))
ax.axhline(10, color=GREY, linewidth=1, linestyle=(0, (4, 3)), zorder=3)
ax.annotate("typical production failure cost (our estimate) sits above ~$10",
            xy=(20, 11.5), fontsize=7.2, color=GREY)
ax.annotate("PREMIUM JUSTIFIED\n(failure costs more than break-even)",
            xy=(30, 28), fontsize=7.6, color="#1C5D46", ha="center",
            fontweight="bold")
ax.annotate("floor wins", xy=(6.5, 1.15), fontsize=7.4, color="#8F3421",
            fontweight="bold")
ax.set_xlabel("reliability edge, Opus success minus cheap-tier success (points)")
ax.set_ylabel("break-even failure cost, $ per failed attempt (log)")
ax.set_yticks([1, 3, 10, 30])
ax.set_yticklabels(["$1", "$3", "$10", "$30"])
style_ax(ax)
title_block(fig,
            "The premium survives its own stress test: at any real reliability edge, failure need only cost a few dollars",
            "Break-even failure cost F* = (p_o x c_m - p_m x c_o) / (p_m - p_o), Opus success p_o = 90%. Above the curve the "
            "reliability premium is cheaper per completed task. Prices T1; workload and costs our assumptions, T2.")
save(fig, "pw_sensitivity.png")

# ------------------------------------------- 2. margin vs output price
fig, ax = plt.subplots(figsize=(7.2, 3.5))
fig.subplots_adjust(top=0.80, left=0.09, right=0.97, bottom=0.14)
price = np.linspace(3.5, 32, 400)
lo, mid, hi = 6.0, 7.0, 8.0
ax.fill_between(price, (1 - hi / price) * 100, (1 - lo / price) * 100,
                color="#2a78d6", alpha=0.13, linewidth=0, zorder=1)
ax.plot(price, (1 - mid / price) * 100, color=GREY, linewidth=1.4, zorder=2)
ax.axhline(0, color=INK, linewidth=1, zorder=2)
ax.annotate("breakeven: output price = serving cost", xy=(15.5, 4),
            fontsize=7.2, color=GREY)
ax.annotate("serving-cost band $6-8 per Mtok out\n(our estimate, T2)",
            xy=(11.5, 62), fontsize=7.2, color=GREY)
# Luna and Grok share the $6 / -17% point: Luna drawn as an open ring
# behind Grok's filled marker so both stay visible
labels = {"GPT-5.6 Luna": (6.8, -7), "Grok 4.5": (6.8, -25),
          "Muse Spark 1.1": (4.7, -57), "Claude Opus 4.8": (23.2, 58),
          "GPT-5.6 Sol": (26.2, 84)}
for name, pin, pout, color in MODELS:
    m = (1 - mid / pout) * 100
    if name == "GPT-5.6 Luna":
        ax.plot([pout], [m], marker="o", markersize=12, zorder=4,
                markerfacecolor="white", markeredgecolor=color,
                markeredgewidth=1.8)
    else:
        ax.plot([pout], [m], marker="o", markersize=8, color=color, zorder=5,
                markeredgecolor="white", markeredgewidth=1.5)
    lx, ly = labels[name]
    ax.annotate(f"{name}  {m:+.0f}%", xy=(lx, ly), fontsize=7.4,
                color=color, fontweight="bold")
ax.set_xlabel("output list price, $ per Mtok")
ax.set_ylabel("implied gross margin (%)")
ax.set_ylim(-95, 95)
style_ax(ax)
title_block(fig,
            "Every output price below ~$8 is gross-margin negative at today's serving cost",
            "Implied model-layer gross margin = 1 - serving cost / output list price, at the $7 midpoint of the "
            "$6-8 serving band. Prices T1; serving cost our estimate, T2; markers at each model's output price.")
save(fig, "pw_margin_vs_price.png")

# --------------------------------------- 3. layer economics, two panels
fig, (axl, axr) = plt.subplots(1, 2, figsize=(7.2, 3.3),
                               gridspec_kw={"width_ratios": [1.25, 1]})
fig.subplots_adjust(top=0.78, left=0.07, right=0.985, bottom=0.12, wspace=0.28)

labs = ["Anthropic", "OpenAI", "xAI (AI segment)"]
arr = [47, 25, 3.2]
op = [0.559, None, -6.36]
x = np.arange(len(labs))
w = 0.38
axl.bar(x - w / 2, arr, width=w, color=ARR_BLUE, zorder=3, label="ARR ($B)")
for xi, v in zip(x, arr):
    axl.annotate(f"${v:g}B", xy=(xi - w / 2, v + 1), ha="center", fontsize=7.4,
                 color=INK)
axl.bar([x[0] + w / 2, x[2] + w / 2], [op[0], op[2]], width=w, color=OP_ORANGE,
        zorder=3, label="operating result ($B)")
axl.annotate("+$0.56B\nQ2, adj.", xy=(x[0] + w / 2, 2.2), ha="center",
             fontsize=6.8, color=INK)
axl.annotate("n.d.", xy=(x[1] + w / 2, 1.5), ha="center", fontsize=7.2,
             color=GREY)
axl.annotate("-$6.4B FY25", xy=(x[2] + w / 2, -10.5), ha="center",
             fontsize=6.8, color=INK)
axl.axhline(0, color=INK, linewidth=1)
axl.set_xticks(x)
axl.set_xticklabels(labs, fontsize=7.4)
axl.set_ylabel("$B")
axl.set_ylim(-14, 55)
axl.legend(loc="upper right", fontsize=6.8, frameon=False)
axl.set_title("Model layer: revenue vs operating result (T2)", fontsize=8,
              color=NAVY, pad=6)
style_ax(axl)

cons = ["HBM supply\n(allocated)", "Advanced\npackaging", "Permitted DC\npower"]
util = [98, 95, 95]
y = np.arange(len(cons))
axr.barh(y, util, height=0.55, color=ARR_BLUE, zorder=3)
for yi, v in zip(y, util):
    axr.annotate(f"~{v}%", xy=(v - 2, yi), va="center", ha="right",
                 fontsize=7.4, color="white", fontweight="bold")
axr.axvline(100, color=GREY, linewidth=0.8, linestyle=(0, (3, 3)))
axr.set_yticks(y)
axr.set_yticklabels(cons, fontsize=7.2)
axr.invert_yaxis()
axr.set_xlim(0, 105)
axr.set_xlabel("capacity utilization / allocation (%)")
axr.set_title("Buildout layer: indicative utilization (T3)", fontsize=8,
              color=NAVY, pad=6)
style_ax(axr, grid_axis="x")

title_block(fig,
            "The layer cutting prices is the layer losing money; the buildout sells scarcity",
            "Left: revenue bases differ (Anthropic gross run-rate ARR, OpenAI net ARR, xAI AI-segment ARR); Anthropic "
            "operating result is quarterly and adjusted, xAI is FY25. Right: indicative levels from trade press, T3.")
save(fig, "pw_layer_economics.png")
