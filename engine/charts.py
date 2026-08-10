"""House chart factory. Data-driven: a chart spec (JSON) in, a 300-DPI PNG in
the house palette out. Ten chart types cover the report library.

EMBARGO GUARD (hard): no scatter type exists in this factory, and any spec that
pairs AIBQ/quality scores with valuations as x-y coordinates raises
EmbargoError. The dollar-per-point ranked bar is the only cleared expression
of the quality-valuation relationship. Do not add a scatter type.

Spec shape: {"name": "out.png", "type": <type>, "title": ..., "subtitle": ...,
             ...type-specific data...}. See CHART_TYPES at bottom.
"""
from __future__ import annotations
import os, json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

NAVY, SLATE, GREEN = "#1F2A44", "#35506E", "#1C5D46"
GREY, SOFT, WARN, INK = "#6B7280", "#F2F5F9", "#8F3421", "#2B3446"
SERIES = [NAVY, SLATE, GREEN, WARN, GREY, "#5B7B9A"]

plt.rcParams.update({
    "text.parse_math": False, "font.family": "DejaVu Sans", "font.size": 8,
    "text.color": INK, "axes.edgecolor": "#D5DBE4", "axes.labelcolor": GREY,
    "axes.titlesize": 10.5, "axes.linewidth": 0.8, "xtick.color": GREY,
    "ytick.color": GREY, "xtick.labelsize": 7.5, "ytick.labelsize": 7.5,
    "figure.facecolor": "white", "axes.facecolor": "white",
    "savefig.facecolor": "white",
})


class EmbargoError(RuntimeError):
    pass


def _style_ax(ax, grid_axis="x"):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    if grid_axis:
        ax.grid(axis=grid_axis, color=SOFT, linewidth=0.9, zorder=0)
    ax.set_axisbelow(True)


def _title(fig, title, subtitle, x=0.01):
    fig.text(x, 0.985, title, ha="left", va="top", fontsize=10.5,
             fontweight="bold", color=NAVY)
    if subtitle:
        fig.text(x, 0.925, subtitle, ha="left", va="top", fontsize=7.6, color=GREY)


def _save(fig, outdir, name):
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, name)
    fig.savefig(path, dpi=300, bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)
    return path


def _guard(spec):
    t = spec.get("type", "")
    if "scatter" in t:
        raise EmbargoError(
            "scatter is not a house chart type: the quality-valuation "
            "correlation is embargoed; use ranked_bars (per-point ladder).")
    blob = json.dumps(spec).lower()
    if ("aibq" in blob or "quality" in blob) and ("fit" in blob or "trendline" in blob
                                                 or "regression" in blob):
        raise EmbargoError("no fitted lines against quality scores (embargo).")


# ------------------------------------------------------------- chart types
def ranked_bars(spec, outdir):
    """rows: [{label, value, accent?|muted?|est?}], xlabel, annotate?, xlim?"""
    rows = spec["rows"]
    fig, ax = plt.subplots(figsize=(6.5, max(2.2, 0.62 * len(rows) + 1.2)))
    fig.subplots_adjust(top=0.80, left=0.20, right=0.97, bottom=0.13)
    vals = [r["value"] for r in rows]
    for i, r in enumerate(rows):
        col = GREEN if r.get("accent") else GREY if r.get("muted") else \
            SLATE if r.get("alt") else NAVY
        est = bool(r.get("est"))
        ax.barh(i, r["value"], height=0.62, color=col, zorder=3,
                hatch="///" if est else None,
                edgecolor="white" if est else col, linewidth=0.6)
        lbl = r.get("value_label") or f"{r['value']:g}"
        ax.text(r["value"] + max(vals) * 0.015, i, lbl, va="center", ha="left",
                fontsize=8.4, fontweight="bold",
                color=GREEN if r.get("accent") else INK)
    ax.set_yticks(range(len(rows)), [r["label"] for r in rows], fontsize=8.6)
    ax.invert_yaxis() if spec.get("invert") else None
    ax.set_xlim(0, spec.get("xlim") or max(vals) * 1.22)
    ax.set_xlabel(spec.get("xlabel", ""), fontsize=7.8)
    _style_ax(ax, "x")
    if spec.get("annotate"):
        a = spec["annotate"]
        ax.text(a.get("x", max(vals)), a.get("y", len(rows) - 0.4), a["text"],
                fontsize=7.3, color=GREY, ha=a.get("ha", "right"), style="italic")
    _title(fig, spec["title"], spec.get("subtitle"))
    return _save(fig, outdir, spec["name"])


