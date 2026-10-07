# Problem Definition

## 1. Project Objective

Build a machine learning system to classify emails at two levels:

1. Binary classification: Spam vs Ham
2. Multi-class classification: Work, Personal, Promotions, Spam

The main goal is to create an email-processing pipeline that converts raw text into accurate predictions, minimizes false positives for important emails, and is scalable for production use.

## 2. Problem to Solve

### 2.1 Binary Classification
- Input: email subject + email body
- Output: `spam` or `ham`
- Goal: correctly detect promotional, scam, malicious, or junk emails while avoiding misclassifying legitimate emails as spam

### 2.2 Multi-class Classification
- Input: email subject + email body
- Output: one of the following labels:
  - `work`
  - `personal`
  - `promotions`
  - `spam`
- Goal: classify emails by purpose and content while separating legitimate promotional emails from spam.

## 3. Label Definitions

| Label | Meaning | Example |
|---|---|---|
| `ham` | Legitimate email, not spam | Emails from colleagues, friends, or clients |
| `spam` | Junk, scam, or malicious email | "Free prize", "Click here", suspicious offers |
| `work` | Business-related email | Meetings, projects, reports, client communication |
| `personal` | Personal email | Family updates, personal conversations |
| `promotions` | Legitimate promotional email | Sales campaigns, newsletters, discount announcements |

## 4. Input Data

The system will work with email records containing:
- `subject`: email title
- `body`: email content
- `label`: class label
- `source`: data source (Enron, SMS, custom dataset)
- `timestamp` (if available): email sending time

## 5. Data Sources

### 5.1 Enron Email Corpus
- Used to obtain real-world email data similar to business communication
- Suitable for classifying work, personal, and spam emails

### 5.2 SMS Spam Collection
- Used to add short spam/ham examples for testing text classification on shorter messages
- Useful for evaluating model behavior on varied text lengths

### 5.3 Custom Domain-Specific Samples
- Data collected by the user or team
- Used to adapt the model to a specific environment or business domain

## 6. Dataset Characteristics

- Email data often contains noise such as HTML, URLs, special characters, uppercase words, punctuation, and duplicated content
- Some emails may have empty subjects or incomplete bodies
- Class imbalance may occur, where `ham` or `work` classes are much more frequent than `spam`
- Proper preprocessing is required before feeding data into a model

## 7. Constraints and Requirements

- The same email must not be assigned multiple ambiguous labels
- Data must be standardized to a common schema before training
- Empty emails or emails missing labels should be discarded
- Each email must have exactly one valid label
- The system should prioritize minimizing false positives where important emails are incorrectly classified as spam

## 8. Evaluation Metrics

The main metrics for evaluating the model are:

- Precision: prioritize reducing the number of legitimate emails incorrectly classified as spam
- Recall: ensure real spam emails are detected correctly
- F1-score: balances precision and recall
- Confusion Matrix: analyze correct and incorrect predictions across classes
- Accuracy: used as a supporting metric only, not the main metric when class imbalance exists

## 9. Success Criteria

Phase 1 is considered complete when:

- The problem statement is clearly defined and agreed upon
- Labels are clearly specified
- Data has been collected and stored in a consistent structure
- The project environment is set up
- `requirements.txt` contains the necessary dependencies
- Data is ready to proceed to Phase 2: EDA

## 10. Conclusion

Phase 1 is the foundation of the project: it defines the problem, standardizes objectives, and collects the data needed for subsequent stages. If this phase is done well, the following steps—EDA, preprocessing, feature engineering, and model training—will be more reliable and easier to implement.


