# -*- coding: utf-8 -*-
"""AC-HR-LR — Labour Relations (5) and AC-HR-DE — Engagement, Learning and Inclusion (5)."""
from content_lib import P, S

# ── LR: Labour Relations ────────────────────────────────────────────────────
P("AC-HR-LR-01",
  desc="Collective bargaining preparation is conducted ahead of a negotiation with ACPA, CUPE, Teamsters "
       "or UNIFOR, developing the mandate and supporting analysis before formal talks begin.",
  trig="A collective agreement approaches its expiry, requiring negotiation of a renewal.",
  out="An approved bargaining mandate with supporting cost and market analysis, ready for the negotiating "
      "team to open formal talks.",
  note="Bargaining preparation quality directly shapes negotiation outcomes months later, and a mandate "
      "built on weak cost or market analysis constrains the negotiating team's ability to respond to what "
      "actually happens across the table.",
  phases=["Analysis and benchmarking", "Mandate development", "Approval"],
  steps=[
    S("1.1","Conduct cost and market benchmarking analysis","Labour Relations Coordinator","Jeppesen Crew",
      "Current agreement terms and industry comparables","Cost and benchmarking analysis",
      "Completed within the pre-negotiation planning window at 100 percent","N","N",
      "Industry benchmarking data quality varies and is not always directly comparable across different carriers' structures"),
    S("2.1","Develop bargaining mandate options","Labour Relations Coordinator","Jeppesen Crew",
      "Benchmarking analysis","Developed mandate options",
      "Developed within the planning timeline at 100 percent","N","N",
      "A mandate built on weak analysis constrains the negotiating team's ability to respond at the table"),
    S("2.2","Assess operational impact of mandate scenarios","Crew Planning Analyst","Jeppesen Crew",
      "Mandate options","Operational impact assessment",
      "Assessed for 100 percent of material mandate scenarios at 100 percent","Y","N",
      "Contract term changes ripple into crew planning and rostering systems that have to be reconfigured accordingly"),
    S("3.1","Obtain executive approval for the mandate","Labour Relations Coordinator","Jeppesen Crew",
      "Assessed options","Approved bargaining mandate",
      "Approved before formal negotiations open at 100 percent","N","N",
      "A mandate not finalised before talks open leaves the negotiating team without a clear approved position"),
  ],
  kpis=["Completed within the pre-negotiation planning window at 100 percent",
        "Developed within the planning timeline at 100 percent",
        "Assessed for 100 percent of material mandate scenarios at 100 percent",
        "Approved before formal negotiations open at 100 percent"],
  risks=["A mandate built on weak cost or market analysis constraining the negotiating team's ability to respond",
         "Contract term changes rippling into crew planning and rostering systems requiring reconfiguration",
         "Industry benchmarking data not always being directly comparable across different carriers' structures",
         "A mandate not finalised before talks open leaving the team without a clear approved position"])

P("AC-HR-LR-02",
  desc="A grievance is investigated and progressed through the defined process to resolution, covering "
       "ground and corporate employee grievances distinct from the crew-specific process in AC-CM-CC-04.",
  trig="An employee or union representative files a grievance under a collective agreement.",
  out="A grievance investigated and resolved or escalated within the agreement's procedural timelines.",
  note="This mirrors the same procedural discipline as the crew grievance process in AC-CM-CC-04, applied "
      "to the ground and corporate workforce's own distinct bargaining unit agreements.",
  phases=["Grievance intake", "Investigation", "Response and resolution"],
  steps=[
    S("1.1","Receive and log the grievance","Labour Relations Coordinator","Dayforce",
      "Filed grievance","Logged grievance with procedural deadline",
      "Logged within the agreement's required timeframe at 100 percent","N","N",
      "Grievance filing requirements differ across CUPE, Teamsters and UNIFOR agreements"),
    S("2.1","Investigate the underlying facts","Labour Relations Coordinator","Dayforce",
      "Logged grievance","Investigated facts and applicable provisions",
      "Investigated within the procedural deadline at 100 percent","N","N",
      "Investigation depends on roster, pay and disciplinary records that span several systems"),
    S("2.2","Prepare Air Canada's response position","Labour Relations Coordinator","Dayforce",
      "Investigated facts","Prepared response position",
      "Prepared before the procedural deadline at 100 percent","Y","N",
      "A position not correctly applying the agreement provision weakens Air Canada's standing at the next stage"),
    S("3.1","Respond within the procedural timeline","Labour Relations Coordinator","Dayforce",
      "Prepared position","Filed response or resolution",
      "Filed within the agreement's procedural deadline at 100 percent","N","N",
      "A missed deadline constitutes a procedural failure independent of the grievance's actual merits"),
  ],
  kpis=["Logged within the agreement's required timeframe at 100 percent",
        "Investigated within the procedural deadline at 100 percent",
        "Filed within the agreement's procedural deadline at 100 percent",
        "Grievance resolution rate at first stage tracked against escalation rate"],
  risks=["A missed procedural deadline constituting a compliance failure independent of the grievance's actual merits",
         "Grievance filing requirements differing across CUPE, Teamsters and UNIFOR agreements",
         "Investigation depending on records spanning several systems not originally designed to be pulled together",
         "A response not correctly applying the agreement provision weakening Air Canada's standing"])

