#Vecna AI The rule based chatbot
#Developed by Himanshu Kumar
#The name of my AI Vecna is from a netflix series STRANGER THINGS 

import re
import random
import datetime

class RuleBasedChatbot:
    def __init__(self):
        self.name = "Vecna AI"
        self.responses = self._initialize_responses()
        self.context = {}
        self.conversation_log = []
        self.output_file = "output.txt"
        
        # Initialize log file
        self._initialize_log_file()
        
    def _initialize_log_file(self):
        """Initialize the output.txt file with a header"""
        try:
            with open(self.output_file, 'a', encoding='utf-8') as f:
                f.write("=" * 70 + "\n")
                f.write(f"CHATBOT CONVERSATION LOG\n")
                f.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 70 + "\n\n")
            print(f"Log file '{self.output_file}' initialized successfully.")
        except Exception as e:
            print(f"Warning: Could not initialize log file: {e}")
    
    def _initialize_responses(self):
        """Initialize all the rules and responses for the chatbot"""
        
        return {
            # Greeting patterns and responses
            'greetings': {
                'patterns': [
                    r'hello', r'hi', r'hey', r'good morning', r'good afternoon',
                    r'good evening', r'greetings'
                ],
                'responses': [
                    "Hello! How can I help you today?",
                    "Hi there! What can I do for you?",
                    "Hey! Nice to meet you. How can I assist?",
                    "Greetings! I'm here to help with your AI questions."
                ]
            },
            
            # Farewell patterns and responses
            'farewell': {
                'patterns': [
                    r'bye', r'goodbye', r'see you', r'quit', r'exit',
                    r'stop', r'cya'
                ],
                'responses': [
                    "Goodbye! Have a great day!",
                    "See you later!",
                    "Bye! Come back if you have more questions.",
                    "Take care!",
                    "Goodbye! I've saved our conversation to output.txt"
                ]
            },
            
            # Thank you patterns
            'thanks': {
                'patterns': [
                    r'thank you', r'thanks', r'appreciate', r'thankful',
                    r'grateful'
                ],
                'responses': [
                    "You're welcome!",
                    "Happy to help!",
                    "Glad I could assist you!",
                    "Anytime! All conversations are being logged for learning."
                ]
            },
            
            # Name-related patterns
            'name': {
                'patterns': [
                    r'what is your name', r'who are you', r'your name',
                    r'introduce yourself'
                ],
                'responses': [
                    f"I'm {self.name}, a rule-based chatbot created for AI internship tasks. I log all conversations to output.txt.",
                    f"My name is {self.name}. I'm here to help with AI-related questions. I save our chat to a file for analysis.",
                    f"I'm called {self.name}. How can I assist you today? (Note: Our chat is being saved to output.txt)"
                ]
            },
            
            # AI-related questions
            'ai_definition': {
                'patterns': [
                    r'what is ai', r'what is artificial intelligence',
                    r'explain ai', r'define ai', r'meaning of ai'
                ],
                'responses': [
                    "AI (Artificial Intelligence) is the simulation of human intelligence in machines programmed to think and learn.",
                    "Artificial Intelligence refers to computer systems that can perform tasks normally requiring human intelligence.",
                    "AI is a branch of computer science focused on creating intelligent machines that work and react like humans."
                ]
            },
            
            'ml_definition': {
                'patterns': [
                    r'what is machine learning', r'what is ml',
                    r'explain machine learning', r'define ml'
                ],
                'responses': [
                    "Machine Learning is a subset of AI where computers learn from data without being explicitly programmed.",
                    "ML is about creating algorithms that can learn from and make predictions on data.",
                    "Machine Learning enables systems to automatically learn and improve from experience."
                ]
            },
            
            'nlp_definition': {
                'patterns': [
                    r'what is nlp', r'what is natural language processing',
                    r'explain nlp', r'define natural language processing'
                ],
                'responses': [
                    "NLP (Natural Language Processing) is a field of AI that helps computers understand, interpret, and respond to human language.",
                    "Natural Language Processing is about the interaction between computers and human language.",
                    "NLP focuses on enabling computers to understand, process, and generate human language."
                ]
            },
            
            # Internship-related questions
            'internship_help': {
                'patterns': [
                    r'internship task', r'internship project',
                    r'rule based chatbot', r'chatbot task',
                    r'help with chatbot', r'task 1', r'output\.txt',
                    r'save response', r'save chat', r'log conversation'
                ],
                'responses': [
                    "I'm actually the result of Task 1! A rule-based chatbot responds to user inputs using predefined rules and patterns.",
                    "For your internship task, you're building a chatbot like me using if-else statements or pattern matching. I save all chats to output.txt!",
                    "This chatbot demonstrates pattern matching techniques and saves all conversations to output.txt - perfect for your Task 1 documentation!"
                ]
            },
            
            # How are you patterns
            'how_are_you': {
                'patterns': [
                    r'how are you', r'how do you do', r'how is it going',
                    r'how have you been'
                ],
                'responses': [
                    "I'm functioning optimally, thank you! How can I help you? (All our chat is being saved to output.txt)",
                    "I'm doing well, ready to assist with AI questions! I'm also logging this conversation.",
                    "All systems are operational! How about you? (Note: I save responses to output.txt)"
                ]
            },
            
            # Time and date
            'time_date': {
                'patterns': [
                    r'what time is it', r'current time', r'what is the time',
                    r'what day is it', r'date today', r'current date'
                ],
                'responses': self._get_time_date_responses
            },
            
            # Help patterns
            'help': {
                'patterns': [
                    r'help', r'support', r'assistance', r'what can you do',
                    r'capabilities', r'features'
                ],
                'responses': [
                    "I can help with:\n- AI/ML/NLP definitions\n- Internship task guidance\n- General chatbot questions\n- Time and date\n- Basic conversations\n\nAll conversations are saved to output.txt!",
                    "I'm designed to help with AI-related topics and your internship tasks. I also log all chats to output.txt for analysis!",
                    "I'm a rule-based chatbot for AI internship tasks. I save every conversation to output.txt file."
                ]
            },
            
            # File-related patterns
            'file_questions': {
                'patterns': [
                    r'show log', r'view log', r'read output',
                    r'open output\.txt', r'where is output'
                ],
                'responses': [
                    "All our conversations are being saved to output.txt in the current directory.",
                    "I'm saving this chat to output.txt file. You can open it with any text editor.",
                    "Check output.txt file to see our complete conversation history."
                ]
            },
            
            # Default response if no pattern matches
            'default': {
                'patterns': [],
                'responses': [
                    "I'm not sure I understand. Could you rephrase that? (I'll still save this to output.txt)",
                    "I'm still learning. Could you ask about AI, machine learning, or your internship tasks?",
                    "That's interesting! Could you ask me something about artificial intelligence?",
                    "I'm designed to answer questions about AI and your internship tasks. All chats are saved to output.txt!"
                ]
            }
        }
    
    def _get_time_date_responses(self):
        """Generate responses for time/date queries"""
        now = datetime.datetime.now()
        time_str = now.strftime("%I:%M %p")
        date_str = now.strftime("%B %d, %Y")
        day_str = now.strftime("%A")
        
        responses = [
            f"The current time is {time_str}. This conversation is being saved to output.txt.",
            f"Today is {day_str}, {date_str}. The time is {time_str}. Chat logged to file.",
            f"It's {time_str} on {day_str}, {date_str}. (Saved to output.txt)"
        ]
        return responses
    
    def find_match(self, user_input):
        """Find which rule matches the user input"""
        user_input = user_input.lower().strip()
        
        # Check each category of responses
        for category, data in self.responses.items():
            if category == 'default':
                continue
                
            # Check each pattern in the category
            for pattern in data['patterns']:
                if re.search(pattern, user_input):
                    return category
        
        # No match found
        return 'default'
    
    def log_conversation(self, user_input, chatbot_response, category):
        """Save conversation to both memory and file"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Create log entry
        log_entry = {
            'timestamp': timestamp,
            'user_input': user_input,
            'chatbot_response': chatbot_response,
            'category': category
        }
        
        # Add to memory log
        self.conversation_log.append(log_entry)
        
        # Save to file
        try:
            with open(self.output_file, 'a', encoding='utf-8') as f:
                f.write(f"[{timestamp}]\n")
                f.write(f"You: {user_input}\n")
                f.write(f"Bot: {chatbot_response}\n")
                f.write(f"Category: {category}\n")
                f.write("-" * 50 + "\n\n")
        except Exception as e:
            print(f"Warning: Could not write to log file: {e}")
    
    def show_conversation_summary(self):
        """Display summary of conversation"""
        print("\n" + "=" * 60)
        print("CONVERSATION SUMMARY")
        print("=" * 60)
        print(f"Total exchanges: {len(self.conversation_log)}")
        
        # Count by category
        category_count = {}
        for entry in self.conversation_log:
            category = entry['category']
            category_count[category] = category_count.get(category, 0) + 1
        
        print("\nResponses by category:")
        for category, count in category_count.items():
            print(f"  {category}: {count}")
        
        print(f"\nFull conversation saved to: {self.output_file}")
    
    def get_response(self, user_input):
        """Get an appropriate response based on user input"""
        category = self.find_match(user_input)
        response_data = self.responses[category]
        
        # Get the response list
        if category == 'time_date' and callable(response_data['responses']):
            responses = response_data['responses']()
        else:
            responses = response_data['responses']
        
        # Return a random response from the category
        return random.choice(responses), category
    
    def save_full_conversation_report(self):
        """Save a detailed report of the conversation"""
        try:
            report_file = "conversation_report.txt"
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write("=" * 70 + "\n")
                f.write("CHATBOT CONVERSATION ANALYSIS REPORT\n")
                f.write(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 70 + "\n\n")
                
                f.write("CONVERSATION LOG:\n")
                f.write("-" * 70 + "\n\n")
                
                for i, entry in enumerate(self.conversation_log, 1):
                    f.write(f"Exchange #{i}:\n")
                    f.write(f"  Time: {entry['timestamp']}\n")
                    f.write(f"  You: {entry['user_input']}\n")
                    f.write(f"  Bot: {entry['chatbot_response']}\n")
                    f.write(f"  Category: {entry['category']}\n")
                    f.write("\n")
                
                # Summary statistics
                f.write("\n" + "=" * 70 + "\n")
                f.write("SUMMARY STATISTICS\n")
                f.write("=" * 70 + "\n\n")
                
                f.write(f"Total Exchanges: {len(self.conversation_log)}\n\n")
                
                # Category analysis
                category_count = {}
                for entry in self.conversation_log:
                    category = entry['category']
                    category_count[category] = category_count.get(category, 0) + 1
                
                f.write("Responses by Category:\n")
                for category, count in sorted(category_count.items()):
                    percentage = (count / len(self.conversation_log)) * 100
                    f.write(f"  {category}: {count} ({percentage:.1f}%)\n")
                
                # Pattern matching efficiency
                f.write(f"\nDefault Responses: {category_count.get('default', 0)}\n")
                if len(self.conversation_log) > 0:
                    efficiency = ((len(self.conversation_log) - category_count.get('default', 0)) / len(self.conversation_log)) * 100
                    f.write(f"Pattern Matching Efficiency: {efficiency:.1f}%\n")
                
            print(f"\nDetailed report saved to: {report_file}")
        except Exception as e:
            print(f"Could not generate report: {e}")
    
    def start_chat(self):
        """Start the interactive chat session"""
        print("=" * 60)
        print(f"Welcome to {self.name}!")
        print("I'm a rule-based chatbot for AI internship tasks.")
        print("All conversations are saved to 'output.txt'")
        print("Type 'quit', 'exit', or 'bye' to end the conversation.")
        print("=" * 60)
        print("\nWhat would you like to know about AI or your internship tasks?")
        
        while True:
            try:
                # Get user input
                user_input = input("\nYou: ").strip()
                
                # Check for empty input
                if not user_input:
                    print(f"{self.name}: Please type something!")
                    continue
                
                # Get response and category
                response, category = self.get_response(user_input)
                print(f"{self.name}: {response}")
                
                # Log the conversation
                self.log_conversation(user_input, response, category)
                
                # Check if user wants to end the conversation
                if category == 'farewell':
                    self.show_conversation_summary()
                    
                    # Ask if user wants a detailed report
                    save_report = input("\nWould you like a detailed conversation report? (yes/no): ")
                    if save_report.lower().startswith('y'):
                        self.save_full_conversation_report()
                    
                    print("\nThank you for chatting! Goodbye!")
                    break
                    
            except KeyboardInterrupt:
                print(f"\n{self.name}: Goodbye!")
                self.show_conversation_summary()
                break
            except Exception as e:
                print(f"{self.name}: Sorry, I encountered an error. Please try again.")

# Function to demonstrate file logging
def demonstrate_logging():
    """Show how logging works"""
    print("\n" + "=" * 60)
    print("FILE LOGGING DEMONSTRATION")
    print("=" * 60)
    
    chatbot = RuleBasedChatbot()
    
    # Test conversation
    test_queries = [
        "Hello chatbot!",
        "What is AI?",
        "Are you saving our chat?",
        "Thank you",
        "Goodbye"
    ]
    
    print("\nTesting logging with sample queries:")
    print("(All responses will be saved to output.txt)\n")
    
    for query in test_queries:
        print(f"You: {query}")
        response, category = chatbot.get_response(query)
        print(f"Bot: {response}")
        chatbot.log_conversation(query, response, category)
        print("-" * 40)
    
    print(f"\nCheck 'output.txt' file to see the logged conversation!")
    print(f"Total exchanges logged: {len(chatbot.conversation_log)}")

# Function to view the log file
def view_output_file():
    """Display the contents of output.txt"""
    try:
        print("\n" + "=" * 60)
        print("CONTENTS OF output.txt")
        print("=" * 60)
        
        with open("output.txt", 'r', encoding='utf-8') as f:
            content = f.read()
            if content:
                print(content)
            else:
                print("File is empty. Start a conversation to see logs.")
    except FileNotFoundError:
        print("output.txt file not found. Start a conversation to create it.")

# Main program
if __name__ == "__main__":
    # Create chatbot instance
    chatbot = RuleBasedChatbot()
    
    print("Rule-Based Chatbot with File Logging")
    print("=" * 40)
    print("Options:")
    print("1. Start new conversation")
    print("2. View logging demonstration")
    print("3. View output.txt file")
    print("4. Exit")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == '1':
                chatbot.start_chat()
                break
            elif choice == '2':
                demonstrate_logging()
            elif choice == '3':
                view_output_file()
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Please enter a valid option (1-4)")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break