# -*- coding: utf-8 -*-
"""AC-FN-RA — Revenue Accounting (5) and AC-FN-AP — Procure-to-Pay (5)."""
from content_lib import P, S

# ── RA: Revenue Accounting ──────────────────────────────────────────────────
P("AC-FN-RA-01",
  desc="Passenger revenue is recognised on actual flown carriage rather than at the point of sale, "
       "reconciling the coupon lift record against the original fare and building the air traffic "
       "liability position for tickets sold but not yet flown.",
  trig="A flight is completed and coupons are lifted, or the recurring period-close revenue recognition "
       "cycle runs.",
  out="Recognised passenger revenue on flown carriage, with the air traffic liability correctly updated for "
      "unflown tickets.",
  note="Revenue recognition on lift rather than sale is the single largest judgement in the entire finance "
      "close, since it determines the air traffic liability, the value of tickets sold but not yet flown, "
      "which is one of the largest balance sheet items an airline carries.",
  phases=["Coupon lift compilation", "Revenue recognition", "Air traffic liability update"],
  steps=[
    S("1.1","Compile lifted coupon data","Revenue Accounting Analyst","Amadeus Altea Reservations",
      "Flown flight coupon data","Compiled lifted coupons",
      "Compiled within 2 business days of flight completion at 100 percent","N","N",
      "A coupon lifted on a codeshare or interline segment requires matching against a partner's own record"),
    S("2.1","Recognise revenue on flown segments","Revenue Accounting Analyst","Revenue Accounting System",
      "Compiled coupons and original fare value","Recognised revenue",
      "Recognised within the period close timetable at 100 percent","N","N",
      "Fare value allocation across a multi-segment itinerary requires a proration methodology, not a simple split"),
    S("2.2","Update air traffic liability for unflown segments","Revenue Accounting Analyst","Revenue Accounting System",
      "Sold but unflown ticket inventory","Updated liability position",
      "Updated within the period close timetable at 100 percent","Y","N",
      "The liability represents one of the largest balance sheet items an airline carries and demands accuracy"),
    S("3.1","Reconcile recognised revenue to sales","Revenue Accounting Analyst","IATA BSP",
      "Recognised revenue and original sales data","Reconciled position with variance report",
      "Reconciled within the period close timetable at 100 percent","N","N",
      "A reconciliation variance has to be investigated before period close, not carried forward unresolved"),
  ],
  kpis=["Compiled within 2 business days of flight completion at 100 percent",
        "Recognised within the period close timetable at 100 percent",
        "Updated within the period close timetable at 100 percent",
        "Reconciliation variance closed before period close at 100 percent"],
  risks=["The air traffic liability being one of the largest balance sheet items an airline carries",
         "Fare value allocation across a multi-segment itinerary requiring a proration methodology, not a simple split",
         "A coupon lifted on a codeshare or interline segment requiring matching against a partner's own record",
         "A reconciliation variance carried forward unresolved rather than investigated before period close"])

P("AC-FN-RA-02",
  desc="Interline billing is calculated and settled between Air Canada and its Star Alliance and A++ "
       "partners, reconciling carriage performed on behalf of one carrier and sold by another.",
  trig="The recurring interline settlement cycle runs, following completed carriage across partner "
      "airlines.",
  out="Correctly calculated and settled interline balances, reconciling revenue and cost across partner "
      "carriers.",
  note="Interline settlement operates on industry clearing timetables that Air Canada does not control, "
      "which means the settlement discipline here has to accommodate a cycle set externally rather than "
      "one the finance function can adjust to fit its own close calendar.",
  phases=["Interline data compilation", "Billing calculation", "Settlement"],
  steps=[
    S("1.1","Compile interline carriage data","Revenue Accounting Analyst","Star Alliance Interline",
      "Carriage performed for or by partner carriers","Compiled interline carriage data",
      "Compiled within the industry clearing timetable at 100 percent","N","N",
      "Interline data spans several partner carriers each with their own reporting timeline"),
    S("2.1","Calculate interline billing amounts","Revenue Accounting Analyst","Revenue Accounting System",
      "Compiled data and prorate agreements","Calculated billing by partner",
      "Calculated within the industry clearing timetable at 100 percent","N","N",
      "Prorate agreements differ by partner and require correct application to each partner's specific terms"),
    S("2.2","Reconcile calculated amounts against partner statements","Revenue Accounting Analyst","IATA BSP",
      "Calculated billing and partner statements","Reconciled position with variance report",
      "Reconciled within the industry clearing timetable at 100 percent","Y","N",
      "A variance against a partner's own statement requires bilateral investigation, not unilateral correction"),
    S("3.1","Settle interline balances","Revenue Accounting Analyst","SAP S/4HANA",
      "Reconciled position","Settled balances",
      "Settled within the industry clearing timetable at 100 percent","N","N",
      "Settlement operates on a timetable Air Canada does not control, set by the industry clearing house"),
  ],
  kpis=["Compiled within the industry clearing timetable at 100 percent",
        "Calculated within the industry clearing timetable at 100 percent",
        "Reconciled within the industry clearing timetable at 100 percent",
        "Settled within the industry clearing timetable at 100 percent"],
  risks=["Settlement operating on an industry clearing timetable Air Canada does not itself control",
         "A variance against a partner's own statement requiring bilateral investigation, not unilateral correction",
         "Prorate agreements differing by partner and requiring correct application to each partner's specific terms",
         "Interline data spanning several partner carriers each with their own reporting timeline"])