P("AC-HR-LR-03",
  desc="Union consultation is conducted and change notification issued when a workplace change affects "
       "represented employees, meeting the collective agreement's consultation and notice requirements.",
  trig="A planned workplace or operational change affects employees covered by a collective agreement.",
  out="Union consultation completed and change notification issued within the agreement's required "
      "timeframe, before the change is implemented.",
  note="Consultation obligations exist to give the union a genuine opportunity to respond before a change "
      "is implemented, which means consultation conducted as a formality after the decision is already "
      "final does not actually satisfy the underlying obligation.",
  phases=["Change impact assessment", "Consultation", "Notification and implementation"],
  steps=[
    S("1.1","Assess change impact on represented employees","Labour Relations Coordinator","Jeppesen Crew",
      "Planned workplace or operational change","Impact assessment",
      "Assessed before consultation begins at 100 percent","N","N",
      "Impact assessment has to correctly identify every affected bargaining unit, not just the most obviously affected one"),
    S("2.1","Conduct union consultation","Labour Relations Coordinator","Jeppesen Crew",
      "Impact assessment","Completed consultation with union response",
      "Consultation completed within the agreement's required notice period at 100 percent","Y","N",
      "Consultation conducted as a formality after the decision is already final does not satisfy the underlying obligation"),
    S("2.2","Address union feedback where applicable","Labour Relations Coordinator","Jeppesen Crew",
      "Union response","Addressed feedback or documented position",
      "Addressed within the consultation period at 90 percent","N","N",
      "Feedback that goes unaddressed can itself become the basis of a subsequent grievance"),
    S("3.1","Issue change notification and implement","Labour Relations Coordinator","Jeppesen Crew",
      "Completed consultation","Issued notification with implementation",
      "Notification issued within the agreement's required timeframe at 100 percent","N","N",
      "Implementation before the required notice period expires is a direct procedural violation"),
  ],
  kpis=["Assessed before consultation begins at 100 percent",
        "Consultation completed within the agreement's required notice period at 100 percent",
        "Addressed within the consultation period at 90 percent",
        "Notification issued within the agreement's required timeframe at 100 percent"],
  risks=["Consultation conducted as a formality after the decision is already final not satisfying the obligation",
         "Implementation before the required notice period expires being a direct procedural violation",
         "Impact assessment failing to identify every affected bargaining unit, not just the most obvious one",
         "Unaddressed union feedback itself becoming the basis of a subsequent grievance"])

