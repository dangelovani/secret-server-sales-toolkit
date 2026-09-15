# -*- coding: utf-8 -*-
"""Outreach messages for TSS Investor Database - Wave 1.
Three tone options per investor type/section: formal, conversational, bold.
Merge fields [First Name] / [Firm] to be personalised before sending.
UK spelling used throughout (UK/EU expansion focus).
"""

MESSAGES = {
  "hospitality": {
    "formal": (
      "Dear [First Name],\n\n"
      "I am writing to introduce The Secret Server, the first patented 3D augmented-reality menu and "
      "staff-training platform built specifically for hospitality. Our technology lets guests view menu "
      "items in photoreal 3D at the table while giving operators a powerful onboarding and training tool for "
      "front-of-house teams \u2014 all through a single, GDPR-compliant platform.\n\n"
      "Given [Firm]'s deep focus on foodservice and hospitality, I believe there is strong strategic alignment. "
      "We are raising our first institutional round (positioned as seed / Series A) to accelerate a live UK and "
      "European partnership and expand multi-unit rollouts.\n\n"
      "Might I share our deck and arrange a brief introductory call?\n\n"
      "With kind regards,\nChristie Lawler\nCEO & Co-Founder, The Secret Server\n"
      "832.637.6355 \u00b7 hello@thesecretserver.co \u00b7 thesecretserver.co"
    ),
    "conversational": (
      "Hi [First Name],\n\n"
      "I lead The Secret Server \u2014 we\u2019ve built the first patented 3D AR menu and staff-training platform "
      "made just for hospitality. Guests explore dishes in true-to-life 3D at the table, and operators get a "
      "built-in training and onboarding tool for their teams, with GDPR-compliant analytics behind it.\n\n"
      "I\u2019ve been following [Firm]\u2019s work across restaurants and hospitality, and it feels like a natural fit. "
      "We\u2019re opening our first round to fuel a live UK/EU partnership and more multi-unit rollouts.\n\n"
      "Would you be open to a quick call? Happy to send the deck across first.\n\n"
      "Best,\nChristie Lawler \u00b7 CEO & Co-Founder, The Secret Server\n832.637.6355 \u00b7 thesecretserver.co"
    ),
    "bold": (
      "Hi [First Name],\n\n"
      "Restaurants still hand guests a flat paper menu and throw new hires into the deep end. We fix both. "
      "The Secret Server is the first patented 3D AR menu and staff-training platform \u2014 guests see every "
      "dish in photoreal 3D, and operators cut training time with the same tool.\n\n"
      "[Firm] backs the companies redefining hospitality, and we\u2019re next. We\u2019re raising now to scale a live "
      "UK/EU partnership. I\u2019d love 15 minutes to show you why this becomes the new standard.\n\n"
      "Christie Lawler \u00b7 CEO & Co-Founder, The Secret Server\n832.637.6355 \u00b7 thesecretserver.co"
    ),
  },
  "arvr": {
    "formal": (
      "Dear [First Name],\n\n"
      "I am the founder of The Secret Server, the first patented 3D augmented-reality menu and staff-training "
      "platform for hospitality. We deliver photoreal, spatially accurate 3D experiences on standard consumer "
      "devices \u2014 no app friction \u2014 with a clear enterprise use case and recurring revenue model.\n\n"
      "Given [Firm]\u2019s focus on augmented reality and spatial computing, I thought our patented AR technology and "
      "real-world commercial traction would be of interest. We are raising our first institutional round to scale "
      "a live UK and European partnership.\n\n"
      "May I share our deck and a short technical overview?\n\n"
      "With kind regards,\nChristie Lawler\nCEO & Co-Founder, The Secret Server\n"
      "832.637.6355 \u00b7 hello@thesecretserver.co \u00b7 thesecretserver.co"
    ),
    "conversational": (
      "Hi [First Name],\n\n"
      "I\u2019m the founder of The Secret Server \u2014 we\u2019ve turned AR into a real, revenue-generating product for "
      "hospitality: a patented 3D augmented-reality menu and staff-training platform that runs on the devices "
      "people already carry.\n\n"
      "Since [Firm] invests at the frontier of AR and spatial computing, I\u2019d love to show you what genuine "
      "commercial AR traction looks like. We\u2019re raising our first round to scale a live UK/EU partnership.\n\n"
      "Open to a quick call? I\u2019ll send the deck ahead of time.\n\n"
      "Best,\nChristie Lawler \u00b7 CEO & Co-Founder, The Secret Server\n832.637.6355 \u00b7 thesecretserver.co"
    ),
    "bold": (
      "Hi [First Name],\n\n"
      "Most AR startups are still chasing a use case. We already have one that pays. The Secret Server is the "
      "first patented 3D AR menu and staff-training platform \u2014 real customers, recurring revenue, no headset "
      "required.\n\n"
      "[Firm] backs immersive tech before it\u2019s obvious, and this is that moment. We\u2019re raising to scale a live "
      "UK/EU partnership. Give me 15 minutes and I\u2019ll show you AR with a business model.\n\n"
      "Christie Lawler \u00b7 CEO & Co-Founder, The Secret Server\n832.637.6355 \u00b7 thesecretserver.co"
    ),
  },
  "saas": {
    "formal": (
      "Dear [First Name],\n\n"
      "I am writing to introduce The Secret Server, a patented B2B platform for hospitality that combines a 3D "
      "augmented-reality menu with staff training and onboarding. We operate a multi-location subscription model "
      "with GDPR-compliant analytics, delivering measurable value across guest engagement and workforce "
      "efficiency.\n\n"
      "Given [Firm]\u2019s focus on enterprise SaaS and vertical software, I believe our recurring-revenue model and "
      "expanding pipeline would be of interest. We are raising our first institutional round to accelerate a live "
      "UK and European partnership.\n\n"
      "Might I share our deck and key metrics?\n\n"
      "With kind regards,\nChristie Lawler\nCEO & Co-Founder, The Secret Server\n"
      "832.637.6355 \u00b7 hello@thesecretserver.co \u00b7 thesecretserver.co"
    ),
    "conversational": (
      "Hi [First Name],\n\n"
      "I lead The Secret Server \u2014 think vertical SaaS for hospitality, with a twist. We pair a patented 3D AR "
      "menu with staff training in one platform, sold on a multi-location subscription with GDPR-compliant "
      "analytics baked in.\n\n"
      "Given [Firm]\u2019s track record in enterprise SaaS, I\u2019d love to walk you through our recurring-revenue model and "
      "pipeline. We\u2019re raising our first round to scale a live UK/EU partnership.\n\n"
      "Would a short call work? I\u2019ll send the deck first.\n\n"
      "Best,\nChristie Lawler \u00b7 CEO & Co-Founder, The Secret Server\n832.637.6355 \u00b7 thesecretserver.co"
    ),
    "bold": (
      "Hi [First Name],\n\n"
      "Hospitality is one of the largest under-digitised verticals left \u2014 and we own a patented wedge into it. "
      "The Secret Server is a 3D AR menu and staff-training platform sold as multi-location SaaS, with the "
      "analytics to prove ROI.\n\n"
      "[Firm] knows a category-defining SaaS play when it sees one. We\u2019re raising to scale a live UK/EU "
      "partnership. Fifteen minutes and I\u2019ll show you the numbers.\n\n"
      "Christie Lawler \u00b7 CEO & Co-Founder, The Secret Server\n832.637.6355 \u00b7 thesecretserver.co"
    ),
  },
  "edtech": {
    "formal": (
      "Dear [First Name],\n\n"
      "I am the founder of The Secret Server, a patented hospitality platform whose 3D augmented-reality menu is "
      "paired with a powerful staff-training and onboarding capability. Hospitality suffers from high turnover and "
      "costly, inconsistent training; our tool shortens time-to-competence and standardises the guest-facing "
      "experience.\n\n"
      "Given [Firm]\u2019s focus on learning, upskilling and the future of work, I believe our workforce-training "
      "application would resonate. We are raising our first institutional round to scale a live UK and European "
      "partnership.\n\n"
      "May I share our deck and training outcomes?\n\n"
      "With kind regards,\nChristie Lawler\nCEO & Co-Founder, The Secret Server\n"
      "832.637.6355 \u00b7 hello@thesecretserver.co \u00b7 thesecretserver.co"
    ),
    "conversational": (
      "Hi [First Name],\n\n"
      "I\u2019m the founder of The Secret Server. Alongside our patented 3D AR menu, we\u2019ve built a staff-training and "
      "onboarding tool that tackles hospitality\u2019s biggest pain: constant turnover and slow, uneven training.\n\n"
      "Since [Firm] invests in learning and the future of work, I\u2019d love to show you how we cut time-to-competence "
      "for front-line teams. We\u2019re raising our first round to scale a live UK/EU partnership.\n\n"
      "Up for a quick call? Deck incoming if so.\n\n"
      "Best,\nChristie Lawler \u00b7 CEO & Co-Founder, The Secret Server\n832.637.6355 \u00b7 thesecretserver.co"
    ),
    "bold": (
      "Hi [First Name],\n\n"
      "Hospitality burns billions on training people who quit within months. We turn that on its head. The "
      "Secret Server trains and onboards staff through the same patented AR platform guests love \u2014 faster ramp, "
      "consistent service, measurable results.\n\n"
      "[Firm] backs the future of work, and front-line workforces are the biggest untapped piece of it. We\u2019re "
      "raising to scale a live UK/EU partnership. Give me 15 minutes.\n\n"
      "Christie Lawler \u00b7 CEO & Co-Founder, The Secret Server\n832.637.6355 \u00b7 thesecretserver.co"
    ),
  },
  "angels": {
    "formal": (
      "Dear [First Name],\n\n"
      "I am writing to introduce The Secret Server, the first patented 3D augmented-reality menu and "
      "staff-training platform for hospitality. Founded by a hospitality operator with over 30 years\u2019 experience, "
      "we address two costly problems at once \u2014 guest engagement and staff training \u2014 through a single, "
      "GDPR-compliant platform.\n\n"
      "We are raising our first round (seed, positioned as Series A) and welcoming angel participation to "
      "accelerate a live UK and European partnership. I would be glad to share our deck and discuss how members of "
      "[Firm] might take part.\n\n"
      "With kind regards,\nChristie Lawler\nCEO & Co-Founder, The Secret Server\n"
      "832.637.6355 \u00b7 hello@thesecretserver.co \u00b7 thesecretserver.co"
    ),
    "conversational": (
      "Hi [First Name],\n\n"
      "I\u2019m the founder of The Secret Server \u2014 the first patented 3D AR menu and staff-training platform for "
      "hospitality. I\u2019ve spent 30+ years in the industry, and we solve two expensive problems in one platform: "
      "engaging guests and training staff.\n\n"
      "We\u2019re raising our first round and would love angels from [Firm] involved as we scale a live UK/EU "
      "partnership. Could I send the deck and set up a short call?\n\n"
      "Best,\nChristie Lawler \u00b7 CEO & Co-Founder, The Secret Server\n832.637.6355 \u00b7 thesecretserver.co"
    ),
    "bold": (
      "Hi [First Name],\n\n"
      "Early-stage bets on category creators are how the best returns happen \u2014 and this is one. The Secret Server "
      "is the first patented 3D AR menu and staff-training platform for hospitality, built by a 30-year industry "
      "operator who knows exactly where the money leaks.\n\n"
      "We\u2019re raising our first round and inviting sharp angels from [Firm] in early, before our UK/EU rollout "
      "scales. Want the deck and 15 minutes?\n\n"
      "Christie Lawler \u00b7 CEO & Co-Founder, The Secret Server\n832.637.6355 \u00b7 thesecretserver.co"
    ),
  },
  "corporate": {
    "formal": (
      "Dear [First Name],\n\n"
      "I am writing on behalf of The Secret Server, the first patented 3D augmented-reality menu and "
      "staff-training platform for hospitality. Beyond capital, we see a clear strategic fit with [Firm] \u2014 both as "
      "an investment and as a distribution or pilot partner across your hospitality and foodservice footprint.\n\n"
      "We are raising our first institutional round to accelerate a live UK and European partnership, and would "
      "welcome a conversation about strategic collaboration. Might I share our deck and a proposed pilot outline?\n\n"
      "With kind regards,\nChristie Lawler\nCEO & Co-Founder, The Secret Server\n"
      "832.637.6355 \u00b7 hello@thesecretserver.co \u00b7 thesecretserver.co"
    ),
    "conversational": (
      "Hi [First Name],\n\n"
      "I lead The Secret Server \u2014 a patented 3D AR menu and staff-training platform for hospitality. With [Firm], "
      "I see two ways to work together: as an investor in our first round, and as a strategic partner who could "
      "pilot or distribute the platform across your network.\n\n"
      "We\u2019re raising to scale a live UK/EU partnership. Could we find time to explore both angles? I\u2019ll send the "
      "deck and a short pilot idea ahead.\n\n"
      "Best,\nChristie Lawler \u00b7 CEO & Co-Founder, The Secret Server\n832.637.6355 \u00b7 thesecretserver.co"
    ),
    "bold": (
      "Hi [First Name],\n\n"
      "The operators who adopt AR-driven guest engagement and staff training first will pull ahead \u2014 and [Firm] "
      "is positioned to lead. The Secret Server is the first patented platform that does both, ready to pilot "
      "across your footprint.\n\n"
      "We\u2019re raising our first round and looking for strategic partners, not just cheques. Let\u2019s talk about "
      "investment and a pilot in one conversation \u2014 15 minutes?\n\n"
      "Christie Lawler \u00b7 CEO & Co-Founder, The Secret Server\n832.637.6355 \u00b7 thesecretserver.co"
    ),
  },
  "growth": {
    "formal": (
      "Dear [First Name],\n\n"
      "I am writing to introduce The Secret Server, the first patented 3D augmented-reality menu and "
      "staff-training platform for hospitality. We are an experience-led, recurring-revenue business at the "
      "intersection of consumer engagement and enterprise efficiency, with a live UK and European partnership now "
      "underway.\n\n"
      "While our current round is our first, I am building relationships with growth and consumer-focused "
      "investors such as [Firm] ahead of subsequent expansion capital. I would welcome the opportunity to share "
      "our deck and trajectory.\n\n"
      "With kind regards,\nChristie Lawler\nCEO & Co-Founder, The Secret Server\n"
      "832.637.6355 \u00b7 hello@thesecretserver.co \u00b7 thesecretserver.co"
    ),
    "conversational": (
      "Hi [First Name],\n\n"
      "I lead The Secret Server \u2014 a patented 3D AR menu and staff-training platform that sits right where "
      "experience-led consumer meets enterprise SaaS. We\u2019ve got a live UK/EU partnership underway and strong "
      "recurring-revenue momentum.\n\n"
      "We\u2019re closing our first round now, and I\u2019d love to get on [Firm]\u2019s radar ahead of our growth stage. Could I "
      "share the deck and set up an intro call?\n\n"
      "Best,\nChristie Lawler \u00b7 CEO & Co-Founder, The Secret Server\n832.637.6355 \u00b7 thesecretserver.co"
    ),
    "bold": (
      "Hi [First Name],\n\n"
      "The next iconic hospitality brand won\u2019t be a restaurant \u2014 it\u2019ll be the platform every restaurant runs on. "
      "The Secret Server is building it: patented 3D AR menus plus staff training, recurring revenue, live UK/EU "
      "expansion.\n\n"
      "[Firm] backs category winners as they break out. We\u2019re closing our first round now and lining up growth "
      "partners for what\u2019s next. Worth 15 minutes?\n\n"
      "Christie Lawler \u00b7 CEO & Co-Founder, The Secret Server\n832.637.6355 \u00b7 thesecretserver.co"
    ),
  },
}
