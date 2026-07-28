"""Q2 2026 tracker exhibits rebuilt from the workbook tab charts.

Sources: Final__Q2_2026__Quarterly_Unicorn_Tracker_HR_Version.xlsx (annual tab
blocks, rows 7-10 of each named tab) and US_AI_ML_HandScored_1.xlsx Sheet1
(layer/sub-layer counts). The Excel originals are dual-axis bar+line combos;
these use paired single-axis panels instead.
"""
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["text.parse_math"] = False
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

BLUE = "#2a78d6"; ORANGE = "#eb6834"
INK = "#0b0b0b"; SEC = "#52514e"; MUT = "#8a8983"; SURF = "#fcfcfb"; GRID = "#e8e8e4"

YEARS = list(range(2016, 2027))
AGG_VAL = [781.821, 958.646, 1405.379, 1718.922, 2187.046, 3920.26, 4850.36, 4865.999, 5457.269, 7305.428, 8232.506]
AGG_CNT = [229, 286, 395, 510, 647, 1124, 1423, 1488, 1525, 1621, 1743]
DEAL_VAL = [82.439, 83.799, 153.98, 220.347, 159.588, 340.924, 166.09, 109.583, 148.786, 244.995, 396.137]
DEAL_CNT = [959, 1001, 1231, 1272, 1384, 1894, 1081, 702, 764, 872, 444]
MED_POST = [0.11, 0.18, 0.258, 0.352, 0.49, 1.15, 1.324, 1.157, 1.185, 1.572, 2.0]
AVG_POST = [1.082, 0.858, 1.7, 1.437, 1.633, 2.305, 2.526, 2.556, 3.338, 4.821, 18.187]
STEP_MED = [1.838, 1.884, 2.0, 1.922, 1.89, 2.641, 2.143, 1.365, 1.68, 2.048, 2.201]
TBR_MED = [1.063, 1.1, 1.088, 1.058, 1.055, 0.833, 0.885, 1.318, 1.445, 1.205, 0.981]
DOWN_CNT = [25, 30, 23, 25, 36, 30, 22, 30, 34, 31, 6]
AI_VAL = [80.205, 103.659, 282.19, 416.555, 655.611, 1332.192, 1689.124, 1721.835, 2139.921, 3487.226, 5076.421]
EXIT_VAL = [34.6097, 49.0064, 165.9027, 188.0418, 245.8645, 843.7833, 90.03, 92.9404, 85.4175, 205.5424, 2110.8992]
EXIT_CNT = [16, 26, 41, 42, 51, 132, 47, 44, 53, 76, 50]
SPACEX_EXIT = 1690.2418
RVVC_MED = [0.643, 0.614, 0.935, 0.822, 0.757, 1.762, 1.175, 0.234, 0.376, 0.932, 1.418]

XLBL = [str(y) for y in YEARS[:-1]] + ["2026*"]

def style_ax(ax, ygrid=True):
    ax.set_facecolor(SURF)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color("#dcdcd6")
    if ygrid:
        ax.grid(axis="y", color=GRID, lw=0.7)
    ax.set_axisbelow(True)
    ax.tick_params(colors=SEC, labelsize=8.5, length=0)

def header(fig, title, sub, src):
    fig.patch.set_facecolor(SURF)
    fig.text(0.06, 0.955, title, fontsize=15.5, fontweight="bold", color=INK, ha="left")
    fig.text(0.06, 0.912, sub, fontsize=9.5, color=SEC, ha="left")
    if len(src) > 130 and "\n" not in src:
        cut = src.rfind(" ", 0, 130)
        src = src[:cut] + "\n" + src[cut + 1:]
    fig.text(0.06, 0.058 if "\n" in src else 0.022, src, fontsize=7.8, color=MUT,
             ha="left", va="top" if "\n" in src else "baseline", linespacing=1.5)

def bar_labels(ax, xs, vals, fmt, sel=None, dy=3):
    for i, (x, v) in enumerate(zip(xs, vals)):
        if sel is None or i in sel:
            ax.annotate(fmt(v), (x, v), textcoords="offset points", xytext=(0, dy),
                        ha="center", va="bottom", fontsize=8.2, color=SEC)

