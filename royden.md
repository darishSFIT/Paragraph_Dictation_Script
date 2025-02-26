# DATA SCIENCE QUESTION BANK SOLUTIONS

## MODULE 1: TEXT PROCESSING AND INFORMATION EXTRACTION

### 1. N-gram Modelling and its Applications

N-gram modeling is a probabilistic language modeling technique that predicts the occurrence of a word based on the occurrence of its previous (n-1) words. An n-gram is a contiguous sequence of n items from a given sample of text.

**Types of N-grams:**
- Unigram (n=1): Single word
- Bigram (n=2): Two consecutive words
- Trigram (n=3): Three consecutive words

**Applications:**
1. Speech Recognition
2. Machine Translation
3. Spelling Correction
4. Text Generation
5. Information Retrieval
6. Document Classification

### 2. Named Entity Recognition (NER) Application

Named Entity Recognition is the process of identifying and classifying named entities in text into predefined categories such as person names, organizations, locations, etc.

**Block Diagram:**

```
[Text Input] → [Preprocessing] → [Feature Extraction] → [NER Model] → [Post-Processing] → [Named Entities]
                     ↓                     ↓                ↓                  ↓
               [Tokenization]        [Word Embeddings]   [CRF/LSTM/           [Entity
                [POS Tagging]        [Contextual         Transformer]          Consolidation]
                                      Features]
```

**Applications of NER:**
- Information extraction from unstructured text
- Question answering systems
- Customer support automation
- Resume parsing
- Medical record analysis

### 3. Stemming and Stop Word Removal Process

**Stemming:**
Stemming is the process of reducing words to their word stem or root form by removing suffixes and sometimes prefixes.

**Common Stemming Algorithms:**
1. Porter Stemmer
2. Snowball Stemmer (Porter2)
3. Lancaster Stemmer
4. Lovins Stemmer

**Example:**
- "running", "runner", "runs" → "run"
- "connection", "connected", "connecting" → "connect"

**Stop Word Removal:**
Stop words are common words that typically don't contribute much meaning to the text (e.g., "the", "is", "at", "which").

**Process:**
1. Define or use a predefined list of stop words
2. Tokenize the text
3. Remove all tokens that appear in the stop word list
4. Reconstruct the text (if needed) without stop words

### 4. Tokenization with Example

Tokenization is the process of breaking text into smaller units called tokens, which can be words, characters, or subwords.

**Types of Tokenization:**
1. Word Tokenization
2. Sentence Tokenization
3. Character Tokenization
4. Subword Tokenization

**Example of Word Tokenization:**

Input text:
```
"Data science involves extracting knowledge from data. It employs techniques from statistics and computer science."
```

After tokenization:
```
["Data", "science", "involves", "extracting", "knowledge", "from", "data", ".", "It", "employs", "techniques", "from", "statistics", "and", "computer", "science", "."]
```

### 5. Unsupervised Information Extraction

Unsupervised Information Extraction refers to methods that automatically extract structured information from unstructured text without requiring labeled training data.

**Key Approaches:**
1. Open Information Extraction (OpenIE)
2. Clustering-based approaches
3. Distributional Semantics
4. Pattern Learning

**Advantages:**
- No need for labeled training data
- Can discover unexpected patterns and relationships
- Adaptable to different domains and languages

## MODULE 2: TEXT CLUSTERING AND CLASSIFICATION

### 1. Text Clustering with Example

Text clustering is the process of grouping similar documents together based on their content, without predefined categories.

**Example:**
Consider a collection of news articles. Text clustering might automatically group them into clusters like:
- Technology news (containing words like "AI", "smartphone", "software")
- Political news (containing words like "election", "government", "policy")
- Sports news (containing words like "tournament", "player", "championship")

**Common Algorithms:**
1. K-means clustering
2. Hierarchical clustering
3. DBSCAN
4. Topic Modeling (LDA)

### 2. Text Clustering vs. Text Classification

| Feature | Text Clustering | Text Classification |
|---------|----------------|---------------------|
| **Learning Type** | Unsupervised | Supervised |
| **Training Data** | Unlabeled data | Labeled data |
| **Categories** | Not predefined, discovered automatically | Predefined categories |
| **Purpose** | To discover natural groupings | To assign documents to known categories |
| **Evaluation** | Internal metrics (e.g., silhouette score) | External metrics (e.g., accuracy, F1-score) |
| **Algorithms** | K-means, Hierarchical clustering, DBSCAN | Naive Bayes, SVM, Decision Trees, Neural Networks |
| **Applications** | Document organization, topic discovery | Spam detection, sentiment analysis, news categorization |
| **Output** | Groups of similar documents | Category labels for documents |

### 3. Hidden Markov Models (HMM) vs. Conditional Random Fields (CRF)

| Aspect | Hidden Markov Models (HMM) | Conditional Random Fields (CRF) |
|--------|----------------------------|--------------------------------|
| **Model Type** | Generative model | Discriminative model |
| **Probability Modeled** | Joint probability P(X,Y) | Conditional probability P(Y\|X) |
| **Independence Assumptions** | Strong independence assumptions (Markov property) | Fewer assumptions, can handle overlapping features |
| **Feature Engineering** | Limited feature representation | Can incorporate arbitrary, overlapping features |
| **Long-range Dependencies** | Difficult to model | Can handle better |
| **Training** | Maximum Likelihood Estimation | Maximum Entropy principles |
| **Performance** | Good with limited training data | Generally outperforms HMM with sufficient data |
| **Applications** | Speech recognition, simple sequence labeling | Named entity recognition, POS tagging, complex sequence labeling |

### 4. Distance-based Clustering Algorithms

