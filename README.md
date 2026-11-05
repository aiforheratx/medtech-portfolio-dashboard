# Portfolio Intelligence — Medical Devices Dashboard (Prototype)

Interactive, presentation-ready portfolio dashboard for a medical-device business: all portfolios and therapies, geography, markets, focus recommendations and project intake.

**Live:** https://aiforheratx.github.io/medtech-portfolio-dashboard/

> All figures are illustrative dummy data.

## Views
1. **Executive Overview** – revenue, vs. plan, market size, share, penetration, white space, pipeline NPV; portfolio cards; trend + forecast; regions
2. **Portfolio & Therapies** – zoomable portfolio map (portfolio → operating unit → product) and sortable product scorecard
3. **Geography** – world revenue map, regional mix, regional performance
4. **Markets & Focus** – where-to-play matrix (market growth vs. share), FY28 growth opportunity, focus score & recommendations
5. **Project Intake** – stage-gate funnel, gate cycle time vs. target, monthly intake, project pipeline

## How to use
- Click any card, bar, block or bubble to drill in; breadcrumbs or `Backspace` to zoom out
- Year and region filters apply everywhere
- **Present** (or `P`) for full-screen; `←` / `→` to move between views, `1`–`5` to jump, `Esc` to exit
- Light/dark toggle; fits any window size

Single static `index.html` (ECharts from CDN) — no build step.
