# NLP analysis on Hemingway
# EDA

use AWS comprehend by boto3 and ipython

```python
import boto3
client = boto3.client('comprehend')

```

Do something like this for sentiment analysis:
```
response = client.detect_sentiment(
    Text='string',
    LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt'|'ar'|'hi'|'ja'|'ko'|'zh'|'zh-TW'
)
```

Grab text into string