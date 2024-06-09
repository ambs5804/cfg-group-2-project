import unittest
from unittest.mock import patch, Mock
from app.routes import recipe_search, save_to_json
import json
import os

class TestRecipeFunctions(unittest.TestCase):

    @patch('app.routes.requests.get')
    def test_recipe_search_valid_ingredient(self, mock_get):
        mock_response = Mock()
        expected_data = {
            'hits': [
                {
                    'recipe': {
                        'label': 'Chicken Soup',
                        'url': 'http://example.com/chicken_soup',
                        'image': 'http://example.com/chicken_soup.jpg',
                        'ingredientLines': ['chicken', 'water', 'salt']
                    }
                }
            ]
        }
        mock_response.json.return_value = expected_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = recipe_search('chicken')
        self.assertEqual(result, expected_data['hits'])

        ingredient = 'chicken'
        save_to_json(result, ingredient)
        file_name = f"{ingredient}_recipes.json"
        with open(file_name, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
        self.assertEqual(json_data, [
            {
                'Recipe': 'Chicken Soup',
                'URL': 'http://example.com/chicken_soup',
                'Image': 'http://example.com/chicken_soup.jpg',
                'Ingredients': ['chicken', 'water', 'salt']
            }
        ])
        os.remove(file_name)

    @patch('app.routes.requests.get')  # Ensure this matches your actual project structure
    def test_recipe_search_invalid_ingredient(self, mock_get):
        mock_response = Mock()
        expected_data = {'hits': []}
        mock_response.json.return_value = expected_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = recipe_search('nonexistent_ingredient')
        self.assertEqual(result, [])

    @patch('app.routes.requests.get')
    def test_recipe_search_zero_ingredient(self, mock_get):
        mock_response = Mock()
        expected_data = {'hits': []}
        mock_response.json.return_value = expected_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = recipe_search('')
        self.assertEqual(result, [])

    @patch('app.routes.requests.get')
    def test_recipe_search_api_error(self, mock_get):
        mock_get.side_effect = requests.RequestException("API Error")
        result = recipe_search('ingredient')
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