P("AC-FN-RA-03",
  desc="Sales reported through the IATA Billing and Settlement Plan and the US Airlines Reporting "
       "Corporation are reconciled against Air Canada's own booking and ticketing records.",
  trig="The recurring BSP and ARC settlement cycle runs, following agency ticket sales.",
  out="Reconciled agency sales settlement, with any variance between reported sales and Air Canada's own "
      "records investigated and resolved.",
  note="BSP and ARC are the settlement mechanisms for agency-sold tickets, distinct from direct sales, and "
      "a reconciliation gap here can mean Air Canada is owed money by an agency channel that has already "
      "reported the sale as settled.",
  phases=["Settlement data receipt", "Reconciliation", "Variance resolution"],
  steps=[
    S("1.1","Receive BSP and ARC settlement data","Revenue Accounting Analyst","IATA BSP",
      "Agency-reported ticket sales","Received settlement data",
      "Received on the industry settlement schedule at 100 percent","N","N",
      "BSP and ARC operate on separate schedules and data formats despite serving a similar function"),
    S("2.1","Reconcile against Air Canada's own sales records","Revenue Accounting Analyst","Amadeus Altea Reservations",
      "Settlement data and internal ticketing records","Reconciled position with variance list",
      "Reconciled within the settlement cycle at 100 percent","N","N",
      "A ticket voided or exchanged after issuance can create a timing mismatch between the two records"),
    S("2.2","Investigate and resolve variances","Revenue Accounting Analyst","Revenue Accounting System",
      "Variance list","Resolved variance",
      "Resolved within the settlement cycle for 95 percent of variances","N","Y",
      "An unresolved variance can mean Air Canada is owed money by an agency channel that has already reported settlement"),
    S("3.1","Post reconciled settlement to the ledger","Revenue Accounting Analyst","SAP S/4HANA",
      "Resolved reconciliation","Posted settlement",
      "Posted within the financial close timetable at 100 percent","N","N",
      "A posting delay compounds into the broader finance close this settlement feeds"),
  ],
  kpis=["Received on the industry settlement schedule at 100 percent",
        "Reconciled within the settlement cycle at 100 percent",
        "Resolved within the settlement cycle for 95 percent of variances",
        "Posted within the financial close timetable at 100 percent"],
  risks=["An unresolved variance meaning Air Canada is owed money by an agency channel already reporting settlement",
         "A ticket voided or exchanged after issuance creating a timing mismatch between the two settlement records",
         "BSP and ARC operating on separate schedules and formats despite serving a similar settlement function",
         "A posting delay compounding into the broader finance close this settlement feeds"])

