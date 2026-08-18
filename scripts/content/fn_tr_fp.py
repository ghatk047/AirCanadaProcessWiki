# -*- coding: utf-8 -*-
"""AC-FN-TR — Treasury and Risk (5) and AC-FN-FP — Planning and Analysis (5)."""
from content_lib import P, S

# ── TR: Treasury and Risk ───────────────────────────────────────────────────
P("AC-FN-TR-01",
  desc="Air Canada's daily cash position is monitored and managed across accounts and currencies, ensuring "
       "sufficient liquidity is available for operational needs, including the payment runs covered in "
       "AC-FN-AP-04.",
  trig="The daily cash position monitoring cycle runs.",
  out="A confirmed daily cash position with sufficient liquidity for scheduled obligations, and any "
      "shortfall addressed before it affects payment execution.",
  note="Cash positioning is the treasury discipline that the payment run in AC-FN-AP-04 depends on; a "
      "shortfall not caught here becomes a payment execution problem the following day.",
  phases=["Position compilation", "Liquidity assessment", "Shortfall management"],
  steps=[
    S("1.1","Compile cash position across accounts","Treasury Analyst","SAP S/4HANA",
      "Bank account balances and pending transactions","Compiled consolidated cash position",
      "Compiled daily by the start of business at 100 percent","N","N",
      "Cross-currency accounts require conversion at a consistent rate to produce a genuinely comparable position"),
    S("2.1","Assess liquidity against scheduled obligations","Treasury Analyst","SAP S/4HANA",
      "Compiled position and scheduled payments","Liquidity assessment",
      "Assessed daily for 100 percent of scheduled obligations at 100 percent","N","N",
      "A large scheduled obligation, such as a payment run, can require liquidity planning several days ahead"),
    S("2.2","Identify and address a projected shortfall","Treasury Analyst","SAP S/4HANA",
      "Liquidity assessment showing a gap","Addressed shortfall via facility draw or timing adjustment",
      "Addressed before the shortfall affects a scheduled obligation at 100 percent","Y","N",
      "A shortfall not caught in this process becomes a payment execution problem the following day"),
    S("3.1","Report daily cash position to treasury management","Treasury Analyst","SAP Analytics Cloud",
      "Assessed position","Daily position report",
      "Reported by the close of business at 100 percent","N","N",
      "A position report that arrives too late in the day limits same-day corrective action"),
  ],
  kpis=["Compiled daily by the start of business at 100 percent",
        "Assessed daily for 100 percent of scheduled obligations at 100 percent",
        "Addressed before the shortfall affects a scheduled obligation at 100 percent",
        "Reported by the close of business at 100 percent"],
  risks=["A shortfall not caught in this process becoming a payment execution problem the following day",
         "Cross-currency accounts requiring conversion at a consistent rate for a genuinely comparable position",
         "A large scheduled obligation requiring liquidity planning several days ahead of the actual payment date",
         "A position report arriving too late in the day to allow same-day corrective action"])

P("AC-FN-TR-02",
  desc="Foreign exchange exposure from CAD and USD revenue and cost flows is measured and hedged, "
       "protecting Air Canada's financial results against adverse currency movement.",
  trig="The recurring FX exposure review cycle runs, or a material currency movement requires an "
       "off-cycle assessment.",
  out="Measured FX exposure with an appropriate hedging position established within Air Canada's risk "
      "tolerance.",
  note="Air Canada's revenue and cost bases sit in different currency mixes, CAD primary with material USD "
      "exposure from international operations and aircraft-related costs, which creates a structural "
      "exposure that has to be actively managed rather than something that nets out naturally.",
  phases=["Exposure measurement", "Hedge strategy determination", "Position execution"],
  steps=[
    S("1.1","Measure FX exposure by currency","Treasury Analyst","SAP S/4HANA",
      "Forecast revenue and cost flows by currency","Measured exposure by currency pair",
      "Measured for 100 percent of material currency exposures each cycle","N","N",
      "Exposure forecasting depends on revenue and cost projections that carry their own uncertainty"),
    S("2.1","Determine hedge ratio against risk tolerance","Treasury Analyst","SAP S/4HANA",
      "Measured exposure and risk policy","Determined hedge ratio",
      "Determined within the defined risk tolerance for 100 percent of material exposures","Y","N",
      "Hedging trades away potential upside from favourable currency movement in exchange for protection against adverse movement"),
    S("2.2","Execute hedging instruments","Treasury Analyst","SAP S/4HANA",
      "Determined hedge ratio","Executed hedge position",
      "Executed within the planning cycle at 100 percent","N","N",
      "Hedge execution timing itself carries market risk if delayed relative to the exposure measurement"),
    S("3.1","Monitor hedge effectiveness","Treasury Analyst","SAP Analytics Cloud",
      "Executed position and actual currency movement","Effectiveness assessment",
      "Assessed each reporting cycle for 100 percent of active hedges","N","N",
      "A hedge that no longer matches the underlying exposure, because the forecast changed, needs active rebalancing"),
  ],
  kpis=["Measured for 100 percent of material currency exposures each cycle",
        "Determined within the defined risk tolerance for 100 percent of material exposures",
        "Executed within the planning cycle at 100 percent",
        "Hedge effectiveness meeting target each reporting cycle"],
  risks=["Hedging trading away potential upside from favourable currency movement in exchange for downside protection",
         "A hedge no longer matching the underlying exposure once the original forecast changes",
         "Exposure forecasting depending on revenue and cost projections that carry their own uncertainty",
         "Hedge execution timing itself carrying market risk if delayed relative to the exposure measurement"])