P("AC-HR-LR-04",
  desc="Employee discipline and performance issues for the ground and corporate workforce are addressed "
       "through the defined process, applied consistently and within collective agreement due process "
       "requirements.",
  trig="A performance or conduct issue involving a represented or non-represented employee is identified.",
  out="A performance issue addressed through the defined process, with consistent application and full "
      "compliance with applicable due process requirements.",
  note="This mirrors the same discipline consistency discipline as the crew process in AC-CM-CC-05, applied "
      "across CUPE, Teamsters, UNIFOR and non-represented corporate employees, each with a different set of "
      "due process protections that has to be correctly identified before action is taken.",
  phases=["Issue documentation", "Process application", "Resolution"],
  steps=[
    S("1.1","Document the performance issue","Labour Relations Coordinator","Dayforce",
      "Observed or reported issue","Documented issue with factual basis",
      "Documented within the required timeframe at 100 percent","N","N",
      "Documentation quality at this stage determines whether the process can withstand later scrutiny"),
    S("2.1","Apply progressive discipline framework","Labour Relations Coordinator","Dayforce",
      "Documented issue and prior record","Determined discipline level",
      "Applied consistently against the framework at 100 percent","Y","N",
      "Discipline consistency across similar cases and different employee groups is essential to withstand a grievance challenge"),
    S("2.2","Confirm applicable due process requirements","Labour Relations Coordinator","Dayforce",
      "Determined discipline","Confirmed due process compliance",
      "100 percent compliant with the applicable agreement or policy due process at 100 percent","Y","N",
      "Due process requirements differ across three union agreements and the non-represented employee policy"),
    S("3.1","Communicate and implement the outcome","Labour Relations Coordinator","Dayforce",
      "Confirmed process","Implemented discipline outcome",
      "Implemented within the required timeframe at 100 percent","N","N",
      "An outcome implemented outside due process requirements is vulnerable to grievance and reversal"),
  ],
  kpis=["Documented within the required timeframe at 100 percent",
        "Applied consistently against the framework at 100 percent",
        "100 percent compliant with the applicable agreement or policy due process at 100 percent",
        "Discipline decisions upheld on grievance challenge above target"],
  risks=["Due process requirements differing across three union agreements and the non-represented employee policy",
         "Discipline consistency across similar cases and employee groups being essential to withstand challenge",
         "An outcome implemented outside due process requirements being vulnerable to grievance and reversal",
         "Documentation quality at identification determining whether the process withstands later scrutiny"])

P("AC-HR-LR-05",
  desc="Labour cost scenarios are modelled to support negotiation and workforce planning decisions, "
       "quantifying the financial impact of different contract terms and staffing structures.",
  trig="A negotiation scenario or workforce planning decision requires labour cost modelling.",
  out="A labour cost scenario model quantifying the financial impact of proposed terms or structures, "
      "supporting an informed decision.",
  note="Labour cost modelling feeds directly into the bargaining mandate development in AC-HR-LR-01, and "
      "the quality of the underlying cost model is what actually determines whether the mandate reflects "
      "the true financial stakes of a negotiation position.",
  phases=["Scenario definition", "Cost modelling", "Scenario comparison"],
  steps=[
    S("1.1","Define labour cost scenarios to model","Labour Relations Coordinator","SAP Analytics Cloud",
      "Negotiation position or workforce planning question","Defined scenarios",
      "Defined for 100 percent of material negotiation positions at 100 percent","N","N",
      "Scenario definition has to capture the full range of positions actually under negotiation consideration"),
    S("2.1","Model financial impact by scenario","Labour Relations Coordinator","SAP Analytics Cloud",
      "Defined scenarios and current cost base","Modelled financial impact",
      "Modelled for 100 percent of defined scenarios at 100 percent","N","N",
      "Multi-year cost projections carry compounding assumptions that need to be made explicit, not buried in the model"),
    S("2.2","Validate model assumptions against actuals","Labour Relations Coordinator","SAP Analytics Cloud",
      "Modelled scenarios","Validated model",
      "Validated against current actual cost data before use at 100 percent","Y","N",
      "A model built on stale cost assumptions can materially misstate the true financial stakes of a position"),
    S("3.1","Present scenario comparison to decision-makers","Labour Relations Coordinator","SAP Analytics Cloud",
      "Validated scenarios","Presented comparison",
      "Presented within the negotiation or planning timeline at 100 percent","N","N",
      "A comparison presented without clear assumptions risks being taken as more certain than the model actually supports"),
  ],
  kpis=["Defined for 100 percent of material negotiation positions at 100 percent",
        "Modelled for 100 percent of defined scenarios at 100 percent",
        "Validated against current actual cost data before use at 100 percent",
        "Presented within the negotiation or planning timeline at 100 percent"],
  risks=["A model built on stale cost assumptions materially misstating the true financial stakes of a position",
         "Multi-year cost projections carrying compounding assumptions that need to be made explicit, not buried",
         "A comparison presented without clear assumptions being taken as more certain than the model supports",
         "Scenario definition failing to capture the full range of positions actually under negotiation consideration"])

