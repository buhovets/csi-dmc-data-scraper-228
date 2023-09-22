import json
import os

from apify_client import ApifyClient


class ApifyScraper:
    """
    A class for running an Apify actor and saving its results to a JSON file.

    Args:
        api_token (str): Your Apify API token.

    Methods:
        __init__(api_token: str)
            Initialize the ApifyScraper instance.

        run(actor_id: str, input_data: Dict, output_file: str) -> List[Dict]:
            Run an Apify actor with the provided input data and save the results.

        save(output_file: str, data: List[Dict]) -> None:
            Save data to a JSON file.
    """
    def __init__(self, api_token: str):
        self.client = ApifyClient(api_token)

    def run(self, actor_id: str, input_data: dict) -> list[dict]:
        """
        Run an Apify actor with the provided input data and save the results.

        Args:
            actor_id (str): The ID or name of the Apify actor.
            input_data (Dict): Input data for the actor.
            output_file (str): The name of the JSON file to save the results to.

        Returns:
            List[Dict]: A list of dictionaries containing the scraped data.
        """
        print("Parsing pages... This usually takes about 4 minutes.\n")
        print(f"You can check the progress of the actor in your Apify console: https://console.apify.com/actors/ -> "
              f"Select your actor -> Runs\n")
        run = self.client.actor(actor_id).call(run_input=input_data)

        items = []
        for item in self.client.dataset(run["defaultDatasetId"]).iterate_items():
            items.append(dict(item))
            print(json.dumps(items, indent=4))
        return items

    def save(self, output_file: str, data: list[dict]):
        """
        Save data to a JSON file.

        Args:
            output_file (str): The name of the JSON file to save the data to.
            data (List[Dict]): The data to be saved.
        """
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Parsing results was saved to: {output_file}")
