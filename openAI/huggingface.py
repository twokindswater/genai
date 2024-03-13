from transformers import pipeline

distilled_student_sentiment_classifier = pipeline(
    model="lxyuan/distilbert-base-multilingual-cased-sentiments-student",
)

print("1")
distilled_student_sentiment_classifier("I love this movie and i would watch it again and again!")
print("2")

