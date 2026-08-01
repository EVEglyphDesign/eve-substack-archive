---
title: "Never Use Reports to Manage Business Logic"
subtitle: "Bradenton, Florida, October 2024"
date: 2024-10-29
publication: "Frictionless Decisions"
author: "Zane Hall"
source_url: https://zanehall.substack.com/p/never-use-reports-to-manage-business
audience: everyone
wordcount: 565
reactions: 2
comments: 0
restacks: 0
ingested_by: EVEglyphDesign eve-substack-archive
---

# Never Use Reports to Manage Business Logic

*Bradenton, Florida, October 2024*

![](https://substackcdn.com/image/fetch/$s_!ca-z!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F50f6662a-53c1-4c20-8f69-d61931b1c5b9_5712x3579.jpeg) *(This is the third article in my series, “The 00001010 Commandments of Data”. You can read the [introduction to this series here](https://zanehall.substack.com/p/the-00001010-commandments-of-data?r=4chtg6).) *

[Subscribe now](https://zanehall.substack.com/subscribe?)

A few summers ago, I bought a “bear bell” that hung from my backpack and jingled everywhere I hiked. It gave me some confidence that I wouldn’t get attacked by a bear in the wilderness. Then, last summer, two different park rangers told me that the bear-bell isn’t just annoying to other hikers--which it is!--but it also sounds like a cow bell...and grizzly bears think cows are delicious. 

It’s like that with report writing. It might not get you killed, but like my bear bell, you’ll get into a lot more trouble than you expected if you use reports to manage business logic.

Any time you add code to a report that modifies, transforms, translates, interprets, or changes the data, you’ve added a layer of business logic. Never do this with reports. This might sound counterintuitive to you, if you’ve spent your entire career responding to questions by creating new reports, but if your company doesn’t change this behavior, you’ll end up with business logic in a thousand places. 

### Writing Reports or Asking Questions?

Recently, a finance executive wisely said to me, “Analytics is not about having the right data; it’s about asking the right questions.” 

He’s not looking for answers to predefined questions from reports**, **because that approach fundamentally misunderstands how data analysts work.** **Analysts don’t know the question until they see the data. They *explore *data, asking new questions with every click.

But many companies have thousands of reports in their systems. Where do all those reports come from?

They come from those very same analysts, who will keep asking for more and more reports if that’s the only option you give them. 

An analyst looks at a metric, and that leads to a “why” question. Time for a new report!** **But this leads to another question. Time for a new report!  One question leads to another, and sooner or later, the existing library of reports cannot answer the new questions. Time for a new report! 

It leads to a whole universe of single-use reports. 

### Move Logic Down

Think of your data solution like a sandwich, with source systems at the bottom, reports on top, and your data platform in the middle. 

 ![](https://substackcdn.com/image/fetch/$s_!wEDE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F19f250e8-b606-4a78-99c1-7da43bcce9aa_473x670.png) The purpose of the reporting layer (at the top) is to help people navigate and visualize data. The purpose of your data platform (in the middle) is to manage logic. 

Instead of building more reports, make data more accessible. Make it easy for hands-on data analysts to answer questions. Do this by moving business logic downward in your data architecture - into your data platform, below the reporting layer. The closer you move business logic to the source data, the more consistent and accessible the data becomes.

I’m not sure what led me to believe that I was smarter than every other hiker in the wilderness. Imagine if every hiker on the trail carried a bear bell; that much noise would ruin the experience for everyone and do nothing to scare off the bears. That’s what it sounds like at a company that manages decisions by creating more reports.

.[The 00001010 Commandments of Data](https://zanehall.substack.com/p/the-00001010-commandments-of-data?r=4chtg6)

[Previous post: Never Give Anyone Access to Raw Data](https://zanehall.substack.com/p/second-commandment-never-give-anyone?r=4chtg6)

Thanks for reading Frictionless Data! Subscribe for free to receive new posts and support my work.

---

Source: [Never Use Reports to Manage Business Logic](https://zanehall.substack.com/p/never-use-reports-to-manage-business)