# 1. Aggregate universe (landing) ------------------------------------------
fig, (a1, a2) = plt.subplots(2, 1, figsize=(11.5, 7.1), dpi=200,
                             gridspec_kw=dict(height_ratios=[2.1, 1], hspace=0.32))
header(fig,
       "The universe peaked at $8.7 trillion in Q1 and ended the half at $8.23 trillion",
       "Aggregate post-money valuation ($B, top) and active unicorn count (bottom), 2016 to mid-2026.",
       "Source: PitchBook Q2 2026 Quarterly Unicorn Tracker, 'Aggregate unicorns' tab | *As of 6/30/2026. Q1 2026 peak $8,699.7B from the quarterly series; SpaceX's June listing removed its value from the universe.")
style_ax(a1)
a1.bar(YEARS, AGG_VAL, width=0.62, color=BLUE, edgecolor=SURF, linewidth=1)
bar_labels(a1, YEARS, AGG_VAL, lambda v: f"{v:,.0f}", sel={0, 5, 9, 10})
a1.scatter([2026.31], [8699.7], marker="_", s=260, color=INK, zorder=6)
a1.annotate("Q1 2026 peak $8,699.7B", (2026.31, 8699.7), textcoords="offset points",
            xytext=(-2, 9), ha="right", fontsize=8.4, color=INK)
a1.set_xticks(YEARS); a1.set_xticklabels(XLBL)
a1.set_ylabel("Aggregate value ($B)", fontsize=9, color=SEC)
a1.set_ylim(0, 9600)
style_ax(a2)
a2.plot(YEARS, AGG_CNT, color=BLUE, lw=2, marker="o", ms=4.5, markerfacecolor=BLUE,
        markeredgecolor=SURF, markeredgewidth=1.2)
for i in (0, 5, 10):
    a2.annotate(f"{AGG_CNT[i]:,}", (YEARS[i], AGG_CNT[i]), textcoords="offset points",
                xytext=(0, 8), ha="center", fontsize=8.2, color=SEC)
a2.set_xticks(YEARS); a2.set_xticklabels(XLBL)
a2.set_ylabel("Active unicorns", fontsize=9, color=SEC)
a2.set_ylim(0, 2100)
fig.subplots_adjust(left=0.075, right=0.97, top=0.865, bottom=0.09)
fig.savefig("q2_2026_aggregate_universe.png", facecolor=SURF)
plt.close(fig)

# 2. Deal activity ----------------------------------------------------------
fig, (a1, a2) = plt.subplots(2, 1, figsize=(11.5, 7.1), dpi=200,
                             gridspec_kw=dict(height_ratios=[2.1, 1], hspace=0.32))
header(fig,
       "2026 deal value is a record built on far fewer deals",
       "Unicorn deal value ($B, top) and deal count (bottom), 2016 to mid-2026.",
       "Source: PitchBook Q2 2026 Quarterly Unicorn Tracker, 'Unicorn deal activity' tab | *2026 is YTD through 6/30/2026: Q1 $251.3B, Q2 $144.9B.")
style_ax(a1)
a1.bar(YEARS, DEAL_VAL, width=0.62, color=BLUE, edgecolor=SURF, linewidth=1)
bar_labels(a1, YEARS, DEAL_VAL, lambda v: f"{v:,.0f}", sel={5, 9, 10})
a1.annotate("Q1 251.3 + Q2 144.9", (2026, 396.137), textcoords="offset points",
            xytext=(0, 16), ha="center", fontsize=8.2, color=MUT)
a1.set_xticks(YEARS); a1.set_xticklabels(XLBL)
a1.set_ylabel("Deal value ($B)", fontsize=9, color=SEC)
a1.set_ylim(0, 470)
style_ax(a2)
a2.plot(YEARS, DEAL_CNT, color=BLUE, lw=2, marker="o", ms=4.5, markerfacecolor=BLUE,
        markeredgecolor=SURF, markeredgewidth=1.2)
for i in (5, 10):
    a2.annotate(f"{DEAL_CNT[i]:,}", (YEARS[i], DEAL_CNT[i]), textcoords="offset points",
                xytext=(0, 8), ha="center", fontsize=8.2, color=SEC)
