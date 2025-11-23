Glossary

Introduction

This glossary is written from my perspective as a learner, to help others understand the key terms I grappled with while building Resale HDBuddy. As a 57 year old non techie, I had to learn not just the concepts of AI and RAG, but also how to use tools like Google Colab, GitHub, local command prompts, and Streamlit Cloud. These terms represent the building blocks of my journey — the words I kept bumping into, the ideas I had to wrestle with, and the lessons that eventually clicked.

________________________________________
Retrieval Augmented Generation (RAG)

A method where an AI model retrieves information from external datasets before answering. In Resale HDBuddy, RAG ensures that chatbot answers are grounded in trend_data.csv and hdb_resale_clean.csv.  
•	Strengths: Provides accurate, data driven answers.  
•	Limitations: Can run into token limits if too much data is retrieved.  
•	My learning: I started with only 10 records, but the chatbot often said it had “no records.” Expanding to 50 records and aggregating data gave richer context while staying efficient.

Token Limit

Tokens are the “word pieces” AI models use to process text. Every prompt and dataset consumes tokens, and there’s a maximum limit.  
•	My learning: I had to balance token usage by summarizing data and limiting retrieval size. This taught me that efficiency matters as much as accuracy.

Prompt Injection

A type of attack where someone tries to trick the AI into ignoring its instructions.  
•	My safeguard: I kept system prompts simple and restricted the assistant to only explain resale trends using the provided datasets.

Pre retrieval, Retrieval, Post retrieval

The three stages of RAG workflow:  
•	Pre retrieval: Detect towns mentioned in the user’s question.  
•	Retrieval: Pull relevant records (up to 50) from the dataset.  
•	Post retrieval: Summarize and aggregate the data so the chatbot can respond clearly and within token limits.

Regression

A statistical method used to predict values based on input variables. In Resale HDBuddy, regression logic is used in the Price Estimator to project resale prices based on town, flat type, floor area, and year.

Streamlit

A Python framework that makes it easy to build interactive dashboards and web apps. I used Streamlit to design the login page, charts, and chatbot interface.

GitHub

An online platform for storing and sharing code. I used GitHub to manage my project files and keep track of changes.

Google Colab Notebook

A cloud based environment where you can run Python code without installing anything locally. I used Colab to experiment with code and test ideas before moving them into Streamlit.
Command Prompt (Local Cmd)
The text based interface on my computer where I could run commands like streamlit run app.py to launch the dashboard locally.