def combo_bars_line(spec, outdir):
    """labels[], bars[], line[]; bar/line ylabels; accent_last?"""
    labels, bars, line = spec["labels"], spec["bars"], spec.get("line")
    fig, ax = plt.subplots(figsize=(6.5, 3.2))
    fig.subplots_adjust(top=0.80, left=0.09, right=0.91, bottom=0.12)
    x = np.arange(len(labels))
    cols = [SLATE] * len(bars)
    if spec.get("accent_last", True):
        cols[-1] = GREEN
    ax.bar(x, bars, width=0.56, color=cols, zorder=3)
    for i, v in enumerate(bars):
        ax.text(i, v / 2, spec.get("bar_fmt", "{:g}").format(v), ha="center",
                va="center", color="white", fontsize=8.4, fontweight="bold")
    ax.set_xticks(x, labels, fontsize=8.2)
    ax.set_ylim(0, max(bars) * 1.25)
    ax.set_ylabel(spec.get("bar_ylabel", ""), fontsize=7.8)
    _style_ax(ax, "y")
    if line:
        ax2 = ax.twinx()
        ax2.plot(x, line, color=WARN, linewidth=2.0, marker="o", markersize=5.5, zorder=5)
        for i, v in enumerate(line):
            ax2.annotate(spec.get("line_fmt", "{:+g}%").format(v), (i, v),
                         textcoords="offset points", xytext=(0, 9), ha="center",
                         fontsize=8.2, fontweight="bold", color=WARN)
        lo, hi = min(line), max(line)
        span = (hi - lo) or 1
        # Deep bottom pad keeps the line clear of the bars beneath it.
        y0, y1 = spec.get("line_ylim", (lo - span * 0.7, hi + span * 0.35))
        ax2.set_ylim(y0, y1)
        ax2.set_ylabel(spec.get("line_ylabel", ""), fontsize=7.8, color=WARN)
        ax2.tick_params(colors=WARN, labelsize=7.5)
        ax2.spines["top"].set_visible(False)
        ax2.spines["right"].set_color("#E3C4B8")
    _title(fig, spec["title"], spec.get("subtitle"))
    return _save(fig, outdir, spec["name"])


def series_bars(spec, outdir):
    """Vertical bars over time: labels[], values[], value_fmt, accents (idx list)."""
    labels, values = spec["labels"], spec["values"]
    fig, ax = plt.subplots(figsize=(6.5, 3.1))
    fig.subplots_adjust(top=0.80, left=0.09, right=0.97, bottom=0.13)
    x = np.arange(len(labels))
    accents = set(spec.get("accents", [len(values) - 1]))
    cols = [GREEN if i in accents else NAVY for i in range(len(values))]
    ax.bar(x, values, width=0.6, color=cols, zorder=3)
    for i, v in enumerate(values):
        ax.text(i, v + max(values) * 0.02, spec.get("value_fmt", "{:g}").format(v),
                ha="center", va="bottom", fontsize=8.2, fontweight="bold", color=INK)
    ax.set_xticks(x, labels, fontsize=8.0)
    ax.set_ylim(0, max(values) * 1.22)
    ax.set_ylabel(spec.get("ylabel", ""), fontsize=7.8)
    _style_ax(ax, "y")
    _title(fig, spec["title"], spec.get("subtitle"))
    return _save(fig, outdir, spec["name"])


