import streamlit as st
import pyttsx3

def initialize_tts():
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    return engine

def speak(text, engine):
    engine.say(text)
    engine.runAndWait()

def load_knowledge_base():
    knowledge_base = [
        {
            "category": "greetings",
            "question": "hi",
            "answer": "Hello! How can I help you?"
        },
        {
            "category": "greetings",
            "question": "hello",
            "answer": "Hi there! What do you want to ask?"
        },
        {
            "category": "programming",
            "question": "what is python",
            "answer": "Python is a high-level programming language created by Guido van Rossum in 1990."
        },
        {
            "category": "programming",
            "question": "what is a variable",
            "answer": "A variable is a container for storing data values in programming."
        },
        {
            "category": "science",
            "question": "what is the speed of light",
            "answer": "The speed of light is approximately 299,792 kilometers per second."
        },
        {
            "category": "science",
            "question": "who discovered gravity",
            "answer": "Gravity was discovered by Sir Isaac Newton."
        },
        {
            "category": "history",
            "question": "who was the first president of the united states",
            "answer": "George Washington was the first president of the United States."
        },
        {
            "category": "history",
            "question": "when was the declaration of independence signed",
            "answer": "The Declaration of Independence was signed on July 4, 1776."
        },
        {
            "category": "fun facts",
            "question": "tell me a fun fact about animals",
            "answer": "Octopuses have three hearts and blue blood!"
        },
        {
            "category": "fun facts",
            "question": "what is a unique fact about the sun",
            "answer": "The sun accounts for 99.8% of the mass in the solar system."
        },
        {
            "category": "general knowledge",
            "question": "what is the capital of France",
            "answer": "The capital of France is Paris."
        },
        {
            "category": "general knowledge",
            "question": "what is the largest ocean",
            "answer": "The Pacific Ocean is the largest ocean on Earth."
        },
        {
            "category": "math",
            "question": "what is pi",
            "answer": "Pi is a mathematical constant approximately equal to 3.14159."
        },
        {
            "category": "math",
            "question": "what is the fibonacci sequence",
            "answer": "The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones."
        },
        {
            "category": "personal",
            "question": "how are you",
            "answer": "I'm just a bot, but I'm doing great! How about you?"
        },
        {
            "category": "personal",
            "question": "who created you",
            "answer": "I was created by Shristi."
        },
        {
            "category": "technology",
            "question": "what is artificial intelligence",
            "answer": "Artificial Intelligence (AI) is the simulation of human intelligence by machines."
        },
        {
            "category": "technology",
            "question": "what is machine learning",
            "answer": "Machine learning is a subset of AI that focuses on training machines to learn from data."
        },
        {
            "category": "sports",
            "question": "who won the first FIFA World Cup",
            "answer": "Uruguay won the first FIFA World Cup in 1930."
        },
        {
            "category": "sports",
            "question": "how many players are on a soccer team",
            "answer": "A soccer team has 11 players on the field."
        },
        {
            "category": "philosophy",
            "question": "What is the meaning of life?",
            "answer": "The meaning of life has been debated for centuries, but it often revolves around personal fulfillment, love, and growth."
        },
        {
            "category": "health",
            "question": "What is the normal body temperature?",
            "answer": "The normal human body temperature is approximately 98.6°F (37°C)."
        },
        {
            "category": "geography",
            "question": "Which is the smallest country in the world?",
            "answer": "Vatican City is the smallest country in the world."
        },
        {
            "category": "astronomy",
            "question": "What is a black hole?",
            "answer": "A black hole is a region of space where gravity is so strong that nothing, not even light, can escape."
        },
        {
            "category": "biology",
            "question": "What is the largest organ in the human body?",
            "answer": "The skin is the largest organ in the human body."
        },
        {
            "category": "literature",
            "question": "Who wrote 'Pride and Prejudice'?",
            "answer": "'Pride and Prejudice' was written by Jane Austen."
        },
        {
            "category": "music",
            "question": "Who is known as the King of Pop?",
            "answer": "Michael Jackson is known as the King of Pop."
        },
        {
            "category": "movies",
            "question": "Which movie won the first Academy Award for Best Picture?",
            "answer": "The first Academy Award for Best Picture was won by 'Wings' in 1929."
        },
        {
            "category": "travel",
            "question": "What is the tallest waterfall in the world?",
            "answer": "Angel Falls in Venezuela is the tallest waterfall in the world."
        },
        {
            "category": "food",
            "question": "What is sushi traditionally wrapped in?",
            "answer": "Sushi is traditionally wrapped in seaweed, also known as nori."
        },
        {
            "category": "inventions",
            "question": "Who invented the telephone?",
            "answer": "The telephone was invented by Alexander Graham Bell."
        },
        {
            "category": "environment",
            "question": "What is the largest rainforest in the world?",
            "answer": "The Amazon Rainforest is the largest rainforest in the world."
        },
        {
            "category": "economics",
            "question": "What is inflation?",
            "answer": "Inflation is the rate at which the general level of prices for goods and services rises over time."
        },
        {
            "category": "psychology",
            "question": "What is the placebo effect?",
            "answer": "The placebo effect is when a person experiences a perceived improvement in their condition due to believing they are receiving treatment, even if it is inactive."
        },
        {
            "category": "languages",
            "question": "What is the most spoken language in the world?",
            "answer": "English is the most widely spoken language, but Mandarin Chinese has the most native speakers."
        },
        {
            "category": "space exploration",
            "question": "Who was the first person to walk on the moon?",
            "answer": "Neil Armstrong was the first person to walk on the moon in 1969."
        },
        {
            "category": "art",
            "question": "Who painted the Mona Lisa?",
            "answer": "The Mona Lisa was painted by Leonardo da Vinci."
        },
        {
            "category": "mythology",
            "question": "Who is the Greek god of the sea?",
            "answer": "Poseidon is the Greek god of the sea."
        },
        {
            "category": "technology",
            "question": "What does HTTP stand for?",
            "answer": "HTTP stands for HyperText Transfer Protocol."
        },
        {
            "category": "sports",
            "question": "What sport uses a shuttlecock?",
            "answer": "Badminton uses a shuttlecock."
        },
        {
            "category": "business",
            "question": "What is a startup?",
            "answer": "A startup is a young company founded to develop a unique product or service and bring it to market."
        },
        {
            "category": "nature",
            "question": "What is the fastest land animal?",
            "answer": "The cheetah is the fastest land animal, capable of speeds up to 70 mph."
        },
        {
            "category": "physics",
            "question": "What is Newton's third law of motion?",
            "answer": "Newton's third law states that for every action, there is an equal and opposite reaction."
        },
        {
            "category": "space",
            "question": "What planet is known as the Red Planet?",
            "answer": "Mars is known as the Red Planet."
        },
        {
            "category": "fun facts",
            "question": "What is the only mammal capable of flight?",
            "answer": "Bats are the only mammals capable of sustained flight."
        },
        {
            "category": "hardware",
            "question": "What is a CPU?",
            "answer": "The CPU, or Central Processing Unit, is the main processor of a computer responsible for executing instructions."
        },
        {
            "category": "hardware",
            "question": "What is the function of RAM?",
            "answer": "RAM, or Random Access Memory, temporarily stores data that the CPU needs to access quickly."
        },
        {
            "category": "hardware",
            "question": "What is an SSD?",
            "answer": "An SSD, or Solid-State Drive, is a type of storage device that uses flash memory to store data and is faster than traditional hard drives."
        },
        {
            "category": "hardware",
            "question": "What is a motherboard?",
            "answer": "The motherboard is the main circuit board of a computer that connects all components like the CPU, RAM, and storage."
        },
        {
            "category": "hardware",
            "question": "What is a GPU?",
            "answer": "A GPU, or Graphics Processing Unit, is specialized hardware designed to render graphics and perform parallel computations."
        },
        {
            "category": "software",
            "question": "What is an operating system?",
            "answer": "An operating system is software that manages computer hardware and software resources and provides services for applications."
        },
        {
            "category": "software",
            "question": "What is open-source software?",
            "answer": "Open-source software is software whose source code is freely available for modification and redistribution."
        },
        {
            "category": "software",
            "question": "What is the purpose of an antivirus program?",
            "answer": "An antivirus program detects, prevents, and removes malicious software from a computer."
        },
        {
            "category": "programming",
            "question": "What is a programming language?",
            "answer": "A programming language is a formal language used to write instructions that a computer can execute."
        },
        {
            "category": "programming",
            "question": "What is an algorithm?",
            "answer": "An algorithm is a step-by-step procedure or formula for solving a problem or performing a task."
        },
        {
            "category": "programming",
            "question": "What is debugging?",
            "answer": "Debugging is the process of identifying and fixing errors or bugs in a program's code."
        },
        {
            "category": "programming",
            "question": "What is a compiler?",
            "answer": "A compiler is a program that translates source code written in a programming language into machine code that a computer can execute."
        },
        {
            "category": "networking",
            "question": "What is an IP address?",
            "answer": "An IP address is a unique identifier assigned to each device connected to a network, used for communication between devices."
        },
        {
            "category": "networking",
            "question": "What is a firewall?",
            "answer": "A firewall is a security system that monitors and controls incoming and outgoing network traffic based on predetermined rules."
        },
        {
            "category": "networking",
            "question": "What is DNS?",
            "answer": "DNS, or Domain Name System, translates human-readable domain names (like www.example.com) into IP addresses."
        },
        {
            "category": "computer history",
            "question": "Who is known as the father of computers?",
            "answer": "Charles Babbage is known as the father of computers."
        },
        {
            "category": "computer history",
            "question": "When was the first computer invented?",
            "answer": "The first general-purpose computer, ENIAC, was invented in 1945."
        },
        {
            "category": "computer history",
            "question": "Who invented the World Wide Web?",
            "answer": "The World Wide Web was invented by Tim Berners-Lee in 1989."
        },
        {
            "category": "cybersecurity",
            "question": "What is phishing?",
            "answer": "Phishing is a cyberattack where attackers impersonate trusted entities to steal sensitive information like passwords or credit card details."
        },
        {
            "category": "cybersecurity",
            "question": "What is encryption?",
            "answer": "Encryption is the process of converting information into a code to prevent unauthorized access."
        },
        {
            "category": "data storage",
            "question": "What is cloud storage?",
            "answer": "Cloud storage is a service that allows users to save data on remote servers accessed via the internet."
        },
        {
            "category": "data storage",
            "question": "What is a database?",
            "answer": "A database is an organized collection of data that can be accessed, managed, and updated easily."
        },
        {
            "category": "AI",
            "question": "What is artificial intelligence?",
            "answer": "Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn."
        },
        {
            "category": "AI",
            "question": "What is machine learning?",
            "answer": "Machine learning is a subset of AI that involves training algorithms to learn patterns from data and make predictions or decisions."
        },
        {
            "category": "programming",
            "question": "What is object-oriented programming?",
            "answer": "Object-oriented programming is a programming paradigm based on the concept of objects, which contain data and methods."
        }
    ]   
    return knowledge_base



def find_response(input_text, knowledge_base):
    for entry in knowledge_base:
        if input_text.lower() == entry["question"]:
            return entry["answer"]
    return "I don't know the answer to that. Please ask something else!"

def chatbot():
    st.title("Wuzzu ~ The Chatbot")
    data = st.text_input("Write your name: ", " ")
    tts_engine = initialize_tts()
    knowledge_base = load_knowledge_base()
    st.write(f"Hi! How are you {data}?")
    user_input = st.text_input(f"{data} says: ", "")
    if user_input:
        response = find_response(user_input, knowledge_base)
        st.write(f"Wuzzu: {response}")
        speak(response, tts_engine)
        continue_input = st.radio("Do you want to ask more?", ["Yes", "No"])
        if continue_input == "No":
            st.write("Goodbye! Have a great day!")

if __name__ == "__main__":
    chatbot()