P("AC-FN-RA-04",
  desc="The air traffic liability, the value of tickets sold but not yet flown, is periodically valued and "
       "reported, incorporating expiry and no-show assumptions distinct from the loyalty points liability "
       "covered in AC-AP-TM-06.",
  trig="The recurring financial reporting cycle requires an updated air traffic liability valuation.",
  out="A current air traffic liability valuation reflecting outstanding ticket inventory and expiry "
      "assumptions, reported for the financial statements.",
  note="This liability requires assumptions about tickets that will never be flown, whether through expiry, "
      "no-show or unused credit, that are conceptually similar to the breakage assumption in loyalty "
      "accounting but calculated against a materially different underlying asset.",
  phases=["Outstanding ticket compilation", "Expiry assumption application", "Liability reporting"],
  steps=[
    S("1.1","Compile outstanding unflown ticket inventory","Revenue Accounting Analyst","Amadeus Altea Reservations",
      "Sold but unflown tickets","Compiled outstanding inventory",
      "Compiled at each period close at 100 percent","N","N",
      "Outstanding inventory spans tickets at every stage from recently sold to approaching expiry"),
    S("2.1","Apply expiry and no-show assumptions","Revenue Accounting Analyst","Revenue Accounting System",
      "Compiled inventory and historical expiry pattern","Expiry-adjusted liability base",
      "Applied using a documented statistical method at 100 percent","N","N",
      "Expiry assumptions are forward-looking estimates about ticket usage behaviour that has not yet occurred"),
    S("2.2","Calculate final liability valuation","Revenue Accounting Analyst","SAP S/4HANA",
      "Expiry-adjusted base","Final valuation",
      "Calculated within the period close timetable at 100 percent","N","N",
      "The valuation is sensitive to any shift in booking-to-travel lead time patterns across the network"),
    S("3.1","Report the valuation for financial statements","Revenue Accounting Analyst","SAP Analytics Cloud",
      "Final valuation","Reported liability",
      "Reported within the financial close timetable at 100 percent","N","N",
      "A material valuation error requires prompt correction given the size of this balance sheet item"),
  ],
  kpis=["Compiled at each period close at 100 percent",
        "Applied using a documented statistical method at 100 percent",
        "Calculated within the period close timetable at 100 percent",
        "Reported within the financial close timetable at 100 percent"],
  risks=["Expiry assumptions being forward-looking estimates about ticket usage behaviour not yet observed",
         "The valuation being sensitive to any shift in booking-to-travel lead time patterns across the network",
         "A material valuation error requiring prompt correction given the size of this balance sheet item",
         "Outstanding inventory spanning tickets at every stage from recently sold to approaching expiry"])

P("AC-FN-RA-05",
  desc="Revenue leakage is audited and recovered, identifying underbilled fares, missed ancillary charges "
       "and other systematic revenue collection gaps across the booking and ticketing chain.",
  trig="The recurring revenue audit cycle runs, or a specific leakage pattern is flagged for "
       "investigation.",
  out="Identified revenue leakage patterns with recovery action taken where possible, and a systemic fix "
      "recommended to prevent recurrence.",
  note="Revenue audit differs from the revenue integrity function in AC-RM-YM-04 in its direction: revenue "
      "integrity looks for customer-side fare abuse, while this process looks for internal collection gaps, "
      "money Air Canada was owed but did not actually collect.",
  phases=["Leakage pattern screening", "Recovery investigation", "Systemic remediation"],
  steps=[
    S("1.1","Screen for revenue leakage patterns","Revenue Accounting Analyst","Revenue Accounting System",
      "Booking, ticketing and ancillary transaction data","Flagged leakage pattern candidates",
      "Screened for 100 percent of defined leakage categories each cycle","N","N",
      "Leakage patterns are often small individually and only become visible in aggregate"),
    S("2.1","Investigate flagged leakage instances","Revenue Accounting Analyst","Amadeus Altea Reservations",
      "Flagged candidates","Confirmed or dismissed leakage instance",
      "Investigated within 10 business days of flagging at 90 percent","N","Y",
      "Confirming genuine leakage versus a legitimate fare exception requires case-by-case judgement"),
    S("2.2","Recover collectable amounts where possible","Revenue Accounting Analyst","SAP S/4HANA",
      "Confirmed leakage","Recovered amount or documented uncollectable finding",
      "Recovery pursued for 100 percent of confirmed material leakage at 100 percent","N","N",
      "Recovery from a customer or agency long after the original transaction is often commercially impractical"),
    S("3.1","Recommend systemic fix to prevent recurrence","Revenue Accounting Analyst","ITSM Platform",
      "Confirmed leakage pattern","Systemic fix recommendation",
      "Recommended within 10 business days of confirmation for 100 percent of systemic patterns","N","N",
      "A recovery without a systemic fix means the same leakage pattern continues generating new instances"),
  ],
  kpis=["Screened for 100 percent of defined leakage categories each cycle",
        "Investigated within 10 business days of flagging at 90 percent",
        "Recovery pursued for 100 percent of confirmed material leakage at 100 percent",
        "Revenue leakage recovered or prevented tracked as a value metric each cycle"],
  risks=["Leakage patterns being small individually and only becoming visible in aggregate",
         "Recovery from a customer or agency long after the transaction being often commercially impractical",
         "A recovery without a systemic fix meaning the same leakage pattern continues generating new instances",
         "Confirming genuine leakage versus a legitimate fare exception requiring case-by-case judgement"])

