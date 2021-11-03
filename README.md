## cf_embeddia

This package provides wrapper widgets for services developed in the context of the EU Embeddia project.

Currently available:


- **Article analyzer** (from [https://embeddia-demo.texta.ee/api/v1/article_analyzer/](https://embeddia-demo.texta.ee/api/v1/article_analyzer/))

    Widget wrapping this service provides all available analysis methods and features two outputs: keywords and named entities.

- **Comment analyzer (moderator)** (from [https://embeddia-demo.texta.ee/api/v1/comment_analyzer/](https://embeddia-demo.texta.ee/api/v1/comment_analyzer/))  

    Widget wrapping this service clears the input corpus of offensive comments using the given threshold. Please note that because the service accepts only one document at a time the input corpus must be small to avoid flooding the service with requests.
