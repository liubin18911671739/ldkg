from app.services.search_service import SearchService
from app.services.research_data_service import ResearchDataService
from app.services.teaching_data_service import TeachingDataService

search_service = SearchService()
research_data_service = ResearchDataService()
teaching_data_service = TeachingDataService()

__all__ = [
    'search_service',
    'research_data_service',
    'teaching_data_service'
]