a2.set_xticks(YEARS); a2.set_xticklabels(XLBL)
a2.set_ylabel("Deal count", fontsize=9, color=SEC)
a2.set_ylim(0, 2200)
fig.subplots_adjust(left=0.075, right=0.97, top=0.865, bottom=0.09)
fig.savefig("q2_2026_deal_activity.png", facecolor=SURF)
plt.close(fig)

# 3. Median vs average post value ------------------------------------------
fig, ax = plt.subplots(figsize=(11.5, 7.1), dpi=200)
header(fig,
       "The median and the average describe two different markets",
       "Median and average unicorn post-money valuation ($B), log scale, 2016 to mid-2026.",
       "Source: PitchBook Q2 2026 Quarterly Unicorn Tracker, 'MedAvg Uni Post Value' tab | *As of 6/30/2026. The 2026 average-to-median ratio is 9.1x, vs 3.1x in 2025.")
style_ax(ax)
ax.set_yscale("log")
from matplotlib.ticker import FixedLocator, NullFormatter, FuncFormatter
yt = [0.1, 0.25, 0.5, 1, 2, 5, 10, 20]
ax.yaxis.set_major_locator(FixedLocator(yt))
ax.yaxis.set_major_formatter(FuncFormatter(lambda v, p: f"{v:g}"))
ax.yaxis.set_minor_locator(FixedLocator([]))
ax.yaxis.set_minor_formatter(NullFormatter())
ax.plot(YEARS, AVG_POST, color=ORANGE, lw=2, marker="o", ms=4.5,
        markerfacecolor=ORANGE, markeredgecolor=SURF, markeredgewidth=1.2, label="Average")
ax.plot(YEARS, MED_POST, color=BLUE, lw=2, marker="o", ms=4.5,
        markerfacecolor=BLUE, markeredgecolor=SURF, markeredgewidth=1.2, label="Median")
ax.annotate("Average $18.19B", (2026, 18.187), textcoords="offset points", xytext=(-2, 12),
            ha="right", fontsize=8.8, color=INK)
ax.annotate("Median $2.0B", (2026, 2.0), textcoords="offset points", xytext=(-4, -18),
            ha="right", fontsize=8.8, color=INK)
ax.set_xticks(YEARS); ax.set_xticklabels(XLBL)
ax.set_ylabel("Post-money valuation ($B, log)", fontsize=9, color=SEC)
ax.set_ylim(0.08, 40)
ax.legend(loc="upper left", frameon=False, fontsize=9)
fig.subplots_adjust(left=0.075, right=0.97, top=0.865, bottom=0.09)
fig.savefig("q2_2026_median_average.png", facecolor=SURF)
plt.close(fig)

# 4. Repricing: step-up, interval, down rounds ------------------------------
fig, axes = plt.subplots(1, 3, figsize=(11.5, 6.4), dpi=200)
fig.subplots_adjust(left=0.06, right=0.975, top=0.80, bottom=0.11, wspace=0.3)
header(fig,
       "Companies that raised were repriced upward quickly",
       "Median valuation step-up (x), median years between rounds, and down-round count, 2016 to mid-2026.",
       "Source: PitchBook Q2 2026 Quarterly Unicorn Tracker, 'MedAvg Uni Val Step Up', 'MedAvg Uni Time Between Rnds', 'Unicorn down round activity' tabs | *2026 is YTD through 6/30/2026.")
panels = [("Median step-up (x)", STEP_MED, "line", "2.20x"),
          ("Median years between rounds", TBR_MED, "line", "0.98yr"),
          ("Down rounds (count)", DOWN_CNT, "bar", "6")]
for ax, (t, series, kind, endlab) in zip(axes, panels):
    style_ax(ax)
    ax.set_title(t, fontsize=9.5, color=SEC, loc="left", pad=8)
    if kind == "line":
        ax.plot(YEARS, series, color=BLUE, lw=2, marker="o", ms=3.6,
                markerfacecolor=BLUE, markeredgecolor=SURF, markeredgewidth=1)
    else:
        ax.bar(YEARS, series, width=0.62, color=BLUE, edgecolor=SURF, linewidth=1)
    ax.annotate(endlab, (2026, series[-1]), textcoords="offset points",
                xytext=(0, 8), ha="center", fontsize=8.6, color=INK, fontweight="bold")
    ax.set_xticks([2016, 2021, 2026]); ax.set_xticklabels(["2016", "2021", "2026*"])
