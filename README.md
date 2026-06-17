# AI Real Estate Listing Intelligence Agent

## Overview

AI Real Estate Listing Intelligence Agent is an Agentic AI solution that automates property opportunity discovery and investment analysis.

The system retrieves real estate listings from Realtor API, evaluates investment potential using a custom scoring engine, generates AI-powered property insights using Groq LLM, and sends alerts for high-potential opportunities.

---

## Business Problem

Property investors and brokers spend significant time manually reviewing listings across multiple platforms.

Challenges include:

* Continuous monitoring of new listings
* Identifying undervalued opportunities
* Comparing investment potential
* Generating property summaries
* Tracking opportunities efficiently

This project automates the entire workflow using Agentic AI and workflow automation.

---

## Key Features

### Automated Property Discovery

* Retrieves property listings through Realtor API

### Investment Scoring Engine

* Evaluates listings using:

  * Property Price
  * Bedrooms
  * Bathrooms
  * Lot Size
  * Property Type

### AI Property Analysis

* Generates:

  * Property Summary
  * Strengths
  * Risks
  * Investment Recommendation

### Real-Time Alerts

* Sends high-potential opportunities through Telegram

### Opportunity Tracking

* Stores analyzed properties in Google Sheets

---

## Technology Stack

* Python
* Streamlit
* n8n
* Groq LLM
* Realtor API
* Telegram Bot
* Google Sheets

---

## System Architecture

User → Streamlit Dashboard → n8n Workflow

n8n Workflow:

1. Retrieve Property Listings
2. Clean & Transform Data
3. Calculate Investment Score
4. Generate AI Analysis (Groq)
5. Send Telegram Alert
6. Store Results in Google Sheets

---

## Example Output

Property: 18010 Bambriar Dr

Investment Score: 8/10

Recommendation:
High Potential Opportunity

AI Summary:
Competitive pricing, good family-home configuration, and strong investment potential.

---

## Business Impact

* Automated property opportunity discovery
* Faster investment analysis
* Reduced manual screening effort
* Real-time opportunity notifications
* Centralized opportunity tracking

---

## Future Enhancements

* Property Price Prediction
* Rental Yield Estimation
* Location Intelligence
* Property Comparison Engine
* CRM Integration

---

## 🔗AI-RealEstate-Intelligence-Agent-WebApp
https://ai-realestate-listing-intelligence-agent.streamlit.app/

---

## Author

Swati Arya

