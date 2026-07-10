"""Chart generation for the Databricks initiation note.
Renders 10 embargo-safe PNGs at 300 DPI in the house palette.
No score-versus-valuation scatter, no trendlines, no correlation statistics.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

NAVY = "#1F2A44"
SLATE = "#35506E"
GREEN = "#1C5D46"
GREY = "#6B7280"
SOFT = "#F2F5F9"
WARN = "#8F3421"
INK = "#2B3446"

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

def style_ax(ax, grid_axis="x"):
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    if grid_axis:
        ax.grid(axis=grid_axis, color=SOFT, linewidth=0.9, zorder=0)
    ax.set_axisbelow(True)

def title_block(fig, title, subtitle, x=0.01):
    fig.text(x, 0.985, title, ha="left", va="top", fontsize=10.5,
             fontweight="bold", color=NAVY)
    fig.text(x, 0.925, subtitle, ha="left", va="top", fontsize=7.6, color=GREY)

def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=300, bbox_inches="tight",
                pad_inches=0.12)
    plt.close(fig)
    print("wrote", name)

# ---------------------------------------------------------------- 1. hero
def per_point_ladder():
    rows = [
        ("xAI (implied, est.)", 345, GREY, True),
        ("OpenAI", 188, NAVY, False),
        ("Anthropic", 118, SLATE, False),
        ("Databricks", 15.2, GREEN, False),
    ]
    fig, ax = plt.subplots(figsize=(6.5, 3.1))
    fig.subplots_adjust(top=0.80, left=0.17, right=0.97, bottom=0.13)
    y = np.arange(len(rows))
    for i, (name, val, col, est) in enumerate(rows):
        ax.barh(i, val, height=0.62, color=col, zorder=3,
                hatch="///" if est else None, edgecolor="white" if est else col,
                linewidth=0.6)
        lbl = f"${val:,.1f}B / pt" if val < 100 else f"~${val:,.0f}B / pt"
        ax.text(val + 6, i, lbl, va="center", ha="left", fontsize=8.4,
                fontweight="bold",
                color=GREEN if col == GREEN else INK)
    ax.set_yticks(y, [r[0] for r in rows], fontsize=8.6)
    ax.set_xlim(0, 430)
    ax.set_xlabel("Valuation per AIBQ point ($B)", fontsize=7.8)
    style_ax(ax, "x")
    ax.text(345, 3.52, "23x the Databricks price per unit of quality",
            fontsize=7.3, color=GREY, ha="right", style="italic")
    title_block(fig, "The buyer pays the least per unit of quality in the cohort",
                "Valuation per AIBQ point, July 2026. Databricks $134B / 8.81; Anthropic $965B / 8.20; OpenAI $852B / 4.53;\n"
                "xAI est. ~$1.55T implied inside listed SpaceX / 4.49. SSI excluded (pre-revenue; ratio not meaningful).")
    save(fig, "per_point.png")

# ---------------------------------------------------------- 2. acceleration
def acceleration():
    labels = ["Sep 2025", "Dec 2025", "Feb 2026", "Jun 2026"]
    rr = [4.0, 4.8, 5.4, 6.9]
    gr = [50, 55, 65, 80]
    fig, ax = plt.subplots(figsize=(6.5, 3.2))
    fig.subplots_adjust(top=0.80, left=0.08, right=0.92, bottom=0.12)
    x = np.arange(4)
    cols = [SLATE, SLATE, SLATE, GREEN]
    ax.bar(x, rr, width=0.56, color=cols, zorder=3)
    for i, v in enumerate(rr):
        ax.text(i, v / 2, f"${v:.1f}B", ha="center", va="center",
                color="white", fontsize=8.4, fontweight="bold")
    ax.set_xticks(x, labels, fontsize=8.2)
    ax.set_ylim(0, 8.6)
    ax.set_ylabel("Revenue run-rate ($B)", fontsize=7.8)
    style_ax(ax, "y")
    ax2 = ax.twinx()
    ax2.plot(x, gr, color=WARN, linewidth=2.0, marker="o", markersize=5.5,
             zorder=5)
    for i, v in enumerate(gr):
        ax2.annotate(f"+{v}%", (i, v), textcoords="offset points",
                     xytext=(0, 9), ha="center", fontsize=8.2,
                     fontweight="bold", color=WARN)
    ax2.set_ylim(30, 95)
    ax2.set_ylabel("YoY growth (%)", fontsize=7.8, color=WARN)
    ax2.tick_params(colors=WARN, labelsize=7.5)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_color("#E3C4B8")
    title_block(fig, "Growth is accelerating at $7B scale, not decelerating",
                "Annualized revenue run-rate (bars, left) and year-over-year growth (line, right), company disclosures Sep 2025 to Jun 2026.")
    save(fig, "acceleration.png")

# ------------------------------------------------- 3. growth-adjusted multiple
def growth_adjusted():
    fig, ax = plt.subplots(figsize=(6.5, 3.6))
    fig.subplots_adjust(top=0.82, left=0.08, right=0.97, bottom=0.13)
    g = np.linspace(0, 100, 200)
    # iso-value rays: multiple = k x growth-points
    for k in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]:
        ax.plot(g, k * g, color="#DDE3EC", linewidth=0.8, zorder=1)
        yl = k * 96
        if yl < 24.5:
            ax.text(97, yl, f"{k:.1f}x/pt", fontsize=6.4, color="#B4BCC9",
                    va="center")
    ax.plot(g, 0.24 * g, color=GREEN, linewidth=1.4, linestyle="--", zorder=2)
    ax.plot(g, 0.49 * g, color=NAVY, linewidth=1.4, linestyle="--", zorder=2)
    ax.scatter([80], [19.4], s=180, color=GREEN, zorder=6,
               edgecolor="white", linewidth=1.4)
    ax.scatter([31], [15.3], s=180, color=NAVY, zorder=6,
               edgecolor="white", linewidth=1.4)
    ax.annotate("Databricks\n19.4x fwd run-rate, +80% growth\n= 0.24x per growth point",
                (80, 19.4), xytext=(56, 8.0), fontsize=8.0, color=GREEN,
                fontweight="bold",
                arrowprops=dict(arrowstyle="-", color=GREEN, lw=0.9))
    ax.annotate("Snowflake\n15.3x fwd product revenue, +31% guide\n= 0.49x per growth point",
                (31, 15.3), xytext=(6.0, 20.0), fontsize=8.0, color=NAVY,
                fontweight="bold",
                arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.9))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 25)
    ax.set_xlabel("Forward revenue growth (%)", fontsize=7.8)
    ax.set_ylabel("Forward revenue multiple (x)", fontsize=7.8)
    style_ax(ax, "")
    title_block(fig, "Growth-adjusted, Databricks trades at roughly half Snowflake's price",
                "Revenue multiple vs growth rate, July 2026. Dashed rays are iso-value lines (equal multiple per point of growth);\n"
                "a lower ray means the buyer pays less for each unit of growth purchased. Two-company comparison; no fitted line.")
    save(fig, "growth_adjusted.png")

# ----------------------------------------------------------------- 4. radar
def radar():
    dims = ["Capital\nEfficiency (20%)", "Revenue\nQuality (25%)",
            "Compute\nIndependence (15%)", "Governance\nOptionality (20%)",
            "Moat\nDurability (20%)"]
    dbx = [8.9, 9.0, 8.0, 8.9, 9.0]
    cohort = [5.6, 6.0, 5.9, 5.2, 5.5]
    ang = np.linspace(0, 2 * np.pi, len(dims), endpoint=False).tolist()
    dbx_c = dbx + dbx[:1]
    coh_c = cohort + cohort[:1]
    ang_c = ang + ang[:1]
    fig = plt.figure(figsize=(6.5, 3.9))
    ax = fig.add_subplot(111, polar=True)
    fig.subplots_adjust(top=0.76, bottom=0.05)
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.plot(ang_c, coh_c, color=GREY, linewidth=1.4, linestyle="--", zorder=3)
    ax.fill(ang_c, coh_c, color=GREY, alpha=0.08, zorder=2)
    ax.plot(ang_c, dbx_c, color=GREEN, linewidth=2.0, zorder=4)
    ax.fill(ang_c, dbx_c, color=GREEN, alpha=0.16, zorder=3)
    for a, v in zip(ang, dbx):
        ax.annotate(f"{v:.1f}", (a, v), textcoords="offset points",
                    xytext=(0, 7), ha="center", fontsize=8.2,
                    fontweight="bold", color=GREEN)
    ax.set_xticks(ang)
    ax.set_xticklabels(dims, fontsize=7.6, color=INK)
    ax.set_ylim(0, 10)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels(["2", "4", "6", "8", ""], fontsize=6.5, color="#B4BCC9")
    ax.grid(color="#E4E9F0", linewidth=0.8)
    ax.spines["polar"].set_color("#E4E9F0")
    leg = [plt.Line2D([], [], color=GREEN, lw=2, label="Databricks (8.81 composite)"),
           plt.Line2D([], [], color=GREY, lw=1.4, ls="--",
                      label="Frontier Five average (5.65, desk est.)")]
    ax.legend(handles=leg, loc="lower center", bbox_to_anchor=(0.5, -0.22),
              ncol=2, frameon=False, fontsize=7.6)
    title_block(fig, "Elite on four dimensions; compute independence is the honest notch",
                "AIBQ dimension scores (0-10, weights in parentheses), July 2026. Cohort dimension averages are desk estimates\n"
                "consistent with published composites. Databricks CI 8.0 reflects hyperscaler distribution dependence, mitigated by multi-cloud posture.")
    save(fig, "radar.png")

# ------------------------------------------------------------ 5. gate gauge
def gate_gauge():
    fig, ax = plt.subplots(figsize=(6.5, 2.3))
    fig.subplots_adjust(top=0.70, left=0.03, right=0.97, bottom=0.22)
    lo, hi = 60, 86
    ax.axvspan(lo, 70, color=WARN, alpha=0.10, zorder=1)
    ax.axvspan(70, hi, color=GREEN, alpha=0.07, zorder=1)
    ax.axvline(70, color=WARN, linewidth=2.0, zorder=4)
    ax.text(70, 1.42, "efficiency-gate floor: 70%", ha="center", fontsize=8.0,
            fontweight="bold", color=WARN)
    ax.barh(0.55, 74 - lo, left=lo, height=0.34, color=GREEN, zorder=3)
    ax.text(74 + 0.4, 0.55, "74%  (Jun 2026)", va="center", fontsize=9.0,
            fontweight="bold", color=GREEN)
    ax.plot([80.5, 80.5], [0.38, 0.72], color=GREY, linewidth=2.0, zorder=4)
    ax.text(80.5, 0.86, ">80% (2025 level)", ha="center", fontsize=7.4,
            color=GREY)
    ax.annotate("", xy=(74, 0.16), xytext=(70, 0.16),
                arrowprops=dict(arrowstyle="<->", color=INK, lw=1.1))
    ax.text(72, 0.02, "cushion: ~4 pts (~$280M of annualized gross profit)",
            ha="center", fontsize=7.6, color=INK, style="italic")
    ax.set_xlim(lo, hi)
    ax.set_ylim(-0.1, 1.6)
    ax.set_yticks([])
    ax.set_xticks([60, 65, 70, 75, 80, 85])
    ax.set_xticklabels(["60%", "65%", "70%", "75%", "80%", "85%"])
    style_ax(ax, "")
    ax.spines["left"].set_visible(False)
    title_block(fig, "The number that changes the rating: gross margin vs the 70% gate",
                "Gross margin against the AIBQ efficiency-gate floor. A print below 70% breaks the gate and forces a re-score.\n"
                "Guided lower on agentic compute costs; watch the ~Sep-Oct 2026 disclosure.")
    save(fig, "gate_gauge.png")

# ------------------------------------------------------------------ 6. CE bars
def ce_bars():
    rows = [("Anthropic (est.)", 0.38, SLATE), ("Databricks", 0.34, GREEN),
            ("OpenAI (est.)", 0.14, NAVY), ("xAI (est.)", 0.07, GREY)]
    fig, ax = plt.subplots(figsize=(6.5, 2.9))
    fig.subplots_adjust(top=0.78, left=0.16, right=0.96, bottom=0.15)
    y = np.arange(len(rows))[::-1]
    for yi, (name, v, c) in zip(y, rows):
        ax.barh(yi, v, height=0.6, color=c, zorder=3)
        ax.text(v + 0.008, yi, f"{v:.2f}x", va="center", fontsize=8.6,
                fontweight="bold", color=GREEN if c == GREEN else INK)
    ax.set_yticks(y, [r[0] for r in rows], fontsize=8.6)
    ax.set_xlim(0, 0.46)
    ax.set_xlabel("Run-rate revenue per dollar of lifetime equity raised (x)",
                  fontsize=7.8)
    style_ax(ax, "x")
    ax.text(0.45, 3.35, "only two members of the cohort compound;\nthe rest consume",
            fontsize=7.3, color=GREY, ha="right", style="italic")
    title_block(fig, "Capital efficiency: growth funded from within, not from the capital markets",
                "Revenue run-rate divided by cumulative equity raised (debt excluded by AIBQ ruling), July 2026.\n"
                "Databricks: $6.9B / ~$20.2B. Peer ratios are desk estimates from reported raises and run-rates.")
    save(fig, "ce_bars.png")

# ------------------------------------------------------------ 7. football field
def football_field():
    fig, ax = plt.subplots(figsize=(6.5, 3.0))
    fig.subplots_adjust(top=0.78, left=0.20, right=0.96, bottom=0.16)
    scen = [("Bull:  durability re-rate", 205, 240, SLATE),
            ("Base:  growth does the work", 155, 190, GREEN),
            ("Bear:  gate breaks", 115, 130, WARN)]
    for i, (name, a, b, c) in enumerate(scen):
        ax.barh(i, b - a, left=a, height=0.5, color=c, zorder=3, alpha=0.92)
        ax.text(a - 3, i, f"${a}B", va="center", ha="right", fontsize=8.0,
                color=INK)
        ax.text(b + 3, i, f"${b}B" + ("+" if i == 0 else ""), va="center",
                ha="left", fontsize=8.0, color=INK)
    ax.axvline(134, color=INK, linewidth=1.5, linestyle="-", zorder=4)
    ax.text(134, 2.62, "current mark $134B\n(Series L, Feb 2026)", ha="center",
            fontsize=7.4, color=INK)
    ax.axvspan(165, 175, color=SLATE, alpha=0.18, zorder=2)
    ax.text(170, -0.62, "rumored range $165-175B\n(unclosed; press reports, Jun 9)",
            ha="center", fontsize=7.4, color=SLATE)
    ax.set_yticks(range(3), [s[0] for s in scen], fontsize=8.4)
    ax.set_xlim(95, 260)
    ax.set_ylim(-1.0, 3.1)
    ax.set_xlabel("Implied valuation ($B), 12-month view", fontsize=7.8)
    style_ax(ax, "x")
    title_block(fig, "The base case reaches the rumored range without adopting it",
                "Scenario valuation ranges, 12-month forward view anchored on the $134B mark. The rumored raise is a reference\n"
                "line, not an input: the base case is fundamentals (forward run-rate x sustained multiple), not the last private print.")
    save(fig, "football_field.png")

# ------------------------------------------------------------- 8. sensitivity
def sensitivity():
    rr = [9.5, 10.5, 11.5, 12.5, 13.5]
    mult = [20, 18, 16, 14, 12, 10]
    grid = np.array([[m * r for r in rr] for m in mult])
    cmap = LinearSegmentedColormap.from_list("navy_seq", [SOFT, "#8FA5C4", NAVY])
    fig, ax = plt.subplots(figsize=(6.5, 3.4))
    fig.subplots_adjust(top=0.80, left=0.13, right=0.97, bottom=0.14)
    im = ax.imshow(grid, cmap=cmap, aspect="auto", vmin=80, vmax=280)
    for i in range(len(mult)):
        for j in range(len(rr)):
            v = grid[i, j]
            ax.text(j, i, f"${v:.0f}B", ha="center", va="center", fontsize=8.2,
                    fontweight="bold",
                    color="white" if v > 180 else NAVY)
    # base intersection: 11.5B x 14-16x
    ax.add_patch(mpatches.Rectangle((2 - 0.5, 2 - 0.5), 1, 2, fill=False,
                                    edgecolor=GREEN, linewidth=2.4, zorder=5))
    ax.text(2, 1.28, "base case", ha="center", fontsize=7.8, fontweight="bold",
            color=GREEN)
    ax.set_xticks(range(len(rr)), [f"${r}B" for r in rr], fontsize=8)
    ax.set_yticks(range(len(mult)), [f"{m}x" for m in mult], fontsize=8)
    ax.set_xlabel("Mid-2027E revenue run-rate", fontsize=7.8)
    ax.set_ylabel("Run-rate multiple", fontsize=7.8)
    for s in ax.spines.values():
        s.set_visible(False)
    title_block(fig, "Valuation sensitivity: run-rate times multiple, twelve months out",
                "Implied valuation ($B) across forward run-rate and multiple. Base case: ~$11.5B run-rate (graceful deceleration\n"
                "to ~65-70% growth) at 14-16x, a de-rate from today's 19.4x. Bear and bull corners shown for discipline, not drama.")
    save(fig, "sensitivity.png")

# ------------------------------------------------------------ 9. composition
def composition():
    cats = [("Core platform &\nother", NAVY), ("Databricks SQL", SLATE),
            ("AI products", GREEN)]
    actual = [3.7, 1.5, 1.7]   # Jun 2026
    fwd = [5.5, 2.5, 3.5]      # Jun 2027E
    fig, ax = plt.subplots(figsize=(6.5, 3.3))
    fig.subplots_adjust(top=0.80, left=0.08, right=0.75, bottom=0.10)
    for xi, vals, tot in [(0, actual, 6.9), (1, fwd, 11.5)]:
        bottom = 0
        for (name, col), v in zip(cats, vals):
            ax.bar(xi, v, bottom=bottom, width=0.5, color=col, zorder=3,
                   edgecolor="white", linewidth=1.6,
                   alpha=1.0 if xi == 0 else 0.82)
            if v > 0.8:
                ax.text(xi, bottom + v / 2, f"${v:.1f}B", ha="center",
                        va="center", color="white", fontsize=8.4,
                        fontweight="bold")
            bottom += v
        ax.text(xi, bottom + 0.22, f"${tot:.1f}B", ha="center", fontsize=9.0,
                fontweight="bold", color=INK)
    ax.annotate("AI share: 25%", (0.27, 6.05), fontsize=8.0, color=GREEN,
                fontweight="bold")
    ax.annotate("AI share: ~30% (est.)", (1.27, 9.8), fontsize=8.0,
                color=GREEN, fontweight="bold")
    ax.set_xticks([0, 1], ["Jun 2026 (disclosed)", "Jun 2027E (desk est.)"],
                  fontsize=8.4)
    ax.set_xlim(-0.55, 2.1)
    ax.set_ylim(0, 13)
    ax.set_ylabel("Revenue run-rate ($B)", fontsize=7.8)
    style_ax(ax, "y")
    handles = [mpatches.Patch(color=c, label=n.replace("\n", " "))
               for n, c in cats[::-1]]
    ax.legend(handles=handles, loc="center left", bbox_to_anchor=(1.02, 0.5),
              frameon=False, fontsize=7.8)
    title_block(fig, "The AI line is the largest and fastest product, on top of a profitable core",
                "Revenue composition by product line. Jun 2026: AI products $1.7B, Databricks SQL $1.5B, core platform ~$3.7B\n"
                "(residual). Forward split is a desk estimate; AI line grew ~70% in four months ($1.4B Feb to $1.7B Jun).")
    save(fig, "composition.png")

# ------------------------------------------------------------ 10. absorption
def absorption():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.5, 3.2),
                                   gridspec_kw={"width_ratios": [1.25, 1]})
    fig.subplots_adjust(top=0.76, left=0.16, right=0.97, bottom=0.14,
                        wspace=0.52)
    rows = [("SpaceX + xAI", 1.77, GREY, "listed Jun 2026,\n+23% since debut"),
            ("OpenAI", 1.00, NAVY, "target; paperwork\nreportedly filed"),
            ("Anthropic", 0.965, SLATE, "last mark; paperwork\nreportedly filed"),
            ("Databricks", 0.17, GREEN, "if rumored range\nmarks (est.)")]
    y = np.arange(len(rows))[::-1]
    for yi, (n, v, c, note) in zip(y, rows):
        ax1.barh(yi, v, height=0.58, color=c, zorder=3)
        ax1.text(v + 0.04, yi + 0.13, f"${v:,.2f}T", va="center", fontsize=8.2,
                 fontweight="bold", color=GREEN if c == GREEN else INK)
        ax1.text(v + 0.04, yi - 0.22, note, va="center", fontsize=6.2,
                 color=GREY)
    ax1.set_yticks(y, [r[0] for r in rows], fontsize=8.2)
    ax1.set_xlim(0, 2.75)
    ax1.set_xlabel("Listing value ($T)", fontsize=7.8)
    style_ax(ax1, "x")
    ax1.set_title("The wave: ~$3.9T of listings", fontsize=8.6, color=NAVY,
                  fontweight="bold", loc="left", pad=8)
    bars = [("Potential combined\nprimary raises", 240, NAVY),
            ("Total 2025 US\nIPO proceeds", 45, GREY)]
    x = np.arange(2)
    for xi, (n, v, c) in zip(x, bars):
        ax2.bar(xi, v, width=0.52, color=c, zorder=3)
        ax2.text(xi, v + 7, f"~${v}B", ha="center", fontsize=8.6,
                 fontweight="bold", color=INK)
    ax2.set_xticks(x, [b[0] for b in bars], fontsize=7.6)
    ax2.set_ylim(0, 300)
    ax2.set_ylabel("$B", fontsize=7.8)
    style_ax(ax2, "y")
    ax2.set_title("The wall: 5x a full year's issuance", fontsize=8.6,
                  color=NAVY, fontweight="bold", loc="left", pad=8)
    title_block(fig, "The absorption question: a mega-listing wave against a $45B-a-year market",
                "Left: AI mega-listing values ($T); SpaceX has already cleared. Right: potential combined primary raises vs total 2025\n"
                "US IPO proceeds ($44-47B per Deloitte/EY). Databricks needs the least primary capital of any name in the wave.")
    save(fig, "absorption.png")

# ------------------------------------------------------- 11. valuation ladder
def valuation_ladder():
    rounds = [
        ("Series G\nFeb 2021", 28, "$1.0B"),
        ("Series H\nAug 2021", 38, "$1.6B"),
        ("Series I\nNov 2023", 43, "$0.7B"),
        ("Series J\nDec 2024", 62, "$10.2B"),
        ("Series K\nSep 2025", 100, "$1.0B"),
        ("Series L\nDec 25/Feb 26", 134, "$7.0B"),
    ]
    fig, ax = plt.subplots(figsize=(6.5, 3.3))
    fig.subplots_adjust(top=0.78, left=0.08, right=0.97, bottom=0.16)
    x = np.arange(len(rounds))
    vals = [r[1] for r in rounds]
    cols = [SLATE] * 5 + [GREEN]
    ax.bar(x, vals, width=0.58, color=cols, zorder=3)
    for i, (name, v, size) in enumerate(rounds):
        ax.text(i, v + 4, f"${v}B" + ("+" if v == 100 else ""), ha="center",
                fontsize=8.6, fontweight="bold",
                color=GREEN if i == 5 else INK)
        if v > 40:
            ax.text(i, v / 2, size, ha="center", va="center", fontsize=7.2,
                    color="white")
        else:
            ax.text(i, v + 16, size, ha="center", fontsize=7.0, color=GREY)
    ax.bar([6], [10], bottom=165, width=0.58, color=SLATE, alpha=0.35,
           hatch="///", edgecolor="white", zorder=3)
    ax.text(6, 181, "$165-175B", ha="center", fontsize=8.2, fontweight="bold",
            color=SLATE)
    ax.text(6, 148, "in talks,\nunclosed", ha="center", fontsize=6.8,
            color=GREY)
    ax.set_xticks(list(x) + [6],
                  [r[0] for r in rounds] + ["Reported talks\nJun 2026"],
                  fontsize=7.2)
    ax.set_ylim(0, 205)
    ax.set_ylabel("Post-money valuation ($B)", fontsize=7.8)
    style_ax(ax, "y")
    title_block(fig, "Six marks in five years, each cleared by the fundamentals beneath it",
                "Post-money valuation by round; bar labels show round size (PitchBook deal records; company announcements).\n"
                "Both Series L closes priced at $134B. The reported $165-175B round was unclosed as of Jul 10, 2026 and anchors nothing here.")
    save(fig, "val_ladder.png")

if __name__ == "__main__":
    per_point_ladder()
    acceleration()
    growth_adjusted()
    radar()
    gate_gauge()
    ce_bars()
    football_field()
    sensitivity()
    composition()
    absorption()
    valuation_ladder()
    print("done")