# ── AP: Procure-to-Pay ───────────────────────────────────────────────────────
P("AC-FN-AP-01",
  desc="A purchase requisition is raised and approved through SAP Ariba, initiating the procure-to-pay "
       "chain for goods or services required across the business.",
  trig="An employee or department identifies a need to purchase goods or services.",
  out="An approved purchase requisition ready for supplier order, with spend correctly categorised and "
      "authorised at the appropriate level.",
  note="Requisition approval is the point where spend authority is actually exercised, which makes correct "
      "delegation of authority enforcement here more important than transaction processing speed alone.",
  phases=["Requisition creation", "Approval routing", "Requisition confirmation"],
  steps=[
    S("1.1","Create purchase requisition","Procurement Coordinator","SAP Ariba",
      "Business need for goods or services","Created requisition with spend category",
      "Created with correct spend categorisation at 95 percent","N","N",
      "Spend categorisation quality directly affects downstream spend analytics and supplier consolidation opportunities"),
    S("2.1","Route requisition for approval","Procurement Coordinator","SAP Ariba",
      "Created requisition","Routed for approval per delegation of authority",
      "Routed correctly against delegation of authority at 100 percent","Y","N",
      "Delegation of authority thresholds have to be correctly configured and kept current as roles change"),
    S("2.2","Approve or reject requisition","Approving Manager","SAP Ariba",
      "Routed requisition","Approved or rejected requisition",
      "Decided within the standard approval service level at 90 percent","N","N",
      "Approval delay for a time-sensitive purchase can create operational pressure to bypass the process"),
    S("3.1","Confirm requisition ready for sourcing","Procurement Coordinator","SAP Ariba",
      "Approved requisition","Confirmed requisition",
      "Confirmed within 1 business day of approval at 100 percent","N","N",
      "A requisition confirmed without complete specification detail generates rework at the sourcing stage"),
  ],
  kpis=["Created with correct spend categorisation at 95 percent",
        "Routed correctly against delegation of authority at 100 percent",
        "Decided within the standard approval service level at 90 percent",
        "Confirmed within 1 business day of approval at 100 percent"],
  risks=["Delegation of authority thresholds not being kept current as roles and responsibilities change",
         "Approval delay for a time-sensitive purchase creating operational pressure to bypass the process",
         "Spend categorisation quality directly affecting downstream spend analytics and consolidation opportunities",
         "A requisition confirmed without complete specification generating rework at the sourcing stage"])

P("AC-FN-AP-02",
  desc="A new supplier is onboarded and their master data established in SAP, covering the qualification, "
       "banking and tax information required before the supplier can be paid.",
  trig="A new supplier relationship is established requiring master data setup.",
  out="A qualified supplier with complete, verified master data, ready to receive purchase orders and "
      "payment.",
  note="Supplier master data errors, particularly in banking information, are a known fraud vector, which "
      "makes verification here a financial control against payment fraud, not just an administrative setup "
      "step.",
  phases=["Supplier qualification", "Master data capture", "Verification"],
  steps=[
    S("1.1","Qualify the new supplier","Procurement Coordinator","SAP Ariba",
      "Candidate supplier and business need","Qualified supplier",
      "Qualified against defined criteria for 100 percent of new suppliers at 100 percent","N","N",
      "Qualification depends on documentation the supplier itself provides and is not independently verified in every case"),
    S("2.1","Capture supplier master data","Procurement Coordinator","SAP S/4HANA",
      "Qualified supplier","Captured master data including banking and tax information",
      "Captured for 100 percent of qualified suppliers before first order at 100 percent","N","N",
      "Banking information errors, whether accidental or fraudulent, are a known and material payment fraud vector"),
    S("2.2","Verify banking information through an independent channel","Procurement Coordinator","SAP S/4HANA",
      "Captured banking data","Verified banking information",
      "Verified through a channel independent of the supplier's own submission for 100 percent of new suppliers","Y","N",
      "Verifying banking data only against the supplier's own submission does not protect against a fraudulent submission"),
    S("3.1","Activate supplier for ordering","Procurement Coordinator","SAP Ariba",
      "Verified master data","Activated supplier",
      "Activated within 5 business days of verification at 95 percent","N","N",
      "An activation before verification completes creates a window where a fraudulent supplier record could be paid"),
  ],
  kpis=["Qualified against defined criteria for 100 percent of new suppliers at 100 percent",
        "Captured for 100 percent of qualified suppliers before first order at 100 percent",
        "Verified through an independent channel for 100 percent of new suppliers",
        "Activated within 5 business days of verification at 95 percent"],
  risks=["Banking information errors, accidental or fraudulent, being a known and material payment fraud vector",
         "Verifying banking data only against the supplier's own submission not protecting against fraudulent submission",
         "Qualification depending on supplier-provided documentation not independently verified in every case",
         "Activation before verification completes creating a window where a fraudulent record could be paid"])

