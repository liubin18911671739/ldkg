from datetime import datetime

class ResearchData:
    def __init__(self, title, authors, publication_date, abstract, keywords, citation_count):
        self.title = title
        self.authors = authors
        self.publication_date = publication_date
        self.abstract = abstract
        self.keywords = keywords
        self.citation_count = citation_count

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data.get('title'),
            authors=data.get('authors'),
            publication_date=datetime.strptime(data.get('publication_date'), '%Y-%m-%d'),
            abstract=data.get('abstract'),
            keywords=data.get('keywords'),
            citation_count=data.get('citation_count')
        )

    def to_dict(self):
        return {
            'title': self.title,
            'authors': self.authors,
            'publication_date': self.publication_date.strftime('%Y-%m-%d'),
            'abstract': self.abstract,
            'keywords': self.keywords,
            'citation_count': self.citation_count
        }