---
title: "AI Governance for BI Platforms"
subtitle: "Key Considerations for Business Intelligence Applications"
date: 2026-06-12
publication: "Frictionless Decisions"
author: "Zane Hall"
source_url: https://zanehall.substack.com/p/ai-governance-for-bi-platforms
audience: everyone
wordcount: 1325
reactions: 0
comments: 0
restacks: 0
ingested_by: EVEglyphDesign eve-substack-archive
---

# AI Governance for BI Platforms

*Key Considerations for Business Intelligence Applications*

![](https://substackcdn.com/image/fetch/$s_!CAUP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe8d98a24-b2ba-442d-9ca7-584faf31881e_5712x3652.jpeg)
-

---

I’m not an AI architect, not a subject matter expert, and I haven’t personally managed any corporate AI implementations. In other words, I’m probably just like you.

I do, however, hear from you, my readers. You’re making technical decisions at a faster rate and higher cost than I’ve seen before. Although the AI tools you’re using are all similar to each other, your approaches to managing them vary widely. I want to help you avoid repeating the mistakes I experienced when previous “game-changing” analytic solutions were quickly adopted.

Let’s talk about governance. Even with the best tools, the process you follow for managing them ultimately determines how well your company uses them to make decisions.

It’s all about balance: giving analysts autonomy without losing the benefits of control and coordination. Analysts provide the most value when they can freely explore data, but you can’t synchronize decisions with a data free-for-all. Without hands-on decisions about change control, even the best strategy can fail.

Those of you I’ve talked with are taking three different approaches to governing AI in the business intelligence (BI) space:

**Decentralized access**. With full access to all data sources, analysts independently develop data models, generate analysis, draw conclusions, and report to management. AI accelerates reporting by eliminating technical barriers to accessing and interpreting data.

- **New software layer.** Third-party software provides tools for managing data definitions (semantics) and provides direct access without losing the governance needed for alignment. They may include knowledge mapping capabilities, a critical feature for AI language processing.

- **Data products.** An interpretive layer provides access to enterprise application data using the[standardized](https://www.cdata.com/blog/introducing-cdata-mcp-servers) MCP ([model context protocol](https://moderndata101.substack.com/p/architecture-data-products-ai-interactions?utm_source=publication-search)) design. This leverages native source system security without adding new processes. You can almost think of all data architecture as building context for decisions.

The first approach - decentralized access - mirrors the “democratic” approach advocated by many software vendors over the years. Tableau Software, for example, appealed to users for this reason: every user gets a license and the freedom to build their own data models. The problem with this approach isn’t the software - interactive visualization truly changed the way people interact with data. But most companies now recognize the chaos that thousands of dashboards create for their overall decision processes.

The second approach - adding new governance software - is a step in the right direction. Unfortunately, it tries to solve the complexity of governing your data by adding more complexity. That might be okay if you don’t have a data team to handle the more sophisticated solutions, but your company’s data models are your own secret sauce. One-size-fits-all solutions won’t save you money and will limit your capabilities.

The third approach - governed data products - most closely aligns with the *Frictionless Data* solutions I managed and write about.

### Federal Framework

Governance is the framework for making decisions about your data platform. In[this article](https://zanehall.substack.com/p/its-time-to-share-the-road), I compare the democratic, centralized, and federal data governance models. The trend of shifting work from traditional IT teams to those who understand data modeling best - the analysts - isn’t new. Tableau and Power BI, for example, introduced this model over a decade ago.

Without some kind of centralized process for qualifying content and solutions, this shift can lead to chaos, just like it did with every previous BI transformation.

Governance can eliminate the chaos and create leverage. The goals of governance include:

- **Alignment **- ensuring consistent, trusted answers from data across functional teams, management layers, and time periods.

- **Scale **- delivering data to everyone at the same time, without processing or interpretive delays.

- **Cost **- eliminating duplicate work, processing, and missed value-add opportunities.

Governance should be formalized early on in your journey. Keep in mind three considerations as you ramp up your solution:

#### **Security**

This is[the hidden scaler](https://zanehall.substack.com/p/use-security-to-build-great-business) for decisions. Security makes certain that people have complete access to only the data they need to do their job, without adding cost and complexity. It cannot be an afterthought; defining permissions and the ability to enforce them must be designed into the solution’s foundation. MCPs and 3rd party solutions probably don’t know your data well enough to deliver this value out of the box.

*Make a clear distinction between operational security and analytic security*. People view data in two directions. Operational teams view data through the lens of a business process, like order fulfillment. Business management teams view data vertically, across all functions; for example, they view the business through the lens of a P&L. These views imply different security frameworks.

#### **Source Data**

It’s easy to get so excited about the data modeling capabilities in AI that you ignore your biggest problem: [the data you need the most](https://zanehall.substack.com/p/the-most-important-data-you-dont-e57) is the data you don’t have in any platform. AI closes the data access gap, but better source data is equally important. Take a broad view of the source data you need for decisions:

- **Enterprise systems. **MCPs accelerate access to most of your operational data, replacing traditional ETL processes. Ask if AI outperforms the industrial-class solutions your data team has (hopefully) perfected over the years. If the answer is “yes,” use AI to transform that process.

- **New product data. **Most of this data does not exist in your enterprise platforms. You probably won’t find off-the-shelf MCPs for this type of data. It’s also your smallest data set, so stay aware of the proverbial case of using a sledgehammer to kill an ant.

- **Extended data**. Some of your most important data is materialized through logical shortcuts, such as end-market data. The processing and time required to link demand-fulfillment flows to end-customer decisions are beyond the reach of traditional business systems and analytics platforms. AI can solve this.

- **Business Intelligence hierarchies. **One of the most important values you get from a BI solution is aggregating data into the categories executives use for their communications. The best BI solutions recognize this and manage it in the most agile, responsive place they know: their data platform. These categories will overlap with the taxonomies used by your new AI language models.

- **Narrative.** The semantic descriptions behind variance explanations are data; it’s also proprietary to your company. Your AI platform should give you the ability to explicitly define concept relationships instead of leaving them to system-generated probabilities. Controlling these taxonomies adds efficiency and alignment. This is likely a new techno-functional skill your data team needs.

- **Data quality**. Managing and automating data quality requires a solution for[defining business rules](https://zanehall.substack.com/p/exception-reports-the-power-of-a?r=4chtg6&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false) and closing the loop between reporting data and business systems.

#### **Synchronizing Financials**

Financial data[links business processes](https://zanehall.substack.com/p/the-hidden-data-framework-behind) with strategic decision-making. Ensure these connections are maintained throughout the platform. Without maintaining these connections, any analysis that uses financial data to measure the business will not flow naturally from your solutions.

### Correcting Claude

I’m just as excited about using AI as you. Claude Pro just automated my data modeling work for [Common Ground](https://thecommonground.org/), the non-profit we support. It pulls the demographic data together for our annual report in about a minute. Even developing the program went really fast; together, we built the model in just a few hours. It scales up, too. I can use the same model to analyze any city in the country.

I corrected Claude’s work dozens of times as we built it; other people call this “training.” But Claude did the heavy lifting and educated me about the source data along the way. I have no interest in manually developing automated (API) connections to the census data. Researching the data relationships and geospatial tables doesn’t interest me either. AI gets all credit for this solution; I’m happy to hand over the programming work to AI.

But AI won’t govern itself. That’s the core wisdom I think you need as you step into using it.

---

 ![](https://substackcdn.com/image/fetch/$s_!J2gz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d684362-3d11-457c-bacc-799a9d9be1fc_900x900.jpeg) To remind you of this week’s data concept, enjoy *[Secret Separation](https://open.spotify.com/track/6pc34sMIcdcr9mpiZCSz9X?si=f7b0a46f1f40492f) *by The Fixx from the [Frictionless Data Spotify playlist](https://open.spotify.com/playlist/4PKCEghEMZ7MxCJMwlrnFV?si=b6X-1CP0RXmRNqqQs8AK8A)**.**

---

For the full story about making data flow faster and better, check out *Frictionless Data* on [Amazon](https://www.amazon.com/dp/1637428200?ref=cm_sw_r_ffobk_cp_ud_dp_X9E1MYZA0MX6ASKBVQQ1_1&ref_=cm_sw_r_ffobk_cp_ud_dp_X9E1MYZA0MX6ASKBVQQ1_1&social_share=cm_sw_r_ffobk_cp_ud_dp_X9E1MYZA0MX6ASKBVQQ1_1&bestFormat=true&previewDoh=1&previewDohDeal=1).

 ![](https://substackcdn.com/image/fetch/$s_!RFYI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc83074f5-ac33-4a97-97fc-608268c1c44b_347x522.jpeg)

---

Source: [AI Governance for BI Platforms](https://zanehall.substack.com/p/ai-governance-for-bi-platforms)