fig.savefig("q2_2026_repricing.png", facecolor=SURF)
plt.close(fig)

# 5. AI vs universe aggregate ----------------------------------------------
fig, ax = plt.subplots(figsize=(11.5, 7.1), dpi=200)
header(fig,
       "AI reached 61.7% of all unicorn value at mid-2026",
       "Aggregate post-money valuation ($B): all unicorns and the AI cohort, 2016 to mid-2026.",
       "Source: PitchBook Q2 2026 Quarterly Unicorn Tracker, 'Aggregate unicorns' and 'AI Aggregate unicorns' tabs | *As of 6/30/2026. AI share of value: 39% in 2024, 48% in 2025, 61.7% at mid-2026.")
style_ax(ax)
ax.plot(YEARS, AGG_VAL, color=MUT, lw=2, marker="o", ms=4.2,
        markerfacecolor=MUT, markeredgecolor=SURF, markeredgewidth=1.2, label="All unicorns")
ax.plot(YEARS, AI_VAL, color=BLUE, lw=2.4, marker="o", ms=4.5,
        markerfacecolor=BLUE, markeredgecolor=SURF, markeredgewidth=1.2, label="AI unicorns")
ax.annotate("All unicorns $8,232.5B", (2026, 8232.5), textcoords="offset points",
            xytext=(2, 10), ha="right", fontsize=8.8, color=SEC)
ax.annotate("AI $5,076.4B", (2026, 5076.4), textcoords="offset points",
            xytext=(-2, 12), ha="right", fontsize=8.8, color=INK)
ax.set_xticks(YEARS); ax.set_xticklabels(XLBL)
ax.set_ylabel("Aggregate value ($B)", fontsize=9, color=SEC)
ax.set_ylim(0, 9600)
ax.legend(loc="upper left", frameon=False, fontsize=9)
fig.subplots_adjust(left=0.075, right=0.97, top=0.865, bottom=0.09)
fig.savefig("q2_2026_ai_aggregate.png", facecolor=SURF)
plt.close(fig)

# 6. Exit activity ----------------------------------------------------------
fig, (a1, a2) = plt.subplots(2, 1, figsize=(11.5, 7.1), dpi=200,
                             gridspec_kw=dict(height_ratios=[2.1, 1], hspace=0.32))
header(fig,
       "One listing is four-fifths of 2026 exit value",
       "Unicorn exit value ($B, top; SpaceX shown separately in 2026) and exit count (bottom), 2016 to mid-2026.",
       "Source: PitchBook Q2 2026 Quarterly Unicorn Tracker, 'Unicorn exit activity' and PT-Exits tabs | *2026 is YTD through 6/30/2026. SpaceX listing $1,690.2B; all other 2026 exits $420.7B.")
style_ax(a1)
ex_other = EXIT_VAL[:-1] + [EXIT_VAL[-1] - SPACEX_EXIT]
a1.bar(YEARS, ex_other, width=0.62, color=BLUE, edgecolor=SURF, linewidth=1, label="Exit value")
a1.bar([2026], [SPACEX_EXIT], width=0.62, bottom=[ex_other[-1]], color="#a9c7ec",
       edgecolor=SURF, linewidth=1, label="SpaceX listing (2026)")
bar_labels(a1, YEARS, EXIT_VAL, lambda v: f"{v:,.0f}", sel={5, 10})
a1.annotate("ex-SpaceX 420.7", (2026, ex_other[-1]), textcoords="offset points",
            xytext=(-16, 4), ha="right", va="center", fontsize=8.2, color=SEC)
a1.set_xticks(YEARS); a1.set_xticklabels(XLBL)
a1.set_ylabel("Exit value ($B)", fontsize=9, color=SEC)
a1.set_ylim(0, 2500)
a1.legend(loc="upper left", frameon=False, fontsize=8.6)
style_ax(a2)
a2.plot(YEARS, EXIT_CNT, color=BLUE, lw=2, marker="o", ms=4.5, markerfacecolor=BLUE,
        markeredgecolor=SURF, markeredgewidth=1.2)
for i in (5, 10):
    a2.annotate(f"{EXIT_CNT[i]}", (YEARS[i], EXIT_CNT[i]), textcoords="offset points",
                xytext=(0, 8), ha="center", fontsize=8.2, color=SEC)
