# -*- coding: utf-8 -*-
"""AC-CX-CR — Complaints, APPR and Claims (5 remaining, CR-02 already in a_pilot)."""
from content_lib import P, S

P("AC-CX-CR-01",
  desc="An incoming customer complaint, from any channel, is registered, classified and triaged to the "
       "correct resolution path, whether that is a straightforward service recovery or a formal APPR "
       "determination.",
  trig="A customer submits a complaint through the web form, contact centre, social media or a CTA "
      "referral.",
  out="A registered, correctly classified complaint routed to the appropriate resolution path with a "
      "committed response timeline.",
  note="Triage accuracy at this first step determines everything downstream: a complaint incorrectly routed "
      "as a simple service issue when it actually carries APPR entitlement misses the regulatory clock that "
      "starts running from the original complaint, not from when it is correctly reclassified.",
  phases=["Intake and registration", "Classification", "Routing"],
  steps=[
    S("1.1","Register the complaint","Customer Relations Agent","Salesforce Service Cloud",
      "Customer complaint submission","Registered case with timestamp",
      "Registered within 1 business day of receipt at 100 percent","N","N",
      "Complaints arrive across channels with very different levels of structured detail"),
    S("1.2","Classify complaint category and severity","Customer Relations Agent","Salesforce Service Cloud",
      "Registered complaint content","Classified category and severity",
      "Correctly classified on first pass at 85 percent","N","N",
      "A complaint that touches multiple issues, such as both baggage and a delay, needs the correct primary classification"),
    S("2.1","Screen for APPR entitlement indicators","Customer Relations Agent","Salesforce Service Cloud",
      "Classified complaint","Flagged for APPR review or standard service recovery",
      "APPR indicators correctly flagged at 90 percent","Y","N",
      "A complaint that reads as a general service issue can actually carry APPR entitlement not obvious from the initial text"),
    S("3.1","Route to the correct resolution path","Customer Relations Agent","Salesforce Service Cloud",
      "Flagged classification","Routed case with committed response timeline",
      "Routed within 1 business day of registration at 95 percent","N","N",
      "A misrouted complaint loses time before the correct team even begins working it"),
  ],
  kpis=["Registered within 1 business day of receipt at 100 percent",
        "Correctly classified on first pass at 85 percent",
        "APPR indicators correctly flagged at 90 percent",
        "Routed within 1 business day of registration at 95 percent"],
  risks=["A complaint carrying APPR entitlement not obvious from the initial text being routed as standard service recovery",
         "The regulatory clock running from the original complaint even if it is later reclassified",
         "A misrouted complaint losing meaningful time before the correct team begins working it",
         "A complaint touching multiple issues being classified only against its least significant component"])

P("AC-CX-CR-03",
  desc="A CTA-referred complaint is escalated and a formal regulatory response is prepared, distinct from "
       "the standard entitlement determination in AC-CX-CR-02, when the Canadian Transportation Agency "
       "itself becomes involved.",
  trig="The Canadian Transportation Agency notifies Air Canada of a formal complaint referral or opens a "
       "review of a prior determination.",
  out="A complete, defensible regulatory response filed with the CTA within its required deadline.",
  note="A CTA referral is a different order of process from a standard complaint: it carries a hard "
       "regulatory deadline, and the response has to be defensible to a regulator, not just satisfactory to "
       "the customer.",
  phases=["Referral intake", "Case building", "Regulatory response"],
  steps=[
    S("1.1","Receive and register CTA referral","Regulatory Affairs Analyst","CTA Complaint Interface",
      "CTA notification","Registered referral with regulatory deadline",
      "Registered within 1 business day of receipt at 100 percent","N","N",
      "The CTA's own notification format and channel are separate from Air Canada's standard complaint intake"),
    S("2.1","Assemble the complete case file","Regulatory Affairs Analyst","Salesforce Service Cloud",
      "Referral and original complaint history","Assembled case file with full evidence",
      "Assembled within the first half of the response window at 100 percent","N","N",
      "Assembling a defensible file means pulling records from booking, operations and the original case together"),
    S("2.2","Obtain legal review of the response position","Regulatory Affairs Analyst","Salesforce Service Cloud",
      "Assembled case file","Legally reviewed response position",
      "Legal review completed before filing for 100 percent of CTA referrals","Y","N",
      "Legal review timelines have to fit within the CTA's own hard deadline, which does not flex"),
    S("3.1","File the formal response with the CTA","Regulatory Affairs Analyst","CTA Complaint Interface",
      "Reviewed response position","Filed regulatory response",
      "Filed within the CTA's required deadline at 100 percent","N","N",
      "A missed regulatory filing deadline is itself a compliance failure independent of the underlying case merits"),
  ],
  kpis=["Registered within 1 business day of receipt at 100 percent",
        "Legal review completed before filing for 100 percent of CTA referrals",
        "Filed within the CTA's required deadline at 100 percent",
        "Response upheld on subsequent CTA review above target"],
  risks=["A missed regulatory filing deadline constituting a compliance failure independent of case merits",
         "Legal review timelines having to fit within a hard CTA deadline that does not flex",
         "Assembling a defensible file requiring records from multiple systems not originally designed to be pulled together",
         "The CTA's own notification channel being separate from and inconsistent with standard complaint intake"])