def football_field(spec, outdir):
    """rows: [{label, lo, hi, marker?}], vline: {x, label}?, xlabel"""
    rows = spec["rows"]
    fig, ax = plt.subplots(figsize=(6.5, max(2.4, 0.6 * len(rows) + 1.3)))
    fig.subplots_adjust(top=0.82, left=0.28, right=0.97, bottom=0.14)
    for i, r in enumerate(rows):
        ax.barh(i, r["hi"] - r["lo"], left=r["lo"], height=0.5,
                color=SLATE if not r.get("accent") else GREEN, alpha=0.85, zorder=3)
        ax.text(r["hi"] + 2, i, r.get("range_label", f"{r['lo']:g}-{r['hi']:g}"),
                va="center", fontsize=7.8, color=INK)
        if r.get("marker") is not None:
            ax.plot([r["marker"]], [i], marker="D", color=WARN, markersize=6, zorder=5)
    if spec.get("vline"):
        v = spec["vline"]
        ax.axvline(v["x"], color=WARN, linewidth=1.2, linestyle="--", zorder=4)
        ax.text(v["x"], len(rows) - 0.25, " " + v["label"], fontsize=7.2,
                color=WARN, ha="left")
    ax.set_yticks(range(len(rows)), [r["label"] for r in rows], fontsize=8.4)
    ax.set_xlabel(spec.get("xlabel", ""), fontsize=7.8)
    _style_ax(ax, "x")
    _title(fig, spec["title"], spec.get("subtitle"))
    return _save(fig, outdir, spec["name"])


def radar(spec, outdir):
    """dims[], series: [{label, values[], accent?}] on 0-10 scale."""
    dims = spec["dims"]
    N = len(dims)
    ang = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    ang += ang[:1]
    fig, ax = plt.subplots(figsize=(5.6, 4.2), subplot_kw=dict(polar=True))
    fig.subplots_adjust(top=0.78, bottom=0.06)
    for i, s in enumerate(spec["series"]):
        vals = s["values"] + s["values"][:1]
        col = GREEN if s.get("accent") else SERIES[i % len(SERIES)]
        ax.plot(ang, vals, color=col, linewidth=1.8,
                linestyle="-" if s.get("accent") else "--")
        ax.fill(ang, vals, color=col, alpha=0.12 if s.get("accent") else 0.05)
    ax.set_xticks(ang[:-1])
    ax.set_xticklabels(dims, fontsize=7.8)
    ax.set_ylim(0, 10)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels(["2", "4", "6", "8", "10"], fontsize=6.5, color=GREY)
    ax.grid(color="#D5DBE4", linewidth=0.6)
    ax.legend([s["label"] for s in spec["series"]], loc="lower right",
              bbox_to_anchor=(1.18, -0.08), fontsize=7.2, frameon=False)
    _title(fig, spec["title"], spec.get("subtitle"), x=0.02)
    return _save(fig, outdir, spec["name"])