**1. K-means Clustering:**
- **Process**:
  1. Initialize K cluster centroids
  2. Assign each document to the nearest centroid
  3. Recalculate centroids based on assigned documents
  4. Repeat until convergence or maximum iterations

**2. Hierarchical Clustering:**
- **Types**:
  - **Agglomerative** (bottom-up): Start with each document as a cluster and merge
  - **Divisive** (top-down): Start with all documents in one cluster and split
- **Linkage Methods**:
  - Single linkage (minimum distance between clusters)
  - Complete linkage (maximum distance between clusters)
  - Average linkage (average distance between clusters)
  - Ward's method (minimizes variance within clusters)

### 5. Bayesian Network with Example

A Bayesian Network is a probabilistic graphical model that represents variables and their conditional dependencies via a directed acyclic graph (DAG).

**Example Bayesian Network for Student Performance:**

Consider a simple Bayesian Network for predicting student performance with variables:
- Intelligence (I): High, Medium, Low
- Difficulty of Course (D): High, Low
- SAT Score (S): High, Low
- Grade (G): A, B, C, D, F
- Letter of Recommendation (L): Strong, Medium, Weak

**Extending this Bayesian Network:**

1. **Add new variables**:
   - Study Hours (SH): Many, Average, Few
   - Previous Knowledge (PK): Strong, Weak
   - Mental Health (MH): Good, Poor

2. **Add new edges**:
   - Study Hours influences Grade
   - Previous Knowledge influences Grade
   - Mental Health influences Study Hours and Grade

### 6. Classification Methods

**1. Decision Tree Classifiers:**
- Hierarchical model that splits data based on feature values
- Each internal node represents a decision based on a feature
- Each leaf node represents a class label
- Examples: ID3, C4.5, CART

**2. Rule-based Classifiers:**
- Use a set of IF-THEN rules for classification
- Rules can be derived from decision trees or directly from data
- Each rule has a condition part and a prediction part
- Examples: RIPPER, CN2, PART

## MODULE 3: WEB MINING AND SEARCH

### 1. Inverted Indices and Compression in Web Mining

**Inverted Index:**
An inverted index is a data structure used in information retrieval systems that maps content (words, numbers, etc.) to their locations in a document or set of documents.

**Structure:**
- **Dictionary**: Contains all unique terms in the corpus
- **Posting Lists**: For each term, a list of documents containing that term

**Example:**
```
Document 1: "web mining techniques"
Document 2: "data mining and web mining"
Document 3: "advanced web techniques"

Inverted Index:
"web": [1, 2, 3]
"mining": [1, 2]
"techniques": [1, 3]
"data": [2]
"and": [2]
"advanced": [3]
```

**Compression Techniques:**

1. **Dictionary Compression**:
   - Front coding
   - Hashing

2. **Posting List Compression**:
   - Gap encoding
   - Variable byte coding
   - Elias coding

3. **Document Compression**:
   - Huffman coding
   - LZ77/LZ78

### 2. Meta Search and Rank-Based Meta Search

**Meta Search:**
Meta search is the process of combining search results from multiple search engines to provide a more comprehensive search experience.

**Components of Meta Search:**
1. Query Dispatcher
2. Result Aggregator
3. Result Merger
4. User Interface

**Rank-Based Meta Search Methods:**

1. **Borda Count Method**:
   - Assigns scores to documents based on their positions
   - Higher ranks get more points
   - Sum the scores from all search engines
   - Rank documents by total score

2. **Condorcet Method**:
   - Conducts pairwise comparisons between documents
   - A document wins a comparison if it's ranked higher by more search engines

3. **Weighted Combination**:
   - Assigns weights to different search engines based on their reliability
   - Calculates weighted sum of ranks

### 3. Spamming: Link Spamming and Content Spamming

**Web Spamming:**
Web spamming refers to deliberate actions designed to manipulate search engines into ranking certain pages higher than they deserve.

**1. Link Spamming:**
Link spamming involves manipulating the link structure of the web to artificially increase the importance of certain pages.

**Types of Link Spamming:**
- Link Farms
- Paid Links
- Comment Spam
- Private Blog Networks (PBNs)
- Reciprocal Link Exchanges
- Sybil Attacks

**2. Content Spamming:**
Content spamming involves manipulating the content of web pages to rank for specific search queries without providing value.

**Types of Content Spamming:**
- Keyword Stuffing
- Invisible Text
- Tiny Text
- Meta-tag Stuffing
- Doorway Pages
- Scraping
- Cloaking

### 4. Spamming Using Hiding Techniques and Spam Handling

**Common Hiding Techniques:**

1. **Cloaking**:
   - Serving different content based on user agent (search engine bot vs. human user)
   - Using IP-based cloaking to identify search engine crawlers

2. **Invisible/Hidden Text**:
   - Using text color that matches the background color
   - Setting font size to zero or very small
   - Positioning text off-screen using CSS

3. **CSS Tricks**:
   - Using CSS to hide content (display:none, visibility:hidden)
   - Layering content with z-index so spam content is behind visible content

**Spam Handling on the Web:**

1. **Algorithmic Approaches**:
   - PageRank
   - TrustRank
   - Statistical Analysis
   - Machine Learning

2. **Manual Reviews**:
   - Human quality raters evaluating suspicious pages
   - User-reported spam
   - Manual penalties for confirmed spam

3. **Penalties and Consequences**:
   - Reduction in search rankings
   - Complete removal from search index ("deindexing")
   - Domain-level penalties affecting all pages on a site

4. **Preventive Measures**:
   - Nofollow Attribute
   - Canonicalization
   - Spam Traps