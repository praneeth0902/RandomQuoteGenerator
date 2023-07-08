import random
name = input("Enter your name: ")
category = input("Select a category for the quote (motivation, success, life, love, friendship, wisdom): ")
quotes = {
        "motivation": [
        {
            "quote":"Believe you can and you're halfway there.",
            "author": "Theodore Roosevelt"},
        {
            "quote": "The future belongs to those who believe in the beauty of their dreams.",
            "author": "Eleanor Roosevelt"},
        {
            "quote":"Success is not final, failure is not fatal: It is the courage to continue that counts.",
            "author":"Winston Churchill"}
    ],
    "success": [
        {
            "quote":"Success is not the key to happiness. Happiness is the key to success.",
            "author":"Albert Schweitzer"},
        {
             "quote":"Success usually comes to those who are too busy to be looking for it.",
            "author": "Henry David Thoreau"},
        {
             "quote":"The road to success and the road to failure are almost exactly the same.",
            "author": "Colin R. Davis"}
    ],
     "life": [
        {
            "quote":"In the end, it's not the years in your life that count. It's the life in your years.",
            "author":"Abraham Lincoln"},
        {
            "quote":"The purpose of our lives is to be happy.",
            "author": "Dalai Lama"},
        {
            "quote": "Life is what happens when you're busy making other plans.",
            "author": "John Lennon"}
    ],
     "love": [
        {
            "quote": "The greatest happiness of life is the conviction that we are loved; loved for ourselves, or rather, loved in spite of ourselves.",
            "author": "Victor Hugo"},
        {
            "quote": "Love is composed of a single soul inhabiting two bodies.",
            "author": "Aristotle"},
        {
            "quote": "Where there is love, there is life.",
            "author": "Mahatma Gandhi" }
    ],
    'friendship': [
        {
            "quote": "Friendship is born at that moment when one person says to another: 'What! You too? I thought I was the only one.'", 
            "author": "C.S. Lewis"},
        {
            "quote": "A real friend is one who walks in when the rest of the world walks out.", 
            "author": "Walter Winchell"},
        {
             "quote": "Friendship is the only cement that will ever hold the world together.", 
            "author": "Woodrow Wilson"}
    ],
     'wisdom': [
        {
            "quote": "The only true wisdom is in knowing you know nothing.", 
            "author": "Socrates"},
        {
            "quote": "The only way to do great work is to love what you do.",
            "author": "Steve Jobs"},
        {
            "quote": "The best way to predict the future is to create it.", 
            "author": "Peter Drucker"}
    ]
}
if category in quotes:
    quote_obj = random.choice(quotes[category])
    quote = quote_obj["quote"]
    author = quote_obj["author"]
    generated_quote = quote.replace("{name}", name)
    print("Here's your generated quote:")
    print(generated_quote)
    print("-" + author)
else:
    print("Invalid category.")
       
  
                   