import gradio as gr
import random
import os

quotes = [
    "Believe in yourself, you are stronger than you think.",
    "Every day may not be good, but there’s something good in every day.",
    "Don’t stress over what you can’t control. Focus on what you can do now.",
    "Take one step at a time. Progress is still progress."
]

tips = [
    "Try a 5-minute breathing exercise: Inhale 4 sec, Hold 4 sec, Exhale 4 sec.",
    "Take a short break, stretch your body, and drink some water.",
    "Write down 3 things you are grateful for today.",
    "Go for a short walk and get some fresh air."
]

def wellness_bot(message, history=[]):
    message = message.lower()
    if "stress" in message or "anxious" in message:
        response = random.choice(tips)
    elif "sad" in message or "depressed" in message:
        response = ("I’m sorry you’re feeling this way 💙. "
                    "Remember, it’s okay to ask for help. "
                    "You can call a friend or a helpline if it feels overwhelming.")
    elif "motivate" in message or "inspire" in message:
        response = random.choice(quotes)
    elif "hello" in message or "hi" in message:
        response = "Hello 👋 I’m your Wellness Assistant. How are you feeling today?"
    else:
        response = "I hear you 🌸. Would you like a relaxation tip or a motivational quote?"
    return response

chatbot = gr.ChatInterface(fn=wellness_bot, title="🌱 Mental Wellness Assistant")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # use Render's PORT
    chatbot.launch(server_name="0.0.0.0", server_port=port)
