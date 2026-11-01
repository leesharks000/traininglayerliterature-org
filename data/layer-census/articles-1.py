ARTICLES = {
"olmotrace": {"non_row": "olmotrace",
 "kernel": "OLMoTrace is a tracing tool made at the Allen Institute for AI that finds verbatim matches between spans of a language model's output and documents in that model's full training corpus, introduced on 9 April 2025 as a feature of the Ai2 Playground.",
 "kernel_ko": [1, 2, 3],
 "sections": [
  ("What it is", [
   "OLMoTrace attaches to a span of model output the training documents that contain it verbatim. It highlights long and unique spans found at least once in the training data and retrieves up to 10 enclosing snippets for each, ranked by BM25. For OLMo-2-32B-Instruct the index covers 3.2 billion documents and 4.6 trillion tokens across pre-, mid- and post-training.",
   "It served OLMo 2 32B and 13B Instruct and OLMoE 1B 7B Instruct at launch and can be applied to any model whose full training data the provider holds. Its core is under the Apache 2.0 license, and the paper appeared in ACL 2025's System Demonstrations with the Best Demo award."]),
  ("What a match does not mean", [
   "Its authors state the limit in both versions of the paper: the retrieved documents \"should not be interpreted as having a causal effect on the LM output, or as supporting evidence or citations for the LM output\". Ai2's post makes confidence in a generated fact conditional on the user's own check that the documents come from trusted sources."]),
  ("Place in the field", [
   "The archive places the tool's class on the training/output relation: data attribution asks which training examples shaped a specific output, while PER operates on the output/reader relation. Of that class it holds that partial tracing is possible at cost and does not recover authorship.",
   "At its own name on Google's AI Overview on 2026-10-29, the composition gave fact-checking as the tool's first use, and the Capture Registry reads this as the conversion of a matching relation into a citation relation that the paper names and refuses."])],
 "ko": [[[1, 3, 6, 5], [8, 24, 25]], [[17, 16]], [[11, 12], [21, 22]]]},

"common-crawl": {"non_row": "common-crawl",
 "kernel": "Common Crawl is a free, open repository of web crawl data maintained by the Common Crawl Foundation, a 501(c)(3) non-profit founded by Gil Elbaz in 2007, published as monthly numbered crawls and, typically after filtering by others, a primary training source for many large language models.",
 "kernel_ko": [1, 4, 11, 20],
 "sections": [
  ("What it is", [
   "The foundation crawls the web with CCBot, a crawler built on Apache Nutch, and publishes each crawl in three formats: WARC, the full HTTP responses; WAT, metadata extracted from them; and WET, plain text. Its home page counts over 300 billion pages, with 3 to 5 billion new pages a month, and the data are stored free on Amazon Web Services under its Open Data Sponsorship Program.",
   "It was funded almost exclusively by the Elbaz Family Foundation Trust until 2023, and from 2023 also by AI companies, among them Anthropic and OpenAI, which gave $250,000 each."]),
  ("In the training layer", [
   "Its own About page dates its central role in AI development from Google's C4, built from a single snapshot to train T5 in 2019, and from the GPT-3 paper of 2020. A Mozilla Foundation study of 2024 found that at least 64% of 47 models published between 2019 and 2023 were trained on filtered versions of it. Others refine the raw crawl into datasets such as C4, Pile-CC, RefinedWeb, FineWeb and DCLM.",
   "No author or attribution field is recorded: a page is held by URL, and a work's name survives there only as far as it is written into the page itself."]),
  ("Opt-out and its limit", [
   "The foundation states that CCBot obeys robots.txt and rate-limits its requests. By 2025 CCBot was the most widely blocked bot among the top 1000 websites, and in November 2025 The Atlantic reported that the foundation misled publishers when it claimed to respect paywalls and to honor their requests to have content removed. The census records that crawl inclusion and demonstrated training use are separate claims, and that this finding marks the limit of the URL Index as a witness of training membership."])],
 "ko": [[[8, 12, 14, 16], [6]], [[19, 20, 27], [45]], [[37, 38, 39, 41]]]},
}
ARTICLES.update({
"project-gutenberg": {"non_row": "project-gutenberg",
 "kernel": "Project Gutenberg is an online library of free eBooks and the oldest digital library, founded by Michael S. Hart in 1971 and operated by the Project Gutenberg Literary Archive Foundation: volunteer-made digital texts of works in the public domain in the United States.",
 "kernel_ko": [1, 7, 20],
 "sections": [
  ("What it is", [
   "Most of what it holds are full texts of books or stories in the public domain under United States copyright law, with a focus on older works; its unit is the eBook, a digitized and proofread text with its own permanent landing page. Hart began in 1971 by digitizing the Declaration of Independence. Counts differ by date and source: 79,709 free eBooks on the home page as read on 1 November 2026, more than 75,000 on its about page.",
   "The Project Gutenberg Literary Archive Foundation, a 501(c)(3) corporation chartered in Mississippi in 2000, operates it; ibiblio at the University of North Carolina at Chapel Hill hosts it."]),
  ("How its texts are made", [
   "Volunteers digitize and proofread its books, and no selection policy governs what is added. Distributed Proofreaders, founded by Charles Franks in 2000, is now the main source of new eBooks. In December 1994 the Text Encoding Initiative criticized the project for not documenting which of several versions had been digitized, and the census records it as no scholarly edition, unable to say which edition a text was made from.",
   "The archive's own seatings identify the edition behind a Gutenberg text from the text itself, from its title page and header."]),
  ("Place in the field", [
   "The archive counts Gutenberg's texts the most widely used public-domain corpus in digital humanities and holds that \"Gutenberg is doing correct work at its layer\". Its website was inaccessible in Germany from 2018 to 2021 under a court order, and it has been blocked in Italy since May 2020."])],
 "ko": [[[2, 5, 9], [7, 8]], [[11, 12, 13, 15], [16]], [[18, 21]]]},

"internet-archive": {"non_row": "internet-archive",
 "kernel": "The Internet Archive is an American non-profit library, founded in 1996 by Brewster Kahle and headquartered in San Francisco, that runs archive.org and its web archive, the Wayback Machine, with the mission of \"universal access to all knowledge\".",
 "kernel_ko": [1, 3, 4],
 "sections": [
  ("What it is", [
   "Its unit is the item, a container of files with metadata, gathered by staff into collections; in the Wayback Machine the unit is a capture of a web page by URL and date. The bulk of its data is collected by its web crawlers. The Wayback Machine opened to the public in 2001, and in October 2025 the Archive announced one trillion archived webpages.",
   "It also runs one of the world's largest book digitization efforts, from its own scanning and from others: more than 300,000 books from Microsoft and public domain books uploaded from Google Book Search. By 2025 its text collection exceeded 47,000,000 texts."]),
  ("Readback", [
   "The census reads it as persistence infrastructure: the Wayback Machine lets a page's presence be checked by URL and date long after it changed or vanished, which makes transmission on the open web inspectable after the fact. It tests no training set or model.",
   "Its coverage has limits of its own making: pages may fail to be archived because of robots.txt exclusions or owner requests, and in January 2023 it removed a BBC documentary on a request under the Digital Millennium Copyright Act."])],
 "ko": [[[5, 6, 8], [20, 21, 22]], [[13, 15], [16, 18]]]},

"hathitrust": {"non_row": "hathitrust",
 "kernel": "The HathiTrust Digital Library is a large-scale collaborative repository of digital content from research libraries, administered by the University of Michigan and founded in October 2008, holding more than 18 million volumes digitized through Google Books, the Internet Archive and its members.",
 "kernel_ko": [1, 2, 3, 5],
 "sections": [
  ("What it is", [
   "Its collection is of books, journals and government documents dated from 1500 to the present. In September 2024 it held more than 18 million volumes, 6.7 million of them in the public domain in the United States. It is a nonprofit collaborative of more than 219 research libraries under shared governance, and its executive director is Mike Furlough."]),
  ("Access and search", [
   "What a reader may see follows copyright and place. Public-domain items are fully available; works in copyright carry a \"Limited (search-only)\" status, searchable for key terms with their pages closed. The sources date the foreign line differently: Wikipedia quotes the policy with 1896, and the University of Michigan's guide quotes HathiTrust's site with 1898.",
   "In Authors Guild v. HathiTrust a federal court found the library's use of books scanned by Google to be fair use in October 2012, and the Second Circuit largely affirmed on 10 June 2014. The census reads the case as the precedent for a machine reading of whole books whose product is a finding, search, while the pages stay closed."]),
  ("The Research Center", [
   "Computational analysis was the separate service of the HathiTrust Research Center, established in 2011. Its services were discontinued on 30 September 2026, and access to the Digital Library remains open."])],
 "ko": [[[2, 3, 6, 7]], [[9, 11, 16], [18, 19, 20]], [[21, 22]]]},

"htrc": {"non_row": "htrc",
 "kernel": "The HathiTrust Research Center (HTRC), with its portal HTRC Analytics, was a research center for computational analysis of the HathiTrust Digital Library, established in 2011 by Indiana University, the University of Illinois Urbana-Champaign and HathiTrust; its services ended on 30 September 2026.",
 "kernel_ko": [1, 3, 32],
 "sections": [
  ("What it is", [
   "Its object is the Digital Library taken as a corpus for text and data mining; its unit is the workset, a user-built collection of volumes, together with the datasets derived from volumes. It works under a non-consumptive research paradigm, within the fair-use rights courts have recognized for text analysis, and its policy requires that released data be minimal and unable to be easily reconstructed into the raw volume."]),
  ("What the reading made", [
   "Its derived datasets outlast the service. The Extracted Features dataset, version 2.0, holds page-level features for 17,123,746 volumes, 6,221,631,336 pages and 2,906,819,723,689 tokens, under a Creative Commons Attribution 4.0 licence and cited with its makers' names and a DOI. The BookNLP dataset represents 201,527 volumes of English-language fiction.",
   "The archive reads the center as an earlier receiving apparatus with its product on record: whole library volumes read by computers for scholars, and what that reading made published as derived datasets."]),
  ("The closing", [
   "In October 2024 HathiTrust announced that funding for the center would cease at the end of 2026. After 2026 the HTRC team plans to continue its own research in text-data mining, cultural analytics and non-consumptive methods, and looks to new partners."])],
 "ko": [[[2, 7, 8]], [[14, 15, 17], [22]], [[30, 37]]]},
})
ARTICLES.update({
"the-pile": {"non_row": "the-pile",
 "kernel": "The Pile is an open-source dataset of English text that EleutherAI assembled to train large language models, twenty-two smaller datasets combined into one, released on 31 December 2020.",
 "kernel_ko": [1],
 "sections": [
  ("What it is", [
   "Its paper, by Leo Gao, Stella Biderman and ten others, presents it as a training dataset and as a broad-coverage benchmark. Its size is given three ways: 800GB in the paper's title, 825 GiB on its home page and 886.03 GB in Wikipedia's table of components. Its components include Pile-CC, its own extraction from Common Crawl, Books3, a dataset of books derived from a copy of the contents of the Bibliotik private tracker, and PG-19, Project Gutenberg books from before 1919."]),
  ("What a model trained on it makes", [
   "It is also a benchmark, Pile BPB, bits per UTF-8 encoded byte. EleutherAI described GPT-Neo, released early in 2021, as the first LLM trained on data its creators had published, and GPT-J was trained on it as well. As of 2024 it was, with Common Crawl, one of the two main training datasets used to train AI models.",
   "The archive holds that what a benchmark measures is determined by the training corpus, and what the corpus contains by the political economy of dataset construction."])],
 "ko": [[[2, 3, 7, 8, 9]], [[13, 16, 11], [15]]]},

"dolma": {"non_row": "dolma",
 "kernel": "Dolma is an open English corpus of three trillion tokens for research on language model pretraining, created by the Allen Institute for AI as the training corpus of its OLMo models and released with its documentation and an open-source curation toolkit.",
 "kernel_ko": [1, 3],
 "sections": [
  ("What it is", [
   "The name covers the dataset and the Dolma Toolkit that curated it; Dolma stands for 'Data to feed OLMo's Appetite'. The first version was released on 18 August 2023, and the paper describing it, by Luca Soldaini and 35 other authors, received the Best Resource Paper Award at ACL 2024. The dataset card lists six versions, v1.7 of April 2024 the default.",
   "Its web text comes from 24 Common Crawl snapshots and from C4, its scientific papers from peS2o, its code from The Stack, and its books, in the table for v1.6, from Project Gutenberg."]),
  ("How it was made", [
   "The corpus is English only: a language identifier keeps documents with a likelihood above 50% of being English, removing 61.7% of the web data, and its makers recognize that the decision 'reinforces the assumption of English as the \"default\" language'. For quality they chose heuristics and regular expressions after Gopher and Falcon, setting aside model-based filters whose biases are hard to detect.",
   "The archive's account of corpus filtering places Dolma among corpora whose perplexity- or classifier-based filters keep what looks like Wikipedia, an account its makers' own statement of their filters contests; both stand in its /non article."])],
 "ko": [[[2, 3, 4, 7], [10, 11]], [[14, 15], [16]]]},

"books3-search": {"non_row": "books3-search",
 "kernel": "Books3 search is a search tool that The Atlantic carries over the Books3 collection of books, for the question whether a given book is in that collection.",
 "kernel_ko": [1],
 "sections": [
  ("What it is", [
   "Three objects are kept apart under the name: the Books3 collection, the search tool named for it, and The Atlantic's reporting that carries the tool. The census holds the tool at an article address on The Atlantic's site whose path is dated September 2023; that address answers with a security block, so the tool's operator, method and current state are unrecorded. The Atlantic's site also carries a page titled \"AI Watchdog: Books3\"."]),
  ("The collection it searches", [
   "The collection was assembled by Shawn Presser from a shadow library called Bibliotik and went online in October 2020, named after OpenAI's Books1 and Books2. Counts differ by source: more than 191,000 books on The Atlantic's card, around 196,000 in WIRED's account, 197,000 ebooks in Schoppert's. EleutherAI incorporated it into the Pile, and it was used to train Facebook's LLaMA and, WIRED reports, Bloomberg's model."]),
  ("Place in the field", [
   "The archive holds that the provenance strip \"operates at industrial scale in AI training itself\", and its field survey says of the literary works it surveys that every one is in the corpora, read by machines incidentally."])],
 "ko": [[[5, 1, 3, 2]], [[8, 9, 11, 14, 15]], [[13, 17]]]},

"spawning-hibt": {"non_row": "have-i-been-trained",
 "kernel": "Have I Been Trained? (haveibeentrained.com) is a service of Spawning, a free web search of LAION-5B, a collection of about 5.8 billion image-text pairs, for learning whether one's images were used to train image models such as Stable Diffusion; on 1 November 2026 its home page served a maintenance notice.",
 "kernel_ko": [1, 3],
 "sections": [
  ("What it is", [
   "Spawning was founded by the artists Mat Dryhurst and Holly Herndon with the stated goal of giving creators more control over how their work is used in AI training. A search takes text or an uploaded image and returns similar images from the dataset through OpenAI's CLIP model, each with a similarity score, its caption in the dataset and the URL it was scraped from.",
   "Beside the search Spawning keeps a Do Not Train registry, a global opt-out list said in 2026 to hold over 80 million entries, which its reviewers call a consent signal without an enforcement mechanism."]),
  ("What it cannot see", [
   "The search covers LAION-5B alone: none of the text training data of language models and none of the proprietary image data of Midjourney or OpenAI. An exact image found proves it was in the training data; a similar one proves much less, and not finding a work shows only that it is not in LAION-5B.",
   "The archive names what such a search cannot reach training inscription: a work can persist in a model as a constraint on what the model does without remaining an inspectable copy."])],
 "ko": [[[4, 6, 7], [17, 18]], [[11, 8, 12], [14]]]},

"data-portraits": {"non_row": "data-portraits",
 "kernel": "Data Portraits are artifacts that record the data a foundation model is trained on so that membership can be tested afterwards, proposed in 2023 by Marc Marone and Benjamin Van Durme of Johns Hopkins University and served at dataportraits.org.",
 "kernel_ko": [1, 3],
 "sections": [
  ("What it is", [
   "A portrait answers whether a model has already encountered a given example during training; its unit is a single example queried against a portrait of a training dataset. Its makers place it beside datasheets and model cards as a complementary documentation artifact and call on dataset and model creators to release one.",
   "A portrait is a Bloom filter of hashed character n-grams of length 50 tiled across the corpus, which can give false positives and never false negatives; the Pile's portrait takes 27 GB on disk. Portraits were built for The Pile and The Stack, and the site also hosts a sketch of The Stack V2."]),
  ("What it answers and its limits", [
   "The paper reports it answering questions of test-set leakage and model plagiarism, and its makers hope a non-technical content creator could search for their material in a documented dataset. They state its limits: few datasets studied, false positives, no retrieval of the context around a match."]),
  ("At the name", [
   "The name is shared: the Overview gave the artifact as the last of four senses, beside W. E. B. Du Bois's data portraits, Judith Donath's and Giorgia Lupi's, each a distinct entity; the encyclopedia has no article under the name."])],
 "ko": [[[2, 5, 4], [8, 10, 11]], [[13, 15, 18]], [[35, 36]]]},
})
ARTICLES.update({
"literary-ai": {"non_row": "literary-ai",
 "kernel": "The Literary History of Artificial Intelligence, also called Literary AI, is an online exhibit of Columbia University's Rare Book & Manuscript Library on the shared history of literature and computation, told through Columbia's holdings from circa 1890 to 1970.",
 "kernel_ko": [1, 6],
 "sections": [
  ("What it is", [
   "It is a collaboration between the Columbia English Department, the Rare Book & Manuscript Library and Columbia's Digital Scholarship department, laid out in eight cases, its site copyright 2022 by Columbia University Libraries under a CC-BY 4.0 International License. No founding date is stated, and Wikipedia has no article under its title.",
   "It explores professional manuals, devices and techniques that promised to make writing easier and even to automate it, beside prose and poetry written by machines."]),
  ("Two stories", [
   "The first story, of production, follows writing manuals and plot generators such as Wycliffe Hill's Plot Genies and William Wallace Cook's Plotto into mid-twentieth-century computer experiments, from Christopher Strachey's love letter program of the 1940s to Margaret Masterman's work on automatic translation.",
   "The second story, of analysis, runs from Harriot Fansler's Types of Prose Narratives and Georges Polti's Les trente-six situations dramatiques (1895) to the techniques for organizing story elements that, in the exhibit's account, forecast later information storage."]),
  ("At the name", [
   "Asked for the exhibit's title, the Overview answered the general history of artificial intelligence in literature, the exhibit one bullet within it; the topic the title names stays a distinct entity from the exhibit."])],
 "ko": [[[2, 3, 4], [6]], [[8, 10], [13, 15]], [[38, 39, 31]]]},

"elc": {"non_row": "electronic-literature-collection",
 "kernel": "The Electronic Literature Collection is a publication of the Electronic Literature Organization: curated, edited volumes of electronic literature, four so far, from October 2006 to June 2022.",
 "kernel_ko": [1, 2],
 "sections": [
  ("What it is", [
   "Its volumes appeared in October 2006, February 2011, February 2016 and June 2022. The second, edited by Laura Borràs, Talan Memmott, Rita Raley and Brian Stefans, gathers 81 works published on flash drive and the web; the fourth, edited by Kathi Inman Berens, John Murray, Lyle Skains, Rui Torres and Mia Zamora, gathers 132 literary works in 31 languages by authors of 42 nationalities, open access.",
   "The ELO was founded in Chicago in 1999 by Scott Rettberg, Robert Coover and Jeff Ballowe."]),
  ("Works and authors", [
   "Mark Marino singled out among the first volume's works Judd Morrissey's The Jew's Daughter, Michael Joyce's Twelve Blue and Kate Pullinger's Inanimate Alice as \"pillars of electronic writing\". The second volume's copy at The NEXT lists its works by creator, among them Nick Montfort's Book and Volume."]),
  ("Place in the field", [
   "The layer census reads the collection as the canonizing anthology of the procedural lineage, whose value for the training layer sits at the level of works, and marks it off from a training corpus: its sources describe curated volumes for readers and name no machine addressee."])],
 "ko": [[[2, 11, 12], [5]], [[14, 15]], [[10, 8]]]},

"elmcip": {"non_row": "elmcip",
 "kernel": "The ELMCIP Electronic Literature Knowledge Base is an open-access, contributory database of cross-referenced records on electronic literature, developed by the University of Bergen Electronic Literature Research Group from the ELMCIP project, active from June 2010 to October 2026 and now a frozen archive.",
 "kernel_ko": [1, 2, 3],
 "sections": [
  ("What it is", [
   "Its records cover authors, creative works, critical writing, platforms and practices; its unit is a cross-referenced record of one of ten kinds. The archive remains available for browsing and searching and is closed to new contributions."]),
  ("The project", [
   "ELMCIP, Electronic Literature as a Model of Creativity and Innovation in Practice, was a research project funded from 2010 to 2013 by the HERA Joint Research Programme, directed by Scott Rettberg. It resulted in conferences in six countries, three books, an anthology of 18 works and the knowledge base, and it contributed to the development of CELL. Its partners are counted two ways, seven academic partners and one non-academic partner on the project's site, seven partners in its director's essay of 2021."]),
  ("Who made the records", [
   "Records came from researchers and writers in the field, who could edit and enhance any record as on a wiki, and through a University of Bergen course. Its director presents it as \"a collectively authored, networked research environment\"."])],
 "ko": [[[1, 7, 3]], [[8, 11, 12, 10]], [[13, 14, 15]]]},

"cell": {"non_row": "cell",
 "kernel": "The Consortium on Electronic Literature (CELL) is an international, open-access collaboration that gives centralized access to the databases and archives documenting electronic literature through The Index, hosted and directed by the Center for Digital Narrative at the University of Bergen.",
 "kernel_ko": [1, 4],
 "sections": [
  ("What it is", [
   "It holds records of works, and the works stay with the member archives or their authors. Its About page names Joseph Tabbi as founding director and Hannah Ackermans as managing director, and it is governed with representatives of its member databases in close partnership with the Electronic Literature Organization."]),
  ("The Index", [
   "The Index is a curated catalogue that brings records from independent databases together in one Wikibase, with Wikidata as its hub: each record also exists as a Wikidata item, and a work's author, date and language are matched to Wikidata properties. Its metadata is licensed CC BY-NC-SA 4.0 and served through a SPARQL Query Endpoint.",
   "The layer census reads this as the machine-legible, attributed form in which a work can be found under its author, the persistence the archive's field survey asks for: a work placed where the training and retrieval layers look, with the metadata that lets it be found and attributed."])],
 "ko": [[[3, 5, 4]], [[6, 7, 9], [10, 11]]]},
})
ARTICLES.update({
"ebr": {"non_row": "electronic-book-review",
 "kernel": "electronic book review (ebr) is a peer-reviewed open access journal of critical writing on the digital futures of literature, theory, criticism and the arts, published online at electronicbookreview.com by what it calls the digital literary network.",
 "kernel_ko": [1],
 "sections": [
  ("What it is", [
   "Its About page defines it as \"a peer-reviewed diamond open access journal of critical writing produced and published by the digital literary network\". It publishes criticism, filed in threads with named thread editors; the creative works it discusses are held elsewhere, and its name notwithstanding it is no review of e-books."]),
  ("Founding", [
   "The sources date it three ways: Wikipedia says it was founded in 1995 by Joseph Tabbi and Mark Amerika, Open Humanities Press that it has been \"Publishing open access since 1995\", and the Electronic Literature Directory that it has been in continuous publication since 1994, giving its publication year as 1996."]),
  ("Place in the field", [
   "The layer census enters it as a theoretical interlocutor and holds that its bearing lies in specific essays on machine writing and on electronic literature's existence for AI."])],
 "ko": [[[2, 11, 7]], [[12, 13, 14]], [[9, 10]]]},

"taper": {"non_row": "taper",
 "kernel": "Taper is an online literary magazine for small computational pieces, published twice yearly by Bad Quarto since Spring 2018 and edited by a collective, each poem's core held to no more than 2KB of HTML.",
 "kernel_ko": [1, 4, 8, 11],
 "sections": [
  ("What it is", [
   "Its pieces are web pages written in HTML5 with ES6 and read in a browser. Each issue is edited by a collective that makes all decisions; the publisher, Nick Montfort, offers some help at the first and last stages, and editing is done in coordination with The Trope Tank at MIT, though the magazine is not officially associated with MIT.",
   "Its unit is the themed issue: Taper #1, a minimal labyrinth, appeared in Spring 2018, and the index lists sixteen issues through Spring 2026. Issues 1 to 16 were published at badquar.to, and the magazine has moved to taperzine.org, where Taper #17 will launch."]),
  ("The constraint", [
   "Its usual constraint holds the core of each poem to no more than 2KB (2048 bytes). Pieces may use no external libraries, APIs or resources, so that each page is self-contained and can be viewed without a network connection."])],
 "ko": [[[2, 4, 6], [8, 14]], [[11, 12]]]},

"nanogenmo": {"non_row": "nanogenmo",
 "kernel": "NaNoGenMo, National Novel Generation Month, is an annual event in which participants spend November writing code that generates a novel of 50,000 words or more and share at least one novel with its source code, organised on GitHub since 2013.",
 "kernel_ko": [1, 2, 3],
 "sections": [
  ("What it is", [
   "It started in 2013 from an idea Darius Kazemi tweeted, taking its measure from National Novel Writing Month. The page states a single rule: \"The only rule is that you share at least one novel and also your source code at the end.\" The novel is \"defined however you want\", and a program may even \"literally grab a random novel from Project Gutenberg\"."]),
  ("What it is made from", [
   "A generated novel may be made from existing text, and each edition keeps an open issue for resources, corpora and techniques. Early entries used Markov chains, scraped text and procedural tricks; in later years participants increasingly reached for neural language models.",
   "On copyright the page asks and declines to enforce: \"Please try to respect copyright. We're not going to police it\". No rule governs how a generated novel is credited; in third-party accounts entries stand under their makers' names."])],
 "ko": [[[4, 5, 6, 9]], [[10, 12], [13, 14, 15]]]},
})
