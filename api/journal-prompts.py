from http.server import BaseHTTPRequestHandler
import json

# Journal prompts - 30 unique prompts for daily rotation
JOURNAL_PROMPTS = [
    "What was the most meaningful moment of your day?",
    "Describe a challenge you faced today and how you handled it.",
    "What made you smile today, even briefly?",
    "If today were a chapter in your life story, what would you title it?",
    "What did you learn about yourself today?",
    "Describe a conversation that stayed with you today.",
    "What would you do differently if you could relive today?",
    "What are you looking forward to tomorrow?",
    "Write about something small that you noticed today.",
    "How did you take care of yourself today?",
    "What thought kept returning to your mind today?",
    "Describe a moment when you felt at peace today.",
    "What surprised you today?",
    "Write about someone who influenced your day.",
    "What emotion dominated your day, and why?",
    "What are you holding onto that you could let go of?",
    "Describe a sound, smell, or taste that stood out today.",
    "What do you need more of in your life right now?",
    "Write about a decision you made today, big or small.",
    "What does your ideal tomorrow look like?",
    "Describe a moment of connection with another person today.",
    "What are you avoiding thinking about?",
    "Write about something that tested your patience today.",
    "What would make tomorrow better than today?",
    "Describe how your body felt throughout the day.",
    "What boundaries did you set or need to set?",
    "Write about a moment of creativity today.",
    "What questions are you sitting with tonight?",
    "Describe a small act of kindness you witnessed or performed.",
    "What do you want to remember about this day?"
]

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        self.wfile.write(json.dumps(JOURNAL_PROMPTS).encode())
        return