P("AC-FN-TR-03",
  desc="The fuel hedging programme is administered, protecting Air Canada's operating cost base against jet "
       "fuel price volatility within a defined risk management framework.",
  trig="The recurring fuel hedging programme review cycle runs, or a material fuel price movement requires "
       "an off-cycle assessment.",
  out="A fuel hedging position maintained within the programme's defined risk parameters, protecting a "
      "portion of forecast fuel consumption cost.",
  note="Fuel is one of the largest and most volatile cost lines in the airline's operating budget, which "
      "makes the hedging programme a direct input to the financial planning and forecasting process covered "
      "in AC-FN-FP-02.",
  phases=["Consumption forecast", "Hedge position determination", "Programme monitoring"],
  steps=[
    S("1.1","Forecast fuel consumption","Treasury Analyst","SAP S/4HANA",
      "Network schedule and fleet fuel burn data","Forecast consumption by period",
      "Forecast for 100 percent of the hedging horizon each cycle","N","N",
      "Consumption forecast depends on the network schedule, which itself changes between hedge planning and actual flying"),
    S("2.1","Determine hedge coverage against the programme framework","Treasury Analyst","SAP S/4HANA",
      "Forecast consumption and risk framework","Determined hedge coverage percentage",
      "Determined within the programme's defined risk parameters at 100 percent","Y","N",
      "A hedge coverage decision trades cost certainty against the possibility of paying above the eventual market price"),
    S("2.2","Execute fuel hedge instruments","Treasury Analyst","SAP S/4HANA",
      "Determined coverage","Executed hedge position",
      "Executed within the planning cycle at 100 percent","N","N",
      "Fuel hedge instruments carry counterparty and market timing risk in their own right"),
    S("3.1","Monitor programme performance against market price","Treasury Analyst","SAP Analytics Cloud",
      "Executed position and market fuel price","Performance assessment",
      "Assessed each reporting cycle for 100 percent of the active programme","N","N",
      "Programme performance judged only against realised market price ignores the risk reduction value the hedge actually provided"),
  ],
  kpis=["Forecast for 100 percent of the hedging horizon each cycle",
        "Determined within the programme's defined risk parameters at 100 percent",
        "Executed within the planning cycle at 100 percent",
        "Programme performance assessed each reporting cycle for 100 percent of the active programme"],
  risks=["A hedge coverage decision trading cost certainty against paying above the eventual market price",
         "Consumption forecast depending on a network schedule that itself changes between planning and actual flying",
         "Fuel hedge instruments carrying counterparty and market timing risk in their own right",
         "Programme performance judged only against realised price ignoring the risk reduction value actually provided"])