def gauge(spec, outdir):
    """value, floor, lo, hi, label, floor_label: semicircular gate gauge."""
    lo, hi, v, floor = spec["lo"], spec["hi"], spec["value"], spec["floor"]
    fig, ax = plt.subplots(figsize=(5.2, 3.0))
    fig.subplots_adjust(top=0.78, bottom=0.02)
    ax.axis("off")
    th = np.linspace(np.pi, 0, 200)
    ax.plot(np.cos(th), np.sin(th), color="#D5DBE4", linewidth=14, solid_capstyle="butt")
    fr = (floor - lo) / (hi - lo)
    th_bad = np.linspace(np.pi, np.pi * (1 - fr), 80)
    ax.plot(np.cos(th_bad), np.sin(th_bad), color="#E8C9BF", linewidth=14,
            solid_capstyle="butt")
    vr = min(max((v - lo) / (hi - lo), 0), 1)
    ang = np.pi * (1 - vr)
    ax.annotate("", xy=(0.82 * np.cos(ang), 0.82 * np.sin(ang)), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=NAVY, linewidth=2.4))
    fa = np.pi * (1 - fr)
    ax.plot([0.86 * np.cos(fa), 1.10 * np.cos(fa)],
            [0.86 * np.sin(fa), 1.10 * np.sin(fa)], color=WARN, linewidth=1.6)
    ax.text(1.13 * np.cos(fa), 1.13 * np.sin(fa), spec.get("floor_label", f"{floor:g}"),
            fontsize=7.6, color=WARN, ha="left" if fa < np.pi / 2 else "right")
    ax.text(0, -0.14, spec.get("value_label", f"{v:g}"), fontsize=17,
            fontweight="bold", color=NAVY, ha="center")
    ax.text(0, -0.30, spec.get("label", ""), fontsize=7.8, color=GREY, ha="center")
    ax.text(-1.02, -0.06, f"{lo:g}", fontsize=7, color=GREY, ha="center")
    ax.text(1.02, -0.06, f"{hi:g}", fontsize=7, color=GREY, ha="center")
    ax.set_xlim(-1.32, 1.32); ax.set_ylim(-0.36, 1.18)
    ax.set_aspect("equal")
    _title(fig, spec["title"], spec.get("subtitle"), x=0.02)
    return _save(fig, outdir, spec["name"])


def heatmap(spec, outdir):
    """grid: 2D values; row_labels, col_labels, fmt, highlight: [r,c]?"""
    grid = np.array(spec["grid"], dtype=float)
    fig, ax = plt.subplots(figsize=(6.5, 0.5 * grid.shape[0] + 1.7))
    fig.subplots_adjust(top=0.80, left=0.16, right=0.97, bottom=0.16)
    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list("house", ["#FFFFFF", "#DCE7E2", "#1C5D46"])
    ax.imshow(grid, cmap=cmap, aspect="auto")
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            frac = (grid[r, c] - grid.min()) / max(grid.max() - grid.min(), 1e-9)
            hl = spec.get("highlight") == [r, c]
            ax.text(c, r, spec.get("fmt", "{:g}").format(grid[r, c]), ha="center",
                    va="center", fontsize=7.8,
                    fontweight="bold" if hl else "normal",
                    color="white" if frac > 0.62 else INK)
            if hl:
                ax.add_patch(plt.Rectangle((c - .5, r - .5), 1, 1, fill=False,
                                           edgecolor=WARN, linewidth=2))
    ax.set_xticks(range(grid.shape[1]), spec["col_labels"], fontsize=7.6)
    ax.set_yticks(range(grid.shape[0]), spec["row_labels"], fontsize=7.6)
    ax.set_xlabel(spec.get("xlabel", ""), fontsize=7.8)
    ax.set_ylabel(spec.get("ylabel", ""), fontsize=7.8)
    for s in ax.spines.values():
        s.set_visible(False)
    _title(fig, spec["title"], spec.get("subtitle"))
    return _save(fig, outdir, spec["name"])


def composition(spec, outdir):
    """Single stacked horizontal bar: parts: [{label, value}], total_label."""
    parts = spec["parts"]
    fig, ax = plt.subplots(figsize=(6.5, 2.3))
    fig.subplots_adjust(top=0.72, left=0.04, right=0.97, bottom=0.18)
    left = 0.0
    total = sum(p["value"] for p in parts)
    for i, p in enumerate(parts):
        col = SERIES[i % len(SERIES)]
        ax.barh(0, p["value"], left=left, height=0.5, color=col, zorder=3)
        ax.text(left + p["value"] / 2, 0.42, p["label"], ha="center", fontsize=7.4,
                color=INK, rotation=0)
        ax.text(left + p["value"] / 2, 0, spec.get("fmt", "{:g}").format(p["value"]),
                ha="center", va="center", fontsize=8.0, fontweight="bold", color="white")
        left += p["value"]
    ax.text(total * 1.01, 0, spec.get("total_label", f"{total:g}"), va="center",
            fontsize=8.4, fontweight="bold", color=INK)
    ax.set_xlim(0, total * 1.14)
    ax.set_ylim(-0.6, 0.85)
    ax.axis("off")
    _title(fig, spec["title"], spec.get("subtitle"))
    return _save(fig, outdir, spec["name"])


