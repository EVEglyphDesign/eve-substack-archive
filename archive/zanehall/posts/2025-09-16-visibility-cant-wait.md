---
title: "Visibility Can\u2019t Wait"
subtitle: "Data Management Best Practices"
date: 2025-09-16
publication: "Frictionless Decisions"
author: "Zane Hall"
source_url: https://zanehall.substack.com/p/visibility-cant-wait
audience: everyone
wordcount: 650
reactions: 3
comments: 2
restacks: 1
ingested_by: EVEglyphDesign eve-substack-archive
---

# Visibility Can’t Wait

*Data Management Best Practices*

![](https://substackcdn.com/image/fetch/$s_!nXPt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F29abc490-9eeb-451b-a24e-7c10aeea6c8a_5712x4284.jpeg)
- San Clemente, California, September 2025

---

When my friend Yakov first used the term** **“data wrangling,” I assumed he’d just made it up. If anyone else had used that phrase, I’d assume that our company’s data was out of control, like the Wild West.

But data wrangling is [an official term among data scientists](https://www.geeksforgeeks.org/what-is-data-munging/). They use the term interchangeably with “mung”-ing (pronounced “m-uh-n-j”). It’s a word for a series of potentially destructive or irrevocable changes to a piece of data. It’s also an acronym: Mash Until No Good. The acronym evolved to mean “Mung Until No Good,” making MUNG one of the first known [recursive acronyms in the English language](https://web.archive.org/web/20050424050957/http://wombat.doc.ic.ac.uk/foldoc/foldoc.cgi?mung).[1](#footnote-1)

Most data science teams are forced to use uncontrolled and sometimes unstable data sources. However, much of the data Yakov’s team used came from our data warehouse, which they appreciated because it allowed them to go straight to advanced analytics, no data wrangling or munging required. I’m sure even cowboys preferred cattle herds that moved in the right direction without wrangling.

Amazingly, software vendors don’t seem to see the big picture: data wrangling is usually a necessary evil. They [develop tools for self-service](https://www.alteryx.com/glossary/data-wrangling#:~:text=Data%20wrangling%20is%20the%20process,solutions%2C%20decisions%2C%20and%20outcomes.) data wrangling (a redundant term), define its steps, and create online courses to teach people how to use their munging software. However, there’s nothing new about collecting and preparing data for analysis; old-school data engineers refer to this process as “extract, transform, and load” (ETL).

That’s the difference: [data wranglers get the job done, right now](https://businessanalytics.substack.com/p/data-wrangling-a-to-z?r=4chtg6&utm_medium=ios&triedRedirect=true), without waiting for long approval cycles and testing. IT data engineering teams, on the other hand, set up programs that prepare data in the most failproof, high-scale way possible.

### Time to Visibility

What does this funny name for a common IT data task prove?

> Data scientists understand this simple truth: decision-makers need to know what’s happening in the business right now. They work with urgency, doing whatever it takes to answer questions (with data) because the business demands it, even if that requires wrangling and munging.

Yakov drew a diagram on my whiteboard once that illustrated this urgency. He called it “Time to Visibility.” Visibility describes how effectively a company measures its business activities. Good visibility means people can view the data from any perspective, at any level of detail, with any unit of measure, for the longest time horizon, past, present, and future.

The horizontal X-axis on Yakov’s chart (below) represents time. The vertical Y-axis measures the degree to which people in your company can “see” what’s happening in the business.

 ![](https://substackcdn.com/image/fetch/$s_!T_Pc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6cbf68e7-ffd4-4aa9-b5dc-fb2b26fd934a_904x456.png) Every executive should understand two critical implications of Yakov’s chart:

**Lack of business visibility costs money.** Your company may be years away from consolidating all its data into a single business system. You should do everything possible to make the data appear connected as soon as possible. Every day that decision-makers don’t have the visibility they need costs your company.

- **Business systems shouldn’t determine your data architecture.** People think that good data architecture depends on understanding the layout of their business systems. That’s false. Build your data architecture to align with the decisions people make in your industry.

### When Everyone Becomes a Wrangler

How much visibility does your company need? How long can people wait for it?

Just asking these questions explains why data scientists aren’t the only data wranglers in your company. Everyone becomes a wrangler when the data they need isn’t easily accessible.

That’s where a good data team makes all the difference. They have the technical skills (and tools) to make business data fit together perfectly, even if the data in your business systems looks nothing like that. They can make your data look like it should, in its end state. I call that “thought architecture” – shaping the way the business thinks, with data.[2](#footnote-2) An enterprise business system delivers far more value when its data aligns with your company’s thought architecture.

Until that happens, you might need to wrangle some data.

[1](#footnote-anchor-1)Dating recursive acronyms is an imprecise task, since many of them start out as “backronyms”, which are words that start as an acronym before they become a phrase. Homer Simpson invented the second recursive acronym when he defined grunge rock as “[Guitar Rock Utilizing Nihilist GRUNGE Energy](https://www.youtube.com/watch?v=Rjmzf3IETdM).”

[2](#footnote-anchor-2)AI “ontologists” use a similar concept known as “knowledge management,” something I’ll discuss more in future posts.

---

To help remind you of these concepts, I’m now adding a hit 80s song to the [Frictionless Data Spotify playlist](https://open.spotify.com/playlist/4PKCEghEMZ7MxCJMwlrnFV?si=b6X-1CP0RXmRNqqQs8AK8A) each week. This week, enjoy *[See The Lights](https://open.spotify.com/track/7EUzbGgfQWeNN5qoTor9At)*[by Simple Minds](https://open.spotify.com/track/7EUzbGgfQWeNN5qoTor9At).

---

Source: [Visibility Can’t Wait](https://zanehall.substack.com/p/visibility-cant-wait)
