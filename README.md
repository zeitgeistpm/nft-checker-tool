# nft-checker-tool

The purpose of this repository is to create an endpoint that indicates whether the address provided is the owner of any of the NFTs of a series of collections.
Warning: the endpoint may take a while, but this is how it works.

Once developed, the address can be checked in <site domain>/?address=<address>

## How it works
First of all, the 'collection_scraper.py' file must be opened and the list of collections that will be part of the collection set to be evaluated must be edited (change in line 46). This will result in a json file called 'collection-scraper.json' that will replace the current one.
Once this is created, you can run the app.py file, which will create this endpoint that will test the address provided using the function contained in the 'owning_check.py' file.