P("AC-FN-TR-04",
  desc="Aircraft financing arrangements, including lease and debt structures, are administered and their "
       "accounting treatment maintained, covering a fleet financed through a mix of ownership and lease "
       "structures.",
  trig="A new aircraft financing arrangement is executed, or the recurring lease accounting cycle runs.",
  out="Correctly administered financing arrangements with accurate lease and debt accounting treatment "
      "maintained across the fleet.",
  note="Fleet financing structure directly affects the balance sheet presentation of aircraft assets and "
      "obligations, which makes correct lease classification and accounting treatment a material input to "
      "the financial statements, not a back-office administrative detail.",
  phases=["Financing arrangement administration", "Lease accounting treatment", "Reporting"],
  steps=[
    S("1.1","Administer financing arrangement terms","Treasury Analyst","SAP S/4HANA",
      "Executed lease or debt agreement","Administered arrangement in the system",
      "Administered within 10 business days of execution at 100 percent","N","N",
      "Financing terms for a large aircraft transaction are genuinely complex and easy to mis-capture"),
    S("2.1","Determine lease accounting classification","Treasury Analyst","SAP S/4HANA",
      "Arrangement terms","Determined accounting classification",
      "Determined correctly against accounting standards for 100 percent of arrangements at 100 percent","Y","N",
      "Lease classification judgement calls have material balance sheet presentation consequences"),
    S("2.2","Maintain ongoing accounting treatment","Treasury Analyst","SAP S/4HANA",
      "Classified arrangement","Maintained treatment through the arrangement's life",
      "Maintained accurately each reporting period for 100 percent of active arrangements at 100 percent","N","N",
      "A modification to an existing arrangement can require reassessing the original classification"),
    S("3.1","Report financing position for financial statements","Treasury Analyst","SAP Analytics Cloud",
      "Maintained treatment","Reported financing position",
      "Reported within the financial close timetable at 100 percent","N","N",
      "An incorrect classification carried forward compounds across every subsequent reporting period"),
  ],
  kpis=["Administered within 10 business days of execution at 100 percent",
        "Determined correctly against accounting standards for 100 percent of arrangements at 100 percent",
        "Maintained accurately each reporting period for 100 percent of active arrangements at 100 percent",
        "Reported within the financial close timetable at 100 percent"],
  risks=["Lease classification judgement calls having material balance sheet presentation consequences",
         "An incorrect classification carried forward compounding across every subsequent reporting period",
         "A modification to an existing arrangement requiring reassessment of the original classification",
         "Financing terms for a large aircraft transaction being genuinely complex and easy to mis-capture"])

P("AC-FN-TR-05",
  desc="Card payment acceptance and settlement are managed across customer channels, coordinating with "
       "acquiring banks and card schemes for the full range of ticket and ancillary purchase transactions.",
  trig="A card payment transaction is processed through any Air Canada customer channel.",
  out="Card payments correctly authorised, settled and reconciled against the acquiring bank's settlement "
      "position.",
  note="Card acceptance sits underneath every digital, contact centre and airport channel that takes "
      "payment, including the PCI-DSS-compliant secure capture flow in AC-CX-CC-06, which makes this a "
      "foundational payment infrastructure process rather than a single-channel concern.",
  phases=["Transaction authorisation", "Acquirer settlement", "Reconciliation"],
  steps=[
    S("1.1","Process card authorisation across channels","Treasury Analyst","SAP S/4HANA",
      "Customer card transaction","Authorised transaction",
      "Authorised within the standard processing time at 98 percent","N","N",
      "Authorisation decline rates and reasons differ by channel and acquiring relationship"),
    S("2.1","Settle with acquiring bank","Treasury Analyst","SAP S/4HANA",
      "Authorised transactions","Settled batch",
      "Settled within the acquirer's settlement cycle at 100 percent","N","N",
      "Multiple acquiring relationships across different card schemes and markets each carry their own settlement timing"),
    S("2.2","Reconcile settlement against transaction records","Treasury Analyst","SAP S/4HANA",
      "Settled batch and transaction records","Reconciled position with variance report",
      "Reconciled within 5 business days of settlement at 100 percent","Y","N",
      "A reconciliation variance can indicate a fee miscalculation or a genuine settlement discrepancy requiring investigation"),
    S("3.1","Resolve variances and post to the ledger","Treasury Analyst","SAP S/4HANA",
      "Reconciliation variance","Resolved and posted settlement",
      "Posted within the financial close timetable at 100 percent","N","N",
      "An unresolved variance affects the accuracy of both cash positioning and revenue accounting"),
  ],
  kpis=["Authorised within the standard processing time at 98 percent",
        "Settled within the acquirer's settlement cycle at 100 percent",
        "Reconciled within 5 business days of settlement at 100 percent",
        "Posted within the financial close timetable at 100 percent"],
  risks=["Multiple acquiring relationships across card schemes and markets carrying their own settlement timing",
         "A reconciliation variance indicating either a fee miscalculation or a genuine settlement discrepancy",
         "An unresolved variance affecting the accuracy of both cash positioning and revenue accounting",
         "Authorisation decline rates and reasons differing by channel and acquiring relationship"])

