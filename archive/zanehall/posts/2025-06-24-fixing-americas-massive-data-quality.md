---
title: "Fixing America\u2019s Massive Data Quality Problem"
subtitle: "Case Study: Musk and Social Security Part 1"
date: 2025-06-24
publication: "Frictionless Decisions"
author: "Zane Hall"
source_url: https://zanehall.substack.com/p/fixing-americas-massive-data-quality
audience: everyone
wordcount: 869
reactions: 2
comments: 0
restacks: 1
ingested_by: EVEglyphDesign eve-substack-archive
---

# Fixing America’s Massive Data Quality Problem

*Case Study: Musk and Social Security Part 1*

![](https://substackcdn.com/image/fetch/$s_!VgfC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4946a47c-6654-4b32-801f-8a0a791ebbe4_4032x3024.jpeg) Florida Gulf Coast, June 2025*This article continues my Exception Reporting focus, which you can read [here](https://zanehall.substack.com/p/exception-reports-the-origin-story?r=4chtg6).*

---

On February 16, Elon Musk [showed a spreadsheet to the cameras](https://www.newsweek.com/elon-musk-major-social-security-warning-fraud-billion-week-lost-2029244) listing 18.9 million people over the age of 112 in the Social Security system. Then he tweeted, "Maybe Twilight is real and there are a lot of vampires collecting Social Security…[h]aving tens of millions of people marked in Social Security as “ALIVE” when they are definitely dead is a HUGE problem."

But those “vampires” weren’t collecting benefits. It was bad data.

The whole story – America’s most massive data quality problem – sounded all too familiar to people like me who struggle daily to keep data “clean” in their workplaces. Millions of Americans work in jobs that directly manage and analyze data. Sometimes, fixing data issues feels like playing Whack-A-Mole: new problems pop up faster than you can fix them.

But there is such a thing as good, clean data that helps a company make better decisions. We can’t fix bad data by sharing it on television, like Musk tried, and embarrass the people who manage it. I’ve tried using email to do that, and it didn’t work either.

People like us need better strategies.

When I started [writing about Exception Reports](https://zanehall.substack.com/p/exception-reports-the-origin-story?r=4chtg6) a few months ago, I didn’t expect a story like this to hit the news and provide such a great illustration for my solution to fixing bad data. But here we are and here we go. I hope the political context of this story doesn’t distract us from the core problem: we need good data. Wish me luck!

### Determining “Aliveness”

The social security fraud issue isn’t new.** **In 2014 (under the Obama Administration), the agency[created the Office of Anti-Fraud Program Management (OPAM)](https://www.ssa.gov/legislation/Anti-Fraud%20Initiatives%20Report%20FY2014.pdf) to address the problem. At that time, they estimated the SSA made $124 billion in improper payments annually, mainly from benefits paid to dead people. OPAM's efforts led the Social Security Administration (SSA) to implement a fix that prevented payments to anyone in the file over 112 years old.

But they didn't fix the underlying data problem.

The agency maintains a database called the Death Master File, which contains information about people's status (dead or alive). [That file updates the SSA's Numident (Numerical Identity) system](https://oig.ssa.gov/congressional-testimony/2015-03-17-newsroom-congressional-testimony-march16-hsgac/#:~:text=Federal%20agencies%20and%20their%20inspectors,eligibility%20before%20releasing%20Federal%20funds.), which assigns Social Security numbers to individuals. Right or wrong, this file is the government’s source of truth for “aliveness.”

Updates to the DMF file come from various sources, including family members who notify the Social Security Administration, funeral homes, financial institutions, and postal authorities.[1](#footnote-1) The problem isn't just the 18.9 million people over 112 years old labeled as "active"; it also includes some 20,000 living people marked as "dead." [And there's no process to reactivate them](https://www.npr.org/transcripts/622040779).

---

 ![](https://substackcdn.com/image/fetch/$s_!Iw-o!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1abccc21-f97b-4bbe-9e0e-c34c8695f3eb_2542x463.jpeg) [Buy now on Amazon](https://a.co/d/e7uApb1)

---

### Eternal Debates

Only a small fraction of the 18.9 million dead people missing from the DMF would have received benefits. Social Security executives said Musk had pulled his data from the wrong Numident table. Instead of fixing the data in the Numident system (or the DMF file), the SSA added logic to their payment system that compares it to the Treasury Department's "Do Not Pay" file.

IT people call this approach a "patch" or a "Band-Aid.”

They went on to explain that consultants told them it would cost $9 million to fix the issue permanently, so they decided on a different solution due to the high cost and the "limited benefit" of fixing the data at the source. As of 2023, [the SSA and the Inspector General continued to argue](https://oig.ssa.gov/assets/uploads/a-06-21-51022.pdf) about whether they should fix the source data.

### Fix Processes or Start Over?

Think about the risk workers take when changing a person’s status from alive to dead in the Social Security system. No process exists to bring them back to life. If you make a mistake, the victim can’t even own a bank account. That creates a huge disincentive for Social Security workers to update *anyone* to inactive status.

No wonder the SSA resists change so strongly.

Bad data always starts with a broken business process or, in this case, a completely missing process. If the SSA defined a secure way to bring people back to life in the system, data quality might naturally improve, and they might avoid that $9 million consulting fee to fix the issue.

Chief Information Officers (CIOs) hear stories similar to the Death Master File data issue all the time in their companies; the debates about fixing data seem to extend into eternity. After working through the code, Musk and DOGE finally decided it would be easier to recreate entire systems than to fix them. You might recognize that pattern: many large companies make the same decision when they acknowledge the fragility of their business systems. They replace the software altogether.

The SSA could have used [a good Exception Reporting system](https://zanehall.substack.com/p/exception-reports-the-power-of-a?r=4chtg6) long ago. If I’m lucky, maybe DOGE will take my advice and install that solution, but I’m not waiting for that. We can all rewrite this story in our own workplaces, using good data quality management to breathe new life into our companies and make it a cultural value. [Fix data at its source instead of writing more code](https://zanehall.substack.com/p/write-business-rules-not-code?r=4chtg6). Fix processes before firing the people. Make real, lasting fixes to the data.

[1](#footnote-anchor-1)*You can query the DMF database here: [SortedByName.com](http://sortedbyname.com). I checked the data for myself and some of my extended family, and fortunately, all the data was accurate.*

---

Source: [Fixing America’s Massive Data Quality Problem](https://zanehall.substack.com/p/fixing-americas-massive-data-quality)