# ── DE: Engagement, Learning and Inclusion ──────────────────────────────────
P("AC-HR-DE-01",
  desc="An employee engagement survey is conducted and action planning developed against the results, "
       "closing the loop from employee feedback to a documented organisational response.",
  trig="The recurring employee engagement survey cycle runs.",
  out="Survey results analysed with action plans developed by function, closing the loop between employee "
      "feedback and organisational response.",
  note="A survey with no visible action plan afterward teaches employees that the survey does not matter, "
      "which erodes response rate and honesty in every subsequent cycle, making action planning the step "
      "that actually determines the survey's long-term value.",
  phases=["Survey execution", "Results analysis", "Action planning"],
  steps=[
    S("1.1","Execute the engagement survey","People Analytics Coordinator","SAP S/4HANA",
      "Employee population","Collected survey responses",
      "Response rate meeting target across the employee population at 100 percent","N","N",
      "A survey with no visible action plan from the prior cycle erodes response rate and honesty in this one"),
    S("2.1","Analyse results by function and demographic","People Analytics Coordinator","SAP Analytics Cloud",
      "Collected responses","Analysed results",
      "Analysed within the standard post-survey timeline at 100 percent","N","N",
      "Aggregate results can mask a specific function or demographic with a materially different experience"),
    S("2.2","Identify priority themes","People Analytics Coordinator","SAP Analytics Cloud",
      "Analysed results","Identified priority themes",
      "Identified for 100 percent of functions with material findings at 100 percent","N","N",
      "Too many priority themes at once dilutes the organisational capacity to actually act on any of them"),
    S("3.1","Develop and publish action plans","People Analytics Coordinator","SAP S/4HANA",
      "Priority themes","Published action plans by function",
      "Published within the required timeframe after results release at 90 percent","N","N",
      "Action planning is the step that actually determines the survey's long-term value to employees"),
  ],
  kpis=["Response rate meeting target across the employee population at 100 percent",
        "Analysed within the standard post-survey timeline at 100 percent",
        "Identified for 100 percent of functions with material findings at 100 percent",
        "Published within the required timeframe after results release at 90 percent"],
  risks=["A survey with no visible action plan from the prior cycle eroding response rate and honesty in this one",
         "Aggregate results masking a specific function or demographic with a materially different experience",
         "Too many priority themes at once diluting the organisational capacity to actually act on any of them",
         "Action plans published without genuine follow-through undermining trust in future survey cycles"])

P("AC-HR-DE-02",
  desc="Diversity, equity and inclusion programme initiatives are delivered and their impact measured "
       "against defined organisational goals.",
  trig="The annual DEI programme cycle runs, or a specific initiative reaches its delivery milestone.",
  out="Delivered DEI initiatives with measured impact against defined goals, feeding the next cycle's "
      "programme design.",
  note="DEI impact measurement matters because a programme that is delivered without honest measurement of "
      "whether it actually moved the underlying metrics risks becoming an activity for its own sake rather "
      "than a genuine organisational change effort.",
  phases=["Initiative delivery", "Impact measurement", "Programme reporting"],
  steps=[
    S("1.1","Deliver planned DEI initiatives","DEI Programme Coordinator","SAP S/4HANA",
      "Approved programme plan","Delivered initiatives",
      "Delivered within the planned timeline for 90 percent of initiatives at 100 percent","N","N",
      "Delivery quality across a large, distributed workforce is genuinely harder to maintain consistently than at a single site"),
    S("2.1","Measure representation and inclusion metrics","People Analytics Coordinator","SAP Analytics Cloud",
      "Workforce demographic and survey data","Measured metrics against goals",
      "Measured for 100 percent of defined organisational goals each cycle at 100 percent","N","N",
      "Representation metrics alone do not capture whether the workplace experience itself has genuinely improved"),
    S("2.2","Assess initiative-specific impact","People Analytics Coordinator","SAP Analytics Cloud",
      "Delivered initiatives and measured metrics","Impact assessment by initiative",
      "Assessed for 100 percent of material initiatives each cycle at 100 percent","N","N",
      "Isolating a single initiative's specific impact from concurrent organisational changes is genuinely difficult"),
    S("3.1","Report programme results and inform next cycle","DEI Programme Coordinator","SAP S/4HANA",
      "Impact assessment","Reported results with next-cycle recommendations",
      "Reported within the annual programme reporting timeline at 100 percent","N","N",
      "A programme delivered without honest measurement risks becoming an activity for its own sake"),
  ],
  kpis=["Delivered within the planned timeline for 90 percent of initiatives at 100 percent",
        "Measured for 100 percent of defined organisational goals each cycle at 100 percent",
        "Assessed for 100 percent of material initiatives each cycle at 100 percent",
        "Reported within the annual programme reporting timeline at 100 percent"],
  risks=["A programme delivered without honest measurement risking becoming an activity for its own sake",
         "Representation metrics alone not capturing whether the workplace experience has genuinely improved",
         "Isolating a single initiative's specific impact from concurrent organisational changes",
         "Delivery quality across a large, distributed workforce being harder to maintain than at a single site"])