P("AC-CX-CR-04",
  desc="A complaint that Air Canada could not resolve directly with the customer is escalated into the "
       "third-party arbitration pilot, tracking the case through the arbitrator's process to a binding "
       "outcome.",
  trig="A complaint remains unresolved after standard determination and the customer or Air Canada refers "
       "it to the arbitration pilot.",
  out="A case tracked through the third-party arbitration process to a binding outcome, with the decision "
      "implemented.",
  note="The arbitration pilot launched in 2026 covering an initial 500 cases is itself a novel process, "
       "distinct from both the standard APPR determination and a CTA regulatory referral, and how well it "
       "performs is being watched closely given public criticism that it amounts to little more than a "
       "procedural gesture.",
  phases=["Case referral", "Arbitration process tracking", "Outcome implementation"],
  steps=[
    S("1.1","Refer the case to arbitration","Customer Relations Team Lead","Salesforce Service Cloud",
      "Unresolved complaint","Referred case with arbitration reference",
      "Referred within the pilot's defined intake window at 100 percent","N","N",
      "The pilot's eligibility criteria are new and not always intuitive to apply consistently"),
    S("2.1","Submit Air Canada's position to the arbitrator","Regulatory Affairs Analyst","Salesforce Service Cloud",
      "Case file and referral","Submitted position with supporting evidence",
      "Submitted within the arbitrator's required timeline at 100 percent","N","N",
      "Evidence standards for an independent arbitrator may exceed what the original case file was built to support"),
    S("2.2","Track case status through the arbitration process","Regulatory Affairs Analyst","Salesforce Service Cloud",
      "Submitted case","Tracked status and any information requests",
      "Status tracked and information requests answered within the arbitrator's deadline at 100 percent","N","N",
      "The pilot's process maturity means timelines and requirements are still being established in practice"),
    S("3.1","Implement the binding arbitration outcome","Customer Relations Team Lead","SAP S/4HANA",
      "Arbitrator's binding decision","Implemented outcome, including any compensation",
      "Implemented within the arbitrator's required timeframe at 100 percent","N","N",
      "A binding outcome that contradicts Air Canada's own original determination still has to be honoured in full"),
  ],
  kpis=["Referred within the pilot's defined intake window at 100 percent",
        "Submitted within the arbitrator's required timeline at 100 percent",
        "Implemented within the arbitrator's required timeframe at 100 percent",
        "Case volume through the pilot tracked against the initial 500-case scope"],
  risks=["A binding outcome contradicting Air Canada's original determination still requiring full implementation",
         "Pilot eligibility criteria being new enough to apply inconsistently across similar cases",
         "Evidence standards for an independent arbitrator exceeding what the original case file was built to support",
         "Process immaturity in a first-year pilot creating timeline and requirement uncertainty"])