def grouped_bars(spec, outdir):
    """groups[], series: [{label, values[], accent?}], ylabel, fmt."""
    groups = spec["groups"]
    ser = spec["series"]
    n, m = len(groups), len(ser)
    width = 0.8 / m
    fig, ax = plt.subplots(figsize=(6.5, 3.1))
    fig.subplots_adjust(top=0.80, left=0.09, right=0.97, bottom=0.13)
    x = np.arange(n)
    for i, s in enumerate(ser):
        col = GREEN if s.get("accent") else SERIES[i % len(SERIES)]
        pos = x + (i - (m - 1) / 2) * width
        ax.bar(pos, s["values"], width * 0.92, color=col, zorder=3, label=s["label"])
        for xx, v in zip(pos, s["values"]):
            ax.text(xx, v + max(max(t["values"]) for t in ser) * 0.02,
                    spec.get("fmt", "{:g}").format(v), ha="center", va="bottom",
                    fontsize=7.4, fontweight="bold", color=INK)
    ax.set_xticks(x, groups, fontsize=8.2)
    ax.set_ylabel(spec.get("ylabel", ""), fontsize=7.8)
    ax.set_ylim(0, max(max(t["values"]) for t in ser) * 1.25)
    ax.legend(fontsize=7.4, frameon=False, loc="upper right")
    _style_ax(ax, "y")
    _title(fig, spec["title"], spec.get("subtitle"))
    return _save(fig, outdir, spec["name"])


def line_series(spec, outdir):
    """labels[], series: [{label, values[], accent?}], ylabel, fmt?"""
    labels = spec["labels"]
    fig, ax = plt.subplots(figsize=(6.5, 3.1))
    fig.subplots_adjust(top=0.80, left=0.09, right=0.97, bottom=0.13)
    x = np.arange(len(labels))
    for i, s in enumerate(spec["series"]):
        col = GREEN if s.get("accent") else SERIES[i % len(SERIES)]
        ax.plot(x, s["values"], color=col, linewidth=2.0, marker="o",
                markersize=4.5, label=s["label"], zorder=4)
    ax.set_xticks(x, labels, fontsize=8.0)
    ax.set_ylabel(spec.get("ylabel", ""), fontsize=7.8)
    ax.legend(fontsize=7.4, frameon=False)
    _style_ax(ax, "y")
    _title(fig, spec["title"], spec.get("subtitle"))
    return _save(fig, outdir, spec["name"])


CHART_TYPES = {
    "ranked_bars": ranked_bars, "combo_bars_line": combo_bars_line,
    "series_bars": series_bars, "football_field": football_field,
    "radar": radar, "gauge": gauge, "heatmap": heatmap,
    "composition": composition, "grouped_bars": grouped_bars,
    "line_series": line_series,
}


def render_spec(spec, outdir):
    _guard(spec)
    fn = CHART_TYPES.get(spec.get("type"))
    if fn is None:
        raise ValueError(f"unknown chart type {spec.get('type')!r}; "
                         f"house types: {sorted(CHART_TYPES)}")
    return fn(spec, outdir)


def render_file(path, outdir=None):
    """Render every spec in a charts.json file (list of specs)."""
    with open(path, encoding="utf-8") as fh:
        specs = json.load(fh)
    outdir = outdir or os.path.join(os.path.dirname(os.path.abspath(path)), "charts")
    return [render_spec(s, outdir) for s in specs]