P("AC-FN-AP-03",
  desc="A supplier invoice is processed and matched three ways against the purchase order and goods "
       "receipt before payment, confirming Air Canada only pays for what was actually ordered and "
       "received.",
  trig="A supplier submits an invoice against a purchase order.",
  out="A three-way matched invoice approved for payment, or a documented discrepancy routed for "
      "resolution before payment proceeds.",
  note="Three-way matching, invoice against purchase order against goods receipt, is the core control "
      "against paying for goods or services that were never actually delivered, which makes this one of the "
      "most consequential controls in the entire finance function.",
  phases=["Invoice receipt", "Three-way matching", "Payment approval"],
  steps=[
    S("1.1","Receive and register supplier invoice","Accounts Payable Analyst","SAP S/4HANA",
      "Submitted supplier invoice","Registered invoice",
      "Registered within 2 business days of receipt at 100 percent","N","N",
      "Invoice format and submission channel vary by supplier, complicating consistent intake"),
    S("2.1","Match invoice to purchase order","Accounts Payable Analyst","SAP S/4HANA",
      "Registered invoice and purchase order","Matched or unmatched invoice",
      "Matched for 100 percent of invoices with a valid PO at 95 percent","Y","N",
      "A price or quantity discrepancy against the PO requires resolution before matching can complete"),
    S("2.2","Match against goods receipt confirmation","Accounts Payable Analyst","SAP S/4HANA",
      "PO-matched invoice and goods receipt","Three-way matched invoice",
      "Matched for 100 percent of applicable invoices at 95 percent","N","N",
      "A goods receipt not yet confirmed in the system blocks payment even when the goods have physically arrived"),
    S("3.1","Approve invoice for payment","Accounts Payable Analyst","SAP S/4HANA",
      "Three-way matched invoice","Approved for payment",
      "Approved within the standard processing timeline at 90 percent","N","N",
      "Three-way matching is the core control against paying for goods or services never actually delivered"),
  ],
  kpis=["Registered within 2 business days of receipt at 100 percent",
        "Matched for 100 percent of invoices with a valid PO at 95 percent",
        "Matched for 100 percent of applicable invoices at 95 percent",
        "Approved within the standard processing timeline at 90 percent"],
  risks=["A goods receipt not yet confirmed in the system blocking payment even when goods have physically arrived",
         "Three-way matching being the core control against paying for undelivered goods or services",
         "Invoice format and submission channel varying by supplier, complicating consistent intake",
         "A price or quantity discrepancy against the PO requiring resolution before matching can complete"])

