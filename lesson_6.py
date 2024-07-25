python_reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "This was a poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords = ('good', 'excellent', 'bad', 'poor', 'average')

def keyword_highlighter(review):
    for keyword in keywords:
        if keyword in review.lower():
            review = review.replace(keyword, keyword.upper())
    return review

def main():
    for review in python_reviews:
        new_review = keyword_highlighter(review)
        print(new_review)
        print()

main()





