# Nutrition Analysis API

The Nutrition Analysis API is a Flask-based application that combines a CNN (Convolutional Neural Network) model and the Gemini AI model to classify food images and provide detailed nutrition information.

## Prerequisites

- Python 3.9
- Flask
- Google Generative AI
- TensorFlow 2.15.0
- NumPy
- Pillow
- Gunicorn

## Installation

1. Clone the repository:

```bash
git clone https://github.com/capstone-entsh122/aktivio-classification.git
```

2. Navigate to the project directory:

```bash
cd aktivio-classification
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Set the Google API key as an environment variable:

```bash
export GOOGLE_API_KEY=your_api_key_here
```

## Usage

1. Start the Flask application:

```bash
python app.py
```

The application will run on `http://localhost:8080`.

2. Send a POST request to the `/api/classify` endpoint with the following parameters:
   - `image`: The food image file to be analyzed.

Example using cURL:

```bash
curl -X POST -F "image=@/path/to/image.jpg" http://localhost:8080/api/classify
```

3. The API will respond with a JSON object containing the classified food label and the detailed nutrition information:

```json
{
  "class_label": "Nasi Goreng",
  "nutrition_response": {
    "Porsi": "1 porsi",
    "Kalori": 500,
    "Protein": 20,
    "Lemak": 15,
    "Karbohidrat": 70,
    "Serat": 5
  }
}
```

## API Documentation

### Endpoint: `/api/classify`

- Method: POST
- Description: Classifies a food image and provides detailed nutrition information.
- Request Parameters:
  - `image` (file): The food image file to be analyzed.
- Response:
  - `class_label` (string): The classified food label.
  - `nutrition_response` (object): The detailed nutrition information.
    - `Porsi` (string): The serving size.
    - `Kalori` (number): The calorie content.
    - `Protein` (number): The protein content.
    - `Lemak` (number): The fat content.
    - `Karbohidrat` (number): The carbohydrate content.
    - `Serat` (number): The fiber content.

## Deployment

The application can be deployed using Docker. The provided `Dockerfile` can be used to build the Docker image.

1. Build the Docker image:

```bash
docker build -t nutrition-analysis-api .
```

2. Run the Docker container:

```bash
docker run -p 8080:8080 -e GOOGLE_API_KEY=your_api_key_here nutrition-analysis-api
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- The CNN model (`aktivio9986.h5`) was trained separately and is loaded in the application.
- The Gemini AI model is used for generating detailed nutrition information based on the classified food label.
- The Flask framework is used for building the API endpoints.
- Gunicorn is used as the WSGI server for production deployment.