P("AC-FN-AP-04",
  desc="A payment run is executed and disbursed to suppliers, releasing approved invoices in a scheduled "
       "batch run against the treasury cash position.",
  trig="The scheduled payment run cycle comes due.",
  out="Approved invoices disbursed on schedule, with payment correctly reflecting terms and the treasury "
      "cash position.",
  note="A payment run has to coordinate approved invoice volume against the treasury cash position covered "
      "in AC-FN-TR-01, since disbursing more than the available cash position supports creates a genuine "
      "liquidity problem, not just an accounting entry.",
  phases=["Payment run preparation", "Cash position coordination", "Disbursement"],
  steps=[
    S("1.1","Compile approved invoices for the payment run","Accounts Payable Analyst","SAP S/4HANA",
      "Approved and matched invoices","Compiled payment run batch",
      "Compiled within the scheduled run preparation window at 100 percent","N","N",
      "Payment terms vary by supplier and determine which invoices are actually due in this specific run"),
    S("2.1","Coordinate against treasury cash position","Accounts Payable Analyst","SAP S/4HANA",
      "Compiled batch and available cash position","Confirmed run within cash availability",
      "Confirmed before disbursement for 100 percent of scheduled runs at 100 percent","Y","N",
      "Disbursing more than the available cash position supports creates a genuine liquidity problem"),
    S("2.2","Apply early payment discount where available","Accounts Payable Analyst","SAP S/4HANA",
      "Confirmed batch","Applied discount where terms allow",
      "Applied for 100 percent of eligible invoices at 100 percent","N","N",
      "A missed early payment discount is a small but avoidable cost across a high invoice volume"),
    S("3.1","Execute disbursement","Accounts Payable Analyst","SAP S/4HANA",
      "Confirmed and discount-applied batch","Disbursed payments",
      "Disbursed on the scheduled run date at 100 percent","N","N",
      "A disbursement error, wrong amount or wrong supplier, is harder to reverse once funds have moved"),
  ],
  kpis=["Compiled within the scheduled run preparation window at 100 percent",
        "Confirmed before disbursement for 100 percent of scheduled runs at 100 percent",
        "Applied for 100 percent of eligible invoices at 100 percent",
        "Disbursed on the scheduled run date at 100 percent"],
  risks=["Disbursing more than the available cash position supports creating a genuine liquidity problem",
         "A disbursement error being harder to reverse once funds have already moved",
         "A missed early payment discount being a small but avoidable cost across a high invoice volume",
         "Payment terms varying by supplier and determining which invoices are actually due in a given run"])

P("AC-FN-AP-05",
  desc="Contract compliance and spend against negotiated supplier agreements is analysed, identifying "
       "off-contract spend and maverick buying that erode the value negotiated in the original agreement.",
  trig="The recurring spend analytics review cycle runs.",
  out="A spend analysis identifying compliance against contracted terms, with off-contract spend flagged "
      "for correction and negotiated value protected.",
  note="Negotiated contract terms only deliver their value if actual purchasing behaviour follows them, "
      "which makes this analytics function the discipline that protects procurement's negotiated savings "
      "from quietly eroding through uncontrolled spend.",
  phases=["Spend data compilation", "Compliance analysis", "Corrective action"],
  steps=[
    S("1.1","Compile spend data by supplier and category","Procurement Coordinator","SAP Ariba",
      "Purchase order and invoice data","Compiled spend data",
      "Compiled within 5 business days of period close at 100 percent","N","N",
      "Off-contract spend that bypassed the formal purchasing process is harder to capture completely"),
    S("2.1","Analyse compliance against negotiated contract terms","Procurement Coordinator","SAP Analytics Cloud",
      "Compiled spend and contract terms","Compliance analysis",
      "Analysed for 100 percent of material contracts each cycle at 100 percent","N","N",
      "Negotiated contract terms only deliver value if actual purchasing behaviour follows them"),
    S("2.2","Identify off-contract and maverick spend","Procurement Coordinator","SAP Analytics Cloud",
      "Compliance analysis","Identified off-contract spend",
      "Identified for 100 percent of material categories each cycle at 100 percent","N","N",
      "Maverick spend often happens for legitimate urgency reasons, not deliberate policy evasion"),
    S("3.1","Route findings for corrective action","Procurement Coordinator","SAP Ariba",
      "Identified off-contract spend","Routed corrective action",
      "Routed within 10 business days of identification at 100 percent","N","N",
      "Correction has to address the underlying reason for bypassing the contract, not just flag the transaction"),
  ],
  kpis=["Compiled within 5 business days of period close at 100 percent",
        "Analysed for 100 percent of material contracts each cycle at 100 percent",
        "Identified for 100 percent of material categories each cycle at 100 percent",
        "Contract compliance rate meeting target, trending toward improvement"],
  risks=["Off-contract spend that bypassed the formal purchasing process being harder to capture completely",
         "Maverick spend often happening for legitimate urgency reasons rather than deliberate policy evasion",
         "Negotiated contract value quietly eroding through uncontrolled spend without active analysis",
         "Correction addressing only the flagged transaction without resolving the underlying reason for bypass"])
