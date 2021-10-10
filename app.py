from flask import Flask, request, render_template, redirect, url_for
from owning_check import nft_checker
import json

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def search_api():
    query = request.args.get('address')
    return nft_checker(query, 'collection-scraper.json')


if __name__ == '__main__':
    app.run(port=5000)
