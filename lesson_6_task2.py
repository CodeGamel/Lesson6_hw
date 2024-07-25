python_reviews = [
         "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "This was a poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]

python_positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 

negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def analyze_sentiment(review):
    review_lower = review.lower()  
    words = review_lower.split()  
    
    positive_count = sum(word in python_positive_words for word in words)
    
    negative_count = sum(word in negative_words for word in words)
    
    if positive_count > negative_count:
        return "Positive"
    elif negative_count > positive_count:
        return "Negative"
    else:
        return "Neutral"

for review in python_reviews:
    sentiment = analyze_sentiment(review)
    print(f"Review: {review}")
    print(f"Sentiment: {sentiment}")
    print()