# ── FP: Planning and Analysis ───────────────────────────────────────────────
P("AC-FN-FP-01",
  desc="The annual budget and operating plan are built, consolidating input from every business function "
       "into a single approved financial plan for the coming year.",
  trig="The annual budget cycle opens.",
  out="An approved annual budget and operating plan, consolidated across all business functions and ready "
      "to serve as the year's financial baseline.",
  note="Budget consolidation is where every function's individual assumptions, from network capacity in "
      "AC-NP-SP-02 to crew establishment in AC-CM-CP-01, have to reconcile into one internally consistent "
      "financial plan.",
  phases=["Functional input collection", "Consolidation and review", "Approval"],
  steps=[
    S("1.1","Issue budget guidance to functions","Financial Planning Analyst","SAP Analytics Cloud",
      "Corporate financial targets and assumptions","Issued budget guidance",
      "Issued before the functional input window opens at 100 percent","N","N",
      "Guidance that arrives late compresses the time functions have to build a considered budget submission"),
    S("2.1","Collect budget input from each function","Financial Planning Analyst","SAP Analytics Cloud",
      "Function-level operating plans","Collected budget input",
      "Collected within the defined submission window at 90 percent","N","N",
      "Functional budget assumptions are not always internally consistent with each other before consolidation"),
    S("2.2","Consolidate and reconcile across functions","Financial Planning Analyst","SAP Analytics Cloud",
      "Collected input","Consolidated budget with reconciled assumptions",
      "Consolidated within the planning timeline at 100 percent","Y","N",
      "Reconciling inconsistent functional assumptions is the genuinely difficult part of consolidation"),
    S("3.1","Obtain executive and board approval","Financial Planning Analyst","SAP Analytics Cloud",
      "Consolidated budget","Approved annual budget",
      "Approved before the fiscal year begins at 100 percent","N","N",
      "A budget not approved before the fiscal year begins leaves functions operating without an approved baseline"),
  ],
  kpis=["Issued before the functional input window opens at 100 percent",
        "Collected within the defined submission window at 90 percent",
        "Consolidated within the planning timeline at 100 percent",
        "Approved before the fiscal year begins at 100 percent"],
  risks=["Functional budget assumptions not being internally consistent with each other before consolidation",
         "A budget not approved before the fiscal year begins leaving functions without an approved baseline",
         "Guidance arriving late compressing the time available to build a considered budget submission",
         "Reconciling inconsistent functional assumptions being the genuinely difficult part of consolidation"])

P("AC-FN-FP-02",
  desc="A monthly forecast and reforecast is produced against the annual budget, incorporating actual "
       "performance and updated assumptions as the year progresses.",
  trig="The monthly forecast cycle runs following period close.",
  out="An updated forecast reflecting actual performance and current assumptions, distinct from the fixed "
      "annual budget baseline.",
  note="The monthly forecast is what keeps the annual budget from becoming stale within weeks of being set, "
      "since actual network, fuel and revenue performance diverge from the original plan continuously "
      "throughout the year.",
  phases=["Actual performance compilation", "Forecast update", "Variance reporting"],
  steps=[
    S("1.1","Compile actual performance against budget","Financial Planning Analyst","SAP Analytics Cloud",
      "Actual period results","Compiled actual performance",
      "Compiled within 5 business days of period close at 100 percent","N","N",
      "Actual performance data draws on results from every function that need to close on a consistent timetable"),
    S("2.1","Update forecast assumptions","Financial Planning Analyst","SAP Analytics Cloud",
      "Actual performance and updated business assumptions","Updated forecast assumptions",
      "Updated for 100 percent of material forecast lines each cycle at 100 percent","N","N",
      "Updating every assumption every month is not proportionate, so materiality judgement determines what actually gets revised"),
    S("2.2","Produce updated forecast","Financial Planning Analyst","SAP Analytics Cloud",
      "Updated assumptions","Produced forecast for remainder of year",
      "Produced within the monthly forecast timeline at 100 percent","N","N",
      "A forecast that simply extrapolates the budget rather than incorporating genuine new information adds little value"),
    S("3.1","Report variance against budget and prior forecast","Financial Planning Analyst","SAP Analytics Cloud",
      "Produced forecast","Distributed variance report",
      "Distributed within 10 business days of period close at 100 percent","N","N",
      "Variance attribution has to distinguish a timing difference from a genuine change in the year's expected outcome"),
  ],
  kpis=["Compiled within 5 business days of period close at 100 percent",
        "Updated for 100 percent of material forecast lines each cycle at 100 percent",
        "Produced within the monthly forecast timeline at 100 percent",
        "Distributed within 10 business days of period close at 100 percent"],
  risks=["A forecast that simply extrapolates the budget without incorporating genuine new information",
         "Variance attribution failing to distinguish a timing difference from a genuine change in expected outcome",
         "Actual performance data drawing on results from every function needing to close on a consistent timetable",
         "Materiality judgement about what actually gets revised each month being applied inconsistently"])

