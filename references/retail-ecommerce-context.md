# Retail / e-commerce / omnichannel context

General conventions for large omnichannel retailers (Walmart-style). Use them to suggest metrics, spot missing stakeholders and sanity-check numbers. These are not company-internal facts: any company-specific baseline, system name, policy or figure must come from the PM or their documents. Never state internal Walmart details as if known.

## Business model lenses
- Omnichannel: in-store, online with pickup, delivery (including same-day/express), shipping, marketplace (third-party sellers), membership (subscription), advertising/retail media, financial services, health, and associate-facing tools.
- Everyday-low-price positioning: price-sensitive customers, margin pressure, trust in price accuracy, value perception.
- Scale and seasonality: peak events (holiday, back-to-school, major sales), extreme traffic spikes, store and fulfillment capacity limits.
- Physical-digital seams: inventory accuracy, store picking, substitutions, delivery slots, returns, store associate workload.

## Metric vocabulary (pick, then define precisely)
**Acquisition / engagement**: visits, active customers, app adoption, search usage, session depth, repeat rate, frequency, retention/churn, membership sign-up and renewal.
**Conversion funnel**: search -> PLP -> PDP -> add-to-cart -> checkout -> order. Conversion rate, add-to-cart rate, cart abandonment, checkout completion, search null/zero-result rate, search CTR and refinement rate, search-to-purchase.
**Value**: GMV, net sales, AOV/basket size, units per order, items per basket, attach rate, revenue per visit, incremental margin, contribution margin, ad revenue/ROAS (retail media), take rate (marketplace).
**Fulfillment / operations**: order defect rate, cancellation rate, substitution rate and acceptance, out-of-stock/fill rate, on-time/in-full (OTIF), delivery promise adherence, pickup wait time, pick accuracy, items per hour / picker productivity, cost-to-serve per order, last-mile cost, returns rate, inventory accuracy, shrink.
**Customer experience**: NPS/CSAT, contacts per 100 orders, first-contact resolution, time to resolution, refund/credit cost, reviews and ratings, complaint themes.
**Associate / seller / supplier**: task completion time, training time, adoption, error rate, seller onboarding time, listing quality, item-setup cycle time, content completeness.
**Platform / quality**: page load/latency p95, availability, error rate, API success rate, crash-free sessions, accessibility conformance.

## Typical guardrails by domain
- Growth / conversion changes: margin per order, cancellations, returns, CX contacts, page latency.
- Delivery / fulfillment: on-time rate, cost-to-serve, picker/driver productivity, substitution acceptance, safety.
- Search / discovery / recommendations: relevance, diversity, sponsored-vs-organic balance, null rate, latency, price fairness.
- Pricing / promotions: price accuracy, margin, trust, legal compliance.
- AI assistants / agents: hallucination rate, policy violation rate, escalation rate, cost per resolved task, CSAT.
- Associate tools: task time, error rate, workload, adoption.

## Stakeholder prompts (who else is touched?)
Merchandising/category, pricing, supply chain and fulfillment, store operations and associates, delivery/last-mile partners, marketplace sellers and suppliers, retail media/ads, finance, legal/privacy/compliance, security, customer care, data/analytics/experimentation, brand/marketing, accessibility, international markets.

## Domain risk prompts
Inventory accuracy and out-of-stocks; price or promo mismatch between channels; peak load; store capacity and labor impact; substitution quality; fraud and abuse; alcohol/pharmacy/age-restricted items; regulated categories; privacy of purchase history; seller and supplier trust; accessibility; rollout across stores/regions in phases.

## Sizing pattern
Affected population (customers, orders, stores, sessions) x behavior rate x impact per unit x frequency/year = annualized impact. State each assumption and its source or confidence; give a low/base/high range when the data is thin.
