pip install gradio                                                                                                                                               

import gradio as gr
from difflib import get_close_matches

# Knowledge base with 40 questions and answers
responses = {
    "how to prepare for a job interview": "Research the company, practice common questions, review your resume, and prepare questions to ask the interviewer.",
    "what to wear for an interview": "Dress professionally. For most roles, business casual or formal attire is appropriate.",
    "how to answer tell me about yourself": "Give a brief overview of your background, highlight key accomplishments, and explain why you're interested in this role.",
    "what are your strengths": "Choose 2-3 strengths relevant to the job, and back them up with real examples.",
    "what are your weaknesses": "Pick a real but minor weakness and explain how you’re working to improve it.",
    "how to write a resume": "Keep it concise, tailor it to the job, highlight achievements, and use action verbs.",
    "should I follow up after an interview": "Yes, send a thank-you email within 24 hours. Reaffirm your interest and appreciation.",
    "how to handle salary questions": "If asked early, say you'd like to learn more about the role first. Later, provide a range based on research.",
    "what are behavioral interview questions": "These ask about past experiences. Use the STAR method to answer: Situation, Task, Action, Result.",
    "how to stay calm during an interview": "Prepare thoroughly, take deep breaths, and remember the interview is a conversation.",
    "what to bring to an interview": "Bring copies of your resume, a notepad, pen, and any documents the employer requested.",
    "how to answer why do you want this job": "Show that you’ve researched the company, and link your skills and goals to the role.",
    "how long should my resume be": "One page for less experience, two max for seasoned professionals.",
    "what questions should I ask the interviewer": "Ask about company culture, team structure, growth opportunities, and success metrics.",
    "how to research a company before an interview": "Check their website, recent news, social media, and Glassdoor reviews.",
    "how to explain gaps in employment": "Be honest, keep it positive, and share what you did during the gap (learning, volunteering, etc.).",
    "what is a phone interview": "A screening call to assess basic fit before inviting you to an in-person or virtual interview.",
    "how to answer where do you see yourself in 5 years": "Mention goals that align with the role and show ambition, but flexibility.",
    "how to negotiate salary": "Do research, be confident, and wait until you have an offer to discuss compensation.",
    "how to handle interview rejection": "Stay positive, ask for feedback if possible, and keep applying. It’s part of the process.",
    "can i bring notes to an interview": "Yes, having a few notes or questions is fine, but avoid reading from them constantly.",
    "how early should i arrive for an interview": "Arrive 10–15 minutes early. It shows punctuality without being too early.",
    "how to send a thank you email": "Be brief, thank them for their time, highlight something discussed, and reaffirm interest.",
    "what is the star method": "A technique to answer behavioral questions: Situation, Task, Action, Result.",
    "how to deal with a panel interview": "Address each panelist, make eye contact, and treat it like a group conversation.",
    "how to handle a virtual interview": "Find a quiet space, check your tech, dress professionally, and make eye contact through the camera.",
    "what is your greatest achievement": "Pick a proud moment with measurable impact, and link it to the job role if possible.",
    "how to explain a career change": "Focus on transferable skills and your motivation for changing careers.",
    "how to answer why should we hire you": "Summarize your strengths, fit with the company, and enthusiasm for the role.",
    "can i ask about work-life balance": "Yes, but wait until later interview stages or frame it positively.",
    "how to build interview confidence": "Practice, mock interviews, positive self-talk, and knowing your material helps.",
    "what are common interview mistakes": "Being late, not researching the company, rambling, or badmouthing past employers.",
    "how to handle a tough interviewer": "Stay calm, professional, and focus on answering questions thoughtfully.",
    "how to answer do you have any questions": "Always say yes. Ask something thoughtful that shows engagement.",
    "how to show enthusiasm in an interview": "Smile, show curiosity, express why the company or role excites you.",
    "how to discuss team experience": "Share examples of collaboration, communication, and positive outcomes.",
    "how to answer tell me about a conflict at work": "Use the STAR method to show how you resolved it professionally.",
    "how to prep for a technical interview": "Practice problems, review fundamentals, and understand the company’s tech stack.",
    "what if I don't know an answer": "Be honest, share how you'd find the answer, or describe your approach to solving it.",
    "bye": "Goodbye! Best of luck with your interview — you've got this!"
}

def chatbot(user_input):
    user_input = user_input.lower().strip()
    match = get_close_matches(user_input, responses.keys(), n=1, cutoff=0.5)
    if match:
        return responses[match[0]]
    return "Hmm, I don't have an answer for that yet. Try rephrasing or ask something interview-related."

# Gradio Interface
iface = gr.Interface(fn=chatbot,
                     inputs=gr.Textbox(lines=2, placeholder="Ask me about job interviews..."),
                     outputs="text",
                     title="💼 Job Interview Prep Chatbot",
                     description="Ask me anything about interviews, resumes, or career tips! 👩‍💼👨‍💼")

iface.launch() 
