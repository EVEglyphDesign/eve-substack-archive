---
title: "AI and Imposter Syndrome"
subtitle: "Anthropic\u2019s Common Sense Approach to Business Intelligence"
date: 2026-06-26
publication: "Frictionless Decisions"
author: "Zane Hall"
source_url: https://zanehall.substack.com/p/ai-and-imposter-syndrome
audience: everyone
wordcount: 674
reactions: 5
comments: 0
restacks: 1
ingested_by: EVEglyphDesign eve-substack-archive
---

# AI and Imposter Syndrome

*Anthropic’s Common Sense Approach to Business Intelligence*

![](https://substackcdn.com/image/fetch/$s_!YYZ3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F95a56897-2985-4a26-942f-b7da2a8995da_5712x4284.jpeg)
- ***Frictionless Decisions** brings you counterintuitive, original, jargon-free ideas for connecting data to decisions. *

[Share Frictionless Decisions](https://zanehall.substack.com/?utm_source=substack&utm_medium=email&utm_content=share&action=share)

---

A year ago, I wrote a simple post about data warehousing, called “[Always Warehouse the Data First](https://zanehall.substack.com/p/always-warehouse-the-data-first).” Honestly, I wondered if anyone would think this decades-old data management approach sounded relevant. People online weren’t just asking if data warehousing was relevant; they were actively predicting how AI would eliminate data management. I’m sure that got a lot of clicks, but I didn’t feel qualified to step into the debate.

Imposter Syndrome strikes back.

Making matters worse for me, many experts I follow have completely abandoned data warehousing in favor of AI solutions for organizing data. A few weeks ago, for example, Modern Data 101[ published a piece](https://moderndata101.substack.com/p/semantic-foundations?utm_source=post-email-title&publication_id=1170209&post_id=198375585&utm_campaign=email-post-title&isFreemail=true&r=44vu16&triedRedirect=true&utm_medium=email) explaining how AI can resolve differences in business definitions using a good ontology. The author asks how you can get AI to consistently deliver a correct answer to the question, “What was Q3 revenue?” to everyone in a company. Their solution is very technical, but I’ll summarize it as ingesting all the language used across different departments and mapping it to a single, larger semantic model.

I never had a problem delivering accurate financial totals to everyone using data in my company. We did this with good data governance practices in a data warehouse. I love ontologies (thank you, !), but I wondered why anyone would ever think you needed AI to solve this problem. It seemed like the classic “[Law of the Instrument](https://en.wikipedia.org/wiki/Law_of_the_instrument)“ bias: when you only know how to use a hammer, everything looks like a nail.

### Claude Chimes In

To my surprise, [Claude chimed in](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude?shem=rimspwouoe,,rimspwouoe,) on this problem a few weeks ago. Anthropic’s own data analytics team addressed the relationship between Artificial Intelligence and Business Intelligence. They address the age-old question of how a data team can balance self-service analytics with the need for trusted, accurate results. It’s a brilliant piece.

You’ll find two core management insights in their article. First, business analytic questions are different from other types of knowledge; there’s only one correct answer. You’re not looking to resolve ambiguity. This table explains the differences they see:

 ![](https://substackcdn.com/image/fetch/$s_!LhM4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F900d6ac5-4329-4f8a-932f-a319648d25a7_698x319.png) Second, while AI is amazing at helping non-technical people navigate data, it will only be successful in business analytics when it is querying a well-governed data foundation. A few key quotes from their article:

“Standard data engineering and data quality practices such as dimensional modeling, shift-left testing, freshness and completeness checks on critical pipelines all still apply (and we won’t relitigate these).”

- “The data foundations layer is aimed primarily at ambiguity: if revenue, for example, resolves to one governed dataset instead of forty plausible candidates, the problem largely disappears before the agent ever has to search. It’s also where the first staleness defense lives, since the same repo that defines the canonical models is the natural place to enforce that they stay current.”

- “The goal is that when an agent searches for a concept, it finds a single governed answer.”

 ![](https://substackcdn.com/image/fetch/$s_!a7rw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb7d0a974-5879-4537-a5b6-e8e32433565a_1600x1200.png)

### Common Sense Prevails

My friend[ Yakov Shkolnikov](https://www.linkedin.com/pulse/agenthouses-agentic-donuts-yakov-shkolnikov-ujjrc/), one of the smartest AI engineers I know, has been making this case for years. When I shared the Claude article with him, he summarized it by saying,

“Start with an accurate revenue report. And then disaggregate to a level your data accuracy allows. No reason to create completely unmanageable and unmaintainable semantic and knowledge graphs.”

I’m happy to report that common sense has prevailed. Or at least it has a strong foothold. Thank you to *Frictionless Decisions *reader **[Diana Nekhorosheva](https://www.linkedin.com/in/diana-nekhorosheva-19059829/) **for sharing the Claude essay with me!

If you’re struggling to get your AI tool (or any BI tool) to deliver accurate, trusted answers, don’t forget the Seventh Commandment of Data:[ Always Warehouse the Data First](https://zanehall.substack.com/p/always-warehouse-the-data-first).

---

 ![](https://substackcdn.com/image/fetch/$s_!J2gz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d684362-3d11-457c-bacc-799a9d9be1fc_900x900.jpeg) To remind you of this week’s data concept, enjoy *[Party Out of Bounds](https://open.spotify.com/track/7kWu31DOcgoosVElnFZ1OO?si=2e3c0aebc4534bf7), *by the B-52s, from the [Frictionless Data Spotify playlist](https://open.spotify.com/playlist/4PKCEghEMZ7MxCJMwlrnFV?si=b6X-1CP0RXmRNqqQs8AK8A)**. When you listen to this song, don’t forget that it’s a metaphor (like most B-52s songs)!**

---

For the full story about making data flow faster and better, check out *Frictionless Data* on [Amazon](https://www.amazon.com/dp/1637428200?ref=cm_sw_r_ffobk_cp_ud_dp_X9E1MYZA0MX6ASKBVQQ1_1&ref_=cm_sw_r_ffobk_cp_ud_dp_X9E1MYZA0MX6ASKBVQQ1_1&social_share=cm_sw_r_ffobk_cp_ud_dp_X9E1MYZA0MX6ASKBVQQ1_1&bestFormat=true&previewDoh=1&previewDohDeal=1).

 ![](https://substackcdn.com/image/fetch/$s_!RFYI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc83074f5-ac33-4a97-97fc-608268c1c44b_347x522.jpeg)

---

Source: [AI and Imposter Syndrome](https://zanehall.substack.com/p/ai-and-imposter-syndrome)
