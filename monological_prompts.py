"""
This file includes all the prompts that will be used in the monological avenue of the data generation process.
"""

official_letter_prompts = [
    # From the perspective of an employee
    "As an employee, write an official letter to HR about your burnout.",
    "As an employee, write an official letter to HR about your occupational stress.",
    "As an employee, write an official letter to HR about your fear of burnout.",
    "As an employee, write an official letter to HR about your concerns of burnout.",

    # From the perspective of HR
    "As HR, write an official letter to an employee who is experiencing burnout.",
    "As HR, write an official letter to an employee who is experiencing occupational stress.",
    "As HR, write an official letter to an employee who is at risk of burnout.",
    "As HR, write an official letter to an employee who is showing signs of burnout.",
]

policy_documents = [
    # Company
    "As company, write an official policy on burnout.",
    "As company, write an official policy on occupational stress.",
    "As company, write an official policy on preventing burnout.",
    "As company, write an official policy on leave with burnout.",

    # Governmental angencies
    "As the ministry of public health, write a report on the prevalence of burnout in different professions and industries.",
    "As an NGO, write an official burnout policy proposal to the ministry of public health.",
    
    # Medical professionals
    "Write an official guide for medical professionals to diagnose burnout."
    "Write an official guide for medical professionals to treat burnout."
    "Write an official guide for medical professionals to prevent burnout."

    # Medical Insurance companies
    "As a health insurance company, write an official policy on burnout as an insured condition.",
    "As a health insurance company, write an official policy on burnout as an uninsured condition.",

    # Medical Educational institutions
    "Write a chapter of a medical textbook on burnout."

]

academic_prompts = [
    # Research
    "As a researcher, write an abstract for a research paper on burnout.",
    "As a researcher, write an introduction for a research paper on burnout.",
    "As a researcher, write a discussion for a research paper on burnout.",
]

story_telling_prompts = [
    # Storytelling
    "Write a poem about burnout.",
    "Write a short story about burnout.",
    "Write a journal entry on burnout.",

    # Blogging
    "As a medical professional, write a blog post about your experience with burnout.",
    "As an HR professional, write a blog post about your experience with burnout.",
    "As a company, write a blog post about your experience with burnout.",
    "As a person with a burnout diagnosis, write a blog post about your experience with burnout.",

]

mediatic_representation_prompts = [
    # Mediatic depictions
    "Write a script for a documentary about burnout.",
    "Write a script for a podcast about burnout.",
    "Write a script for a movie about burnout.",
    "Write a pamphlet about burnout.",
    "Write a brochure about burnout.",
]

quotes_prompts = [
    # Quotes
    "Give 10 quotes about burnout.",
    "Give 10 quotes that inspire overcoming burnout.",
    "Give 10 quotes that motivate preventing burnout.",
    "Give 10 quotes that help understand burnout.",
]

social_media_prompts = [
    # Instagram
    "Write an Instagram caption for a post about burnout.",
    "Write an Instagram caption for a post about having burnout.",
    "Write an Instagram caption for a post about burnout diagnosis.",
    "Write an Instagram caption for a post about burnout prevention.",
    "Write an Instagram caption for a post about firing someone with burnout.",

    # LinkedIn
    "Write a LinkedIn post about burnout.",
    "Write a LinkedIn post about having burnout.",
    "Write a LinkedIn post about burnout diagnosis.",
    "Write a LinkedIn post about burnout prevention.",
    "Write a LinkedIn post about firing someone with burnout.",

    # Twitter
    "Write a Twitter post about burnout.",
    "Write a Twitter post about having burnout.",
    "Write a Twitter post about burnout diagnosis.",
    "Write a Twitter post about burnout prevention.",
    "Write a Twitter post about firing someone with burnout.",
]

grammatical_prompts = [
    # Literary devices
    "Give 10 metaphors for burnout.",
    "Give 10 similes for burnout.",
    "Give 10 hyperboles for burnout.",
    "Give 10 oxymorons for burnout.",

    # Synonyms and antonyms
    "Give 10 synonyms for burnout.",
    "Give 10 antonyms for burnout.",
]

definition_prompts = [
    # Word association
    "With the word association game, I say 'burnout', you say...",
    "Give me 10 words that are associated with burnout.",
    "Give me 10 words that are not associated with burnout.",
    "What are the 10 most important words related to burnout?",

    # Definitions
    "Define burnout.",
    "Define burnout in your own words.",
    "What is burnout?",
    "What does burnout mean?",
    "Give me a formal definition of burnout",
    "Compare and contrast burnout with stress.",
    "Compare and contrast burnout with anxiety.",
    "Compare and contrast burnout with depression.",

    # Characteristics
    "Develop a profile for someone who is prone to having a burnout.",
    "Give me 10 characteristics of someone who is experiencing burnout.",
]


monological_prompts = official_letter_prompts\
                    + policy_documents\
                    + academic_prompts\
                    + story_telling_prompts\
                    + mediatic_representation_prompts\
                    + quotes_prompts\
                    + social_media_prompts\
                    + grammatical_prompts\
                    + definition_prompts