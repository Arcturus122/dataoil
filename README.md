# Data oil
> This project is about doing some rersearch and analysis on oil (crude mainly but also derived product)


## Install

`pip install dataoil`

## How to use

Youd need to xreate a file called credentials.json with the following content

{
<br>
    "api_key":"YOUR API KEY"
<br>
}

```python
from dataoil.api import Api
api = Api()
wti = api.fetch_spot('WTI')
print(wti.head())
```

            date  price
    0 2020-06-23  40.40
    1 2020-06-22  40.60
    2 2020-06-19  39.72
    3 2020-06-18  38.79
    4 2020-06-17  37.91

