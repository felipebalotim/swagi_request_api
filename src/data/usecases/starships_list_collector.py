from typing import Dict, List, Type
from src.domain.usecases import StarshipsListCollectorInterface

from src.infra.swapi_api_consumer import SwapiApiConsumer

class StarshipsListCollector(StarshipsListCollectorInterface):
    """ StarshipsListCollector usecase """

    def __init__(self, api_consumer: Type[SwapiApiConsumer]) -> None:
        self.__api_consumer = api_consumer

    def list(self, page: int) -> List[Dict]:
        """ Must implement """

        response = self.__api_consumer.get_starships(page)
        print(response)