P("AC-HR-DE-03",
  desc="Learning curriculum is designed and delivered across the employee population, from mandatory "
       "compliance training to role-specific skill development.",
  trig="A curriculum requirement is identified, from a new regulatory obligation, a role change, or a "
       "recurring compliance training cycle.",
  out="Designed and delivered learning curriculum meeting the requirement, with completion tracked against "
      "target.",
  note="Mandatory compliance training carries a hard completion deadline in a way that skill development "
      "training does not, which means curriculum delivery has to treat the two categories with materially "
      "different urgency despite both running through the same delivery infrastructure.",
  phases=["Curriculum design", "Delivery", "Completion tracking"],
  steps=[
    S("1.1","Design curriculum against the requirement","Learning and Development Coordinator","SAP S/4HANA",
      "Identified requirement","Designed curriculum",
      "Designed within the required lead time before the delivery deadline at 100 percent","N","N",
      "Mandatory compliance content and skill development content have materially different design and urgency needs"),
    S("2.1","Deliver curriculum to the target population","Learning and Development Coordinator","SAP S/4HANA",
      "Designed curriculum","Delivered training",
      "Delivered to 100 percent of the target population within the required window at 90 percent","N","N",
      "Delivery to a geographically and functionally distributed workforce has genuine logistical complexity"),
    S("2.2","Track completion against deadline","Learning and Development Coordinator","SAP S/4HANA",
      "Delivered training","Tracked completion status",
      "Tracked continuously against 100 percent completion for mandatory training at 100 percent","N","N",
      "Mandatory training completion has a hard compliance deadline that skill development training does not carry"),
    S("3.1","Follow up on incomplete mandatory training","Learning and Development Coordinator","SAP S/4HANA",
      "Incomplete tracking status","Follow-up action with completion or escalation",
      "Followed up before the compliance deadline for 100 percent of incomplete mandatory training at 95 percent","N","Y",
      "Incomplete mandatory training past its deadline is a compliance gap that has to be escalated, not merely noted"),
  ],
  kpis=["Designed within the required lead time before the delivery deadline at 100 percent",
        "Delivered to 100 percent of the target population within the required window at 90 percent",
        "Tracked continuously against 100 percent completion for mandatory training at 100 percent",
        "Followed up before the compliance deadline for 100 percent of incomplete mandatory training at 95 percent"],
  risks=["Mandatory compliance training carrying a hard completion deadline that skill development training does not",
         "Delivery to a geographically and functionally distributed workforce having genuine logistical complexity",
         "Incomplete mandatory training past its deadline being a compliance gap requiring escalation, not just a note",
         "Mandatory and skill development content having materially different design and urgency needs despite shared infrastructure"])

