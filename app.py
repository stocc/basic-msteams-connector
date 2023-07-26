from flask import request, Flask, logging
import os, json, requests, pymsteams

MSTEAMS_URL= os.getenv('MSTEAMS_URL')


app = Flask(__name__)
logger = logging.create_logger(app)

@app.route('/')
def index():
    return ''


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_data(as_text=True)
    logger.info(data)


    teams_message = pymsteams.connectorcard(MSTEAMS_URL)
    teams_message.text(data)
    try:
        teams_message.send()
    except Exception as e:
        logger.error(e)
        return {'status': 'error'}, 500
    
    return {'status': 'success'}, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)