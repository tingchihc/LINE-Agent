# 🤖 Domain Knowledge QA System with MongoDB and LLM Agent

This project allows you to inject **your own domain knowledge** into a chatbot powered by a **Large Language Model (LLM)**. You can store your custom data in **MongoDB**, retrieve the most relevant info using **vector search**, and have the LLM provide accurate, context-aware answers — all integrated with **LINE Messaging API**.

---

## 📘 Use Case

Use this system to:
- Build a chatbot for your company’s products or services.
- Create a smart FAQ assistant for your app or website.
- Provide contextual customer service via LINE.

---

## 🧠 How It Works

1. **Prepare Domain Knowledge**

   Create a `qa.json` file like this:

   ```json
   {
     "001": ["What is the return policy?", "You can return items within 30 days of purchase."],
     "002": ["How do I reset my password?", "Click on 'Forgot Password' at the login screen."]
   }