P("AC-HR-DE-04",
  desc="Official Languages Act compliance is maintained in the employee workplace experience, ensuring "
       "bilingual capability and service in designated bilingual positions and regions.",
  trig="A position is designated bilingual, or the recurring Official Languages compliance review runs.",
  out="Confirmed bilingual capability in designated positions, with the workplace experience meeting "
      "Official Languages Act obligations.",
  note="Official Languages obligations apply to the employee experience itself, not only to the "
      "customer-facing channels covered throughout AC-CX, which makes this a distinct compliance dimension "
      "of the HR function rather than a customer service concern alone.",
  phases=["Bilingual position designation", "Capability verification", "Compliance monitoring"],
  steps=[
    S("1.1","Designate positions requiring bilingual capability","HR Compliance Coordinator","SAP S/4HANA",
      "Role and regional service requirement","Designated bilingual position",
      "Designated correctly for 100 percent of applicable roles at 100 percent","N","N",
      "Designation criteria have to correctly reflect actual customer and colleague interaction patterns for the role"),
    S("2.1","Verify bilingual capability at hiring or transfer","Talent Acquisition Coordinator","SAP S/4HANA",
      "Candidate for a designated position","Verified capability",
      "Verified before placement in the role for 100 percent of designated positions at 100 percent","Y","N",
      "Language capability assessment has to be consistent and defensible if later challenged"),
    S("2.2","Support language training where a capability gap exists","Learning and Development Coordinator","SAP S/4HANA",
      "Identified capability gap","Supported training toward the required standard",
      "Support provided within a defined timeframe for 90 percent of identified gaps","N","N",
      "A capability gap not addressed within a reasonable timeframe leaves a designated position under-served"),
    S("3.1","Monitor compliance across designated positions","HR Compliance Coordinator","SAP Analytics Cloud",
      "Verified and supported positions","Compliance monitoring report",
      "Monitored each reporting cycle for 100 percent of designated positions at 100 percent","N","N",
      "This obligation applies to the employee experience itself, distinct from the customer-facing channels"),
  ],
  kpis=["Designated correctly for 100 percent of applicable roles at 100 percent",
        "Verified before placement in the role for 100 percent of designated positions at 100 percent",
        "Support provided within a defined timeframe for 90 percent of identified gaps",
        "Monitored each reporting cycle for 100 percent of designated positions at 100 percent"],
  risks=["Official Languages obligations applying to the employee experience itself, not only customer-facing channels",
         "Designation criteria not correctly reflecting actual customer and colleague interaction patterns",
         "A capability gap not addressed within a reasonable timeframe leaving a position under-served",
         "Language capability assessment needing to be consistent and defensible if later challenged"])

P("AC-HR-DE-05",
  desc="Talent review and succession planning is conducted for critical roles, identifying and developing "
       "internal candidates ready to step into a leadership or specialised position.",
  trig="The recurring talent review cycle runs, or a critical role's succession risk is flagged.",
  out="A documented succession plan for critical roles, with development actions in place for identified "
      "successors.",
  note="Succession planning value is entirely forward-looking, so a plan that identifies a successor but "
      "never actually develops them against the gap between their current and required capability offers "
      "little real protection when the critical role actually needs to be filled.",
  phases=["Critical role identification", "Successor assessment", "Development planning"],
  steps=[
    S("1.1","Identify critical roles requiring succession coverage","People Analytics Coordinator","SAP S/4HANA",
      "Organisational structure and risk assessment","Identified critical roles",
      "Identified for 100 percent of critical roles each review cycle at 100 percent","N","N",
      "Criticality assessment has to look beyond seniority alone to genuinely irreplaceable specialised knowledge"),
    S("2.1","Assess potential internal successors","People Analytics Coordinator","SAP S/4HANA",
      "Identified critical roles and internal talent pool","Assessed successor candidates",
      "Assessed for 100 percent of critical roles at 100 percent","N","N",
      "A role with no credible internal successor represents a genuine succession risk requiring an external plan"),
    S("2.2","Identify development gap for each successor","People Analytics Coordinator","SAP S/4HANA",
      "Assessed successors","Identified development gap",
      "Identified for 100 percent of assessed successors at 100 percent","Y","N",
      "A successor identified but never developed against their actual gap offers little real protection"),
    S("3.1","Implement development plan for successors","Learning and Development Coordinator","SAP S/4HANA",
      "Identified gap","Implemented development plan",
      "Implemented within the planning cycle for 90 percent of identified successors at 100 percent","N","N",
      "Development plans without genuine follow-through leave the succession plan a document rather than a real capability"),
  ],
  kpis=["Identified for 100 percent of critical roles each review cycle at 100 percent",
        "Assessed for 100 percent of critical roles at 100 percent",
        "Identified for 100 percent of assessed successors at 100 percent",
        "Implemented within the planning cycle for 90 percent of identified successors at 100 percent"],
  risks=["A successor identified but never developed against their actual gap offering little real protection",
         "A critical role with no credible internal successor representing a genuine succession risk",
         "Criticality assessment looking only at seniority rather than genuinely irreplaceable specialised knowledge",
         "Development plans without genuine follow-through leaving the succession plan a document, not a real capability"])
