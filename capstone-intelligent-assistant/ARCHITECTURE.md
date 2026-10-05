# Capstone - Intelligent Student Assistant

## What this project is
An AI assistant that helps students by answering questions using
their own course notes, instead of just generic AI knowledge.

## How everything connects

1. **Client Layer**
   - Student opens the web dashboard (Module 1 - Next.js) or the
     mobile app (Module 11 - Android)
   - They type or ask a question

2. **Security & Routing**
   - The question goes to the backend (Module 2 - Node.js,
     Module 3 - FastAPI)
   - Firebase (Module 4) checks that the student is logged in
   - Redis (Module 7) checks if this exact question was already
     answered recently, to save time

3. **Knowledge Retrieval**
   - If the answer isn't cached, the system searches for related
     course notes using MongoDB Atlas Vector Search (Module 5)
     and/or Pinecone (Module 6)

4. **Agentic Reasoning**
   - LangChain (Module 10) builds a prompt combining the student's
     question with the notes that were found
   - The agent (Module 12) decides whether to search notes,
     calculate something (like GPA), or answer directly

5. **Cloud Infrastructure**
   - All backend services are packaged with Docker (Module 8)
   - Everything is deployed on Google Cloud Platform (Module 9),
     with IAM controlling who can access what

6. **GitHub Submission**
   - All 12 modules, their code, and this architecture document
     are committed and pushed to GitHub

## What I learned building this
Each piece solves one specific problem (routing, security, search,
caching, reasoning), and a real AI assistant needs all of them
working together, not just one AI model on its own.