a2.set_xticks(YEARS); a2.set_xticklabels(XLBL)
a2.set_ylabel("Exit count", fontsize=9, color=SEC)
a2.set_ylim(0, 160)
fig.subplots_adjust(left=0.075, right=0.97, top=0.865, bottom=0.09)
fig.savefig("q2_2026_exit_activity.png", facecolor=SURF)
plt.close(fig)

# 7. RVVC -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11.5, 7.1), dpi=200)
header(fig,
       "Value created per dollar invested is back above its pre-boom level",
       "Median relative velocity of value creation (new valuation created per dollar invested), 2016 to mid-2026.",
       "Source: PitchBook Q2 2026 Quarterly Unicorn Tracker, 'MedAvg Uni RVVC' tab | *As of 6/30/2026. Pre-boom baseline 0.73 = 2016-2018 average of annual medians.")
style_ax(ax)
ax.axhline(1.0, color="#dcdcd6", lw=1)
ax.text(2015.7, 1.03, "1.0x: a dollar in, a dollar of new value out", fontsize=8.2, color=MUT)
ax.axhline(0.7306, color=MUT, lw=1, ls=(0, (4, 3)))
ax.text(2015.7, 0.66, "pre-boom baseline 0.73x", fontsize=8.2, color=MUT)
ax.plot(YEARS, RVVC_MED, color=BLUE, lw=2.2, marker="o", ms=4.6,
        markerfacecolor=BLUE, markeredgecolor=SURF, markeredgewidth=1.2)
for i, lab in [(5, "1.76x"), (7, "0.23x"), (10, "1.42x")]:
    dy = 10 if i != 7 else -16
    ax.annotate(lab, (YEARS[i], RVVC_MED[i]), textcoords="offset points",
                xytext=(0, dy), ha="center", fontsize=8.8, color=INK)
ax.set_xticks(YEARS); ax.set_xticklabels(XLBL)
ax.set_ylabel("Median RVVC (x)", fontsize=9, color=SEC)
ax.set_ylim(0, 2.0)
fig.subplots_adjust(left=0.075, right=0.97, top=0.865, bottom=0.09)
fig.savefig("q2_2026_rvvc.png", facecolor=SURF)
plt.close(fig)

# 8. 301 US AI unicorns by layer -------------------------------------------
fig, ax = plt.subplots(figsize=(11.5, 6.6), dpi=200)
header(fig,
       "The 301 US AI unicorns are mostly applications on someone else's models",
       "Companies by stack layer, with the largest sub-layers of each. Hand-scored roster as of 6/30/2026.",
       "Source: US AI/ML Hand-Scored workbooks (roster and layer classification; scores from the hand-scored panel) | Sub-layer counts shown for the largest groups in each layer.")
style_ax(ax)
ax.grid(axis="x", color=GRID, lw=0.7)
ax.grid(axis="y", visible=False)
layers = [("Application layer", 246, "AI applications 160 · healthcare 27 · robotics/autonomy 21 · defense 8"),
          ("Data & infrastructure layer", 35, "compute/silicon 14 · data/MLOps 6 · accelerator silicon 5 · GPU cloud 4"),
          ("Model layer", 20, "foundation model developers 9 · frontier LLM labs 6")]
ys = [0, 1, 2][::-1]
for (name, cnt, subs), y in zip(layers, ys):
    ax.barh(y, cnt, height=0.52, color=BLUE, edgecolor=SURF, linewidth=1)
    ax.annotate(f"{cnt}", (cnt, y), textcoords="offset points", xytext=(6, 0),
                ha="left", va="center", fontsize=10.5, color=INK, fontweight="bold")
    ax.annotate(subs, (0, y), textcoords="offset points", xytext=(2, -36),
                ha="left", va="center", fontsize=8.4, color=SEC)
ax.set_yticks(ys)
ax.set_yticklabels([l[0] for l in layers], fontsize=9.6, color=INK)
ax.set_xlim(0, 275)
ax.set_xlabel("Companies", fontsize=9, color=SEC)
fig.subplots_adjust(left=0.21, right=0.96, top=0.84, bottom=0.11)
fig.savefig("q2_2026_ai_stack_301.png", facecolor=SURF)
plt.close(fig)

print("done")
