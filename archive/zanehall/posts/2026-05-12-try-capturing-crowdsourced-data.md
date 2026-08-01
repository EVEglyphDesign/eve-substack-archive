---
title: "Try Capturing Crowdsourced Data"
subtitle: "Materializing Executive Plans"
date: 2026-05-12
publication: "Frictionless Decisions"
author: "Zane Hall"
source_url: https://zanehall.substack.com/p/try-capturing-crowdsourced-data
audience: everyone
wordcount: 941
reactions: 1
comments: 2
restacks: 1
ingested_by: EVEglyphDesign eve-substack-archive
---

# Try Capturing Crowdsourced Data

*Materializing Executive Plans*

![](https://substackcdn.com/image/fetch/$s_!JAhs!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde5757f2-d56c-470d-a0bd-6c573c8b156b_5712x3882.jpeg)
- ***Frictionless Decisions** brings you counterintuitive, original, jargon-free ideas for connecting data to decisions.  Every week. *

[Share](https://zanehall.substack.com/p/try-capturing-crowdsourced-data?utm_source=substack&utm_medium=email&utm_content=share&action=share)

---

The smallest datasets - often found on the desktop of an executive - offer more information about where the company is headed than the huge transactional datasets that come from your enterprise systems. This “crowdsourced” data is hard to find, hard to manage, and discouraged by “best practices.”

But this plan data gives visibility into the expectations of your company’s leadership. Capturing this data removes friction from many decisions.

I learned to look for “unseen” data from the unlikeliest of people, a Japanese executive who’d only known videotape manufacturing. Before I share the technical side of managing plan data, let me introduce you to Mr. Yutaka Mori.

### Shipping Junk

In his best-selling book *Chip Wars*, Chris Miller explains how, in the 80s and 90s, U.S. semiconductor companies were essentially “shipping junk.” The worst US-produced chips had [failure rates more than 10 times](https://asianometry.passport.online/member/episode/how-semiconductor-yields-vastly-improved) those of Japanese chip makers, something I experienced first-hand.

Manufacturing breakdowns at the small semiconductor company I worked for kept happening over and over, for a new reason every time; we had recurring non-recurring problems. The semiconductors we made were cutting-edge, but our ability to consistently produce *working* products with advanced technology was seriously lacking. As the Cost Accounting manager, I knew this because I tracked the numbers. The company threw away about 40% of the product produced at our manufacturing plant due to quality issues. Management set a goal to make a big improvement…and only scrap 30%.

TDK Corporation, the Japanese company famous for VHS tapes, knew this problem when they acquired my company. They must have felt their low-tech manufacturing success would translate to high-tech computer hardware.

They sent in Mr. Mori.

When the first results came in after he arrived, all the managers congratulated each other. We’d achieved our 30% scrap goal. But Mr. Mori was deeply troubled. He walked into my office and, in his broken English, asked if I could measure the total dollar value of everything the factory threw away.

“That’s easy,” I answered, “I’ll just set the scrap goal to zero. The metric will show *all *the product we’re wasting.”

### What’s The Plan?

Your company generates huge volumes of transaction data from its business systems, like inventory, sales orders, and manufacturing activity. This operational data reflects the decisions made by your customers and vendors.

> What data represents the decisions of your company’s leadership?

Plan data, obviously. If you’re starting a brand-new company, it’s the only data you have. Plan data reflects the decisions leaders make about where to invest their company’s time and money. Ask your business leaders where they keep their plan data; you’ll probably find it in a spreadsheet, on their desktop.

I know that capturing this data in your data warehouse doesn’t sound as exciting as your next AI project, so I’ll try to spice it up for you by explaining how plan data behaves from a technical perspective. As I walk you through this, think about how it contrasts with all your other data sources.

To manage plan data well, consider its four characteristics:

**Source (where it originates)**. Plan data comes from business managers’ inputs, not from your business applications. You don’t need cutting-edge extraction, transformation, or loading tools for this. Simply create a structure for people in your company to submit their plan data.

- **Velocity (how fast it changes)**. Plan data changes *intermittently*. Like an outfielder in a baseball game, you might not get any action until the ninth inning, but when the ball comes to you, it will be the most critical play of the game. Similarly, plan data changes only now and then, when new news comes in. Sometimes it’s predictable – you know the date of the next corporate review – but other times the changes come out of the blue.

- **Retention (how much you need to save).** Point-in-time “snapshots” matter most for plan data. When fans tune into a baseball game, they usually don’t care about everything that happened during the game. They just want to see the highlights. Similarly, analysts focus mostly on comparisons to previous plan versions. Usually, the snapshots synchronize with the business review calendar.

- **Volume (how fast it grows).** Plan data grows in lumps. A single snapshot of plan data may not be large, but analysts want lots of snapshots for comparisons. They’re always answering questions about changes from the previous plan. So, whenever a new comparison point comes up, the entire dataset is copied (replicated). Plan data tends to pile up in chunks.

### Don’t Lose Control

Mr. Mori thought more like an entrepreneur than a corporate citizen. When I updated the plan data as he requested, the metrics showed we were wasting millions of dollars in inventory each quarter. He told me to send this chart to every member of his staff every week. Sure enough, this scorecard helped him drive a dramatic improvement in factory yields.

Even though he knew nothing about the technical side of managing data, Mr. Mori understood that targets are the only data an executive truly controls. If you don’t capture executive plan data in your data platform, business teams manage it offline and no longer look to your system as the source of truth. You lose control of the data.

Don’t lose control of plan data. Get to know your executives, learn how they think, and manage their data.

---

 ![](https://substackcdn.com/image/fetch/$s_!J2gz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d684362-3d11-457c-bacc-799a9d9be1fc_900x900.jpeg) To remind you of this week’s data concept, enjoy *[Making Plans for Nigel](https://open.spotify.com/track/1XT5kxg6Tk0ukCO2vBQN4v?si=7cd27012bd384e59), *by XTC, from the [Frictionless Data Spotify playlist](https://open.spotify.com/playlist/4PKCEghEMZ7MxCJMwlrnFV?si=b6X-1CP0RXmRNqqQs8AK8A)**.**

---

For the full story about making data flow faster and better, check out *Frictionless Data* on [Amazon](https://www.amazon.com/dp/1637428200?ref=cm_sw_r_ffobk_cp_ud_dp_X9E1MYZA0MX6ASKBVQQ1_1&ref_=cm_sw_r_ffobk_cp_ud_dp_X9E1MYZA0MX6ASKBVQQ1_1&social_share=cm_sw_r_ffobk_cp_ud_dp_X9E1MYZA0MX6ASKBVQQ1_1&bestFormat=true&previewDoh=1&previewDohDeal=1).

 ![](https://substackcdn.com/image/fetch/$s_!RFYI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc83074f5-ac33-4a97-97fc-608268c1c44b_347x522.jpeg)

---

---

Source: [Try Capturing Crowdsourced Data](https://zanehall.substack.com/p/try-capturing-crowdsourced-data)
