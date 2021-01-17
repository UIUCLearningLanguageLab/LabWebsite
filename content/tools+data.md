+++
title = "Tools+Data"
layout = "single-para"
+++

---

## Open-Source Python Packages

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

__Website:__ https://github.com/UIUCLearningLanguageLab/CreateCHILDESCorpus

### English Wikipedia
To create a custom Wikipedia corpus, use the Python package `CreateWikiCorpus`. Due to the size of English Wikipedia - 4billion words as of 2019 - corpus creation is distributed across `Ludwig` workers, and output files are saved to the server. A single corpus is distributed across multiple text files, each created on a separate worker. 

__Website:__  https://github.com/UIUCLearningLanguageLab/CreateWikiCorpus

---

## Ludwig

We use a custom-built job submission system, called `Ludwig`, for computationally expensive simulations. 
Documentation about how `Ludwig` workers are setup is available here:

https://docs.philhuebner.com/ludwig

The system is built on top of 8 workers, and 1 shared file server.
Documentation about the lab's file server and file sharing is available here:

https://docs.philhuebner.com/file-sharing

### Ludwig-Template
Used internally, to quickly get started building jobs to submit to `Ludwig`.

__Website:__  https://github.com/UIUCLearningLanguageLab/Ludwig-Template

### Ludwig-Viz
Used internally, to quickly visualize metrics tracked as part of one or more jobs submitted to `Ludwig`. For example, compare learning curves (e.g. MSE) for groups of neural networks each trained with different hyper-parameters. 

__Website:__  https://github.com/phueb/LudwigViz 


	