P("AC-FN-FP-03",
  desc="Management reporting and the board financial pack are prepared, synthesising financial and "
       "operational performance into the reporting package leadership and the board rely on for decisions.",
  trig="The recurring management and board reporting cycle runs.",
  out="An accurate, timely management report and board pack, correctly synthesising financial and "
      "operational performance for decision-making.",
  note="This reporting package is where the entire finance function's work becomes visible to leadership "
      "and the board, which means any upstream error in revenue accounting, forecasting or treasury "
      "reporting ultimately surfaces here in front of the widest and most consequential audience.",
  phases=["Data synthesis", "Report preparation", "Distribution"],
  steps=[
    S("1.1","Synthesise financial and operational data","Financial Planning Analyst","SAP Analytics Cloud",
      "Financial results and operational KPIs across functions","Synthesised data set",
      "Synthesised within the reporting timeline at 100 percent","N","N",
      "Operational KPIs drawn from several domains need to reconcile with the financial results they should support"),
    S("2.1","Prepare management report content","Financial Planning Analyst","SAP Analytics Cloud",
      "Synthesised data","Prepared report content",
      "Prepared within the reporting timeline at 100 percent","N","N",
      "Any upstream error in revenue accounting or forecasting ultimately surfaces in front of the widest audience here"),
    S("2.2","Prepare board financial pack","Financial Planning Analyst","SAP Analytics Cloud",
      "Prepared management report","Prepared board pack",
      "Prepared before the board meeting deadline at 100 percent","Y","N",
      "The board pack has a hard deadline tied to governance requirements that does not flex for a late close"),
    S("3.1","Distribute reports to stakeholders","Financial Planning Analyst","SAP Analytics Cloud",
      "Prepared reports","Distributed reports",
      "Distributed within the required lead time before the relevant meeting at 100 percent","N","N",
      "A report distributed too close to the meeting gives recipients no genuine time to review before discussion"),
  ],
  kpis=["Synthesised within the reporting timeline at 100 percent",
        "Prepared within the reporting timeline at 100 percent",
        "Prepared before the board meeting deadline at 100 percent",
        "Distributed within the required lead time before the relevant meeting at 100 percent"],
  risks=["Any upstream error in revenue accounting or forecasting ultimately surfacing in front of the widest audience",
         "The board pack deadline being tied to governance requirements that do not flex for a late close",
         "A report distributed too close to the meeting giving recipients no genuine time to review",
         "Operational KPIs from several domains needing to reconcile with the financial results they should support"])

