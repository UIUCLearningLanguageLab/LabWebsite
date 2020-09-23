+++
title = "Tools+Data"
layout = "single-para"
+++

---

## Open-Source Python Packages

### Ludwig-Template
Used internally, to quickly get started building jobs to submit to internal job submission system called `Ludwig`.

__Website:__  https://github.com/UIUCLearningLanguageLab/Ludwig-Template

### Preppy
This repository contains convenienve functions for preparing text data for training NLP models. It is possible to prepare batches of data that preserve the order of documents in the corpus. 
__Website:__ https://github.com/phueb/Preppy

### Visualized
This repository contains convenience functions for common visualizations, built on top of `matplotlib`. 

__Website:__ https://github.com/UIUCLearningLanguageLab/Visualized
	
---

## Natural Language Data

### American-English CHILDES
To create a custom CHILDES corpus, use the Python package `CreateCHILDESCorpus`.
The package allows you to define custom tokenization rules, among other features. The output is a text file containing line-separated transcripts, and will be ordered by the age of the child spoken to.

__Website:__ https://github.com/UIUCLearningLanguageLab

### English Wikipedia
To create a custom Wikipedia corpus, use the Python package `CreateWikiCorpus`. Due to the size of English Wikipedia - 4billion words as of 2019 - corpus creation is distributed across `Ludwig` workers, and output files are saved to the server. A single corpus is distributed across multiple text files, each created on a separate worker. 

__Website:__  https://github.com/UIUCLearningLanguageLab.