P("AC-CX-CR-05",
  desc="A baggage-related compensation claim, distinct from a standard mishandled bag trace, is assessed and "
       "settled, covering delayed, damaged or lost baggage compensation under applicable liability limits.",
  trig="A customer submits a compensation claim for delayed, damaged or lost baggage.",
  out="A settled claim within applicable liability limits, or a documented reason for a reduced or denied "
      "settlement.",
  note="Baggage compensation claims sit under the Montreal Convention liability framework, which sets "
      "specific limits and documentation standards that differ from the airline's general goodwill "
      "discretion elsewhere in customer service.",
  phases=["Claim intake and documentation", "Liability assessment", "Settlement"],
  steps=[
    S("1.1","Receive and register the baggage claim","Customer Relations Agent","Salesforce Service Cloud",
      "Customer claim submission","Registered claim with reference to the original PIR",
      "Registered within 1 business day of submission at 100 percent","N","N",
      "A claim not correctly linked to its original mishandled-bag PIR loses supporting context"),
    S("2.1","Assess claim against Montreal Convention liability limits","Customer Relations Agent","Salesforce Service Cloud",
      "Registered claim and declared value","Assessed liability position",
      "Assessed within 10 business days of registration at 90 percent","Y","N",
      "Declared value versus actual documented value can differ materially and needs consistent evidentiary standards"),
    S("2.2","Validate supporting documentation","Customer Relations Agent","Salesforce Service Cloud",
      "Customer-provided receipts or valuation evidence","Validated documentation",
      "Validated for 100 percent of claims above the standard threshold","N","N",
      "Documentation standards have to be applied consistently to avoid the appearance of arbitrary decisions"),
    S("3.1","Settle the claim","Customer Relations Agent","SAP S/4HANA",
      "Assessed and documented claim","Settlement payment or documented denial",
      "Settled within 30 days of complete documentation at 90 percent","N","N",
      "A settlement delay compounds customer frustration on top of the original baggage incident"),
  ],
  kpis=["Registered within 1 business day of submission at 100 percent",
        "Assessed within 10 business days of registration at 90 percent",
        "Settled within 30 days of complete documentation at 90 percent",
        "Settlement consistency across similar claims tracked for fairness"],
  risks=["A claim not correctly linked to its original mishandled-bag PIR losing supporting context",
         "Documentation standards applied inconsistently, creating an appearance of arbitrary decisions",
         "Declared value and actual documented value diverging materially without a consistent evidentiary standard",
         "A settlement delay compounding customer frustration on top of the original baggage incident"])

P("AC-CX-CR-06",
  desc="A service recovery gesture, distinct from a regulated APPR or Montreal Convention entitlement, is "
       "offered to a customer as a discretionary goodwill measure to repair the relationship after a poor "
       "experience.",
  trig="A customer service interaction identifies an opportunity for discretionary service recovery outside "
       "a formal entitlement.",
  out="A proportionate goodwill gesture offered and delivered, distinct from and not confused with a "
      "regulated compensation entitlement.",
  note="Goodwill gestures have to be kept clearly separate from regulated entitlements, both so agents "
      "apply consistent judgement and so a goodwill offer is never later characterised as an admission "
      "relevant to a formal APPR determination.",
  phases=["Recovery opportunity assessment", "Gesture determination", "Delivery"],
  steps=[
    S("1.1","Assess the service recovery opportunity","Customer Relations Agent","Salesforce Service Cloud",
      "Customer interaction and experience gap","Assessed recovery opportunity",
      "Assessed within the same interaction for 90 percent of eligible cases","N","N",
      "Recognising a genuine recovery opportunity depends on agent judgement that varies in consistency"),
    S("2.1","Determine proportionate gesture within delegation","Customer Relations Agent","Salesforce Service Cloud",
      "Assessed opportunity and delegation limits","Determined gesture",
      "Determined within delegated authority at 95 percent","Y","N",
      "A gesture disproportionate to the actual service gap undermines consistency across similar cases"),
    S("2.2","Distinguish gesture from any regulated entitlement","Customer Relations Agent","Salesforce Service Cloud",
      "Determined gesture and case context","Clearly documented distinction",
      "100 percent of gestures documented as distinct from any entitlement determination","N","N",
      "An undocumented gesture can later be conflated with a regulated entitlement in a subsequent review"),
    S("3.1","Deliver the gesture to the customer","Customer Relations Agent","Aeroplan Platform",
      "Determined gesture","Delivered goodwill gesture",
      "Delivered within 5 business days of determination at 95 percent","N","N",
      "Delivery mechanism, whether points, a voucher or a refund, has to match what was actually communicated to the customer"),
  ],
  kpis=["Determined within delegated authority at 95 percent",
        "100 percent of gestures documented as distinct from any entitlement determination",
        "Delivered within 5 business days of determination at 95 percent",
        "Gesture consistency across similar service gaps tracked for fairness"],
  risks=["A goodwill gesture later being conflated with a regulated entitlement in a subsequent review",
         "A gesture disproportionate to the actual service gap undermining consistency across similar cases",
         "Delivery mechanism not matching what was actually communicated to the customer",
         "Agent judgement varying enough in consistency to create fairness concerns across similar cases"])
