Methodology

Problem Statement

When I first started Resale HDBuddy, the challenge was clear: how can I make AI useful for exploring resale flat data in a way that is stable, affordable, and efficient? I wanted the chatbot to answer questions grounded in actual datasets, but I quickly discovered the limitations of Retrieval Augmented Generation (RAG). With only 10 records retrieved, the chatbot often said it had “no records,” especially when towns were mentioned lower down in the dataset. This was disheartening, and it showed me that while RAG is powerful, it needs careful design to work within token limits and still provide meaningful answers.

Approach to Solving the Problem

My approach was to treat this project as both a technical experiment and a personal learning journey. I broke the problem into smaller parts:  
•	Login and access control to make the app professional.  
•	Resale Trend chart to visualize data directly from trend_data.csv. (Please refer to GitHub scripts on using Regression Model)  
•	Price Estimator using regression logic and ChatGPT to project prices.  (Please refer to GitHub scripts on using predictions)  
•	Henry the Assistant powered by RAG, carefully tuned to balance token usage with useful retrieval.  
By combining these features, I ensured the app wasn’t just a chatbot — it became a full dashboard that demonstrates multiple AI concepts.

Workflow

The workflow follows three main stages:  
1.	Pre retrieval preparation: Detect towns mentioned in the user’s question. This helps narrow down the dataset before retrieval.  
2.	Retrieval: Instead of only reading 10 records, I expanded to 50 records when towns were identified. This gave the chatbot more context while still staying within token limits.  
3.	Post retrieval summarization: Aggregate the data (averages, grouped by year or flat type) so the chatbot has concise, meaningful context to work with.  
This balance — not too little data, not too much — was key to making RAG work smoothly.
Please refer to GitHub scripts for efforts to Clean and trim dataset'.
 
Addressing Prompt Injection

I learned that prompt injection is a real risk when using AI. To safeguard against it, I kept the system prompts simple and focused: the assistant is only allowed to explain resale trends using the provided data. By grounding answers in trend_data.csv and hdb_resale_clean.csv, I reduced the chance of the chatbot being tricked into giving irrelevant or unsafe responses.

Hypothesis Testing & Validation 

My hypothesis was that increasing the retrieval size from 10 to 50 records, combined with data aggregation, would improve the chatbot’s usefulness without exceeding token limits. I tested this by asking questions about towns lower in the dataset, but the results were still unsatisfactory — the chatbot struggled to recognize and respond to those towns.  

To address this, I trimmed the dataset to just two towns, Bedok and Choa Chu Kang, covering 2020–2025 instead of the full 2017–2025 range. This made it easier for the AI to apply RAG effectively, pulling relevant information while staying within token limits. Previously, I often saw either 'no information available' with too few records or 'Error: Exceed Token Limit' with the larger dataset. By understanding these limitations, I’ve become more mindful about the dataset scope I use, ensuring the chatbot remains efficient and genuinely helpful."

I've include WordDoc 'Prompts and Responses that clearly demonstrate the use of RAG in Resale HDBuddy chatbot' in GitHub for reference.

User Impact

For a non technical user, the impact is clear:  
•	The Resale Trend chart provides immediate visual insights.  
•	The Price Estimator gives a practical projection, making the dashboard feel useful.  
•	The Chat Assistant adds interactivity, allowing users to ask questions in natural language.  
Together, these features make the app approachable and informative, even for someone unfamiliar with data science.
Obstacle and Change Management
As a 57 year old non techie, I faced plenty of obstacles: learning Google Colab, GitHub, local command prompts, and Streamlit Cloud was daunting. At times, the chatbot’s limitations were frustrating. But each obstacle became a learning opportunity. By iterating — adjusting retrieval sizes, adding features like charts and estimators, and polishing the login page — I managed change step by step. This taught me resilience and the importance of balancing ambition with practicality.