P("AC-FN-FP-04",
  desc="A capital investment proposal, such as a fleet order or a major technology programme, is appraised "
       "and taken through the approval process before capital is committed.",
  trig="A business function proposes a capital investment.",
  out="A capital investment either approved with committed funding, or declined with documented reasoning, "
      "following rigorous financial appraisal.",
  note="Capital appraisal discipline matters most on exactly the kind of large, multi-year commitment this "
      "wiki's own subject matter touches, a fleet order like the ones referenced throughout AC-NP-FA, so "
      "getting the appraisal right protects decisions with consequences spanning a decade or more.",
  phases=["Proposal intake", "Financial appraisal", "Approval decision"],
  steps=[
    S("1.1","Receive capital investment proposal","Financial Planning Analyst","SAP Analytics Cloud",
      "Business function proposal","Registered proposal",
      "Registered within 5 business days of submission at 100 percent","N","N",
      "Proposals arrive with varying quality of supporting financial and operational justification"),
    S("2.1","Appraise financial return and risk","Financial Planning Analyst","SAP Analytics Cloud",
      "Registered proposal","Financial appraisal with return and risk assessment",
      "Appraised using a consistent methodology for 100 percent of proposals at 100 percent","N","N",
      "A large, multi-year commitment such as a fleet order carries consequences spanning a decade or more"),
    S("2.2","Assess against capital allocation priorities","Financial Planning Analyst","SAP Analytics Cloud",
      "Appraisal","Prioritised position against competing proposals",
      "Assessed within the capital planning cycle at 100 percent","Y","N",
      "Capital is finite, so approving one proposal has an opportunity cost against every other competing proposal"),
    S("3.1","Obtain approval and commit funding","Financial Planning Analyst","SAP Analytics Cloud",
      "Prioritised proposal","Approved and funded investment",
      "Approved within the governance-defined authority level at 100 percent","N","N",
      "An investment committed without appropriate governance-level approval is a control failure regardless of the investment's merit"),
  ],
  kpis=["Registered within 5 business days of submission at 100 percent",
        "Appraised using a consistent methodology for 100 percent of proposals at 100 percent",
        "Assessed within the capital planning cycle at 100 percent",
        "Approved within the governance-defined authority level at 100 percent"],
  risks=["A large, multi-year commitment such as a fleet order carrying consequences spanning a decade or more",
         "Capital being finite, so approving one proposal has a genuine opportunity cost against competing proposals",
         "An investment committed without appropriate governance-level approval being a control failure",
         "Proposals arriving with varying quality of supporting financial and operational justification"])

P("AC-FN-FP-05",
  desc="Benefit realisation from cost transformation initiatives is tracked against the original business "
       "case, confirming a programme actually delivered the savings it was approved on the basis of.",
  trig="A cost transformation initiative reaches its defined benefit realisation checkpoint.",
  out="Tracked benefit realisation against the original business case, with a variance investigated and "
      "reported honestly rather than assumed away.",
  note="A savings initiative approved on a projected business case has genuine value only if the projected "
      "savings are later confirmed to have actually materialised; without this tracking, cost transformation "
      "claims accumulate without any check on whether they were real.",
  phases=["Benefit baseline confirmation", "Realisation measurement", "Variance reporting"],
  steps=[
    S("1.1","Confirm the original business case baseline","Financial Planning Analyst","SAP Analytics Cloud",
      "Approved initiative business case","Confirmed baseline for tracking",
      "Confirmed at initiative approval for 100 percent of tracked initiatives at 100 percent","N","N",
      "A baseline not clearly fixed at approval makes later realisation comparison ambiguous"),
    S("2.1","Measure actual realised benefit","Financial Planning Analyst","SAP Analytics Cloud",
      "Actual cost or revenue performance post-implementation","Measured realised benefit",
      "Measured at each defined checkpoint for 100 percent of tracked initiatives at 100 percent","N","N",
      "Isolating the initiative's specific effect from other concurrent changes to the same cost line is genuinely difficult"),
    S("2.2","Compare realised benefit to the business case","Financial Planning Analyst","SAP Analytics Cloud",
      "Measured benefit and baseline","Variance against business case",
      "Compared for 100 percent of tracked initiatives at each checkpoint at 100 percent","Y","N",
      "A shortfall against the business case is a harder message to report honestly than a success"),
    S("3.1","Report realisation and close or extend tracking","Financial Planning Analyst","SAP Analytics Cloud",
      "Variance comparison","Reported realisation status",
      "Reported at each checkpoint for 100 percent of tracked initiatives at 100 percent","N","N",
      "Without this tracking, cost transformation claims accumulate without any check on whether they were real"),
  ],
  kpis=["Confirmed at initiative approval for 100 percent of tracked initiatives at 100 percent",
        "Measured at each defined checkpoint for 100 percent of tracked initiatives at 100 percent",
        "Compared for 100 percent of tracked initiatives at each checkpoint at 100 percent",
        "Aggregate benefit realisation rate against approved business cases tracked and reported"],
  risks=["Cost transformation claims accumulating without any check on whether the projected savings were real",
         "A shortfall against the business case being a harder message to report honestly than a success",
         "Isolating the initiative's specific effect from other concurrent changes to the same cost line",
         "A baseline not clearly fixed at approval making later realisation comparison ambiguous"])
